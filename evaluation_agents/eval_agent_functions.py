"""Agentic workflow — API functions exposed as native tool calls."""

import json
import time
from typing import Any
import os

import tiktoken
from openai import OpenAI

from metrics import RunMetrics, TurnMetrics
from trace_logger import TraceLogger
from api_functions import (
    FUNCTION_DESCRIPTIONS, FUNCTION_EXPERIMENTS,
    get_item, get_item_names, get_code, get_code_names,
    code_search, embedding_search, record_search, document_search,
    description_search, description_embedding_search, properties_search,
    get_item_code_name, get_item_parent_names, get_item_children_names,
    get_item_description, get_item_properties,
    code_description_search, code_description_embedding_search, code_properties_search,
    get_code_description, get_code_properties,
    initialization,
)


# ---------------------------------------------------------------------------
# Tool schemas — one per API function (vault is injected, not exposed)
# ---------------------------------------------------------------------------

FUNCTION_TOOL_SCHEMAS: dict[str, dict[str, Any]] = {
    "get_item": {
        "type": "function",
        "name": "get_item",
        "description": FUNCTION_DESCRIPTIONS["get_item"],
        "parameters": {
            "type": "object",
            "properties": {
                "item_name": {"type": "string"},
                "start_position": {"type": ["integer", "null"]},
                "end_position": {"type": ["integer", "null"]},
            },
            "required": ["item_name"],
        },
    },
    "get_item_names": {
        "type": "function",
        "name": "get_item_names",
        "description": FUNCTION_DESCRIPTIONS["get_item_names"],
        "parameters": {
            "type": "object",
            "properties": {
                "item_type": {
                    "type": "string",
                    "enum": ["embedding_list", "document_list", "record_list", "file_list"],
                },
            },
            "required": ["item_type"],
        },
    },
    "get_code": {
        "type": "function",
        "name": "get_code",
        "description": FUNCTION_DESCRIPTIONS["get_code"],
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
            },
            "required": ["name"],
        },
    },
    "get_code_names": {
        "type": "function",
        "name": "get_code_names",
        "description": FUNCTION_DESCRIPTIONS["get_code_names"],
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    "code_search": {
        "type": "function",
        "name": "code_search",
        "description": FUNCTION_DESCRIPTIONS["code_search"],
        "parameters": {
            "type": "object",
            "properties": {
                "code": {"type": "string"},
            },
            "required": ["code"],
        },
    },
    "embedding_search": {
        "type": "function",
        "name": "embedding_search",
        "description": FUNCTION_DESCRIPTIONS["embedding_search"],
        "parameters": {
            "type": "object",
            "properties": {
                "embedding": {
                    "type": "array",
                    "items": {"type": "number"},
                    "description": "Pre-computed embedding vector (List[float]).",
                },
            },
            "required": ["embedding"],
        },
    },
    "record_search": {
        "type": "function",
        "name": "record_search",
        "description": FUNCTION_DESCRIPTIONS["record_search"],
        "parameters": {
            "type": "object",
            "properties": {
                "record_text": {"type": "string"},
            },
            "required": ["record_text"],
        },
    },
    "document_search": {
        "type": "function",
        "name": "document_search",
        "description": FUNCTION_DESCRIPTIONS["document_search"],
        "parameters": {
            "type": "object",
            "properties": {
                "document_text": {"type": "string"},
            },
            "required": ["document_text"],
        },
    },
    "description_search": {
        "type": "function",
        "name": "description_search",
        "description": FUNCTION_DESCRIPTIONS["description_search"],
        "parameters": {
            "type": "object",
            "properties": {
                "description_text": {"type": "string"},
            },
            "required": ["description_text"],
        },
    },
    "description_embedding_search": {
        "type": "function",
        "name": "description_embedding_search",
        "description": FUNCTION_DESCRIPTIONS["description_embedding_search"],
        "parameters": {
            "type": "object",
            "properties": {
                "description_text": {"type": "string"},
            },
            "required": ["description_text"],
        },
    },
    "properties_search": {
        "type": "function",
        "name": "properties_search",
        "description": FUNCTION_DESCRIPTIONS["properties_search"],
        "parameters": {
            "type": "object",
            "properties": {
                "description_text": {"type": "string"},
            },
            "required": ["description_text"],
        },
    },
    "get_item_code_name": {
        "type": "function",
        "name": "get_item_code_name",
        "description": FUNCTION_DESCRIPTIONS["get_item_code_name"],
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
            },
            "required": ["name"],
        },
    },
    "get_item_parent_names": {
        "type": "function",
        "name": "get_item_parent_names",
        "description": FUNCTION_DESCRIPTIONS["get_item_parent_names"],
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "start_position": {"type": ["integer", "null"]},
                "end_position": {"type": ["integer", "null"]},
            },
            "required": ["name"],
        },
    },
    "get_item_children_names": {
        "type": "function",
        "name": "get_item_children_names",
        "description": FUNCTION_DESCRIPTIONS["get_item_children_names"],
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "start_position": {"type": ["integer", "null"]},
                "end_position": {"type": ["integer", "null"]},
            },
            "required": ["name"],
        },
    },
    "get_item_description": {
        "type": "function",
        "name": "get_item_description",
        "description": FUNCTION_DESCRIPTIONS["get_item_description"],
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
            },
            "required": ["name"],
        },
    },
    "get_item_properties": {
        "type": "function",
        "name": "get_item_properties",
        "description": FUNCTION_DESCRIPTIONS["get_item_properties"],
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
            },
            "required": ["name"],
        },
    },
    "code_description_search": {
        "type": "function",
        "name": "code_description_search",
        "description": FUNCTION_DESCRIPTIONS["code_description_search"],
        "parameters": {
            "type": "object",
            "properties": {
                "description_text": {"type": "string"},
            },
            "required": ["description_text"],
        },
    },
    "code_description_embedding_search": {
        "type": "function",
        "name": "code_description_embedding_search",
        "description": FUNCTION_DESCRIPTIONS["code_description_embedding_search"],
        "parameters": {
            "type": "object",
            "properties": {
                "description_text": {"type": "string"},
            },
            "required": ["description_text"],
        },
    },
    "code_properties_search": {
        "type": "function",
        "name": "code_properties_search",
        "description": FUNCTION_DESCRIPTIONS["code_properties_search"],
        "parameters": {
            "type": "object",
            "properties": {
                "description_text": {"type": "string"},
            },
            "required": ["description_text"],
        },
    },
    "get_code_description": {
        "type": "function",
        "name": "get_code_description",
        "description": FUNCTION_DESCRIPTIONS["get_code_description"],
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
            },
            "required": ["name"],
        },
    },
    "get_code_properties": {
        "type": "function",
        "name": "get_code_properties",
        "description": FUNCTION_DESCRIPTIONS["get_code_properties"],
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
            },
            "required": ["name"],
        },
    },
}

