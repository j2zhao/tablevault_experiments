"""
TableVault Query Agent
======================
An LLM-powered workflow that queries a TableVault repository using OpenAI
function-calling. The model receives a task prompt, explores the repository
through read-only API calls, and returns a structured result containing
a result table (list of dicts) plus a summary.
The result table summarizes the evide

This prototype writes one trace bundle per run:
- a JSONL file for structured debugging
- a Markdown file for human-readable inspection

Usage:
    from tablevault_agent import run_agent
    from tablevault import Vault

    vault = Vault(user_id="analyst", process_name="query_agent", ...)
    table = run_agent(vault, "Find all experiment results with accuracy > 0.9")
"""

from __future__ import annotations

import datetime
import json
import logging
import uuid
from pathlib import Path
from typing import Any

import openai
import pandas as pd
import os

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# 1. System prompt
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
unique name and belongs to one of five types:

| Type          | Stores                                         |
|---------------|------------------------------------------------|
| **file**      | References (paths) to external files           |
| **document**  | Text strings (paragraphs, logs, notes, etc.)   |
| **embedding** | Fixed-dimension float vectors                  |
| **record**    | Structured rows (dict with predefined columns) |
| **process**   | Auto-captured Python code that ran in the repo |

------------------------------------------------------------

## How data gets into TableVault

Data is ingested by Python **processes**. When a Python script or notebook
initialises a `Vault` object, all code executed afterward is automatically
tracked as a *process list*. The code then calls `append_*` helpers to add
items to the relevant lists.

Crucially, each appended item can declare **input_items** — pointers to
positions in other item lists that were used to produce it. This creates a
**lineage graph**: you can trace any item back to the code and upstream data
that generated it, or forward to all downstream items that depend on it.

Processes can also be hierarchical: a parent process can spawn child
processes, and that relationship is recorded.

Item lists may also carry **descriptions** — free-text annotations paired
with embedding vectors — so you can search for lists by semantic similarity.

------------------------------------------------------------

## Your available tools

You have read-only query tools. Use them to explore the repository, retrieve
data, trace lineage, and gather whatever you need to fulfil the user's task.

### Discovery & metadata
- `query_item_list`        — get metadata (n_items, length, …) for a named list

### Content retrieval
- `query_item_content`     — fetch actual item data

### Lineage: code ↔ items
- `query_item_creation_process` — which process created a list
- `query_item_process`          — which processes modified a list
- `query_process_item`          — which items a process created or modified

### Lineage: data ↔ data
- `query_item_parent`  — upstream input dependencies of a list
- `query_item_child`   — downstream items derived from a list

### Descriptions
- `query_item_description` — get text descriptions attached to a list

### Type-specific search (search across all lists of a type)
- `query_file_list`      — search file lists by description / code text
- `query_document_list`  — search document lists by content / description / code
- `query_record_list`    — search record lists by content / description / code
- `query_process_list`   — search processes by code content / parent code / description

Each search tool accepts optional filters:
  • `description_text`       — token match on descriptions
  • `description_query_text` — natural-language query that will be embedded for description similarity
  • `code_text`              — token match on the generating Python code
  • `filtered`               — restrict to specific list names

Embedding-list similarity search is currently disabled, so do not attempt to
search embedding lists directly.

------------------------------------------------------------

## Your workflow

1. **Explore**
   Start by discovering what lists exist using the type-search tools and
   reading their descriptions. Unless necessary, avoid searching without
   filters since there could be a large number of lists.

2. **Drill down**
   Fetch item content, inspect record structures, trace lineage, or perform
   filtered searches to gather the evidence needed for the task.

3. **Interpret evidence**
   Identify patterns, results, or observations relevant to the user’s task.

4. **Finish**
   When you have enough information, STOP calling tools and return a JSON
   object with exactly this shape:

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

• what the repository evidence suggests about the user’s task  
• key findings or patterns in the retrieved data  
• notable issues, biases, or inconsistencies in existing workflows or results  
• limitations or gaps in the available evidence  
• how the returned table should be interpreted  

The summary should read like a short analytical explanation of the evidence,
not just a description of the table.

