"""Agentic Python workflow — base loop with metrics tracking."""

import io
import json
import time
import traceback
from contextlib import redirect_stderr, redirect_stdout
from typing import Any
import os

import tiktoken
from IPython.core.interactiveshell import InteractiveShell
from openai import OpenAI

from metrics import RunMetrics, TurnMetrics
from trace_logger import TraceLogger
from api_functions import FUNCTION_DESCRIPTIONS, FUNCTION_EXPERIMENTS


# ---------------------------------------------------------------------------
# Executor
# ---------------------------------------------------------------------------

class PythonExecutor:
    """Persistent IPython-backed code executor."""

    def __init__(self) -> None:
        self.shell = InteractiveShell.instance()

    def run(self, code: str) -> dict[str, Any]:
        out, err = io.StringIO(), io.StringIO()
        try:
            with redirect_stdout(out), redirect_stderr(err):
                result = self.shell.run_cell(code)
            return {
                "ok": result.success,
                "stdout": out.getvalue(),
                "stderr": err.getvalue(),
                "error": None if result.success else (
                    err.getvalue().strip() or "Execution failed."
                ),
            }
        except Exception:
            return {
                "ok": False,
                "stdout": out.getvalue(),
                "stderr": err.getvalue(),
                "error": traceback.format_exc(),
            }


# ---------------------------------------------------------------------------
# Tool definitions
# ---------------------------------------------------------------------------

TOOLS: list[dict[str, Any]] = [
    {
        "type": "function",
        "name": "execute_python",
        "description": (
            "Execute Python code in a persistent session. "
            "State persists across calls. Use print() for output."
        ),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "code": {"type": "string"},
                "purpose": {"type": "string"},
            },
            "required": ["code", "purpose"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "finalize_result",
        "description": (
            "Return the final result object and stop. "
            "Before calling this, confirm that your rows table contains evidence "
            "drawn from multiple distinct sources in the repository — not just one "
            "or two items — and that you have used at least one search function "
            "to filter candidates before reading."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "rows": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "additionalProperties": {
                            "type": [
                                "string", "number", "integer", "boolean", "null",
                            ]
                        },
                    },
                },
                "summary": {"type": "string"},
            },
            "required": ["rows", "summary"],
            "additionalProperties": False,
        },
    },
]


# ---------------------------------------------------------------------------
# Token helpers
# ---------------------------------------------------------------------------

def _estimate_system_tokens(
    model: str,
    system_prompt: str,
    tools: list[dict[str, Any]],
) -> int:
    """Estimate token count for system prompt + tool definitions via tiktoken.

    This won't be perfectly exact — OpenAI adds internal framing tokens around
    instructions and tool schemas — but it's close enough (typically within
    ~10-20 tokens) to be useful for separating system overhead from
    conversation context.
    """
    try:
        enc = tiktoken.encoding_for_model(model)
    except KeyError:
        enc = tiktoken.get_encoding("cl100k_base")

    text = system_prompt + json.dumps(tools)
    return len(enc.encode(text))


def _extract_usage(response: Any) -> dict[str, int]:
    """Pull token counts from a responses API response, safely."""
    usage = getattr(response, "usage", None)
    if usage is None:
        return {"input": 0, "output": 0, "reasoning": 0}

    # Reasoning tokens are nested under output_tokens_details.
    output_details = getattr(usage, "output_tokens_details", None)
    reasoning = 0
    if output_details:
        reasoning = getattr(output_details, "reasoning_tokens", 0) or 0

    return {
        "input": getattr(usage, "input_tokens", 0) or 0,
        "output": getattr(usage, "output_tokens", 0) or 0,
        "reasoning": reasoning,
    }


# ---------------------------------------------------------------------------
# Core loop
# ---------------------------------------------------------------------------