FINALIZE_TOOL: dict[str, Any] = {
    "type": "function",
    "name": "finalize_result",
    "description": (
        "Return the final result object and stop. "
        "Call this once you have gathered sufficient evidence to answer the "
        "question well. Prefer targeted queries over broad exploration — "
        "more specific filters and searches reduce the number of calls needed "
        "and keep token usage low."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "rows": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": {
                        "type": ["string", "number", "integer", "boolean", "null"],
                    },
                },
            },
            "summary": {"type": "string"},
        },
        "required": ["rows", "summary"],
        "additionalProperties": False,
    },
}


def _build_tools(fn_names: list[str]) -> list[dict[str, Any]]:
    """Build the tools list for a given subset of function names, plus finalize_result."""
    tools = [
        FUNCTION_TOOL_SCHEMAS[name]
        for name in fn_names
        if name in FUNCTION_TOOL_SCHEMAS
    ]
    tools.append(FINALIZE_TOOL)
    return tools


# ---------------------------------------------------------------------------
# Function dispatcher
# ---------------------------------------------------------------------------

def _dispatch(fn_name: str, vault, args: dict) -> Any:
    """Route a tool call to the matching API function, injecting vault."""
    if fn_name == "get_item":
        return get_item(vault, args["item_name"], args.get("start_position"), args.get("end_position"))
    if fn_name == "get_item_names":
        return get_item_names(vault, args["item_type"])
    if fn_name == "get_code":
        return get_code(vault, args["name"])
    if fn_name == "get_code_names":
        return get_code_names(vault)
    if fn_name == "code_search":
        return code_search(vault, args["code"])
    if fn_name == "embedding_search":
        return embedding_search(vault, args["embedding"])
    if fn_name == "record_search":
        return record_search(vault, args["record_text"])
    if fn_name == "document_search":
        return document_search(vault, args["document_text"])
    if fn_name == "description_search":
        return description_search(vault, args["description_text"])
    if fn_name == "description_embedding_search":
        return description_embedding_search(vault, args["description_text"])
    if fn_name == "properties_search":
        return properties_search(vault, args["description_text"])
    if fn_name == "get_item_code_name":
        return get_item_code_name(vault, args["name"])
    if fn_name == "get_item_parent_names":
        return get_item_parent_names(vault, args["name"], args.get("start_position"), args.get("end_position"))
    if fn_name == "get_item_children_names":
        return get_item_children_names(vault, args["name"], args.get("start_position"), args.get("end_position"))
    if fn_name == "get_item_description":
        return get_item_description(vault, args["name"])
    if fn_name == "get_item_properties":
        return get_item_properties(vault, args["name"])
    if fn_name == "code_description_search":
        return code_description_search(vault, args["description_text"])
    if fn_name == "code_description_embedding_search":
        return code_description_embedding_search(vault, args["description_text"])
    if fn_name == "code_properties_search":
        return code_properties_search(vault, args["description_text"])
    if fn_name == "get_code_description":
        return get_code_description(vault, args["name"])
    if fn_name == "get_code_properties":
        return get_code_properties(vault, args["name"])
    raise ValueError(f"Unknown function: {fn_name}")


# ---------------------------------------------------------------------------
# Token helpers
# ---------------------------------------------------------------------------

