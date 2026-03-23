"""Structured trace logging for agentic workflow runs.

Each turn records:
  - model_input:  the pending messages sent to the API
  - model_output: serialized response output items (text, function_call, etc.)
  - tool_call:    parsed tool name + arguments (None if no tool was called)
  - tool_output:  result returned to the model (executor output or finalize args)
  - metrics:      token counts and latencies
  - error:        any exception or nudge-error string for this turn

Call pattern:
    logger = TraceLogger(task, model, system_prompt)
    logger.record_turn(...)          # once per turn — also prints to stdout
    logger.finalize(final_result, run_error, metrics_summary)
    logger.save(output_dir, stem)    # writes <stem>.json and <stem>.md
"""

from __future__ import annotations

import json
import os
import textwrap
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class TurnTrace:
    turn: int
    model_input: dict                    # {"pending_messages": [...], "previous_response_id": ...}
    model_output: dict                   # {"response_id": ..., "output_items": [...]}
    tool_call: dict | None               # {"name": ..., "call_id": ..., "arguments": {...}} | None
    tool_output: dict | None             # executor result dict, finalize args, or None
    metrics: dict                        # token counts + latencies
    error: str | None = None             # exception text or nudge-error description


@dataclass
class RunTrace:
    run_id: str
    task: str
    model: str
    system_prompt: str
    timestamp: str                        # ISO-8601 UTC
    turns: list[TurnTrace] = field(default_factory=list)
    final_result: dict | None = None
    run_error: str | None = None
    metrics_summary: dict | None = None


# ---------------------------------------------------------------------------
# Serialisation helpers
# ---------------------------------------------------------------------------

def _serialise_output_item(item: Any) -> dict:
    """Convert an OpenAI response output item to a plain dict."""
    item_type = getattr(item, "type", None)

    if item_type == "function_call":
        raw_args = getattr(item, "arguments", "{}")
        try:
            parsed_args = json.loads(raw_args) if isinstance(raw_args, str) else raw_args
        except json.JSONDecodeError:
            parsed_args = raw_args
        return {
            "type": "function_call",
            "name": getattr(item, "name", None),
            "call_id": getattr(item, "call_id", None),
            "arguments": parsed_args,
        }

    if item_type in ("text", "message"):
        return {
            "type": item_type,
            "text": getattr(item, "text", None) or getattr(item, "content", None),
        }

    if item_type == "reasoning":
        # Reasoning items contain a list of summary objects
        summaries = getattr(item, "summary", []) or []
        return {
            "type": "reasoning",
            "summary": [getattr(s, "text", str(s)) for s in summaries],
        }

    # Fallback: dump whatever attributes exist
    try:
        return {"type": item_type, **item.__dict__}
    except AttributeError:
        return {"type": item_type, "raw": str(item)}


# ---------------------------------------------------------------------------
# TraceLogger
# ---------------------------------------------------------------------------