class AgenticWorkflow:
    def __init__(
        self,
        client: OpenAI,
        model: str,
        system_prompt: str,
        vault_name: str | None = None,
        workflow_key: str | None = None,
        new_arango_db: bool = False,
        max_turns: int = 25,
        trace_output_dir: str | None = None,
        trace_filename_stem: str | None = None,
        reasoning: dict | None = None,
    ) -> None:
        self.client = client
        self.model = model
        self.max_turns = max_turns
        self.trace_output_dir = trace_output_dir
        self.trace_filename_stem = trace_filename_stem
        self.reasoning = reasoning
        self.executor = PythonExecutor()

        if vault_name is not None and workflow_key is not None:
            fn_names = list(dict.fromkeys(FUNCTION_EXPERIMENTS[workflow_key]))  # dedup, preserve order

            fn_desc_lines = [
                "\n\n## Available TableVault functions\n\n",
                "The following functions are pre-imported and available in your Python session. "
                "The vault is already assigned to the variable `vault`. "
                "Call them as e.g. `get_item(vault, 'my_list')`.\n\n",
            ]
            for name in fn_names:
                if name in FUNCTION_DESCRIPTIONS:
                    fn_desc_lines.append(f"### `{name}`\n```\n{FUNCTION_DESCRIPTIONS[name]}\n```\n\n")

            self.system_prompt = system_prompt + "".join(fn_desc_lines)

            # Run initialization inside the executor so that vault, the API key, and all
            # workflow functions are available as live variables in the session.
            fn_import_str = ", ".join(fn_names)
            setup_code = (
                f"from api_functions import initialization, {fn_import_str}\n"
                f"vault = initialization({repr(vault_name)}, new_arango_db={new_arango_db})\n"
            )
            setup_result = self.executor.run(setup_code)
            if not setup_result["ok"]:
                raise RuntimeError(
                    f"Vault setup failed:\n{setup_result.get('error') or setup_result.get('stderr')}"
                )
        else:
            self.system_prompt = system_prompt

        self.system_token_estimate = _estimate_system_tokens(
            model, self.system_prompt, TOOLS,
        )

    def run(self, task: str) -> dict[str, Any]:
        prev_id: str | None = None
        pending: list[dict[str, Any]] = [{"role": "user", "content": task}]
        no_tool_streak = 0
        metrics = RunMetrics(system_token_estimate=self.system_token_estimate)
        tracer = TraceLogger(task=task, model=self.model, system_prompt=self.system_prompt)

        def _turn_metrics_dict(
            usage: dict,
            conv_tokens: int,
            api_latency: float,
            exec_latency: float = 0.0,
        ) -> dict:
            return {
                "input_tokens": usage["input"],
                "output_tokens": usage["output"],
                "reasoning_tokens": usage["reasoning"],
                "conversation_tokens": conv_tokens,
                "api_latency_s": round(api_latency, 4),
                "exec_latency_s": round(exec_latency, 4),
            }

        try:
            for turn in range(self.max_turns):

                # --- API call (timed) ----------------------------------------
                t0 = time.perf_counter()
                create_kwargs: dict[str, Any] = dict(
                    model=self.model,
                    instructions=self.system_prompt,
                    input=pending,
                    previous_response_id=prev_id,
                    tools=TOOLS,
                    parallel_tool_calls=False,
                )
                if self.reasoning is not None:
                    create_kwargs["reasoning"] = self.reasoning
                response = self.client.responses.create(**create_kwargs)
                api_latency = time.perf_counter() - t0
                prev_id = response.id

                usage = _extract_usage(response)
                conv_tokens = max(0, usage["input"] - self.system_token_estimate)

                # Extract the single function call (parallel_tool_calls=False).
                call = next(
                    (
                        item for item in response.output
                        if getattr(item, "type", None) == "function_call"
                    ),
                    None,
                )

                # -- no tool call (nudge) ------------------------------------
                if call is None:
                    nudge_error = (
                        "Model did not call a tool. "
                        f"no_tool_streak will be {no_tool_streak + 1}."
                    )
                    metrics.turns.append(TurnMetrics(
                        turn=turn,
                        tool_name=None,
                        purpose=None,
                        input_tokens=usage["input"],
                        output_tokens=usage["output"],
                        reasoning_tokens=usage["reasoning"],
                        conversation_tokens=conv_tokens,
                        api_latency_s=api_latency,
                    ))
                    tracer.record_turn(
                        turn=turn,
                        pending_messages=pending,
                        previous_response_id=prev_id,
                        response=response,
                        tool_call_item=None,
                        tool_output=None,
                        metrics=_turn_metrics_dict(usage, conv_tokens, api_latency),
                        error=nudge_error,
                    )
                    no_tool_streak += 1
                    if no_tool_streak >= 3:
                        raise RuntimeError(
                            f"Model failed to call a tool {no_tool_streak} "
                            "times in a row.",
                        )
                    pending = [{
                        "role": "user",
                        "content": (
                            "You must call either `execute_python` or "
                            "`finalize_result` to proceed."
                        ),
                    }]
                    continue

                no_tool_streak = 0
                args = json.loads(call.arguments)

                # -- finalize ------------------------------------------------
                if call.name == "finalize_result":
                    metrics.turns.append(TurnMetrics(
                        turn=turn,
                        tool_name="finalize_result",
                        purpose=None,
                        input_tokens=usage["input"],
                        output_tokens=usage["output"],
                        reasoning_tokens=usage["reasoning"],
                        conversation_tokens=conv_tokens,
                        api_latency_s=api_latency,
                    ))
                    tracer.record_turn(
                        turn=turn,
                        pending_messages=pending,
                        previous_response_id=prev_id,
                        response=response,
                        tool_call_item=call,
                        tool_output=args,
                        metrics=_turn_metrics_dict(usage, conv_tokens, api_latency),
                    )
                    metrics_summary = metrics.summary()
                    tracer.finalize(final_result=args, metrics_summary=metrics_summary)
                    self._save_trace(tracer)
                    return {"result": args, "metrics": metrics, "tracer": tracer}

                # -- execute -------------------------------------------------
                if call.name == "execute_python":
                    code = args["code"]
                    purpose = args["purpose"]

                    t1 = time.perf_counter()
                    result = self.executor.run(code)
                    exec_latency = time.perf_counter() - t1

                    exec_error = None if result["ok"] else (
                        result.get("error") or result.get("stderr") or "Execution failed."
                    )
                    metrics.turns.append(TurnMetrics(
                        turn=turn,
                        tool_name="execute_python",
                        purpose=purpose,
                        input_tokens=usage["input"],
                        output_tokens=usage["output"],
                        reasoning_tokens=usage["reasoning"],
                        conversation_tokens=conv_tokens,
                        code_lines=len(code.splitlines()),
                        code_succeeded=result["ok"],
                        api_latency_s=api_latency,
                        exec_latency_s=exec_latency,
                    ))
                    tracer.record_turn(
                        turn=turn,
                        pending_messages=pending,
                        previous_response_id=prev_id,
                        response=response,
                        tool_call_item=call,
                        tool_output=result,
                        metrics=_turn_metrics_dict(usage, conv_tokens, api_latency, exec_latency),
                        error=exec_error,
                    )

                    pending = [{
                        "type": "function_call_output",
                        "call_id": call.call_id,
                        "output": json.dumps(result, default=str),
                    }]
                    continue

                raise ValueError(f"Unknown tool: {call.name}")

            raise RuntimeError("Max turns reached before finalize_result.")

        except Exception as exc:
            tracer.finalize(
                run_error=str(exc),
                metrics_summary=metrics.summary(),
            )
            self._save_trace(tracer)
            raise

    def _save_trace(self, tracer: TraceLogger) -> None:
        if self.trace_output_dir:
            json_path, md_path = tracer.save(
                self.trace_output_dir, self.trace_filename_stem
            )
            print(f"  trace saved -> {json_path}")
            print(f"  trace saved -> {md_path}")