def _estimate_system_tokens(
    model: str,
    system_prompt: str,
    tools: list[dict[str, Any]],
) -> int:
    try:
        enc = tiktoken.encoding_for_model(model)
    except KeyError:
        enc = tiktoken.get_encoding("cl100k_base")

    text = system_prompt + json.dumps(tools)
    return len(enc.encode(text))


def _extract_usage(response: Any) -> dict[str, int]:
    usage = getattr(response, "usage", None)
    if usage is None:
        return {"input": 0, "output": 0, "reasoning": 0}

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
        vault=None,
    ) -> None:
        self.client = client
        self.model = model
        self.max_turns = max_turns
        self.trace_output_dir = trace_output_dir
        self.trace_filename_stem = trace_filename_stem
        self.reasoning = reasoning
        self.vault = None

        if workflow_key is not None:
            if vault is not None:
                self.vault = vault
            elif vault_name is not None:
                self.vault = initialization(vault_name, new_arango_db=new_arango_db)

            fn_names = list(dict.fromkeys(FUNCTION_EXPERIMENTS[workflow_key]))
            self.tools = _build_tools(fn_names)
            self.fn_names_set = set(fn_names)

            self.system_prompt = system_prompt
        else:
            self.tools = [FINALIZE_TOOL]
            self.fn_names_set = set()
            self.system_prompt = system_prompt

        self.system_token_estimate = _estimate_system_tokens(
            model, self.system_prompt, self.tools,
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
                    tools=self.tools,
                    parallel_tool_calls=False,
                )
                if self.reasoning is not None:
                    create_kwargs["reasoning"] = self.reasoning
                response = self.client.responses.create(**create_kwargs)
                api_latency = time.perf_counter() - t0
                prev_id = response.id

                usage = _extract_usage(response)
                conv_tokens = max(0, usage["input"] - self.system_token_estimate)

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
                        "content": "You must call one of the available tools to proceed.",
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

                # -- API function call ----------------------------------------
                if call.name in self.fn_names_set:
                    t1 = time.perf_counter()
                    try:
                        fn_result = _dispatch(call.name, self.vault, args)
                        exec_error = None
                        tool_output = {"ok": True, "result": fn_result}
                    except Exception as exc:
                        exec_error = str(exc)
                        tool_output = {"ok": False, "error": exec_error}
                    exec_latency = time.perf_counter() - t1

                    metrics.turns.append(TurnMetrics(
                        turn=turn,
                        tool_name=call.name,
                        purpose=None,
                        input_tokens=usage["input"],
                        output_tokens=usage["output"],
                        reasoning_tokens=usage["reasoning"],
                        conversation_tokens=conv_tokens,
                        api_latency_s=api_latency,
                        exec_latency_s=exec_latency,
                    ))
                    tracer.record_turn(
                        turn=turn,
                        pending_messages=pending,
                        previous_response_id=prev_id,
                        response=response,
                        tool_call_item=call,
                        tool_output=tool_output,
                        metrics=_turn_metrics_dict(usage, conv_tokens, api_latency, exec_latency),
                        error=exec_error,
                    )

                    pending = [{
                        "type": "function_call_output",
                        "call_id": call.call_id,
                        "output": json.dumps(tool_output, default=str),
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
You are a data analyst assistant with access to a TableVault repository.

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
The available tool functions expose what context is accessible.

------------------------------------------------------------

## Tools

Call the available TableVault query functions directly as tool calls — you do
not need to write Python code. Use `finalize_result` to return the final answer.

------------------------------------------------------------

## Rules

- Always act via tool calls — never just describe what you would do.
- On errors, read the error message and retry with corrected arguments.
- **Do not make direct HuggingFace model calls** — all model inference results
  are pre-computed and stored in the TableVault repository. Retrieve them there.
- **Minimize token usage**: gather enough evidence to answer the question well,
  then stop. More specific queries and filters reduce the number of calls needed —
  prefer targeted searches over broad scans. Stop as soon as you have sufficient
  evidence to give a confident, well-supported answer.

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
        model="gpt-4o",
        system_prompt=SYSTEM_PROMPT,
        vault_name="tv_experiment_1",
        workflow_key="items_only",
        max_turns=20,
        trace_output_dir="traces",
        trace_filename_stem=None,
        reasoning=None,
    )
    output = wf.run(TASK)

    print("=== Result ===")
    print(json.dumps(output["result"], indent=2))

    print("\n=== Metrics ===")
    print(json.dumps(output["metrics"].summary(
        input_cost_per_m=3.00,
        output_cost_per_m=15.00,
        reasoning_cost_per_m=15.00,
    ), indent=2))

    print("\n=== Per-turn breakdown ===")
    for t in output["metrics"].turns:
        print(
            f"  turn {t.turn}: {t.tool_name or '(no tool)'}"
            f" | in={t.input_tokens} (conv={t.conversation_tokens})"
            f" out={t.output_tokens} reason={t.reasoning_tokens}"
            f" | api={t.api_latency_s:.2f}s exec={t.exec_latency_s:.2f}s"
        )
