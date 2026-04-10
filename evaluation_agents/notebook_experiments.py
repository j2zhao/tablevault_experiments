"""
notebook_experiments.py

Runs AgenticWorkflow (eval_agent) over each function experiment set in FUNCTION_EXPERIMENTS
for a list of tasks. After all agents complete for a task, a separate OpenAI evaluator
instance rates each result 1–5, seeing all agent results together for comparison.

Full traces are saved in a structured folder hierarchy. A summary JSON capturing tokens
used, API function calls made, and turns taken is saved per task and per function subset.

Folder layout:
    <output_root>/
      <run_id>/
        <task_label>/
          <experiment_name>/
            trace.json
            trace.md
          ratings.json
          summary.json
        global_summary.json
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from typing import Any

from openai import OpenAI

# Ensure the evaluation_agents package is importable when run from the repo root.
sys.path.insert(0, os.path.dirname(__file__))

from eval_agent import AgenticWorkflow, SYSTEM_PROMPT
from api_functions import FUNCTION_EXPERIMENTS

# ---------------------------------------------------------------------------
# Task list with ground-truth metadata for evaluation
# ---------------------------------------------------------------------------

TASK_SPECS: list[dict] = [
    {
        # Easy: all relevant notebooks share 'distilbert_feature_extraction' or a
        # pooling keyword in their names — discoverable by name enumeration alone.
        "task": (
            "How does the pooling strategy used to extract sentence representations "
            "from DistilBERT affect paraphrase detection accuracy on MRPC?"
        ),
        "difficulty": "easy",
        "expected_notebooks": [
            "distilbert_feature_extraction_cosine_mrpc",
            "distilbert_cls_cosine_mrpc",
            "distilbert_max_pool_cosine_mrpc",
            "distilbert_no_special_tokens_mean_cosine_mrpc",
            "distilbert_last4_mean_cosine_mrpc",
            "distilbert_mean_cosine_median_threshold_mrpc",
        ],
        "min_notebooks_expected": 5,
        "discovery_hint": (
            "All relevant notebooks share 'distilbert' and a pooling-related keyword "
            "(cls, max_pool, mean, last4, no_special_tokens) in their names. "
            "A simple name enumeration is sufficient to find them."
        ),
        "key_finding": (
            "Mean pooling (with or without special tokens) generally outperforms "
            "CLS-token and max-pool extraction under cosine-similarity-based "
            "classification. The agent should report accuracy and F1 per pooling "
            "variant and identify which strategy performs best."
        ),
    },
    {
        # Medium: notebooks span three families (bi-encoder, distilbert feature
        # extraction, HF pipeline, cross-encoder). Code search for 'threshold' or
        # description search are needed; name enumeration alone misses cross-family scope.
        "task": (
            "How sensitive are similarity-based paraphrase classifiers to the choice "
            "of decision threshold, and does this vary across model families?"
        ),
        "difficulty": "medium",
        "expected_notebooks": [
            "sentence_transformers_bi_encoder_cosine_mrpc",
            "st_paraphrase_minilm_l6_cosine_threshold_mrpc",
            "st_paraphrase_minilm_l3_cosine_threshold_mrpc",
            "st_all_minilm_l6_l2_distance_threshold_mrpc",
            "distilbert_mean_cosine_median_threshold_mrpc",
            "hf_pipeline_mrpc_threshold_070",
            "quora_cross_encoder_softmax_threshold_065_mrpc",
        ],
        "min_notebooks_expected": 5,
        "discovery_hint": (
            "Relevant notebooks span three families (sentence-transformers bi-encoder, "
            "distilbert feature extraction, HF pipeline, cross-encoder). "
            "Code search for 'threshold' or description/property search are the most "
            "direct routes; name enumeration alone is insufficient without cross-family "
            "awareness."
        ),
        "key_finding": (
            "Threshold choice significantly shifts the precision/recall trade-off. "
            "The agent should identify notebooks from multiple families that vary only "
            "the threshold, report how accuracy and F1 change with threshold, and note "
            "that the optimal threshold differs by model family and similarity metric."
        ),
    },
    {
        # Hard: notebooks are spread across four model families with no shared name
        # pattern. Must be found via code search for bidirectional processing patterns
        # (enc_12/enc_21, margin_12/margin_21) or via description/property search.
        "task": (
            "How do different strategies for enforcing prediction symmetry affect "
            "accuracy when using NLI-based and zero-shot models for paraphrase "
            "detection on MRPC?"
        ),
        "difficulty": "hard",
        "expected_notebooks": [
            "direct_nli_entailment_mrpc",
            "min_direction_margin_mrpc",
            "consensus_then_avg_margin_mrpc",
            "neutral_penalized_margin_mrpc",
            "softmax_gap_mean_mrpc",
            "bidirectional_averaged_zero_shot_mrpc",
            "hf_pipeline_mrpc_bidirectional_order_average",
            "quora_cross_encoder_symmetric_average_mrpc",
        ],
        "min_notebooks_expected": 6,
        "discovery_hint": (
            "Relevant notebooks span four families (direct NLI entailment, zero-shot "
            "NLI pipeline, HF sequence classification pipeline, cross-encoder). "
            "No name pattern unifies them — they must be found by searching code for "
            "bidirectional processing (enc_12/enc_21, margin_12/margin_21) or via "
            "description/property search for symmetry-related concepts."
        ),
        "key_finding": (
            "Bidirectional averaging generally improves over single-direction scoring. "
            "The agent should identify notebooks that process both (S1→S2) and (S2→S1) "
            "and compare aggregation strategies (average margin, min-direction, consensus "
            "vote, neutral penalty). Improvements vary by model family and are more "
            "pronounced for NLI models than for cross-encoders."
        ),
    },
]

TASKS: list[str] = [spec["task"] for spec in TASK_SPECS]

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

VAULT_NAME = "tv_experiment_1"
AGENT_MODEL = "gpt-5.4"
EVALUATOR_MODEL = "gpt-5.4"
DEFAULT_EVALUATOR_REASONING: dict = {"effort": "high"}
MAX_TURNS = 30
OUTPUT_ROOT = "experiment_results"

OPENAI_KEY_FILE = "/Users/jinjinzhao/Documents/work_projects/my_keys/my_keys/openai_jinjin.key"

# ---------------------------------------------------------------------------
# Evaluator
# ---------------------------------------------------------------------------

EVALUATOR_SYSTEM_PROMPT = """\
You are an expert evaluator assessing the quality of AI-generated data analysis responses.