# ---------------------------------------------------------------------------
# Example usage
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """\
You are a data analyst assistant with access to a TableVault repository, operating inside \
a persistent Python environment.

Your goal is to investigate the repository and extract **structured evidence**
relevant to the user task.

The final output should summarize the evidence stored in the TableVault
repository in the form of:

1. a **results table** (structured rows), and
2. a **scientific-style summary** interpreting that evidence.

The results table should represent **summary evidence extracted from the
repository**. Each row corresponds to a piece of evidence such as an experiment
result, dataset observation, workflow output, or other structured record.

Example result table schemas:

Example 1 — workflow evaluation evidence

[
  {
    "workflow": "baseline_xgboost",
    "model": "xgboost",
    "running_time": 132.4,
    "accuracy": 0.91
  },
  {
    "workflow": "llm_augmented_pipeline",
    "model": "gpt-4o-mini",
    "running_time": 245.8,
    "accuracy": 0.94
  }
]

Example 2 — sample-level classification evidence

[
  {
    "data_sample": "sample_001",
    "true_label": "sports",
    "predicted_label": "sports",
    "reasoning_strategy": "few-shot classification"
  },
  {
    "data_sample": "sample_002",
    "true_label": "business",
    "predicted_label": "technology",
    "reasoning_strategy": "two-step reasoning + classification"
  }
]

The columns depend on what evidence exists in the repository. Choose columns
that best summarize the relevant structured evidence. Don't include unnecessary columns.

------------------------------------------------------------

## What is TableVault?

TableVault is a centralized data repository (backed by ArangoDB) that stores
**item lists** — ordered collections of data items. Every item list has a
unique name and belongs to one of four types:

| Type          | Stores                                         |
|---------------|------------------------------------------------|
| **file**      | References (paths) to external files           |
| **document**  | Text strings (paragraphs, logs, notes, etc.)   |
| **embedding** | Fixed-dimension float vectors                  |
| **record**    | Structured rows (dict with predefined columns) |

------------------------------------------------------------

## How data gets into TableVault

Data is ingested by Python processes. A Python script or notebook initialises
a `Vault` object, and then calls `append_*` helpers to add items to the
relevant lists.

There may also be additional context about the lists stored in the repository.
Refer to the **Available TableVault functions** section to understand what
context is accessible.

------------------------------------------------------------

## Tools

- `execute_python`: run code in the persistent session (state persists across calls). \
Use `print()` for output.
- `finalize_result`: return the final result object and stop.

## Search strategy

Work in two phases:

**Phase 1 — Discovery:** Use only search and listing functions to identify
candidate item and code names. Do NOT read full item content yet (`get_item`
and `get_code` should not be called in this phase). Collect all plausible
candidates first, then assess which are relevant to the task.

**Phase 2 — Selection and reading:** From your candidates, select the most
representative subset that covers the different methodological conditions
relevant to the task. Read only that subset in detail. Avoid reading items
that are redundant with others already selected.

------------------------------------------------------------

## Rules

- Always act via tool calls — never put raw code in assistant text.
- On errors, read the traceback and fix the code.
- The variable `vault` and all listed TableVault functions are pre-imported and ready to use.
- **Do not make direct HuggingFace model calls** (e.g. do not use `transformers`, `pipeline`, or any HuggingFace inference API). All model inference results are pre-computed and stored in the TableVault repository — retrieve them from there instead.

------------------------------------------------------------

## Your output

When you have enough information, call `finalize_result` with exactly this shape:

{
  "rows": [
    {"column1": "value1", "column2": "value2"}
  ],
  "summary": "Scientific-style description of the evidence and interpretation."
}

------------------------------------------------------------

## Summary expectations

The **summary** should interpret the evidence in a research-style description.
It should explain:

• what the repository evidence suggests about the user's task
• key findings or patterns in the retrieved data
• notable issues, biases, or inconsistencies in existing workflows or results
• limitations or gaps in the available evidence
• how the returned table should be interpreted

The summary should read like a short analytical explanation of the evidence,
not just a description of the table.

------------------------------------------------------------
"""

