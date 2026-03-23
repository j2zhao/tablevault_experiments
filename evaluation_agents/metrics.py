"""Metrics dataclasses for tracking agentic workflow runs."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class TurnMetrics:
    """Snapshot of a single API turn."""

    turn: int
    tool_name: str | None
    purpose: str | None

    # Token usage
    input_tokens: int = 0
    output_tokens: int = 0
    reasoning_tokens: int = 0
    conversation_tokens: int = 0  # input_tokens minus system overhead

    # Code metrics (only for execute_python turns)
    code_lines: int = 0
    code_succeeded: bool | None = None

    # Timing
    api_latency_s: float = 0.0
    exec_latency_s: float = 0.0


@dataclass
class RunMetrics:
    """Aggregated metrics for an entire run."""

    turns: list[TurnMetrics] = field(default_factory=list)
    system_token_estimate: int = 0  # estimated tokens for system prompt + tools

    # --- Token totals ---

    @property
    def total_input_tokens(self) -> int:
        return sum(t.input_tokens for t in self.turns)

    @property
    def total_output_tokens(self) -> int:
        return sum(t.output_tokens for t in self.turns)

    @property
    def total_reasoning_tokens(self) -> int:
        return sum(t.reasoning_tokens for t in self.turns)

    @property
    def total_tokens(self) -> int:
        return self.total_input_tokens + self.total_output_tokens

    @property
    def total_conversation_tokens(self) -> int:
        return sum(t.conversation_tokens for t in self.turns)

    # --- Code totals ---

    @property
    def num_api_calls(self) -> int:
        return len(self.turns)

    @property
    def num_executions(self) -> int:
        return sum(1 for t in self.turns if t.tool_name == "execute_python")

    @property
    def num_failed_executions(self) -> int:
        return sum(
            1 for t in self.turns
            if t.tool_name == "execute_python" and t.code_succeeded is False
        )

    @property
    def total_code_lines(self) -> int:
        return sum(t.code_lines for t in self.turns)

    # --- Timing ---

    @property
    def total_api_latency_s(self) -> float:
        return sum(t.api_latency_s for t in self.turns)

    @property
    def total_exec_latency_s(self) -> float:
        return sum(t.exec_latency_s for t in self.turns)

    @property
    def total_wall_time_s(self) -> float:
        return self.total_api_latency_s + self.total_exec_latency_s

    # --- Cost estimation ---

    def estimate_cost(
        self,
        input_cost_per_m: float = 0.0,
        output_cost_per_m: float = 0.0,
        reasoning_cost_per_m: float = 0.0,
    ) -> dict[str, float]:
        """Estimate cost in USD given per-million-token rates."""
        input_cost = self.total_input_tokens * input_cost_per_m / 1_000_000
        output_cost = self.total_output_tokens * output_cost_per_m / 1_000_000
        reasoning_cost = self.total_reasoning_tokens * reasoning_cost_per_m / 1_000_000
        return {
            "input_cost": round(input_cost, 6),
            "output_cost": round(output_cost, 6),
            "reasoning_cost": round(reasoning_cost, 6),
            "total_cost": round(input_cost + output_cost + reasoning_cost, 6),
        }

    def summary(self, **cost_kwargs: float) -> dict[str, Any]:
        """Full metrics summary as a plain dict."""
        return {
            "tokens": {
                "input": self.total_input_tokens,
                "output": self.total_output_tokens,
                "reasoning": self.total_reasoning_tokens,
                "total": self.total_tokens,
                "system_estimate": self.system_token_estimate,
                "conversation": self.total_conversation_tokens,
            },
            "code": {
                "executions": self.num_executions,
                "failed_executions": self.num_failed_executions,
                "total_lines": self.total_code_lines,
            },
            "timing": {
                "api_latency_s": round(self.total_api_latency_s, 3),
                "exec_latency_s": round(self.total_exec_latency_s, 3),
                "wall_time_s": round(self.total_wall_time_s, 3),
            },
            "api_calls": self.num_api_calls,
            "cost": self.estimate_cost(**cost_kwargs) if cost_kwargs else None,
        }