You will receive a user task and the results produced by several agents. Each agent used a
different set of API functions to answer the same question against the same data repository.

When ground-truth metadata is provided (expected notebooks, minimum coverage, key finding),
use it to assess each agent result on three dimensions:

  1. Notebook coverage — what fraction of the expected notebooks did the agent cite or
     retrieve? An agent that finds fewer than the minimum required notebooks should not
     score above 3, regardless of the quality of its summary.

  2. Factual correctness — does the agent's reported finding match the expected key finding?
     Penalise results that draw the opposite conclusion or miss the central pattern.

  3. Analytical depth — does the summary interpret the evidence (not just list numbers),
     note cross-family differences, and flag limitations or confounds?

Scoring guide (apply all three dimensions; coverage and correctness carry the most weight):
  5 — Meets minimum notebook coverage, correct key finding, insightful analysis
  4 — Near-minimum coverage or minor factual gap, otherwise complete and correct
  3 — Below minimum coverage OR incorrect/missing key finding, but some valid evidence
  2 — Severely under-covered (1–2 notebooks only) or substantially incorrect conclusion
  1 — Does not address the task, errors dominate, or no relevant notebooks retrieved

When no ground-truth metadata is provided, fall back to general completeness and accuracy.

Return a JSON object with exactly this shape (no markdown fences):
{
  "ratings": {
    "<function_experiment_name>": {
      "score": <int 1–5>,
      "notebook_coverage": "<N of M expected notebooks cited>",
      "rationale": "<brief explanation referencing coverage, correctness, depth>"
    }
  },
  "overall_comment": "<cross-agent comparison and key observations>"
}
"""


def evaluate_results(
    client: OpenAI,
    task: str,
    agent_results: dict[str, dict[str, Any]],
    task_metadata: dict | None = None,
    model: str = EVALUATOR_MODEL,
    reasoning: dict | None = None,
) -> dict[str, Any]:
    """Rate each agent result 1–5 using a single evaluator that sees all results.

    Args:
        client: OpenAI client.
        task: The original task string.
        agent_results: {experiment_name: {"result": {...}, "metrics": RunMetrics, "error": str|None}}
        task_metadata: Optional ground-truth dict from TASK_SPECS (expected_notebooks,
                       min_notebooks_expected, key_finding, difficulty, discovery_hint).
        model: Evaluator model name.
        reasoning: Optional reasoning parameter dict, e.g. {"effort": "high"}.

    Returns:
        Parsed ratings dict from the evaluator, or a fallback dict on parse failure.
    """
    result_blocks: list[str] = []
    for exp_name, run_data in agent_results.items():
        error = run_data.get("error")
        if error:
            result_blocks.append(f"### Agent: {exp_name}\n**ERROR:** {error}\n")
        else:
            result = run_data.get("result") or {}
            rows = result.get("rows", [])
            summary = result.get("summary", "(no summary)")
            result_blocks.append(
                f"### Agent: {exp_name}\n"
                f"**Summary:** {summary}\n\n"
                f"**Result rows ({len(rows)} rows):**\n"
                f"```json\n{json.dumps(rows[:20], indent=2, default=str)}\n```\n"
            )

    ground_truth_block = ""
    if task_metadata:
        expected = task_metadata.get("expected_notebooks", [])
        min_nb = task_metadata.get("min_notebooks_expected", "?")
        key_finding = task_metadata.get("key_finding", "")
        difficulty = task_metadata.get("difficulty", "")
        ground_truth_block = (
            f"## Ground-Truth Reference\n\n"
            f"**Task difficulty:** {difficulty}\n\n"
            f"**Expected notebooks ({len(expected)} total, minimum {min_nb} required):**\n"
            + "\n".join(f"  - {nb}" for nb in expected)
            + f"\n\n**Key finding the agent should identify:**\n{key_finding}\n\n"
            "Use the expected notebook list to assess coverage: count how many of these "
            "names (or close variants) appear in the agent's result rows or summary. "
            "An agent that cites fewer than the minimum required should not score above 3.\n\n"
        )

    user_content = (
        f"## Task\n{task}\n\n"
        + ground_truth_block
        + "## Agent Results\n\n"
        + "\n---\n".join(result_blocks)
    )

    create_kwargs: dict[str, Any] = dict(
        model=model,
        instructions=EVALUATOR_SYSTEM_PROMPT,
        input=[{"role": "user", "content": user_content}],
    )
    if reasoning is not None:
        create_kwargs["reasoning"] = reasoning

    response = client.responses.create(**create_kwargs)

    raw_text = ""
    for item in response.output or []:
        if getattr(item, "type", None) in ("text", "message"):
            raw_text = getattr(item, "text", None) or getattr(item, "content", None) or ""
            break

    try:
        text = raw_text.strip()
        # Strip markdown code fences if the model wrapped the JSON.
        if text.startswith("```"):
            text = re.sub(r"^```[^\n]*\n", "", text)
            text = re.sub(r"\n?```$", "", text).strip()
        return json.loads(text)
    except json.JSONDecodeError:
        return {
            "parse_error": "Could not parse JSON from evaluator response",
            "raw_response": raw_text,
        }


# ---------------------------------------------------------------------------
# Summary helpers
# ---------------------------------------------------------------------------

def _extract_summary_stats(metrics: Any) -> dict[str, Any]:
    """Pull the key statistics we care about from a RunMetrics object."""
    s = metrics.summary()
    return {
        "total_tokens": s["tokens"]["total"],
        "input_tokens": s["tokens"]["input"],
        "output_tokens": s["tokens"]["output"],
        "reasoning_tokens": s["tokens"]["reasoning"],
        # num_api_calls == total OpenAI API calls == number of turns in the loop
        "num_turns": s["api_calls"],
        # num_executions == execute_python calls == vault API function call batches
        "num_api_function_calls": s["code"]["executions"],
        "wall_time_s": s["timing"]["wall_time_s"],
    }


def _safe_avg(values: list[float | int]) -> float | None:
    return round(sum(values) / len(values), 2) if values else None


def _slugify(text: str, max_len: int = 40) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", text).strip("_").lower()
    return slug[:max_len]


# ---------------------------------------------------------------------------
# Main experiment loop
# ---------------------------------------------------------------------------

def run_experiments(
    tasks: list[str] = TASKS,
    task_specs: list[dict] | None = TASK_SPECS,
    vault_name: str = VAULT_NAME,
    agent_model: str = AGENT_MODEL,
    evaluator_model: str = EVALUATOR_MODEL,
    evaluator_reasoning: dict | None = DEFAULT_EVALUATOR_REASONING,
    max_turns: int = MAX_TURNS,
    output_root: str = OUTPUT_ROOT,
    function_experiments: dict[str, list[str]] | None = None,
) -> None:
    """Run all experiments and save results.

    Args:
        tasks: List of task strings to evaluate.
        task_specs: Optional list of TASK_SPECS dicts providing ground-truth metadata
                    (expected_notebooks, key_finding, difficulty) for the evaluator.
                    Must align 1-to-1 with tasks if provided.
        vault_name: TableVault database name passed to initialization().
        agent_model: Model used by the agentic workflow.
        evaluator_model: Model used by the evaluator.
        evaluator_reasoning: Reasoning dict for the evaluator (e.g. {"effort": "high"}).
                             Pass None to disable reasoning.
        max_turns: Maximum turns per agent run.
        output_root: Root directory for all output files.
        function_experiments: Override FUNCTION_EXPERIMENTS; defaults to the full set.
    """
    if function_experiments is None:
        function_experiments = FUNCTION_EXPERIMENTS

    with open(OPENAI_KEY_FILE, "r") as f:
        os.environ["OPENAI_API_KEY"] = f.read().strip()
    client = OpenAI()

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = os.path.join(output_root, run_id)
    os.makedirs(run_dir, exist_ok=True)

    print(
        f"\n=== Experiment run {run_id} | {len(tasks)} task(s) | "
        f"{len(function_experiments)} function set(s) ==="
    )
    print(f"Output directory: {run_dir}\n")

    all_task_summaries: list[dict[str, Any]] = []

    for task_idx, task in enumerate(tasks):
        task_meta = task_specs[task_idx] if task_specs and task_idx < len(task_specs) else None
        task_slug = _slugify(task)
        task_label = f"task_{task_idx:03d}_{task_slug}"
        task_dir = os.path.join(run_dir, task_label)
        os.makedirs(task_dir, exist_ok=True)

        print(f"\n{'='*70}")
        print(f"TASK {task_idx}: {task}")
        print(f"{'='*70}\n")

        agent_results: dict[str, dict[str, Any]] = {}

        # --- Run each function experiment in sequence ---
        for exp_name, fn_list in function_experiments.items():
            print(f"\n--- [{exp_name}] functions: {fn_list} ---")
            exp_dir = os.path.join(task_dir, exp_name)
            os.makedirs(exp_dir, exist_ok=True)

            try:
                wf = AgenticWorkflow(
                    client=client,
                    model=agent_model,
                    system_prompt=SYSTEM_PROMPT,
                    vault_name=vault_name,
                    workflow_key=exp_name,
                    max_turns=max_turns,
                    trace_output_dir=exp_dir,
                    trace_filename_stem="trace",
                    reasoning={"effort": "high"},
                )
                output = wf.run(task)
                agent_results[exp_name] = {
                    "result": output["result"],
                    "metrics": output["metrics"],
                    "error": None,
                }
            except Exception as exc:
                print(f"  [ERROR] experiment '{exp_name}' failed: {exc}")
                agent_results[exp_name] = {
                    "result": None,
                    "metrics": None,
                    "error": str(exc),
                }

        # --- Evaluate all results for this task with a single evaluator call ---
        print(f"\n--- Evaluating {len(agent_results)} agent result(s) ---")
        ratings = evaluate_results(
            client=client,
            task=task,
            agent_results=agent_results,
            task_metadata=task_meta,
            model=evaluator_model,
            reasoning=evaluator_reasoning,
        )

        ratings_path = os.path.join(task_dir, "ratings.json")
        with open(ratings_path, "w", encoding="utf-8") as f:
            json.dump({"task": task, "ratings": ratings}, f, indent=2, default=str)
        print(f"  ratings saved -> {ratings_path}")

        # --- Build per-task summary (stats + rating for each experiment) ---
        task_summary: dict[str, Any] = {
            "task_idx": task_idx,
            "task": task,
            "difficulty": task_meta.get("difficulty") if task_meta else None,
            "expected_notebooks": task_meta.get("expected_notebooks") if task_meta else None,
            "min_notebooks_expected": task_meta.get("min_notebooks_expected") if task_meta else None,
            "key_finding": task_meta.get("key_finding") if task_meta else None,
            "experiments": {},
        }
        per_experiment_ratings: dict[str, Any] = (ratings.get("ratings") or {})
        for exp_name, run_data in agent_results.items():
            entry: dict[str, Any] = {"error": run_data["error"]}
            if run_data["metrics"] is not None:
                entry["stats"] = _extract_summary_stats(run_data["metrics"])
            if exp_name in per_experiment_ratings:
                entry["rating"] = per_experiment_ratings[exp_name]
            task_summary["experiments"][exp_name] = entry

        all_task_summaries.append(task_summary)

        task_summary_path = os.path.join(task_dir, "summary.json")
        with open(task_summary_path, "w", encoding="utf-8") as f:
            json.dump(task_summary, f, indent=2, default=str)
        print(f"  task summary saved -> {task_summary_path}")

        # --- Print per-task results table ---
        difficulty_label = f" [{task_meta['difficulty']}]" if task_meta else ""
        print(f"\n--- Results for task {task_idx}{difficulty_label}: {task} ---")
        if task_meta:
            print(
                f"  Expected notebooks ({task_meta['min_notebooks_expected']} min): "
                + ", ".join(task_meta["expected_notebooks"])
            )
        print(
            f"\n{'Experiment':<35} {'Tokens':>12} {'FnCalls':>10} "
            f"{'Turns':>8} {'Score':>8} {'Coverage':>10}  Rationale"
        )
        print("-" * 115)
        for exp_name, exp_data in task_summary["experiments"].items():
            error = exp_data.get("error")
            if error:
                print(f"{exp_name:<35} {'ERROR':>12}  {error[:60]}")
                continue
            stats = exp_data.get("stats", {})
            rating = exp_data.get("rating", {})
            score = rating.get("score", "-") if isinstance(rating, dict) else "-"
            coverage = rating.get("notebook_coverage", "-") if isinstance(rating, dict) else "-"
            rationale = rating.get("rationale", "") if isinstance(rating, dict) else ""
            print(
                f"{exp_name:<35} "
                f"{str(stats.get('total_tokens', '-')):>12} "
                f"{str(stats.get('num_api_function_calls', '-')):>10} "
                f"{str(stats.get('num_turns', '-')):>8} "
                f"{str(score):>8} "
                f"{str(coverage):>10}  {rationale[:55]}"
            )
        overall = ratings.get("overall_comment", "")
        if overall:
            print(f"\nOverall: {overall}")
        print()

    # --- Aggregate stats across all tasks, grouped by function experiment ---
    by_experiment: dict[str, dict[str, Any]] = {}
    for exp_name in function_experiments:
        token_totals, api_fn_call_totals, turn_totals, scores = [], [], [], []
        for ts in all_task_summaries:
            exp_data = ts["experiments"].get(exp_name, {})
            stats = exp_data.get("stats")
            if stats:
                token_totals.append(stats["total_tokens"])
                api_fn_call_totals.append(stats["num_api_function_calls"])
                turn_totals.append(stats["num_turns"])
            rating = exp_data.get("rating")
            if isinstance(rating, dict) and isinstance(rating.get("score"), (int, float)):
                scores.append(rating["score"])

        by_experiment[exp_name] = {
            "num_tasks_completed": len(token_totals),
            "avg_total_tokens": _safe_avg(token_totals),
            "avg_num_api_function_calls": _safe_avg(api_fn_call_totals),
            "avg_num_turns": _safe_avg(turn_totals),
            "avg_rating": _safe_avg(scores),
        }

    global_summary: dict[str, Any] = {
        "run_id": run_id,
        "agent_model": agent_model,
        "evaluator_model": evaluator_model,
        "evaluator_reasoning": evaluator_reasoning,
        "vault_name": vault_name,
        "num_tasks": len(tasks),
        "by_experiment": by_experiment,
        "per_task": all_task_summaries,
    }

    global_summary_path = os.path.join(run_dir, "global_summary.json")
    with open(global_summary_path, "w", encoding="utf-8") as f:
        json.dump(global_summary, f, indent=2, default=str)
    print(f"\n=== Global summary saved -> {global_summary_path} ===")

    # --- Print aggregate table ---
    print(
        f"\n{'Experiment':<35} {'AvgTokens':>12} {'AvgFnCalls':>12} "
        f"{'AvgTurns':>10} {'AvgScore':>10}"
    )
    print("-" * 82)
    for exp_name, agg in by_experiment.items():
        print(
            f"{exp_name:<35} "
            f"{str(agg['avg_total_tokens']):>12} "
            f"{str(agg['avg_num_api_function_calls']):>12} "
            f"{str(agg['avg_num_turns']):>10} "
            f"{str(agg['avg_rating']):>10}"
        )
    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    run_experiments()