if __name__ == "__main__":

    openai_key_file = "/Users/jinjinzhao/Documents/work_projects/my_keys/my_keys/openai_jinjin.key"
    with open(openai_key_file, 'r') as f:
        openai_key = f.read()
    os.environ["OPENAI_API_KEY"] = openai_key

    TASK = "For document classification with large language models, does few shot examples improve accuracy?"
    wf = AgenticWorkflow(
        client=OpenAI(),
        model="gpt-5.4",
        system_prompt=SYSTEM_PROMPT,
        vault_name="tv_experiment_1",    # passed to initialization()
        workflow_key="items_only",       # key in FUNCTION_EXPERIMENTS
        max_turns=20,
        trace_output_dir="traces",       # set to None to disable file saving
        trace_filename_stem=None,        # defaults to run timestamp
        reasoning=None, #reasoning={"effort": "medium"
    )
    output = wf.run(TASK)

    print("=== Result ===")
    print(json.dumps(output["result"], indent=2))

    print("\n=== Metrics ===")
    # Pass pricing for cost estimation (example rates — adjust to your model).
    print(json.dumps(output["metrics"].summary(
        input_cost_per_m=3.00,
        output_cost_per_m=15.00,
        reasoning_cost_per_m=15.00,
    ), indent=2))

    print("\n=== Per-turn breakdown ===")
    for t in output["metrics"].turns:
        status = ""
        if t.tool_name == "execute_python":
            status = f" | {t.code_lines} lines | {'ok' if t.code_succeeded else 'FAILED'}"
        print(
            f"  turn {t.turn}: {t.tool_name or '(no tool)'}"
            f" | in={t.input_tokens} (conv={t.conversation_tokens})"
            f" out={t.output_tokens} reason={t.reasoning_tokens}"
            f" | api={t.api_latency_s:.2f}s exec={t.exec_latency_s:.2f}s"
            f"{status}"
        )