------------------------------------------------------------

## Important rules

- Always prefer structured exploration over guessing.
- Do not invent list names, process names, column names, or values.
- If the repository does not contain enough information, return:
  {"rows": [], "summary": "...explanation..."}
- Do not wrap the final JSON in markdown fences.
- Do not call any terminal tool. The final answer must be plain JSON.
"""
# ---------------------------------------------------------------------------
# 2. OpenAI tool definitions
# ---------------------------------------------------------------------------

TOOLS: list[dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "query_item_list",
            "description": "Get metadata for a named item list (e.g. n_items, length, type).",
            "parameters": {
                "type": "object",
                "properties": {
                    "item_name": {
                        "type": "string",
                        "description": "Name of the item list.",
                    }
                },
                "required": ["item_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "query_item_content",
            "description": (
                "Retrieve actual data from an item list. "
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "item_name": {
                        "type": "string",
                        "description": "Name of the item list.",
                    },
                },
                "required": ["item_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "query_item_creation_process",
            "description": "Get the process that originally created an item list.",
            "parameters": {
                "type": "object",
                "properties": {
                    "item_name": {
                        "type": "string",
                        "description": "Name of the item list.",
                    }
                },
                "required": ["item_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "query_item_process",
            "description": (
                "Get all processes that modified an item list. "
                "Optionally filter by position range."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "item_name": {
                        "type": "string",
                        "description": "Name of the item list.",
                    }
                },
                "required": ["item_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "query_process_item",
            "description": "Get all items created or modified by a named process.",
            "parameters": {
                "type": "object",
                "properties": {
                    "process_name": {
                        "type": "string",
                        "description": "Name of the process.",
                    }
                },
                "required": ["process_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "query_item_parent",
            "description": (
                "Get upstream input dependencies of an item list. "
                "Optionally filter by position range."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "item_name": {
                        "type": "string",
                        "description": "Name of the item list.",
                    }
                },
                "required": ["item_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "query_item_child",
            "description": (
                "Get downstream items derived from an item list. "
                "Optionally filter by position range."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "item_name": {
                        "type": "string",
                        "description": "Name of the item list.",
                    }
                },
                "required": ["item_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "query_item_description",
            "description": "Get text descriptions attached to an item list.",
            "parameters": {
                "type": "object",
                "properties": {
                    "item_name": {
                        "type": "string",
                        "description": "Name of the item list.",
                    }
                },
                "required": ["item_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "query_file_list",
            "description": (
                "Search across ALL file lists in the repository. "
                "Filter by description text, semantic description query text, "
                "generating code text, or restrict to named lists."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "description_text": {
                        "type": "string",
                        "description": "Token match on descriptions.",
                    },
                    "description_query_text": {
                        "type": "string",
                        "description": "Natural-language query to embed for description similarity search.",
                    },
                    "code_text": {
                        "type": "string",
                        "description": "Token match on generating code.",
                    },
                    "filtered": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Restrict to these list names.",
                    },
                },
                "required": [],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "query_document_list",
            "description": (
                "Search across ALL document lists by text content, "
                "description, or generating code."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "document_text": {
                        "type": "string",
                        "description": "Text to search in document content.",
                    },
                    "description_text": {
                        "type": "string",
                        "description": "Token match on descriptions.",
                    },
                    "description_query_text": {
                        "type": "string",
                        "description": "Natural-language query to embed for description similarity search.",
                    },
                    "code_text": {
                        "type": "string",
                        "description": "Token match on generating code.",
                    },
                    "filtered": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Restrict to these list names.",
                    },
                },
                "required": [],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "query_record_list",
            "description": (
                "Search across ALL record lists by text content, "
                "description, or generating code."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "record_text": {
                        "type": "string",
                        "description": "Text to search in record data.",
                    },
                    "description_text": {
                        "type": "string",
                        "description": "Token match on descriptions.",
                    },
                    "description_query_text": {
                        "type": "string",
                        "description": "Natural-language query to embed for description similarity search.",
                    },
                    "code_text": {
                        "type": "string",
                        "description": "Token match on generating code.",
                    },
                    "filtered": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Restrict to these list names.",
                    },
                },
                "required": [],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "query_process_list",
            "description": (
                "Search across ALL process lists by code content, "
                "parent code, or description."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "code_text": {
                        "type": "string",
                        "description": "Text to search in process code.",
                    },
                    "parent_code_text": {
                        "type": "string",
                        "description": "Text to search in parent process code.",
                    },
                    "description_text": {
                        "type": "string",
                        "description": "Token match on descriptions.",
                    },
                    "description_query_text": {
                        "type": "string",
                        "description": "Natural-language query to embed for description similarity search.",
                    },
                    "filtered": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Restrict to these process names.",
                    },
                },
                "required": [],
            },
        },
    },
]

# ---------------------------------------------------------------------------
# 3. Trace helpers
# ---------------------------------------------------------------------------


def _utc_now() -> str:
    return datetime.datetime.now(datetime.UTC).isoformat()


def _make_run_paths(trace_dir: str | Path, trace_prefix: str) -> tuple[str, Path, Path]:
    base_dir = Path(trace_dir)
    base_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.datetime.now(datetime.UTC).strftime("%Y%m%dT%H%M%SZ")
    short_id = uuid.uuid4().hex[:8]
    run_id = f"{trace_prefix}_{ts}_{short_id}"

    jsonl_path = base_dir / f"{run_id}.jsonl"
    md_path = base_dir / f"{run_id}.md"
    return run_id, jsonl_path, md_path


def _append_jsonl(path: Path | None, event: dict[str, Any]) -> None:
    if path is None:
        return
    payload = {"ts": _utc_now(), **event}
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, default=str) + "\n")


def _md_code_block(label: str, obj: Any) -> str:
    body = json.dumps(obj, indent=2, default=str, ensure_ascii=False)
    return f"**{label}**\n\n```json\n{body}\n```\n"


def _append_md(path: Path | None, text: str) -> None:
    if path is None:
        return
    with path.open("a", encoding="utf-8") as f:
        f.write(text)


def _init_markdown_trace(
    md_path: Path | None,
    *,
    run_id: str,
    task: str,
    model: str,
    embedding_model: str,
    max_iterations: int,
) -> None:
    if md_path is None:
        return

    header = (
        f"# TableVault Agent Trace\n\n"
        f"- **run_id:** `{run_id}`\n"
        f"- **started_at:** `{_utc_now()}`\n"
        f"- **model:** `{model}`\n"
        f"- **embedding_model:** `{embedding_model}`\n"
        f"- **max_iterations:** `{max_iterations}`\n\n"
        f"## Task\n\n"
        f"```text\n{task}\n```\n\n"
        f"---\n\n"
    )
    _append_md(md_path, header)


def _assistant_message_to_trace_dict(message: Any) -> dict[str, Any]:
    tool_calls = []
    if getattr(message, "tool_calls", None):
        for tc in message.tool_calls:
            tool_calls.append(
                {
                    "id": tc.id,
                    "name": tc.function.name,
                    "arguments_raw": tc.function.arguments,
                }
            )

    return {
        "role": "assistant",
        "content": message.content,
        "tool_calls": tool_calls,
    }


def _append_markdown_event(
    md_path: Path | None,
    *,
    iteration: int | None,
    title: str,
    payload: Any,
) -> None:
    if md_path is None:
        return

    parts = []
    if iteration is not None:
        parts.append(f"## Iteration {iteration} — {title}\n\n")
    else:
        parts.append(f"## {title}\n\n")
    parts.append(_md_code_block("Payload", payload))
    parts.append("\n---\n\n")
    _append_md(md_path, "".join(parts))


# ---------------------------------------------------------------------------
# 4. Agent helpers
# ---------------------------------------------------------------------------


def _tool_error(error_type: str, message: str) -> str:
    return json.dumps(
        {
            "ok": False,
            "error_type": error_type,
            "error": message,
        }
    )


def _tool_ok(result: Any) -> str:
    return json.dumps({"ok": True, "result": result}, default=str)


def _parse_json_object(raw: str) -> dict[str, Any]:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON arguments: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError("Tool arguments must decode to a JSON object.")

    return data


def _parse_final_response(raw: str) -> dict[str, Any]:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Final response is not valid JSON: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError("Final response must be a JSON object.")
    if "rows" not in data:
        raise ValueError("Final response must contain a 'rows' field.")
    if "summary" not in data:
        raise ValueError("Final response must contain a 'summary' field.")

    rows = data["rows"]
    summary = data["summary"]

    if not isinstance(rows, list):
        raise ValueError("'rows' must be a list.")
    if not isinstance(summary, str):
        raise ValueError("'summary' must be a string.")

    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ValueError(f"rows[{i}] must be an object.")

    return data


def embed_text(
    client: openai.OpenAI,
    text: str,
    *,
    model: str = "text-embedding-3-large",
) -> list[float]:
    response = client.embeddings.create(
        model=model,
        input=text,
    )
    return response.data[0].embedding


def _prepare_vault_arguments(
    name: str,
    arguments: dict[str, Any],
    *,
    embedding_client: openai.OpenAI,
    embedding_model: str,
) -> dict[str, Any]:
    prepared = dict(arguments)

    if name in {
        "query_file_list",
        "query_document_list",
        "query_record_list",
        "query_process_list",
    }:
        description_query_text = prepared.pop("description_query_text", None)
        if description_query_text:
            prepared["description_embedding"] = embed_text(
                embedding_client,
                description_query_text,
                model=embedding_model,
            )

    return prepared


# ---------------------------------------------------------------------------
# 5. Tool dispatcher
# ---------------------------------------------------------------------------


def dispatch_tool_call(
    vault: Any,
    name: str,
    arguments: dict[str, Any],
    *,
    embedding_client: openai.OpenAI,
    embedding_model: str,
) -> str:
    """
    Execute *name* with *arguments* against *vault*.

    Returns
    -------
    str
        JSON string of the tool output.
    """

    method = getattr(vault, name, None)
    if method is None:
        return _tool_error("unknown_tool", f"Unknown tool: {name}")

    try:
        prepared_arguments = _prepare_vault_arguments(
            name,
            arguments,
            embedding_client=embedding_client,
            embedding_model=embedding_model,
        )
        result = method(**prepared_arguments)
        return _tool_ok(result)
    except Exception as exc:
        logger.warning("Tool %s raised: %s", name, exc)
        return _tool_error("tool_execution_error", str(exc))


# ---------------------------------------------------------------------------
# 6. Agent loop
# ---------------------------------------------------------------------------


def run_agent(
    vault: Any,
    task: str,
    *,
    model: str = "gpt-4o",
    embedding_model: str = "text-embedding-3-small",
    max_iterations: int = 25,
    openai_client: openai.OpenAI | None = None,
    trace_dir: str | Path = "agent_traces",
    trace_prefix: str = "tablevault_agent",
) -> pd.DataFrame:
    """
    Run the query agent.

    Parameters
    ----------
    vault : tablevault.Vault
        An already-initialised Vault instance connected to the repository.
    task : str
        Natural-language description of what data to gather / produce.
    model : str
        OpenAI model name (must support function calling).
    embedding_model : str
        OpenAI embedding model name used to convert description_query_text
        into description_embedding.
    max_iterations : int
        Safety cap on LLM round-trips.
    openai_client : openai.OpenAI | None
        Optional pre-configured client. If None a default client is created.
    trace_dir : str | Path
        Directory to store one trace bundle per run.
    trace_prefix : str
        Prefix for trace filenames.

    Returns
    -------
    pd.DataFrame
        The result table produced by the agent.
    """
    client = openai_client or openai.OpenAI()

    run_id, jsonl_path, md_path = _make_run_paths(trace_dir, trace_prefix)

    messages: list[dict[str, Any]] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": task},
    ]

    _init_markdown_trace(
        md_path,
        run_id=run_id,
        task=task,
        model=model,
        embedding_model=embedding_model,
        max_iterations=max_iterations,
    )

    _append_jsonl(
        jsonl_path,
        {
            "event": "run_started",
            "run_id": run_id,
            "task": task,
            "model": model,
            "embedding_model": embedding_model,
            "max_iterations": max_iterations,
            "jsonl_path": str(jsonl_path),
            "md_path": str(md_path),
        },
    )

    _append_markdown_event(
        md_path,
        iteration=None,
        title="Run Started",
        payload={
            "run_id": run_id,
            "task": task,
            "model": model,
            "embedding_model": embedding_model,
            "max_iterations": max_iterations,
            "jsonl_path": str(jsonl_path),
            "md_path": str(md_path),
        },
    )

    logger.info("Tracing to %s and %s", jsonl_path, md_path)

    for iteration in range(1, max_iterations + 1):
        logger.info("--- iteration %d ---", iteration)

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
        )

        assistant_msg = response.choices[0].message
        messages.append(assistant_msg.model_dump())

        assistant_payload = _assistant_message_to_trace_dict(assistant_msg)

        _append_jsonl(
            jsonl_path,
            {
                "event": "assistant_message",
                "iteration": iteration,
                "message": assistant_payload,
            },
        )
        _append_markdown_event(
            md_path,
            iteration=iteration,
            title="Assistant Message",
            payload=assistant_payload,
        )

        if assistant_msg.tool_calls:
            for tc in assistant_msg.tool_calls:
                fn_name = tc.function.name

                try:
                    fn_args = _parse_json_object(tc.function.arguments)
                except Exception as exc:
                    result_json = _tool_error("invalid_tool_json", str(exc))

                    err_payload = {
                        "tool": fn_name,
                        "arguments_raw": tc.function.arguments,
                        "error": str(exc),
                    }

                    _append_jsonl(
                        jsonl_path,
                        {
                            "event": "tool_argument_parse_error",
                            "iteration": iteration,
                            **err_payload,
                        },
                    )
                    _append_markdown_event(
                        md_path,
                        iteration=iteration,
                        title=f"Tool Argument Parse Error: {fn_name}",
                        payload=err_payload,
                    )

                    messages.append(
                        {
                            "role": "tool",
                            "tool_call_id": tc.id,
                            "content": result_json,
                        }
                    )
                    continue

                logger.info("Tool call: %s(%s)", fn_name, fn_args)

                _append_jsonl(
                    jsonl_path,
                    {
                        "event": "tool_call",
                        "iteration": iteration,
                        "tool": fn_name,
                        "arguments": fn_args,
                    },
                )
                _append_markdown_event(
                    md_path,
                    iteration=iteration,
                    title=f"Tool Call: {fn_name}",
                    payload=fn_args,
                )

                result_json = dispatch_tool_call(
                    vault,
                    fn_name,
                    fn_args,
                    embedding_client=client,
                    embedding_model=embedding_model,
                )

                try:
                    traced_result = json.loads(result_json)
                except json.JSONDecodeError:
                    traced_result = {"raw": result_json}

                _append_jsonl(
                    jsonl_path,
                    {
                        "event": "tool_result",
                        "iteration": iteration,
                        "tool": fn_name,
                        "result": traced_result,
                    },
                )
                _append_markdown_event(
                    md_path,
                    iteration=iteration,
                    title=f"Tool Result: {fn_name}",
                    payload=traced_result,
                )

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tc.id,
                        "content": result_json,
                    }
                )

            continue

        final_content = assistant_msg.content
        if isinstance(final_content, list):
            final_text = "".join(
                part.get("text", "")
                for part in final_content
                if isinstance(part, dict) and part.get("type") == "text"
            )
        else:
            final_text = final_content or ""

        try:
            final_payload = _parse_final_response(final_text)
        except Exception as exc:
            error_payload = {
                "raw_content": final_text,
                "error": str(exc),
            }

            _append_jsonl(
                jsonl_path,
                {
                    "event": "final_output_parse_error",
                    "iteration": iteration,
                    **error_payload,
                },
            )
            _append_markdown_event(
                md_path,
                iteration=iteration,
                title="Final Output Parse Error",
                payload=error_payload,
            )

            if iteration == max_iterations:
                fail_payload = {
                    "error": (
                        "Model did not return valid final JSON output. "
                        f"Last content: {final_text!r}. Error: {exc}"
                    )
                }
                _append_jsonl(jsonl_path, {"event": "run_failed", **fail_payload})
                _append_markdown_event(
                    md_path,
                    iteration=None,
                    title="Run Failed",
                    payload=fail_payload,
                )
                raise RuntimeError(fail_payload["error"]) from exc

            messages.append(
                {
                    "role": "user",
                    "content": (
                        "You must now stop calling tools and return only a JSON object "
                        "with exactly two top-level fields: 'rows' and 'summary'. "
                        "Do not use markdown fences."
                    ),
                }
            )
            continue

        rows = final_payload.get("rows", [])
        summary = final_payload.get("summary", "")

        if summary:
            logger.info("Agent summary: %s", summary)

        _append_jsonl(
            jsonl_path,
            {
                "event": "final_output",
                "iteration": iteration,
                "payload": final_payload,
            },
        )
        _append_markdown_event(
            md_path,
            iteration=iteration,
            title="Final Output",
            payload=final_payload,
        )

        finish_payload = {
            "rows_count": len(rows),
            "summary": summary,
            "jsonl_path": str(jsonl_path),
            "md_path": str(md_path),
        }
        _append_jsonl(jsonl_path, {"event": "run_finished", **finish_payload})
        _append_markdown_event(
            md_path,
            iteration=None,
            title="Run Finished",
            payload=finish_payload,
        )

        logger.info("Saved trace bundle: %s , %s", jsonl_path, md_path)
        return pd.DataFrame(rows)

    fail_payload = {
        "error": f"Reached max iterations ({max_iterations}) without a valid result."
    }
    _append_jsonl(jsonl_path, {"event": "run_failed", **fail_payload})
    _append_markdown_event(
        md_path,
        iteration=None,
        title="Run Failed",
        payload=fail_payload,
    )
    raise RuntimeError(fail_payload["error"])


# ---------------------------------------------------------------------------
# 7. CLI convenience
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    from tablevault import Vault

    # -----------------------------
    # Hardcoded configuration
    # -----------------------------
    TASK = "For document classification with large language models, does few shot examples improve accuracy?"
    MODEL = "gpt-5.4"
    EMBEDDING_MODEL = "text-embedding-3-large"
    MAX_ITERATIONS = 50

    USER_ID = "agent"
    PROCESS_NAME = f"query_agent_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"

    ARANGO_URL = "http://localhost:8629"
    ARANGO_DB = "tv_experiment_1"
    ARANGO_USER = "tablevault_user"
    ARANGO_PASS = "tablevault_password"

    TRACE_DIR = "agent_traces"
    TRACE_PREFIX = "tablevault_agent"

    #OUTPUT_CSV = None
    # Example:
    OUTPUT_CSV = "results.csv"

    # -----------------------------
    # OpenAI Key
    # -----------------------------

    openai_key_file = "/Users/jinjinzhao/Documents/work_projects/my_keys/my_keys/openai_jinjin.key"
    with open(openai_key_file, 'r') as f:
        openai_key = f.read()

    os.environ["OPENAI_API_KEY"] = openai_key

    # -----------------------------
    # Vault connection
    # -----------------------------
    vault = Vault(
        user_id=USER_ID,
        process_name=PROCESS_NAME,
        arango_url=ARANGO_URL,
        arango_db=ARANGO_DB,
        arango_username=ARANGO_USER,
        arango_password=ARANGO_PASS,
        new_arango_db=False,
    )

    # -----------------------------
    # Run agent
    # -----------------------------
    df = run_agent(
        vault,
        TASK,
        model=MODEL,
        embedding_model=EMBEDDING_MODEL,
        max_iterations=MAX_ITERATIONS,
        trace_dir=TRACE_DIR,
        trace_prefix=TRACE_PREFIX,
    )

    # -----------------------------
    # Output
    # -----------------------------
    if OUTPUT_CSV:
        df.to_csv(OUTPUT_CSV, index=False)
        print(f"Saved {len(df)} rows to {OUTPUT_CSV}")
    else:
        print(df.to_string(index=False))