class TraceLogger:
    def __init__(self, task: str, model: str, system_prompt: str) -> None:
        self._trace = RunTrace(
            run_id=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
            task=task,
            model=model,
            system_prompt=system_prompt,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def record_turn(
        self,
        *,
        turn: int,
        pending_messages: list[dict],
        previous_response_id: str | None,
        response: Any,                      # raw OpenAI response object
        tool_call_item: Any | None,         # the function_call output item, or None
        tool_output: dict | None,           # executor result or finalize args
        metrics: dict,
        error: str | None = None,
    ) -> None:
        """Record one turn and immediately print it to stdout."""
        output_items = [_serialise_output_item(i) for i in (response.output or [])]

        # Build tool_call summary from the function_call item
        tool_call: dict | None = None
        if tool_call_item is not None:
            raw_args = getattr(tool_call_item, "arguments", "{}")
            try:
                parsed = json.loads(raw_args) if isinstance(raw_args, str) else raw_args
            except json.JSONDecodeError:
                parsed = raw_args
            tool_call = {
                "name": getattr(tool_call_item, "name", None),
                "call_id": getattr(tool_call_item, "call_id", None),
                "arguments": parsed,
            }

        tt = TurnTrace(
            turn=turn,
            model_input={
                "pending_messages": pending_messages,
                "previous_response_id": previous_response_id,
            },
            model_output={
                "response_id": getattr(response, "id", None),
                "output_items": output_items,
            },
            tool_call=tool_call,
            tool_output=tool_output,
            metrics=metrics,
            error=error,
        )
        self._trace.turns.append(tt)
        self._print_turn(tt)

    def finalize(
        self,
        final_result: dict | None = None,
        run_error: str | None = None,
        metrics_summary: dict | None = None,
    ) -> None:
        self._trace.final_result = final_result
        self._trace.run_error = run_error
        self._trace.metrics_summary = metrics_summary
        self._print_run_footer()

    def save(self, output_dir: str, stem: str | None = None) -> tuple[str, str]:
        """Write <stem>.json and <stem>.md to output_dir. Returns (json_path, md_path)."""
        os.makedirs(output_dir, exist_ok=True)
        stem = stem or self._trace.run_id

        json_path = os.path.join(output_dir, f"{stem}.json")
        md_path = os.path.join(output_dir, f"{stem}.md")

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(self._to_dict(), f, indent=2, default=str)

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(self._to_markdown())

        return json_path, md_path

    def to_dict(self) -> dict:
        return self._to_dict()

    # ------------------------------------------------------------------
    # Internal rendering
    # ------------------------------------------------------------------

    def _to_dict(self) -> dict:
        t = self._trace
        return {
            "run_id": t.run_id,
            "timestamp": t.timestamp,
            "model": t.model,
            "task": t.task,
            "system_prompt": t.system_prompt,
            "turns": [asdict(turn) for turn in t.turns],
            "final_result": t.final_result,
            "run_error": t.run_error,
            "metrics_summary": t.metrics_summary,
        }

    # --- Markdown helpers ---

    @staticmethod
    def _code_block(content: str, lang: str = "") -> str:
        return f"```{lang}\n{content}\n```"

    @staticmethod
    def _json_block(obj: Any) -> str:
        return TraceLogger._code_block(json.dumps(obj, indent=2, default=str), "json")

    def _turn_md(self, tt: TurnTrace) -> str:
        lines: list[str] = []
        status_icon = "ERROR" if tt.error else ("ok" if tt.tool_call else "no-tool")
        tool_label = tt.tool_call["name"] if tt.tool_call else "(no tool called)"
        lines.append(f"## Turn {tt.turn} — `{tool_label}` [{status_icon}]")
        lines.append("")

        # --- Model input ---
        lines.append("### Model Input")
        msgs = tt.model_input.get("pending_messages", [])
        prev_id = tt.model_input.get("previous_response_id")
        lines.append(f"**previous_response_id:** `{prev_id}`")
        lines.append("")
        lines.append("**Pending messages:**")
        lines.append(self._json_block(msgs))
        lines.append("")

        # --- Model output ---
        lines.append("### Model Output")
        lines.append(f"**response_id:** `{tt.model_output.get('response_id')}`")
        lines.append("")
        lines.append("**Output items:**")
        lines.append(self._json_block(tt.model_output.get("output_items", [])))
        lines.append("")

        # --- Tool call ---
        lines.append("### Tool Call")
        if tt.tool_call:
            lines.append(f"**Tool:** `{tt.tool_call['name']}` | **call_id:** `{tt.tool_call['call_id']}`")
            lines.append("")
            lines.append("**Arguments:**")
            args = tt.tool_call.get("arguments", {})
            # For execute_python show code in its own block
            if tt.tool_call["name"] == "execute_python":
                code = args.get("code", "")
                purpose = args.get("purpose", "")
                lines.append(f"> **purpose:** {purpose}")
                lines.append("")
                lines.append(self._code_block(code, "python"))
            else:
                lines.append(self._json_block(args))
        else:
            lines.append("_No tool called this turn._")
        lines.append("")

        # --- Tool output ---
        lines.append("### Tool Output")
        if tt.tool_output is not None:
            if tt.tool_call and tt.tool_call["name"] == "execute_python":
                ok = tt.tool_output.get("ok", False)
                stdout = tt.tool_output.get("stdout", "")
                stderr = tt.tool_output.get("stderr", "")
                error = tt.tool_output.get("error")
                lines.append(f"**Status:** {'SUCCESS' if ok else 'FAILED'}")
                if stdout:
                    lines.append("")
                    lines.append("**stdout:**")
                    lines.append(self._code_block(stdout))
                if stderr:
                    lines.append("")
                    lines.append("**stderr:**")
                    lines.append(self._code_block(stderr))
                if error:
                    lines.append("")
                    lines.append("**error:**")
                    lines.append(self._code_block(error))
            else:
                lines.append(self._json_block(tt.tool_output))
        else:
            lines.append("_No tool output._")
        lines.append("")

        # --- Metrics ---
        lines.append("### Metrics")
        m = tt.metrics
        lines.append(
            f"| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |"
        )
        lines.append("|-----------|------------|-----------|-------------|-------------|--------------|")
        lines.append(
            f"| {m.get('input_tokens', 0)} | {m.get('output_tokens', 0)} "
            f"| {m.get('reasoning_tokens', 0)} | {m.get('conversation_tokens', 0)} "
            f"| {m.get('api_latency_s', 0):.3f}s | {m.get('exec_latency_s', 0):.3f}s |"
        )
        lines.append("")

        # --- Error ---
        if tt.error:
            lines.append("### Error")
            lines.append(self._code_block(tt.error))
            lines.append("")

        lines.append("---")
        lines.append("")
        return "\n".join(lines)

    def _to_markdown(self) -> str:
        t = self._trace
        header = [
            f"# Agent Trace — {t.run_id}",
            "",
            f"**Model:** `{t.model}`  ",
            f"**Timestamp:** {t.timestamp}  ",
            f"**Task:** {t.task}",
            "",
            "**System Prompt:**",
            self._code_block(t.system_prompt),
            "",
            "---",
            "",
        ]

        turn_sections = [self._turn_md(tt) for tt in t.turns]

        footer: list[str] = ["# Run Summary", ""]
        if t.run_error:
            footer += ["**Run ended with error:**", self._code_block(t.run_error), ""]
        if t.final_result:
            footer += ["**Final Result:**", self._json_block(t.final_result), ""]
        if t.metrics_summary:
            footer += ["**Metrics Summary:**", self._json_block(t.metrics_summary), ""]

        return "\n".join(header + turn_sections + footer)

    # --- Stdout printing ---

    def _print_turn(self, tt: TurnTrace) -> None:
        sep = "=" * 70
        tool_label = tt.tool_call["name"] if tt.tool_call else "(no tool)"
        status = "ERROR" if tt.error else ("ok" if tt.tool_call else "nudge")
        print(f"\n{sep}")
        print(f"TURN {tt.turn} | {tool_label} | {status}")
        print(sep)

        m = tt.metrics
        print(
            f"  tokens: in={m.get('input_tokens',0)} out={m.get('output_tokens',0)} "
            f"reason={m.get('reasoning_tokens',0)} conv={m.get('conversation_tokens',0)}"
        )
        print(
            f"  latency: api={m.get('api_latency_s',0):.3f}s "
            f"exec={m.get('exec_latency_s',0):.3f}s"
        )

        if tt.tool_call:
            args = tt.tool_call.get("arguments", {})
            if tt.tool_call["name"] == "execute_python":
                print(f"  purpose: {args.get('purpose', '')}")
                code_preview = textwrap.indent(
                    args.get("code", "")[:400], "    "
                )
                print(f"  code:\n{code_preview}")
            else:
                print(f"  args: {json.dumps(args, default=str)[:300]}")

        if tt.tool_output is not None:
            if tt.tool_call and tt.tool_call["name"] == "execute_python":
                ok = tt.tool_output.get("ok", False)
                stdout = (tt.tool_output.get("stdout") or "").strip()
                err = (tt.tool_output.get("error") or "").strip()
                print(f"  exec: {'SUCCESS' if ok else 'FAILED'}")
                if stdout:
                    preview = textwrap.indent(stdout[:400], "    ")
                    print(f"  stdout:\n{preview}")
                if err:
                    preview = textwrap.indent(err[:400], "    ")
                    print(f"  error:\n{preview}")
            else:
                print(f"  output: {json.dumps(tt.tool_output, default=str)[:300]}")

        if tt.error:
            print(f"  [ERROR] {tt.error[:300]}")

    def _print_run_footer(self) -> None:
        t = self._trace
        sep = "=" * 70
        print(f"\n{sep}")
        print("RUN COMPLETE" if not t.run_error else "RUN FAILED")
        print(sep)
        if t.run_error:
            print(f"  error: {t.run_error}")
        if t.final_result:
            summary = (t.final_result.get("summary") or "")[:200]
            rows = t.final_result.get("rows", [])
            print(f"  summary: {summary}")
            print(f"  rows returned: {len(rows)}")
        if t.metrics_summary:
            timing = t.metrics_summary.get("timing", {})
            tokens = t.metrics_summary.get("tokens", {})
            print(
                f"  total tokens: {tokens.get('total', 0)} | "
                f"wall time: {timing.get('wall_time_s', 0):.2f}s"
            )
        print()
