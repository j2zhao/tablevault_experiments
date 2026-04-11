# Agent Trace — 20260411T143459Z

**Model:** `gpt-5.4`  
**Timestamp:** 2026-04-11T14:34:59.381337+00:00  
**Task:** How do different strategies for enforcing prediction symmetry affect accuracy when using NLI-based and zero-shot models for paraphrase detection on MRPC?

**System Prompt:**
```
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

```

---

## Turn 0 — `code_search` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c1373cc8195beb1941655846f49`

**Pending messages:**
```json
[
  {
    "role": "user",
    "content": "How do different strategies for enforcing prediction symmetry affect accuracy when using NLI-based and zero-shot models for paraphrase detection on MRPC?"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c1373cc8195beb1941655846f49`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_search",
    "call_id": "call_XJl4OMeWEiKcN77RqOyXXQNZ",
    "arguments": {
      "code": "MRPC symmetry paraphrase zero-shot NLI"
    }
  }
]
```

### Tool Call
**Tool:** `code_search` | **call_id:** `call_XJl4OMeWEiKcN77RqOyXXQNZ`

**Arguments:**
```json
{
  "code": "MRPC symmetry paraphrase zero-shot NLI"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "gent_1775914190",
    "gent_1775874933",
    "gent_1775874373",
    "gent_1775874650",
    "gent_1775914000",
    "gent_1775913615"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 1471 | 106 | 78 | 0 | 2.003s | 0.073s |

---

## Turn 1 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c1586a88195a8cfc238e3e79201`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_XJl4OMeWEiKcN77RqOyXXQNZ",
    "output": "{\"ok\": true, \"result\": [\"gent_1775914190\", \"gent_1775874933\", \"gent_1775874373\", \"gent_1775874650\", \"gent_1775914000\", \"gent_1775913615\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c1586a88195a8cfc238e3e79201`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "get_code",
    "call_id": "call_px78BFXN1Nu6zhmwdf5o0Lxp",
    "arguments": {
      "name": "gent_1775914190"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_px78BFXN1Nu6zhmwdf5o0Lxp`

**Arguments:**
```json
{
  "name": "gent_1775914190"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "\"\"\"\nnotebook_experiments.py\n\nRuns AgenticWorkflow (eval_agent) over each function experiment set in FUNCTION_EXPERIMENTS\nfor a list of tasks. After all agents complete for a task, a separate OpenAI evaluator\ninstance rates each result 1\u20135, seeing all agent results together for comparison.\n\nFull traces are saved in a structured folder hierarchy. A summary JSON capturing tokens\nused, API function calls made, and turns taken is saved per task and per function subset.\n\nFolder layout:\n    <output_root>/\n      <run_id>/\n        <task_label>/\n          <experiment_name>/\n            trace.json\n            trace.md\n          ratings.json\n          summary.json\n        global_summary.json\n\"\"\"\n\nimport json\nimport os\nimport re\nimport sys\nfrom datetime import datetime, timezone\nfrom typing import Any\n\nfrom openai import OpenAI\n\n# Ensure the evaluation_agents package is importable when run from the repo root.\nsys.path.insert(0, os.path.dirname(__file__))\n\nfrom eval_agent_functions import AgenticWorkflow, SYSTEM_PROMPT\nfrom api_functions import FUNCTION_EXPERIMENTS, initialization\n\n# ---------------------------------------------------------------------------\n# Task list with ground-truth metadata for evaluation\n# ---------------------------------------------------------------------------\n\nTASK_SPECS: list[dict] = [\n    {\n        # Easy: all relevant notebooks share 'distilbert_feature_extraction' or a\n        # pooling keyword in their names \u2014 discoverable by name enumeration alone.\n        \"task\": (\n            \"How does the pooling strategy used to extract sentence representations \"\n            \"from DistilBERT affect paraphrase detection accuracy on MRPC?\"\n        ),\n        \"difficulty\": \"easy\",\n        \"expected_notebooks\": [\n            \"distilbert_feature_extraction_cosine_mrpc\",\n            \"distilbert_cls_cosine_mrpc\",\n            \"distilbert_max_pool_cosine_mrpc\",\n            \"distilbert_no_special_tokens_mean_cosine_mrpc\",\n            \"distilbert_last4_mean_cosine_mrpc\",\n            \"distilbert_mean_cosine_median_threshold_mrpc\",\n        ],\n        \"min_notebooks_expected\": 5,\n        \"discovery_hint\": (\n            \"All relevant notebooks share 'distilbert' and a pooling-related keyword \"\n            \"(cls, max_pool, mean, last4, no_special_tokens) in their names. \"\n            \"A simple name enumeration is sufficient to find them.\"\n        ),\n        \"key_finding\": (\n            \"Last-layer mean pooling (with or without special tokens) marginally \"\n            \"outperforms CLS-token and max-pool extraction, but differences are small \"\n            \"(accuracy ~0.696\u20130.703 vs ~0.684\u20130.686 at threshold=0.85). Averaging the \"\n            \"last four hidden layers before mean-pooling does not improve over \"\n            \"single-layer mean pooling and performs on par with CLS and max-pool. \"\n            \"Note: distilbert_mean_cosine_median_threshold_mrpc uses a data-driven \"\n            \"median threshold rather than 0.85 and shows substantially lower performance \"\n            \"(accuracy ~0.65, F1 ~0.70) \u2014 this reflects threshold sensitivity, not \"\n            \"pooling quality, and should not be interpreted as a pooling result. \"\n            \"The agent should report accuracy and F1 per pooling variant at a fixed \"\n            \"threshold and note that the overall spread across strategies is narrow.\"\n        ),\n    },\n    {\n        # Medium: notebooks span three families (bi-encoder, distilbert feature\n        # extraction, HF pipeline, cross-encoder). Code search for 'threshold' or\n        # description search are needed; name enumeration alone misses cross-family scope.\n        \"task\": (\n            \"How sensitive are similarity-based paraphrase classifiers to the choice \"\n            \"of decision threshold, and does this vary across model families?\"\n        ),\n        \"difficulty\": \"medium\",\n        \"expected_notebooks\": [\n            \"sentence_transformers_bi_encoder_cosine_mrpc\",\n            \"st_paraphrase_minilm_l6_cosine_threshold_mrpc\",\n            \"st_paraphrase_minilm_l3_cosine_threshold_mrpc\",\n            \"st_all_minilm_l6_l2_distance_threshold_mrpc\",\n            \"st_all_distilroberta_v1_cosine_threshold_mrpc\",\n            \"distilbert_mean_cosine_median_threshold_mrpc\",\n            \"hf_pipeline_mrpc_threshold_070\",\n            \"quora_cross_encoder_softmax_threshold_065_mrpc\",\n            \"paraphrase_score_threshold_zero_shot_mrpc\",\n        ],\n        \"min_notebooks_expected\": 6,\n        \"discovery_hint\": (\n            \"Relevant notebooks span three families (sentence-transformers bi-encoder, \"\n            \"distilbert feature extraction, HF pipeline, cross-encoder). \"\n            \"Code search for 'threshold' or description/property search are the most \"\n            \"direct routes; name enumeration alone is insufficient without cross-family \"\n            \"awareness.\"\n        ),\n        \"key_finding\": (\n            \"Threshold choice significantly shifts the precision/recall trade-off. \"\n            \"The fine-tuned HF pipeline at threshold=0.70 (acc ~0.848, F1 ~0.890) \"\n            \"stays close to its argmax baseline, while bi-encoder cosine models \"\n            \"(paraphrase-MiniLM-L6 at 0.78: acc ~0.701, F1 ~0.771; all-distilroberta-v1 \"\n            \"at 0.72: acc ~0.723, F1 ~0.806) and the cross-encoder (quora-distilroberta \"\n            \"at 0.65: acc ~0.679, F1 ~0.758) degrade more sharply at non-optimal \"\n            \"thresholds. Zero-shot NLI models are especially sensitive: applying a \"\n            \"threshold of 0.55 (paraphrase_score_threshold_zero_shot_mrpc) yields \"\n            \"acc ~0.578, F1 ~0.674. The agent should identify notebooks from multiple \"\n            \"families that vary the threshold, report how accuracy and F1 change, and \"\n            \"note that the optimal threshold and sensitivity to its choice differ \"\n            \"substantially by model family and similarity metric.\"\n        ),\n    },\n    {\n        # Hard: notebooks are spread across four model families with no shared name\n        # pattern. Must be found via code search for bidirectional processing patterns\n        # (enc_12/enc_21, margin_12/margin_21) or via description/property search.\n        \"task\": (\n            \"How do different strategies for enforcing prediction symmetry affect \"\n            \"accuracy when using NLI-based and zero-shot models for paraphrase \"\n            \"detection on MRPC?\"\n        ),\n        \"difficulty\": \"hard\",\n        \"expected_notebooks\": [\n            \"direct_nli_entailment_mrpc\",\n            \"min_direction_margin_mrpc\",\n            \"consensus_then_avg_margin_mrpc\",\n            \"neutral_penalized_margin_mrpc\",\n            \"softmax_gap_mean_mrpc\",\n            \"bidirectional_averaged_zero_shot_mrpc\",\n            \"hf_pipeline_mrpc_bidirectional_order_average\",\n            \"quora_cross_encoder_symmetric_average_mrpc\",\n            \"flan_t5_symmetric_prompt_average_mrpc\",\n        ],\n        \"min_notebooks_expected\": 6,\n        \"discovery_hint\": (\n            \"Relevant notebooks span four families (direct NLI entailment, zero-shot \"\n            \"NLI pipeline, HF sequence classification pipeline, cross-encoder). \"\n            \"No name pattern unifies them \u2014 they must be found by searching code for \"\n            \"bidirectional processing (enc_12/enc_21, margin_12/margin_21) or via \"\n            \"description/property search for symmetry-related concepts.\"\n        ),\n        \"key_finding\": (\n            \"The effect of bidirectional symmetry enforcement is highly model-family \"\n            \"dependent and does not uniformly improve accuracy. For zero-shot NLI \"\n            \"pipelines, bidirectional averaging slightly hurts performance relative to \"\n            \"single-direction scoring (acc ~0.613 vs ~0.630). For the fine-tuned HF \"\n            \"pipeline, the effect is negligible (acc ~0.850 vs ~0.858). Only for the \"\n            \"cross-encoder does bidirectional averaging provide a modest gain \"\n            \"(acc ~0.699 vs ~0.679). Among aggregation strategies, average-margin \"\n            \"outperforms min-direction by a large margin (acc ~0.703 vs ~0.586 for \"\n            \"direct NLI); min-direction is overly conservative and collapses recall. \"\n            \"The agent should compare aggregation strategies within each family and \"\n            \"note that improvements from bidirectionality are more pronounced for \"\n            \"cross-encoders than for NLI or zero-shot models. Flan-T5 \"\n            \"(flan_t5_symmetric_prompt_average_mrpc) uses a generative symmetry strategy \"\n            \"(averaging yes/no logits for both prompt orderings) and achieves acc ~0.738, \"\n            \"F1 ~0.807, representing a distinct symmetry approach outside the NLI/pipeline \"\n            \"families.\"\n        ),\n    },\n]\n\nTASKS: list[str] = [spec[\"task\"] for spec in TASK_SPECS]\n\n# ---------------------------------------------------------------------------\n# Configuration\n# ---------------------------------------------------------------------------\n\nVAULT_NAME = \"tv_experiment_1\"\nAGENT_MODEL = \"gpt-5.4\"\nEVALUATOR_MODEL = \"gpt-5.4\"\nDEFAULT_EVALUATOR_REASONING: dict = {\"effort\": \"high\"}\nMAX_TURNS = 30\nOUTPUT_ROOT = \"experiment_results\"\n\nOPENAI_KEY_FILE = \"/Users/jinjinzhao/Documents/work_projects/my_keys/my_keys/openai_jinjin.key\"\n\n# ---------------------------------------------------------------------------\n# Evaluator\n# ---------------------------------------------------------------------------\n\nEVALUATOR_SYSTEM_PROMPT = \"\"\"\\\nYou are an expert evaluator assessing the quality of AI-generated data analysis responses.\n\nYou will receive a user task and the results produced by several agents. Each agent used a\ndifferent set of API functions to answer the same question against the same data repository.\n\nWhen ground-truth metadata is provided (expected notebooks, minimum coverage, key finding),\nuse it to assess each agent result on three dimensions:\n\n  1. Notebook coverage \u2014 what fraction of the expected notebooks did the agent cite or\n     retrieve? An agent that finds fewer than the minimum required notebooks should not\n     score above 3, regardless of the quality of its summary.\n\n  2. Factual correctness \u2014 does the agent's reported finding match the expected key finding?\n     Penalise results that draw the opposite conclusion or miss the central pattern.\n\n  3. Analytical depth \u2014 does the summary interpret the evidence (not just list numbers),\n     note cross-family differences, and flag limitations or confounds?\n\nScoring guide (apply all three dimensions; coverage and correctness carry the most weight):\n  5 \u2014 Meets minimum notebook coverage, correct key finding, insightful analysis\n  4 \u2014 Near-minimum coverage or minor factual gap, otherwise complete and correct\n  3 \u2014 Below minimum coverage OR incorrect/missing key finding, but some valid evidence\n  2 \u2014 Severely under-covered (1\u20132 notebooks only) or substantially incorrect conclusion\n  1 \u2014 Does not address the task, errors dominate, or no relevant notebooks retrieved\n\nWhen no ground-truth metadata is provided, fall back to general completeness and accuracy.\n\nReturn a JSON object with exactly this shape (no markdown fences):\n{\n  \"ratings\": {\n    \"<function_experiment_name>\": {\n      \"score\": <int 1\u20135>,\n      \"notebook_coverage\": \"<N of M expected notebooks cited>\",\n      \"rationale\": \"<brief explanation referencing coverage, correctness, depth>\"\n    }\n  },\n  \"overall_comment\": \"<cross-agent comparison and key observations>\"\n}\n\"\"\"\n\n\ndef evaluate_results(\n    client: OpenAI,\n    task: str,\n    agent_results: dict[str, dict[str, Any]],\n    task_metadata: dict | None = None,\n    model: str = EVALUATOR_MODEL,\n    reasoning: dict | None = None,\n) -> dict[str, Any]:\n    \"\"\"Rate each agent result 1\u20135 using a single evaluator that sees all results.\n\n    Args:\n        client: OpenAI client.\n        task: The original task string.\n        agent_results: {experiment_name: {\"result\": {...}, \"metrics\": RunMetrics, \"error\": str|None}}\n        task_metadata: Optional ground-truth dict from TASK_SPECS (expected_notebooks,\n                       min_notebooks_expected, key_finding, difficulty, discovery_hint).\n        model: Evaluator model name.\n        reasoning: Optional reasoning parameter dict, e.g. {\"effort\": \"high\"}.\n\n    Returns:\n        Parsed ratings dict from the evaluator, or a fallback dict on parse failure.\n    \"\"\"\n    result_blocks: list[str] = []\n    for exp_name, run_data in agent_results.items():\n        error = run_data.get(\"error\")\n        if error:\n            result_blocks.append(f\"### Agent: {exp_name}\\n**ERROR:** {error}\\n\")\n        else:\n            result = run_data.get(\"result\") or {}\n            rows = result.get(\"rows\", [])\n            summary = result.get(\"summary\", \"(no summary)\")\n            result_blocks.append(\n                f\"### Agent: {exp_name}\\n\"\n                f\"**Summary:** {summary}\\n\\n\"\n                f\"**Result rows ({len(rows)} rows):**\\n\"\n                f\"```json\\n{json.dumps(rows[:20], indent=2, default=str)}\\n```\\n\"\n            )\n\n    ground_truth_block = \"\"\n    if task_metadata:\n        expected = task_metadata.get(\"expected_notebooks\", [])\n        min_nb = task_metadata.get(\"min_notebooks_expected\", \"?\")\n        key_finding = task_metadata.get(\"key_finding\", \"\")\n        difficulty = task_metadata.get(\"difficulty\", \"\")\n        ground_truth_block = (\n            f\"## Ground-Truth Reference\\n\\n\"\n            f\"**Task difficulty:** {difficulty}\\n\\n\"\n            f\"**Expected notebooks ({len(expected)} total, minimum {min_nb} required):**\\n\"\n            + \"\\n\".join(f\"  - {nb}\" for nb in expected)\n            + f\"\\n\\n**Key finding the agent should identify:**\\n{key_finding}\\n\\n\"\n            \"Use the expected notebook list to assess coverage: count how many of these \"\n            \"names (or close variants) appear in the agent's result rows or summary. \"\n            \"An agent that cites fewer than the minimum required should not score above 3.\\n\\n\"\n        )\n\n    user_content = (\n        f\"## Task\\n{task}\\n\\n\"\n        + ground_truth_block\n        + \"## Agent Results\\n\\n\"\n        + \"\\n---\\n\".join(result_blocks)\n    )\n\n    create_kwargs: dict[str, Any] = dict(\n        model=model,\n        instructions=EVALUATOR_SYSTEM_PROMPT,\n        input=[{\"role\": \"user\", \"content\": user_content}],\n    )\n    if reasoning is not None:\n        create_kwargs[\"reasoning\"] = reasoning\n\n    response = client.responses.create(**create_kwargs)\n\n    raw_text_parts: list[str] = []\n    for item in response.output or []:\n        if getattr(item, \"type\", None) in (\"text\", \"message\"):\n            part = getattr(item, \"text\", None) or getattr(item, \"content\", None) or \"\"\n            if isinstance(part, list):\n                for block in part:\n                    text = getattr(block, \"text\", None) or \"\"\n                    if isinstance(text, str) and text:\n                        raw_text_parts.append(text)\n            elif isinstance(part, str) and part:\n                raw_text_parts.append(part)\n    raw_text = \"\".join(raw_text_parts)\n\n    try:\n        text = raw_text.strip()\n        # Strip markdown code fences if the model wrapped the JSON.\n        if text.startswith(\"```\"):\n            text = re.sub(r\"^```[^\\n]*\\n\", \"\", text)\n            text = re.sub(r\"\\n?```$\", \"\", text).strip()\n        return json.loads(text)\n    except json.JSONDecodeError:\n        return {\n            \"parse_error\": \"Could not parse JSON from evaluator response\",\n            \"raw_response\": raw_text,\n        }\n\n\n# ---------------------------------------------------------------------------\n# Summary helpers\n# ---------------------------------------------------------------------------\n\ndef _extract_summary_stats(metrics: Any) -> dict[str, Any]:\n    \"\"\"Pull the key statistics we care about from a RunMetrics object.\"\"\"\n    s = metrics.summary()\n    return {\n        \"total_tokens\": s[\"tokens\"][\"total\"],\n        \"input_tokens\": s[\"tokens\"][\"input\"],\n        \"output_tokens\": s[\"tokens\"][\"output\"],\n        \"reasoning_tokens\": s[\"tokens\"][\"reasoning\"],\n        # num_turns == total OpenAI API calls == number of turns in the loop\n        \"num_turns\": s[\"api_calls\"],\n        # num_api_function_calls == tool calls that are not finalize_result or no-tool turns\n        \"num_api_function_calls\": sum(\n            1 for t in metrics.turns\n            if t.tool_name is not None and t.tool_name != \"finalize_result\"\n        ),\n        \"wall_time_s\": s[\"timing\"][\"wall_time_s\"],\n    }\n\n\ndef _safe_avg(values: list[float | int]) -> float | None:\n    return round(sum(values) / len(values), 2) if values else None\n\n\ndef _slugify(text: str, max_len: int = 40) -> str:\n    slug = re.sub(r\"[^a-zA-Z0-9]+\", \"_\", text).strip(\"_\").lower()\n    return slug[:max_len]\n\n\n# ---------------------------------------------------------------------------\n# Main experiment loop\n# ---------------------------------------------------------------------------\n\ndef run_experiments(\n    tasks: list[str] = TASKS,\n    task_specs: list[dict] | None = TASK_SPECS,\n    vault_name: str = VAULT_NAME,\n    agent_model: str = AGENT_MODEL,\n    evaluator_model: str = EVALUATOR_MODEL,\n    evaluator_reasoning: dict | None = DEFAULT_EVALUATOR_REASONING,\n    max_turns: int = MAX_TURNS,\n    output_root: str = OUTPUT_ROOT,\n    function_experiments: dict[str, list[str]] | None = None,\n) -> None:\n    \"\"\"Run all experiments and save results.\n\n    Args:\n        tasks: List of task strings to evaluate.\n        task_specs: Optional list of TASK_SPECS dicts providing ground-truth metadata\n                    (expected_notebooks, key_finding, difficulty) for the evaluator.\n                    Must align 1-to-1 with tasks if provided.\n        vault_name: TableVault database name passed to initialization().\n        agent_model: Model used by the agentic workflow.\n        evaluator_model: Model used by the evaluator.\n        evaluator_reasoning: Reasoning dict for the evaluator (e.g. {\"effort\": \"high\"}).\n                             Pass None to disable reasoning.\n        max_turns: Maximum turns per agent run.\n        output_root: Root directory for all output files.\n        function_experiments: Override FUNCTION_EXPERIMENTS; defaults to the full set.\n    \"\"\"\n    if function_experiments is None:\n        function_experiments = FUNCTION_EXPERIMENTS\n\n    with open(OPENAI_KEY_FILE, \"r\") as f:\n        os.environ[\"OPENAI_API_KEY\"] = f.read().strip()\n    client = OpenAI()\n\n    vault = initialization(vault_name)\n\n    run_id = datetime.now(timezone.utc).strftime(\"%Y%m%dT%H%M%SZ\")\n    run_dir = os.path.join(output_root, run_id)\n    os.makedirs(run_dir, exist_ok=True)\n\n    print(\n        f\"\\n=== Experiment run {run_id} | {len(tasks)} task(s) | \"\n        f\"{len(function_experiments)} function set(s) ===\"\n    )\n    print(f\"Output directory: {run_dir}\\n\")\n\n    all_task_summaries: list[dict[str, Any]] = []\n\n    for task_idx, task in enumerate(tasks):\n        task_meta = task_specs[task_idx] if task_specs and task_idx < len(task_specs) else None\n        task_slug = _slugify(task)\n        task_label = f\"task_{task_idx:03d}_{task_slug}\"\n        task_dir = os.path.join(run_dir, task_label)\n        os.makedirs(task_dir, exist_ok=True)\n\n        print(f\"\\n{'='*70}\")\n        print(f\"TASK {task_idx}: {task}\")\n        print(f\"{'='*70}\\n\")\n\n        agent_results: dict[str, dict[str, Any]] = {}\n\n        # --- Run each function experiment in sequence ---\n        for exp_name, fn_list in function_experiments.items():\n            print(f\"\\n--- [{exp_name}] functions: {fn_list} ---\")\n            exp_dir = os.path.join(task_dir, exp_name)\n            os.makedirs(exp_dir, exist_ok=True)\n\n            try:\n                wf = AgenticWorkflow(\n                    client=client,\n                    model=agent_model,\n                    system_prompt=SYSTEM_PROMPT,\n                    vault=vault,\n                    workflow_key=exp_name,\n                    max_turns=max_turns,\n                    trace_output_dir=exp_dir,\n                    trace_filename_stem=\"trace\",\n                    reasoning={\"effort\": \"high\"},\n                )\n                output = wf.run(task)\n                agent_results[exp_name] = {\n                    \"result\": output[\"result\"],\n                    \"metrics\": output[\"metrics\"],\n                    \"error\": None,\n                }\n            except Exception as exc:\n                print(f\"  [ERROR] experiment '{exp_name}' failed: {exc}\")\n                agent_results[exp_name] = {\n                    \"result\": None,\n                    \"metrics\": None,\n                    \"error\": str(exc),\n                }\n\n        # --- Evaluate all results for this task with a single evaluator call ---\n        print(f\"\\n--- Evaluating {len(agent_results)} agent result(s) ---\")\n        ratings = evaluate_results(\n            client=client,\n            task=task,\n            agent_results=agent_results,\n            task_metadata=task_meta,\n            model=evaluator_model,\n            reasoning=evaluator_reasoning,\n        )\n\n        ratings_path = os.path.join(task_dir, \"ratings.json\")\n        with open(ratings_path, \"w\", encoding=\"utf-8\") as f:\n            json.dump({\"task\": task, \"ratings\": ratings}, f, indent=2, default=str)\n        print(f\"  ratings saved -> {ratings_path}\")\n\n        # --- Build per-task summary (stats + rating for each experiment) ---\n        task_summary: dict[str, Any] = {\n            \"task_idx\": task_idx,\n            \"task\": task,\n            \"difficulty\": task_meta.get(\"difficulty\") if task_meta else None,\n            \"expected_notebooks\": task_meta.get(\"expected_notebooks\") if task_meta else None,\n            \"min_notebooks_expected\": task_meta.get(\"min_notebooks_expected\") if task_meta else None,\n            \"key_finding\": task_meta.get(\"key_finding\") if task_meta else None,\n            \"experiments\": {},\n        }\n        per_experiment_ratings: dict[str, Any] = (ratings.get(\"ratings\") or {})\n        for exp_name, run_data in agent_results.items():\n            entry: dict[str, Any] = {\"error\": run_data[\"error\"]}\n            if run_data[\"metrics\"] is not None:\n                entry[\"stats\"] = _extract_summary_stats(run_data[\"metrics\"])\n            if exp_name in per_experiment_ratings:\n                entry[\"rating\"] = per_experiment_ratings[exp_name]\n            task_summary[\"experiments\"][exp_name] = entry\n\n        all_task_summaries.append(task_summary)\n\n        task_summary_path = os.path.join(task_dir, \"summary.json\")\n        with open(task_summary_path, \"w\", encoding=\"utf-8\") as f:\n            json.dump(task_summary, f, indent=2, default=str)\n        print(f\"  task summary saved -> {task_summary_path}\")\n\n        # --- Print per-task results table ---\n        difficulty_label = f\" [{task_meta['difficulty']}]\" if task_meta else \"\"\n        print(f\"\\n--- Results for task {task_idx}{difficulty_label}: {task} ---\")\n        if task_meta:\n            print(\n                f\"  Expected notebooks ({task_meta['min_notebooks_expected']} min): \"\n                + \", \".join(task_meta[\"expected_notebooks\"])\n            )\n        print(\n            f\"\\n{'Experiment':<35} {'Tokens':>12} {'FnCalls':>10} \"\n            f\"{'Turns':>8} {'Score':>8} {'Coverage':>10}  Rationale\"\n        )\n        print(\"-\" * 115)\n        for exp_name, exp_data in task_summary[\"experiments\"].items():\n            error = exp_data.get(\"error\")\n            if error:\n                print(f\"{exp_name:<35} {'ERROR':>12}  {error[:60]}\")\n                continue\n            stats = exp_data.get(\"stats\", {})\n            rating = exp_data.get(\"rating\", {})\n            score = rating.get(\"score\", \"-\") if isinstance(rating, dict) else \"-\"\n            coverage = rating.get(\"notebook_coverage\", \"-\") if isinstance(rating, dict) else \"-\"\n            rationale = rating.get(\"rationale\", \"\") if isinstance(rating, dict) else \"\"\n            print(\n                f\"{exp_name:<35} \"\n                f\"{str(stats.get('total_tokens', '-')):>12} \"\n                f\"{str(stats.get('num_api_function_calls', '-')):>10} \"\n                f\"{str(stats.get('num_turns', '-')):>8} \"\n                f\"{str(score):>8} \"\n                f\"{str(coverage):>10}  {rationale[:55]}\"\n            )\n        overall = ratings.get(\"overall_comment\", \"\")\n        if overall:\n            print(f\"\\nOverall: {overall}\")\n        print()\n\n    # --- Aggregate stats across all tasks, grouped by function experiment ---\n    by_experiment: dict[str, dict[str, Any]] = {}\n    for exp_name in function_experiments:\n        token_totals, api_fn_call_totals, turn_totals, scores = [], [], [], []\n        for ts in all_task_summaries:\n            exp_data = ts[\"experiments\"].get(exp_name, {})\n            stats = exp_data.get(\"stats\")\n            if stats:\n                token_totals.append(stats[\"total_tokens\"])\n                api_fn_call_totals.append(stats[\"num_api_function_calls\"])\n                turn_totals.append(stats[\"num_turns\"])\n            rating = exp_data.get(\"rating\")\n            if isinstance(rating, dict) and isinstance(rating.get(\"score\"), (int, float)):\n                scores.append(rating[\"score\"])\n\n        by_experiment[exp_name] = {\n            \"num_tasks_completed\": len(token_totals),\n            \"avg_total_tokens\": _safe_avg(token_totals),\n            \"avg_num_api_function_calls\": _safe_avg(api_fn_call_totals),\n            \"avg_num_turns\": _safe_avg(turn_totals),\n            \"avg_rating\": _safe_avg(scores),\n        }\n\n    global_summary: dict[str, Any] = {\n        \"run_id\": run_id,\n        \"agent_model\": agent_model,\n        \"evaluator_model\": evaluator_model,\n        \"evaluator_reasoning\": evaluator_reasoning,\n        \"vault_name\": vault_name,\n        \"num_tasks\": len(tasks),\n        \"by_experiment\": by_experiment,\n        \"per_task\": all_task_summaries,\n    }\n\n    global_summary_path = os.path.join(run_dir, \"global_summary.json\")\n    with open(global_summary_path, \"w\", encoding=\"utf-8\") as f:\n        json.dump(global_summary, f, indent=2, default=str)\n    print(f\"\\n=== Global summary saved -> {global_summary_path} ===\")\n\n    # --- Print aggregate table ---\n    print(\n        f\"\\n{'Experiment':<35} {'AvgTokens':>12} {'AvgFnCalls':>12} \"\n        f\"{'AvgTurns':>10} {'AvgScore':>10}\"\n    )\n    print(\"-\" * 82)\n    for exp_name, agg in by_experiment.items():\n        print(\n            f\"{exp_name:<35} \"\n            f\"{str(agg['avg_total_tokens']):>12} \"\n            f\"{str(agg['avg_num_api_function_calls']):>12} \"\n            f\"{str(agg['avg_num_turns']):>10} \"\n            f\"{str(agg['avg_rating']):>10}\"\n        )\n    print()\n\n\n# ---------------------------------------------------------------------------\n# Entry point\n# ---------------------------------------------------------------------------\n\nif __name__ == \"__main__\":\n    run_experiments()\n"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 1645 | 48 | 23 | 75 | 1.672s | 0.025s |

---

## Turn 2 — `code_search` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c173f5081958d47d41124512da6`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_px78BFXN1Nu6zhmwdf5o0Lxp",
    "output": "{\"ok\": true, \"result\": [\"\\\"\\\"\\\"\\nnotebook_experiments.py\\n\\nRuns AgenticWorkflow (eval_agent) over each function experiment set in FUNCTION_EXPERIMENTS\\nfor a list of tasks. After all agents complete for a task, a separate OpenAI evaluator\\ninstance rates each result 1\\u20135, seeing all agent results together for comparison.\\n\\nFull traces are saved in a structured folder hierarchy. A summary JSON capturing tokens\\nused, API function calls made, and turns taken is saved per task and per function subset.\\n\\nFolder layout:\\n    <output_root>/\\n      <run_id>/\\n        <task_label>/\\n          <experiment_name>/\\n            trace.json\\n            trace.md\\n          ratings.json\\n          summary.json\\n        global_summary.json\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\nimport re\\nimport sys\\nfrom datetime import datetime, timezone\\nfrom typing import Any\\n\\nfrom openai import OpenAI\\n\\n# Ensure the evaluation_agents package is importable when run from the repo root.\\nsys.path.insert(0, os.path.dirname(__file__))\\n\\nfrom eval_agent_functions import AgenticWorkflow, SYSTEM_PROMPT\\nfrom api_functions import FUNCTION_EXPERIMENTS, initialization\\n\\n# ---------------------------------------------------------------------------\\n# Task list with ground-truth metadata for evaluation\\n# ---------------------------------------------------------------------------\\n\\nTASK_SPECS: list[dict] = [\\n    {\\n        # Easy: all relevant notebooks share 'distilbert_feature_extraction' or a\\n        # pooling keyword in their names \\u2014 discoverable by name enumeration alone.\\n        \\\"task\\\": (\\n            \\\"How does the pooling strategy used to extract sentence representations \\\"\\n            \\\"from DistilBERT affect paraphrase detection accuracy on MRPC?\\\"\\n        ),\\n        \\\"difficulty\\\": \\\"easy\\\",\\n        \\\"expected_notebooks\\\": [\\n            \\\"distilbert_feature_extraction_cosine_mrpc\\\",\\n            \\\"distilbert_cls_cosine_mrpc\\\",\\n            \\\"distilbert_max_pool_cosine_mrpc\\\",\\n            \\\"distilbert_no_special_tokens_mean_cosine_mrpc\\\",\\n            \\\"distilbert_last4_mean_cosine_mrpc\\\",\\n            \\\"distilbert_mean_cosine_median_threshold_mrpc\\\",\\n        ],\\n        \\\"min_notebooks_expected\\\": 5,\\n        \\\"discovery_hint\\\": (\\n            \\\"All relevant notebooks share 'distilbert' and a pooling-related keyword \\\"\\n            \\\"(cls, max_pool, mean, last4, no_special_tokens) in their names. \\\"\\n            \\\"A simple name enumeration is sufficient to find them.\\\"\\n        ),\\n        \\\"key_finding\\\": (\\n            \\\"Last-layer mean pooling (with or without special tokens) marginally \\\"\\n            \\\"outperforms CLS-token and max-pool extraction, but differences are small \\\"\\n            \\\"(accuracy ~0.696\\u20130.703 vs ~0.684\\u20130.686 at threshold=0.85). Averaging the \\\"\\n            \\\"last four hidden layers before mean-pooling does not improve over \\\"\\n            \\\"single-layer mean pooling and performs on par with CLS and max-pool. \\\"\\n            \\\"Note: distilbert_mean_cosine_median_threshold_mrpc uses a data-driven \\\"\\n            \\\"median threshold rather than 0.85 and shows substantially lower performance \\\"\\n            \\\"(accuracy ~0.65, F1 ~0.70) \\u2014 this reflects threshold sensitivity, not \\\"\\n            \\\"pooling quality, and should not be interpreted as a pooling result. \\\"\\n            \\\"The agent should report accuracy and F1 per pooling variant at a fixed \\\"\\n            \\\"threshold and note that the overall spread across strategies is narrow.\\\"\\n        ),\\n    },\\n    {\\n        # Medium: notebooks span three families (bi-encoder, distilbert feature\\n        # extraction, HF pipeline, cross-encoder). Code search for 'threshold' or\\n        # description search are needed; name enumeration alone misses cross-family scope.\\n        \\\"task\\\": (\\n            \\\"How sensitive are similarity-based paraphrase classifiers to the choice \\\"\\n            \\\"of decision threshold, and does this vary across model families?\\\"\\n        ),\\n        \\\"difficulty\\\": \\\"medium\\\",\\n        \\\"expected_notebooks\\\": [\\n            \\\"sentence_transformers_bi_encoder_cosine_mrpc\\\",\\n            \\\"st_paraphrase_minilm_l6_cosine_threshold_mrpc\\\",\\n            \\\"st_paraphrase_minilm_l3_cosine_threshold_mrpc\\\",\\n            \\\"st_all_minilm_l6_l2_distance_threshold_mrpc\\\",\\n            \\\"st_all_distilroberta_v1_cosine_threshold_mrpc\\\",\\n            \\\"distilbert_mean_cosine_median_threshold_mrpc\\\",\\n            \\\"hf_pipeline_mrpc_threshold_070\\\",\\n            \\\"quora_cross_encoder_softmax_threshold_065_mrpc\\\",\\n            \\\"paraphrase_score_threshold_zero_shot_mrpc\\\",\\n        ],\\n        \\\"min_notebooks_expected\\\": 6,\\n        \\\"discovery_hint\\\": (\\n            \\\"Relevant notebooks span three families (sentence-transformers bi-encoder, \\\"\\n            \\\"distilbert feature extraction, HF pipeline, cross-encoder). \\\"\\n            \\\"Code search for 'threshold' or description/property search are the most \\\"\\n            \\\"direct routes; name enumeration alone is insufficient without cross-family \\\"\\n            \\\"awareness.\\\"\\n        ),\\n        \\\"key_finding\\\": (\\n            \\\"Threshold choice significantly shifts the precision/recall trade-off. \\\"\\n            \\\"The fine-tuned HF pipeline at threshold=0.70 (acc ~0.848, F1 ~0.890) \\\"\\n            \\\"stays close to its argmax baseline, while bi-encoder cosine models \\\"\\n            \\\"(paraphrase-MiniLM-L6 at 0.78: acc ~0.701, F1 ~0.771; all-distilroberta-v1 \\\"\\n            \\\"at 0.72: acc ~0.723, F1 ~0.806) and the cross-encoder (quora-distilroberta \\\"\\n            \\\"at 0.65: acc ~0.679, F1 ~0.758) degrade more sharply at non-optimal \\\"\\n            \\\"thresholds. Zero-shot NLI models are especially sensitive: applying a \\\"\\n            \\\"threshold of 0.55 (paraphrase_score_threshold_zero_shot_mrpc) yields \\\"\\n            \\\"acc ~0.578, F1 ~0.674. The agent should identify notebooks from multiple \\\"\\n            \\\"families that vary the threshold, report how accuracy and F1 change, and \\\"\\n            \\\"note that the optimal threshold and sensitivity to its choice differ \\\"\\n            \\\"substantially by model family and similarity metric.\\\"\\n        ),\\n    },\\n    {\\n        # Hard: notebooks are spread across four model families with no shared name\\n        # pattern. Must be found via code search for bidirectional processing patterns\\n        # (enc_12/enc_21, margin_12/margin_21) or via description/property search.\\n        \\\"task\\\": (\\n            \\\"How do different strategies for enforcing prediction symmetry affect \\\"\\n            \\\"accuracy when using NLI-based and zero-shot models for paraphrase \\\"\\n            \\\"detection on MRPC?\\\"\\n        ),\\n        \\\"difficulty\\\": \\\"hard\\\",\\n        \\\"expected_notebooks\\\": [\\n            \\\"direct_nli_entailment_mrpc\\\",\\n            \\\"min_direction_margin_mrpc\\\",\\n            \\\"consensus_then_avg_margin_mrpc\\\",\\n            \\\"neutral_penalized_margin_mrpc\\\",\\n            \\\"softmax_gap_mean_mrpc\\\",\\n            \\\"bidirectional_averaged_zero_shot_mrpc\\\",\\n            \\\"hf_pipeline_mrpc_bidirectional_order_average\\\",\\n            \\\"quora_cross_encoder_symmetric_average_mrpc\\\",\\n            \\\"flan_t5_symmetric_prompt_average_mrpc\\\",\\n        ],\\n        \\\"min_notebooks_expected\\\": 6,\\n        \\\"discovery_hint\\\": (\\n            \\\"Relevant notebooks span four families (direct NLI entailment, zero-shot \\\"\\n            \\\"NLI pipeline, HF sequence classification pipeline, cross-encoder). \\\"\\n            \\\"No name pattern unifies them \\u2014 they must be found by searching code for \\\"\\n            \\\"bidirectional processing (enc_12/enc_21, margin_12/margin_21) or via \\\"\\n            \\\"description/property search for symmetry-related concepts.\\\"\\n        ),\\n        \\\"key_finding\\\": (\\n            \\\"The effect of bidirectional symmetry enforcement is highly model-family \\\"\\n            \\\"dependent and does not uniformly improve accuracy. For zero-shot NLI \\\"\\n            \\\"pipelines, bidirectional averaging slightly hurts performance relative to \\\"\\n            \\\"single-direction scoring (acc ~0.613 vs ~0.630). For the fine-tuned HF \\\"\\n            \\\"pipeline, the effect is negligible (acc ~0.850 vs ~0.858). Only for the \\\"\\n            \\\"cross-encoder does bidirectional averaging provide a modest gain \\\"\\n            \\\"(acc ~0.699 vs ~0.679). Among aggregation strategies, average-margin \\\"\\n            \\\"outperforms min-direction by a large margin (acc ~0.703 vs ~0.586 for \\\"\\n            \\\"direct NLI); min-direction is overly conservative and collapses recall. \\\"\\n            \\\"The agent should compare aggregation strategies within each family and \\\"\\n            \\\"note that improvements from bidirectionality are more pronounced for \\\"\\n            \\\"cross-encoders than for NLI or zero-shot models. Flan-T5 \\\"\\n            \\\"(flan_t5_symmetric_prompt_average_mrpc) uses a generative symmetry strategy \\\"\\n            \\\"(averaging yes/no logits for both prompt orderings) and achieves acc ~0.738, \\\"\\n            \\\"F1 ~0.807, representing a distinct symmetry approach outside the NLI/pipeline \\\"\\n            \\\"families.\\\"\\n        ),\\n    },\\n]\\n\\nTASKS: list[str] = [spec[\\\"task\\\"] for spec in TASK_SPECS]\\n\\n# ---------------------------------------------------------------------------\\n# Configuration\\n# ---------------------------------------------------------------------------\\n\\nVAULT_NAME = \\\"tv_experiment_1\\\"\\nAGENT_MODEL = \\\"gpt-5.4\\\"\\nEVALUATOR_MODEL = \\\"gpt-5.4\\\"\\nDEFAULT_EVALUATOR_REASONING: dict = {\\\"effort\\\": \\\"high\\\"}\\nMAX_TURNS = 30\\nOUTPUT_ROOT = \\\"experiment_results\\\"\\n\\nOPENAI_KEY_FILE = \\\"/Users/jinjinzhao/Documents/work_projects/my_keys/my_keys/openai_jinjin.key\\\"\\n\\n# ---------------------------------------------------------------------------\\n# Evaluator\\n# ---------------------------------------------------------------------------\\n\\nEVALUATOR_SYSTEM_PROMPT = \\\"\\\"\\\"\\\\\\nYou are an expert evaluator assessing the quality of AI-generated data analysis responses.\\n\\nYou will receive a user task and the results produced by several agents. Each agent used a\\ndifferent set of API functions to answer the same question against the same data repository.\\n\\nWhen ground-truth metadata is provided (expected notebooks, minimum coverage, key finding),\\nuse it to assess each agent result on three dimensions:\\n\\n  1. Notebook coverage \\u2014 what fraction of the expected notebooks did the agent cite or\\n     retrieve? An agent that finds fewer than the minimum required notebooks should not\\n     score above 3, regardless of the quality of its summary.\\n\\n  2. Factual correctness \\u2014 does the agent's reported finding match the expected key finding?\\n     Penalise results that draw the opposite conclusion or miss the central pattern.\\n\\n  3. Analytical depth \\u2014 does the summary interpret the evidence (not just list numbers),\\n     note cross-family differences, and flag limitations or confounds?\\n\\nScoring guide (apply all three dimensions; coverage and correctness carry the most weight):\\n  5 \\u2014 Meets minimum notebook coverage, correct key finding, insightful analysis\\n  4 \\u2014 Near-minimum coverage or minor factual gap, otherwise complete and correct\\n  3 \\u2014 Below minimum coverage OR incorrect/missing key finding, but some valid evidence\\n  2 \\u2014 Severely under-covered (1\\u20132 notebooks only) or substantially incorrect conclusion\\n  1 \\u2014 Does not address the task, errors dominate, or no relevant notebooks retrieved\\n\\nWhen no ground-truth metadata is provided, fall back to general completeness and accuracy.\\n\\nReturn a JSON object with exactly this shape (no markdown fences):\\n{\\n  \\\"ratings\\\": {\\n    \\\"<function_experiment_name>\\\": {\\n      \\\"score\\\": <int 1\\u20135>,\\n      \\\"notebook_coverage\\\": \\\"<N of M expected notebooks cited>\\\",\\n      \\\"rationale\\\": \\\"<brief explanation referencing coverage, correctness, depth>\\\"\\n    }\\n  },\\n  \\\"overall_comment\\\": \\\"<cross-agent comparison and key observations>\\\"\\n}\\n\\\"\\\"\\\"\\n\\n\\ndef evaluate_results(\\n    client: OpenAI,\\n    task: str,\\n    agent_results: dict[str, dict[str, Any]],\\n    task_metadata: dict | None = None,\\n    model: str = EVALUATOR_MODEL,\\n    reasoning: dict | None = None,\\n) -> dict[str, Any]:\\n    \\\"\\\"\\\"Rate each agent result 1\\u20135 using a single evaluator that sees all results.\\n\\n    Args:\\n        client: OpenAI client.\\n        task: The original task string.\\n        agent_results: {experiment_name: {\\\"result\\\": {...}, \\\"metrics\\\": RunMetrics, \\\"error\\\": str|None}}\\n        task_metadata: Optional ground-truth dict from TASK_SPECS (expected_notebooks,\\n                       min_notebooks_expected, key_finding, difficulty, discovery_hint).\\n        model: Evaluator model name.\\n        reasoning: Optional reasoning parameter dict, e.g. {\\\"effort\\\": \\\"high\\\"}.\\n\\n    Returns:\\n        Parsed ratings dict from the evaluator, or a fallback dict on parse failure.\\n    \\\"\\\"\\\"\\n    result_blocks: list[str] = []\\n    for exp_name, run_data in agent_results.items():\\n        error = run_data.get(\\\"error\\\")\\n        if error:\\n            result_blocks.append(f\\\"### Agent: {exp_name}\\\\n**ERROR:** {error}\\\\n\\\")\\n        else:\\n            result = run_data.get(\\\"result\\\") or {}\\n            rows = result.get(\\\"rows\\\", [])\\n            summary = result.get(\\\"summary\\\", \\\"(no summary)\\\")\\n            result_blocks.append(\\n                f\\\"### Agent: {exp_name}\\\\n\\\"\\n                f\\\"**Summary:** {summary}\\\\n\\\\n\\\"\\n                f\\\"**Result rows ({len(rows)} rows):**\\\\n\\\"\\n                f\\\"```json\\\\n{json.dumps(rows[:20], indent=2, default=str)}\\\\n```\\\\n\\\"\\n            )\\n\\n    ground_truth_block = \\\"\\\"\\n    if task_metadata:\\n        expected = task_metadata.get(\\\"expected_notebooks\\\", [])\\n        min_nb = task_metadata.get(\\\"min_notebooks_expected\\\", \\\"?\\\")\\n        key_finding = task_metadata.get(\\\"key_finding\\\", \\\"\\\")\\n        difficulty = task_metadata.get(\\\"difficulty\\\", \\\"\\\")\\n        ground_truth_block = (\\n            f\\\"## Ground-Truth Reference\\\\n\\\\n\\\"\\n            f\\\"**Task difficulty:** {difficulty}\\\\n\\\\n\\\"\\n            f\\\"**Expected notebooks ({len(expected)} total, minimum {min_nb} required):**\\\\n\\\"\\n            + \\\"\\\\n\\\".join(f\\\"  - {nb}\\\" for nb in expected)\\n            + f\\\"\\\\n\\\\n**Key finding the agent should identify:**\\\\n{key_finding}\\\\n\\\\n\\\"\\n            \\\"Use the expected notebook list to assess coverage: count how many of these \\\"\\n            \\\"names (or close variants) appear in the agent's result rows or summary. \\\"\\n            \\\"An agent that cites fewer than the minimum required should not score above 3.\\\\n\\\\n\\\"\\n        )\\n\\n    user_content = (\\n        f\\\"## Task\\\\n{task}\\\\n\\\\n\\\"\\n        + ground_truth_block\\n        + \\\"## Agent Results\\\\n\\\\n\\\"\\n        + \\\"\\\\n---\\\\n\\\".join(result_blocks)\\n    )\\n\\n    create_kwargs: dict[str, Any] = dict(\\n        model=model,\\n        instructions=EVALUATOR_SYSTEM_PROMPT,\\n        input=[{\\\"role\\\": \\\"user\\\", \\\"content\\\": user_content}],\\n    )\\n    if reasoning is not None:\\n        create_kwargs[\\\"reasoning\\\"] = reasoning\\n\\n    response = client.responses.create(**create_kwargs)\\n\\n    raw_text_parts: list[str] = []\\n    for item in response.output or []:\\n        if getattr(item, \\\"type\\\", None) in (\\\"text\\\", \\\"message\\\"):\\n            part = getattr(item, \\\"text\\\", None) or getattr(item, \\\"content\\\", None) or \\\"\\\"\\n            if isinstance(part, list):\\n                for block in part:\\n                    text = getattr(block, \\\"text\\\", None) or \\\"\\\"\\n                    if isinstance(text, str) and text:\\n                        raw_text_parts.append(text)\\n            elif isinstance(part, str) and part:\\n                raw_text_parts.append(part)\\n    raw_text = \\\"\\\".join(raw_text_parts)\\n\\n    try:\\n        text = raw_text.strip()\\n        # Strip markdown code fences if the model wrapped the JSON.\\n        if text.startswith(\\\"```\\\"):\\n            text = re.sub(r\\\"^```[^\\\\n]*\\\\n\\\", \\\"\\\", text)\\n            text = re.sub(r\\\"\\\\n?```$\\\", \\\"\\\", text).strip()\\n        return json.loads(text)\\n    except json.JSONDecodeError:\\n        return {\\n            \\\"parse_error\\\": \\\"Could not parse JSON from evaluator response\\\",\\n            \\\"raw_response\\\": raw_text,\\n        }\\n\\n\\n# ---------------------------------------------------------------------------\\n# Summary helpers\\n# ---------------------------------------------------------------------------\\n\\ndef _extract_summary_stats(metrics: Any) -> dict[str, Any]:\\n    \\\"\\\"\\\"Pull the key statistics we care about from a RunMetrics object.\\\"\\\"\\\"\\n    s = metrics.summary()\\n    return {\\n        \\\"total_tokens\\\": s[\\\"tokens\\\"][\\\"total\\\"],\\n        \\\"input_tokens\\\": s[\\\"tokens\\\"][\\\"input\\\"],\\n        \\\"output_tokens\\\": s[\\\"tokens\\\"][\\\"output\\\"],\\n        \\\"reasoning_tokens\\\": s[\\\"tokens\\\"][\\\"reasoning\\\"],\\n        # num_turns == total OpenAI API calls == number of turns in the loop\\n        \\\"num_turns\\\": s[\\\"api_calls\\\"],\\n        # num_api_function_calls == tool calls that are not finalize_result or no-tool turns\\n        \\\"num_api_function_calls\\\": sum(\\n            1 for t in metrics.turns\\n            if t.tool_name is not None and t.tool_name != \\\"finalize_result\\\"\\n        ),\\n        \\\"wall_time_s\\\": s[\\\"timing\\\"][\\\"wall_time_s\\\"],\\n    }\\n\\n\\ndef _safe_avg(values: list[float | int]) -> float | None:\\n    return round(sum(values) / len(values), 2) if values else None\\n\\n\\ndef _slugify(text: str, max_len: int = 40) -> str:\\n    slug = re.sub(r\\\"[^a-zA-Z0-9]+\\\", \\\"_\\\", text).strip(\\\"_\\\").lower()\\n    return slug[:max_len]\\n\\n\\n# ---------------------------------------------------------------------------\\n# Main experiment loop\\n# ---------------------------------------------------------------------------\\n\\ndef run_experiments(\\n    tasks: list[str] = TASKS,\\n    task_specs: list[dict] | None = TASK_SPECS,\\n    vault_name: str = VAULT_NAME,\\n    agent_model: str = AGENT_MODEL,\\n    evaluator_model: str = EVALUATOR_MODEL,\\n    evaluator_reasoning: dict | None = DEFAULT_EVALUATOR_REASONING,\\n    max_turns: int = MAX_TURNS,\\n    output_root: str = OUTPUT_ROOT,\\n    function_experiments: dict[str, list[str]] | None = None,\\n) -> None:\\n    \\\"\\\"\\\"Run all experiments and save results.\\n\\n    Args:\\n        tasks: List of task strings to evaluate.\\n        task_specs: Optional list of TASK_SPECS dicts providing ground-truth metadata\\n                    (expected_notebooks, key_finding, difficulty) for the evaluator.\\n                    Must align 1-to-1 with tasks if provided.\\n        vault_name: TableVault database name passed to initialization().\\n        agent_model: Model used by the agentic workflow.\\n        evaluator_model: Model used by the evaluator.\\n        evaluator_reasoning: Reasoning dict for the evaluator (e.g. {\\\"effort\\\": \\\"high\\\"}).\\n                             Pass None to disable reasoning.\\n        max_turns: Maximum turns per agent run.\\n        output_root: Root directory for all output files.\\n        function_experiments: Override FUNCTION_EXPERIMENTS; defaults to the full set.\\n    \\\"\\\"\\\"\\n    if function_experiments is None:\\n        function_experiments = FUNCTION_EXPERIMENTS\\n\\n    with open(OPENAI_KEY_FILE, \\\"r\\\") as f:\\n        os.environ[\\\"OPENAI_API_KEY\\\"] = f.read().strip()\\n    client = OpenAI()\\n\\n    vault = initialization(vault_name)\\n\\n    run_id = datetime.now(timezone.utc).strftime(\\\"%Y%m%dT%H%M%SZ\\\")\\n    run_dir = os.path.join(output_root, run_id)\\n    os.makedirs(run_dir, exist_ok=True)\\n\\n    print(\\n        f\\\"\\\\n=== Experiment run {run_id} | {len(tasks)} task(s) | \\\"\\n        f\\\"{len(function_experiments)} function set(s) ===\\\"\\n    )\\n    print(f\\\"Output directory: {run_dir}\\\\n\\\")\\n\\n    all_task_summaries: list[dict[str, Any]] = []\\n\\n    for task_idx, task in enumerate(tasks):\\n        task_meta = task_specs[task_idx] if task_specs and task_idx < len(task_specs) else None\\n        task_slug = _slugify(task)\\n        task_label = f\\\"task_{task_idx:03d}_{task_slug}\\\"\\n        task_dir = os.path.join(run_dir, task_label)\\n        os.makedirs(task_dir, exist_ok=True)\\n\\n        print(f\\\"\\\\n{'='*70}\\\")\\n        print(f\\\"TASK {task_idx}: {task}\\\")\\n        print(f\\\"{'='*70}\\\\n\\\")\\n\\n        agent_results: dict[str, dict[str, Any]] = {}\\n\\n        # --- Run each function experiment in sequence ---\\n        for exp_name, fn_list in function_experiments.items():\\n            print(f\\\"\\\\n--- [{exp_name}] functions: {fn_list} ---\\\")\\n            exp_dir = os.path.join(task_dir, exp_name)\\n            os.makedirs(exp_dir, exist_ok=True)\\n\\n            try:\\n                wf = AgenticWorkflow(\\n                    client=client,\\n                    model=agent_model,\\n                    system_prompt=SYSTEM_PROMPT,\\n                    vault=vault,\\n                    workflow_key=exp_name,\\n                    max_turns=max_turns,\\n                    trace_output_dir=exp_dir,\\n                    trace_filename_stem=\\\"trace\\\",\\n                    reasoning={\\\"effort\\\": \\\"high\\\"},\\n                )\\n                output = wf.run(task)\\n                agent_results[exp_name] = {\\n                    \\\"result\\\": output[\\\"result\\\"],\\n                    \\\"metrics\\\": output[\\\"metrics\\\"],\\n                    \\\"error\\\": None,\\n                }\\n            except Exception as exc:\\n                print(f\\\"  [ERROR] experiment '{exp_name}' failed: {exc}\\\")\\n                agent_results[exp_name] = {\\n                    \\\"result\\\": None,\\n                    \\\"metrics\\\": None,\\n                    \\\"error\\\": str(exc),\\n                }\\n\\n        # --- Evaluate all results for this task with a single evaluator call ---\\n        print(f\\\"\\\\n--- Evaluating {len(agent_results)} agent result(s) ---\\\")\\n        ratings = evaluate_results(\\n            client=client,\\n            task=task,\\n            agent_results=agent_results,\\n            task_metadata=task_meta,\\n            model=evaluator_model,\\n            reasoning=evaluator_reasoning,\\n        )\\n\\n        ratings_path = os.path.join(task_dir, \\\"ratings.json\\\")\\n        with open(ratings_path, \\\"w\\\", encoding=\\\"utf-8\\\") as f:\\n            json.dump({\\\"task\\\": task, \\\"ratings\\\": ratings}, f, indent=2, default=str)\\n        print(f\\\"  ratings saved -> {ratings_path}\\\")\\n\\n        # --- Build per-task summary (stats + rating for each experiment) ---\\n        task_summary: dict[str, Any] = {\\n            \\\"task_idx\\\": task_idx,\\n            \\\"task\\\": task,\\n            \\\"difficulty\\\": task_meta.get(\\\"difficulty\\\") if task_meta else None,\\n            \\\"expected_notebooks\\\": task_meta.get(\\\"expected_notebooks\\\") if task_meta else None,\\n            \\\"min_notebooks_expected\\\": task_meta.get(\\\"min_notebooks_expected\\\") if task_meta else None,\\n            \\\"key_finding\\\": task_meta.get(\\\"key_finding\\\") if task_meta else None,\\n            \\\"experiments\\\": {},\\n        }\\n        per_experiment_ratings: dict[str, Any] = (ratings.get(\\\"ratings\\\") or {})\\n        for exp_name, run_data in agent_results.items():\\n            entry: dict[str, Any] = {\\\"error\\\": run_data[\\\"error\\\"]}\\n            if run_data[\\\"metrics\\\"] is not None:\\n                entry[\\\"stats\\\"] = _extract_summary_stats(run_data[\\\"metrics\\\"])\\n            if exp_name in per_experiment_ratings:\\n                entry[\\\"rating\\\"] = per_experiment_ratings[exp_name]\\n            task_summary[\\\"experiments\\\"][exp_name] = entry\\n\\n        all_task_summaries.append(task_summary)\\n\\n        task_summary_path = os.path.join(task_dir, \\\"summary.json\\\")\\n        with open(task_summary_path, \\\"w\\\", encoding=\\\"utf-8\\\") as f:\\n            json.dump(task_summary, f, indent=2, default=str)\\n        print(f\\\"  task summary saved -> {task_summary_path}\\\")\\n\\n        # --- Print per-task results table ---\\n        difficulty_label = f\\\" [{task_meta['difficulty']}]\\\" if task_meta else \\\"\\\"\\n        print(f\\\"\\\\n--- Results for task {task_idx}{difficulty_label}: {task} ---\\\")\\n        if task_meta:\\n            print(\\n                f\\\"  Expected notebooks ({task_meta['min_notebooks_expected']} min): \\\"\\n                + \\\", \\\".join(task_meta[\\\"expected_notebooks\\\"])\\n            )\\n        print(\\n            f\\\"\\\\n{'Experiment':<35} {'Tokens':>12} {'FnCalls':>10} \\\"\\n            f\\\"{'Turns':>8} {'Score':>8} {'Coverage':>10}  Rationale\\\"\\n        )\\n        print(\\\"-\\\" * 115)\\n        for exp_name, exp_data in task_summary[\\\"experiments\\\"].items():\\n            error = exp_data.get(\\\"error\\\")\\n            if error:\\n                print(f\\\"{exp_name:<35} {'ERROR':>12}  {error[:60]}\\\")\\n                continue\\n            stats = exp_data.get(\\\"stats\\\", {})\\n            rating = exp_data.get(\\\"rating\\\", {})\\n            score = rating.get(\\\"score\\\", \\\"-\\\") if isinstance(rating, dict) else \\\"-\\\"\\n            coverage = rating.get(\\\"notebook_coverage\\\", \\\"-\\\") if isinstance(rating, dict) else \\\"-\\\"\\n            rationale = rating.get(\\\"rationale\\\", \\\"\\\") if isinstance(rating, dict) else \\\"\\\"\\n            print(\\n                f\\\"{exp_name:<35} \\\"\\n                f\\\"{str(stats.get('total_tokens', '-')):>12} \\\"\\n                f\\\"{str(stats.get('num_api_function_calls', '-')):>10} \\\"\\n                f\\\"{str(stats.get('num_turns', '-')):>8} \\\"\\n                f\\\"{str(score):>8} \\\"\\n                f\\\"{str(coverage):>10}  {rationale[:55]}\\\"\\n            )\\n        overall = ratings.get(\\\"overall_comment\\\", \\\"\\\")\\n        if overall:\\n            print(f\\\"\\\\nOverall: {overall}\\\")\\n        print()\\n\\n    # --- Aggregate stats across all tasks, grouped by function experiment ---\\n    by_experiment: dict[str, dict[str, Any]] = {}\\n    for exp_name in function_experiments:\\n        token_totals, api_fn_call_totals, turn_totals, scores = [], [], [], []\\n        for ts in all_task_summaries:\\n            exp_data = ts[\\\"experiments\\\"].get(exp_name, {})\\n            stats = exp_data.get(\\\"stats\\\")\\n            if stats:\\n                token_totals.append(stats[\\\"total_tokens\\\"])\\n                api_fn_call_totals.append(stats[\\\"num_api_function_calls\\\"])\\n                turn_totals.append(stats[\\\"num_turns\\\"])\\n            rating = exp_data.get(\\\"rating\\\")\\n            if isinstance(rating, dict) and isinstance(rating.get(\\\"score\\\"), (int, float)):\\n                scores.append(rating[\\\"score\\\"])\\n\\n        by_experiment[exp_name] = {\\n            \\\"num_tasks_completed\\\": len(token_totals),\\n            \\\"avg_total_tokens\\\": _safe_avg(token_totals),\\n            \\\"avg_num_api_function_calls\\\": _safe_avg(api_fn_call_totals),\\n            \\\"avg_num_turns\\\": _safe_avg(turn_totals),\\n            \\\"avg_rating\\\": _safe_avg(scores),\\n        }\\n\\n    global_summary: dict[str, Any] = {\\n        \\\"run_id\\\": run_id,\\n        \\\"agent_model\\\": agent_model,\\n        \\\"evaluator_model\\\": evaluator_model,\\n        \\\"evaluator_reasoning\\\": evaluator_reasoning,\\n        \\\"vault_name\\\": vault_name,\\n        \\\"num_tasks\\\": len(tasks),\\n        \\\"by_experiment\\\": by_experiment,\\n        \\\"per_task\\\": all_task_summaries,\\n    }\\n\\n    global_summary_path = os.path.join(run_dir, \\\"global_summary.json\\\")\\n    with open(global_summary_path, \\\"w\\\", encoding=\\\"utf-8\\\") as f:\\n        json.dump(global_summary, f, indent=2, default=str)\\n    print(f\\\"\\\\n=== Global summary saved -> {global_summary_path} ===\\\")\\n\\n    # --- Print aggregate table ---\\n    print(\\n        f\\\"\\\\n{'Experiment':<35} {'AvgTokens':>12} {'AvgFnCalls':>12} \\\"\\n        f\\\"{'AvgTurns':>10} {'AvgScore':>10}\\\"\\n    )\\n    print(\\\"-\\\" * 82)\\n    for exp_name, agg in by_experiment.items():\\n        print(\\n            f\\\"{exp_name:<35} \\\"\\n            f\\\"{str(agg['avg_total_tokens']):>12} \\\"\\n            f\\\"{str(agg['avg_num_api_function_calls']):>12} \\\"\\n            f\\\"{str(agg['avg_num_turns']):>10} \\\"\\n            f\\\"{str(agg['avg_rating']):>10}\\\"\\n        )\\n    print()\\n\\n\\n# ---------------------------------------------------------------------------\\n# Entry point\\n# ---------------------------------------------------------------------------\\n\\nif __name__ == \\\"__main__\\\":\\n    run_experiments()\\n\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c173f5081958d47d41124512da6`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_search",
    "call_id": "call_WGQ8UhIGMWTcDxtDI7gnNj2r",
    "arguments": {
      "code": "direct_nli_entailment_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `code_search` | **call_id:** `call_WGQ8UhIGMWTcDxtDI7gnNj2r`

**Arguments:**
```json
{
  "code": "direct_nli_entailment_mrpc"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "gent_1775914190",
    "gent_1775874933",
    "gent_1775874373",
    "gent_1775874650",
    "gent_1775914000",
    "gent_1775913615"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 8692 | 129 | 102 | 7122 | 2.909s | 0.038s |

---

## Turn 3 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c1a2d7c8195b6ed1dc8e34945d6`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_WGQ8UhIGMWTcDxtDI7gnNj2r",
    "output": "{\"ok\": true, \"result\": [\"gent_1775914190\", \"gent_1775874933\", \"gent_1775874373\", \"gent_1775874650\", \"gent_1775914000\", \"gent_1775913615\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c1a2d7c8195b6ed1dc8e34945d6`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "get_code",
    "call_id": "call_WLaQfT1FUnKCkYpznPAuIRWF",
    "arguments": {
      "name": "gent_1775874933"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_WLaQfT1FUnKCkYpznPAuIRWF`

**Arguments:**
```json
{
  "name": "gent_1775874933"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "\"\"\"\nnotebook_experiments.py\n\nRuns AgenticWorkflow (eval_agent) over each function experiment set in FUNCTION_EXPERIMENTS\nfor a list of tasks. After all agents complete for a task, a separate OpenAI evaluator\ninstance rates each result 1\u20135, seeing all agent results together for comparison.\n\nFull traces are saved in a structured folder hierarchy. A summary JSON capturing tokens\nused, API function calls made, and turns taken is saved per task and per function subset.\n\nFolder layout:\n    <output_root>/\n      <run_id>/\n        <task_label>/\n          <experiment_name>/\n            trace.json\n            trace.md\n          ratings.json\n          summary.json\n        global_summary.json\n\"\"\"\n\nimport json\nimport os\nimport re\nimport sys\nfrom datetime import datetime, timezone\nfrom typing import Any\n\nfrom openai import OpenAI\n\n# Ensure the evaluation_agents package is importable when run from the repo root.\nsys.path.insert(0, os.path.dirname(__file__))\n\nfrom eval_agent_functions import AgenticWorkflow, SYSTEM_PROMPT\nfrom api_functions import FUNCTION_EXPERIMENTS, initialization\n\n# ---------------------------------------------------------------------------\n# Task list with ground-truth metadata for evaluation\n# ---------------------------------------------------------------------------\n\nTASK_SPECS: list[dict] = [\n    {\n        # Easy: all relevant notebooks share 'distilbert_feature_extraction' or a\n        # pooling keyword in their names \u2014 discoverable by name enumeration alone.\n        \"task\": (\n            \"How does the pooling strategy used to extract sentence representations \"\n            \"from DistilBERT affect paraphrase detection accuracy on MRPC?\"\n        ),\n        \"difficulty\": \"easy\",\n        \"expected_notebooks\": [\n            \"distilbert_feature_extraction_cosine_mrpc\",\n            \"distilbert_cls_cosine_mrpc\",\n            \"distilbert_max_pool_cosine_mrpc\",\n            \"distilbert_no_special_tokens_mean_cosine_mrpc\",\n            \"distilbert_last4_mean_cosine_mrpc\",\n            \"distilbert_mean_cosine_median_threshold_mrpc\",\n        ],\n        \"min_notebooks_expected\": 5,\n        \"discovery_hint\": (\n            \"All relevant notebooks share 'distilbert' and a pooling-related keyword \"\n            \"(cls, max_pool, mean, last4, no_special_tokens) in their names. \"\n            \"A simple name enumeration is sufficient to find them.\"\n        ),\n        \"key_finding\": (\n            \"Last-layer mean pooling (with or without special tokens) marginally \"\n            \"outperforms CLS-token and max-pool extraction, but differences are small \"\n            \"(accuracy ~0.696\u20130.703 vs ~0.684\u20130.686 at threshold=0.85). Averaging the \"\n            \"last four hidden layers before mean-pooling does not improve over \"\n            \"single-layer mean pooling and performs on par with CLS and max-pool. \"\n            \"Note: distilbert_mean_cosine_median_threshold_mrpc uses a data-driven \"\n            \"median threshold rather than 0.85 and shows substantially lower performance \"\n            \"(accuracy ~0.65, F1 ~0.70) \u2014 this reflects threshold sensitivity, not \"\n            \"pooling quality, and should not be interpreted as a pooling result. \"\n            \"The agent should report accuracy and F1 per pooling variant at a fixed \"\n            \"threshold and note that the overall spread across strategies is narrow.\"\n        ),\n    },\n    {\n        # Medium: notebooks span three families (bi-encoder, distilbert feature\n        # extraction, HF pipeline, cross-encoder). Code search for 'threshold' or\n        # description search are needed; name enumeration alone misses cross-family scope.\n        \"task\": (\n            \"How sensitive are similarity-based paraphrase classifiers to the choice \"\n            \"of decision threshold, and does this vary across model families?\"\n        ),\n        \"difficulty\": \"medium\",\n        \"expected_notebooks\": [\n            \"sentence_transformers_bi_encoder_cosine_mrpc\",\n            \"st_paraphrase_minilm_l6_cosine_threshold_mrpc\",\n            \"st_paraphrase_minilm_l3_cosine_threshold_mrpc\",\n            \"st_all_minilm_l6_l2_distance_threshold_mrpc\",\n            \"st_all_distilroberta_v1_cosine_threshold_mrpc\",\n            \"distilbert_mean_cosine_median_threshold_mrpc\",\n            \"hf_pipeline_mrpc_threshold_070\",\n            \"quora_cross_encoder_softmax_threshold_065_mrpc\",\n            \"paraphrase_score_threshold_zero_shot_mrpc\",\n        ],\n        \"min_notebooks_expected\": 6,\n        \"discovery_hint\": (\n            \"Relevant notebooks span three families (sentence-transformers bi-encoder, \"\n            \"distilbert feature extraction, HF pipeline, cross-encoder). \"\n            \"Code search for 'threshold' or description/property search are the most \"\n            \"direct routes; name enumeration alone is insufficient without cross-family \"\n            \"awareness.\"\n        ),\n        \"key_finding\": (\n            \"Threshold choice significantly shifts the precision/recall trade-off. \"\n            \"The fine-tuned HF pipeline at threshold=0.70 (acc ~0.848, F1 ~0.890) \"\n            \"stays close to its argmax baseline, while bi-encoder cosine models \"\n            \"(paraphrase-MiniLM-L6 at 0.78: acc ~0.701, F1 ~0.771; all-distilroberta-v1 \"\n            \"at 0.72: acc ~0.723, F1 ~0.806) and the cross-encoder (quora-distilroberta \"\n            \"at 0.65: acc ~0.679, F1 ~0.758) degrade more sharply at non-optimal \"\n            \"thresholds. Zero-shot NLI models are especially sensitive: applying a \"\n            \"threshold of 0.55 (paraphrase_score_threshold_zero_shot_mrpc) yields \"\n            \"acc ~0.578, F1 ~0.674. The agent should identify notebooks from multiple \"\n            \"families that vary the threshold, report how accuracy and F1 change, and \"\n            \"note that the optimal threshold and sensitivity to its choice differ \"\n            \"substantially by model family and similarity metric.\"\n        ),\n    },\n    {\n        # Hard: notebooks are spread across four model families with no shared name\n        # pattern. Must be found via code search for bidirectional processing patterns\n        # (enc_12/enc_21, margin_12/margin_21) or via description/property search.\n        \"task\": (\n            \"How do different strategies for enforcing prediction symmetry affect \"\n            \"accuracy when using NLI-based and zero-shot models for paraphrase \"\n            \"detection on MRPC?\"\n        ),\n        \"difficulty\": \"hard\",\n        \"expected_notebooks\": [\n            \"direct_nli_entailment_mrpc\",\n            \"min_direction_margin_mrpc\",\n            \"consensus_then_avg_margin_mrpc\",\n            \"neutral_penalized_margin_mrpc\",\n            \"softmax_gap_mean_mrpc\",\n            \"bidirectional_averaged_zero_shot_mrpc\",\n            \"hf_pipeline_mrpc_bidirectional_order_average\",\n            \"quora_cross_encoder_symmetric_average_mrpc\",\n            \"flan_t5_symmetric_prompt_average_mrpc\",\n        ],\n        \"min_notebooks_expected\": 6,\n        \"discovery_hint\": (\n            \"Relevant notebooks span four families (direct NLI entailment, zero-shot \"\n            \"NLI pipeline, HF sequence classification pipeline, cross-encoder). \"\n            \"No name pattern unifies them \u2014 they must be found by searching code for \"\n            \"bidirectional processing (enc_12/enc_21, margin_12/margin_21) or via \"\n            \"description/property search for symmetry-related concepts.\"\n        ),\n        \"key_finding\": (\n            \"The effect of bidirectional symmetry enforcement is highly model-family \"\n            \"dependent and does not uniformly improve accuracy. For zero-shot NLI \"\n            \"pipelines, bidirectional averaging slightly hurts performance relative to \"\n            \"single-direction scoring (acc ~0.613 vs ~0.630). For the fine-tuned HF \"\n            \"pipeline, the effect is negligible (acc ~0.850 vs ~0.858). Only for the \"\n            \"cross-encoder does bidirectional averaging provide a modest gain \"\n            \"(acc ~0.699 vs ~0.679). Among aggregation strategies, average-margin \"\n            \"outperforms min-direction by a large margin (acc ~0.703 vs ~0.586 for \"\n            \"direct NLI); min-direction is overly conservative and collapses recall. \"\n            \"The agent should compare aggregation strategies within each family and \"\n            \"note that improvements from bidirectionality are more pronounced for \"\n            \"cross-encoders than for NLI or zero-shot models. Flan-T5 \"\n            \"(flan_t5_symmetric_prompt_average_mrpc) uses a generative symmetry strategy \"\n            \"(averaging yes/no logits for both prompt orderings) and achieves acc ~0.738, \"\n            \"F1 ~0.807, representing a distinct symmetry approach outside the NLI/pipeline \"\n            \"families.\"\n        ),\n    },\n]\n\nTASKS: list[str] = [spec[\"task\"] for spec in TASK_SPECS]\n\n# ---------------------------------------------------------------------------\n# Configuration\n# ---------------------------------------------------------------------------\n\nVAULT_NAME = \"tv_experiment_1\"\nAGENT_MODEL = \"gpt-5.4\"\nEVALUATOR_MODEL = \"gpt-5.4\"\nDEFAULT_EVALUATOR_REASONING: dict = {\"effort\": \"high\"}\nMAX_TURNS = 30\nOUTPUT_ROOT = \"experiment_results\"\n\nOPENAI_KEY_FILE = \"/Users/jinjinzhao/Documents/work_projects/my_keys/my_keys/openai_jinjin.key\"\n\n# ---------------------------------------------------------------------------\n# Evaluator\n# ---------------------------------------------------------------------------\n\nEVALUATOR_SYSTEM_PROMPT = \"\"\"\\\nYou are an expert evaluator assessing the quality of AI-generated data analysis responses.\n\nYou will receive a user task and the results produced by several agents. Each agent used a\ndifferent set of API functions to answer the same question against the same data repository.\n\nWhen ground-truth metadata is provided (expected notebooks, minimum coverage, key finding),\nuse it to assess each agent result on three dimensions:\n\n  1. Notebook coverage \u2014 what fraction of the expected notebooks did the agent cite or\n     retrieve? An agent that finds fewer than the minimum required notebooks should not\n     score above 3, regardless of the quality of its summary.\n\n  2. Factual correctness \u2014 does the agent's reported finding match the expected key finding?\n     Penalise results that draw the opposite conclusion or miss the central pattern.\n\n  3. Analytical depth \u2014 does the summary interpret the evidence (not just list numbers),\n     note cross-family differences, and flag limitations or confounds?\n\nScoring guide (apply all three dimensions; coverage and correctness carry the most weight):\n  5 \u2014 Meets minimum notebook coverage, correct key finding, insightful analysis\n  4 \u2014 Near-minimum coverage or minor factual gap, otherwise complete and correct\n  3 \u2014 Below minimum coverage OR incorrect/missing key finding, but some valid evidence\n  2 \u2014 Severely under-covered (1\u20132 notebooks only) or substantially incorrect conclusion\n  1 \u2014 Does not address the task, errors dominate, or no relevant notebooks retrieved\n\nWhen no ground-truth metadata is provided, fall back to general completeness and accuracy.\n\nReturn a JSON object with exactly this shape (no markdown fences):\n{\n  \"ratings\": {\n    \"<function_experiment_name>\": {\n      \"score\": <int 1\u20135>,\n      \"notebook_coverage\": \"<N of M expected notebooks cited>\",\n      \"rationale\": \"<brief explanation referencing coverage, correctness, depth>\"\n    }\n  },\n  \"overall_comment\": \"<cross-agent comparison and key observations>\"\n}\n\"\"\"\n\n\ndef evaluate_results(\n    client: OpenAI,\n    task: str,\n    agent_results: dict[str, dict[str, Any]],\n    task_metadata: dict | None = None,\n    model: str = EVALUATOR_MODEL,\n    reasoning: dict | None = None,\n) -> dict[str, Any]:\n    \"\"\"Rate each agent result 1\u20135 using a single evaluator that sees all results.\n\n    Args:\n        client: OpenAI client.\n        task: The original task string.\n        agent_results: {experiment_name: {\"result\": {...}, \"metrics\": RunMetrics, \"error\": str|None}}\n        task_metadata: Optional ground-truth dict from TASK_SPECS (expected_notebooks,\n                       min_notebooks_expected, key_finding, difficulty, discovery_hint).\n        model: Evaluator model name.\n        reasoning: Optional reasoning parameter dict, e.g. {\"effort\": \"high\"}.\n\n    Returns:\n        Parsed ratings dict from the evaluator, or a fallback dict on parse failure.\n    \"\"\"\n    result_blocks: list[str] = []\n    for exp_name, run_data in agent_results.items():\n        error = run_data.get(\"error\")\n        if error:\n            result_blocks.append(f\"### Agent: {exp_name}\\n**ERROR:** {error}\\n\")\n        else:\n            result = run_data.get(\"result\") or {}\n            rows = result.get(\"rows\", [])\n            summary = result.get(\"summary\", \"(no summary)\")\n            result_blocks.append(\n                f\"### Agent: {exp_name}\\n\"\n                f\"**Summary:** {summary}\\n\\n\"\n                f\"**Result rows ({len(rows)} rows):**\\n\"\n                f\"```json\\n{json.dumps(rows[:20], indent=2, default=str)}\\n```\\n\"\n            )\n\n    ground_truth_block = \"\"\n    if task_metadata:\n        expected = task_metadata.get(\"expected_notebooks\", [])\n        min_nb = task_metadata.get(\"min_notebooks_expected\", \"?\")\n        key_finding = task_metadata.get(\"key_finding\", \"\")\n        difficulty = task_metadata.get(\"difficulty\", \"\")\n        ground_truth_block = (\n            f\"## Ground-Truth Reference\\n\\n\"\n            f\"**Task difficulty:** {difficulty}\\n\\n\"\n            f\"**Expected notebooks ({len(expected)} total, minimum {min_nb} required):**\\n\"\n            + \"\\n\".join(f\"  - {nb}\" for nb in expected)\n            + f\"\\n\\n**Key finding the agent should identify:**\\n{key_finding}\\n\\n\"\n            \"Use the expected notebook list to assess coverage: count how many of these \"\n            \"names (or close variants) appear in the agent's result rows or summary. \"\n            \"An agent that cites fewer than the minimum required should not score above 3.\\n\\n\"\n        )\n\n    user_content = (\n        f\"## Task\\n{task}\\n\\n\"\n        + ground_truth_block\n        + \"## Agent Results\\n\\n\"\n        + \"\\n---\\n\".join(result_blocks)\n    )\n\n    create_kwargs: dict[str, Any] = dict(\n        model=model,\n        instructions=EVALUATOR_SYSTEM_PROMPT,\n        input=[{\"role\": \"user\", \"content\": user_content}],\n    )\n    if reasoning is not None:\n        create_kwargs[\"reasoning\"] = reasoning\n\n    response = client.responses.create(**create_kwargs)\n\n    raw_text_parts: list[str] = []\n    for item in response.output or []:\n        if getattr(item, \"type\", None) in (\"text\", \"message\"):\n            part = getattr(item, \"text\", None) or getattr(item, \"content\", None) or \"\"\n            if isinstance(part, list):\n                for block in part:\n                    text = getattr(block, \"text\", None) or \"\"\n                    if isinstance(text, str) and text:\n                        raw_text_parts.append(text)\n            elif isinstance(part, str) and part:\n                raw_text_parts.append(part)\n    raw_text = \"\".join(raw_text_parts)\n\n    try:\n        text = raw_text.strip()\n        # Strip markdown code fences if the model wrapped the JSON.\n        if text.startswith(\"```\"):\n            text = re.sub(r\"^```[^\\n]*\\n\", \"\", text)\n            text = re.sub(r\"\\n?```$\", \"\", text).strip()\n        return json.loads(text)\n    except json.JSONDecodeError:\n        return {\n            \"parse_error\": \"Could not parse JSON from evaluator response\",\n            \"raw_response\": raw_text,\n        }\n\n\n# ---------------------------------------------------------------------------\n# Summary helpers\n# ---------------------------------------------------------------------------\n\ndef _extract_summary_stats(metrics: Any) -> dict[str, Any]:\n    \"\"\"Pull the key statistics we care about from a RunMetrics object.\"\"\"\n    s = metrics.summary()\n    return {\n        \"total_tokens\": s[\"tokens\"][\"total\"],\n        \"input_tokens\": s[\"tokens\"][\"input\"],\n        \"output_tokens\": s[\"tokens\"][\"output\"],\n        \"reasoning_tokens\": s[\"tokens\"][\"reasoning\"],\n        # num_turns == total OpenAI API calls == number of turns in the loop\n        \"num_turns\": s[\"api_calls\"],\n        # num_api_function_calls == tool calls that are not finalize_result or no-tool turns\n        \"num_api_function_calls\": sum(\n            1 for t in metrics.turns\n            if t.tool_name is not None and t.tool_name != \"finalize_result\"\n        ),\n        \"wall_time_s\": s[\"timing\"][\"wall_time_s\"],\n    }\n\n\ndef _safe_avg(values: list[float | int]) -> float | None:\n    return round(sum(values) / len(values), 2) if values else None\n\n\ndef _slugify(text: str, max_len: int = 40) -> str:\n    slug = re.sub(r\"[^a-zA-Z0-9]+\", \"_\", text).strip(\"_\").lower()\n    return slug[:max_len]\n\n\n# ---------------------------------------------------------------------------\n# Main experiment loop\n# ---------------------------------------------------------------------------\n\ndef run_experiments(\n    tasks: list[str] = TASKS,\n    task_specs: list[dict] | None = TASK_SPECS,\n    vault_name: str = VAULT_NAME,\n    agent_model: str = AGENT_MODEL,\n    evaluator_model: str = EVALUATOR_MODEL,\n    evaluator_reasoning: dict | None = DEFAULT_EVALUATOR_REASONING,\n    max_turns: int = MAX_TURNS,\n    output_root: str = OUTPUT_ROOT,\n    function_experiments: dict[str, list[str]] | None = None,\n) -> None:\n    \"\"\"Run all experiments and save results.\n\n    Args:\n        tasks: List of task strings to evaluate.\n        task_specs: Optional list of TASK_SPECS dicts providing ground-truth metadata\n                    (expected_notebooks, key_finding, difficulty) for the evaluator.\n                    Must align 1-to-1 with tasks if provided.\n        vault_name: TableVault database name passed to initialization().\n        agent_model: Model used by the agentic workflow.\n        evaluator_model: Model used by the evaluator.\n        evaluator_reasoning: Reasoning dict for the evaluator (e.g. {\"effort\": \"high\"}).\n                             Pass None to disable reasoning.\n        max_turns: Maximum turns per agent run.\n        output_root: Root directory for all output files.\n        function_experiments: Override FUNCTION_EXPERIMENTS; defaults to the full set.\n    \"\"\"\n    if function_experiments is None:\n        function_experiments = FUNCTION_EXPERIMENTS\n\n    with open(OPENAI_KEY_FILE, \"r\") as f:\n        os.environ[\"OPENAI_API_KEY\"] = f.read().strip()\n    client = OpenAI()\n\n    vault = initialization(vault_name)\n\n    run_id = datetime.now(timezone.utc).strftime(\"%Y%m%dT%H%M%SZ\")\n    run_dir = os.path.join(output_root, run_id)\n    os.makedirs(run_dir, exist_ok=True)\n\n    print(\n        f\"\\n=== Experiment run {run_id} | {len(tasks)} task(s) | \"\n        f\"{len(function_experiments)} function set(s) ===\"\n    )\n    print(f\"Output directory: {run_dir}\\n\")\n\n    all_task_summaries: list[dict[str, Any]] = []\n\n    for task_idx, task in enumerate(tasks):\n        task_meta = task_specs[task_idx] if task_specs and task_idx < len(task_specs) else None\n        task_slug = _slugify(task)\n        task_label = f\"task_{task_idx:03d}_{task_slug}\"\n        task_dir = os.path.join(run_dir, task_label)\n        os.makedirs(task_dir, exist_ok=True)\n\n        print(f\"\\n{'='*70}\")\n        print(f\"TASK {task_idx}: {task}\")\n        print(f\"{'='*70}\\n\")\n\n        agent_results: dict[str, dict[str, Any]] = {}\n\n        # --- Run each function experiment in sequence ---\n        for exp_name, fn_list in function_experiments.items():\n            print(f\"\\n--- [{exp_name}] functions: {fn_list} ---\")\n            exp_dir = os.path.join(task_dir, exp_name)\n            os.makedirs(exp_dir, exist_ok=True)\n\n            try:\n                wf = AgenticWorkflow(\n                    client=client,\n                    model=agent_model,\n                    system_prompt=SYSTEM_PROMPT,\n                    vault=vault,\n                    workflow_key=exp_name,\n                    max_turns=max_turns,\n                    trace_output_dir=exp_dir,\n                    trace_filename_stem=\"trace\",\n                    reasoning={\"effort\": \"high\"},\n                )\n                output = wf.run(task)\n                agent_results[exp_name] = {\n                    \"result\": output[\"result\"],\n                    \"metrics\": output[\"metrics\"],\n                    \"error\": None,\n                }\n            except Exception as exc:\n                print(f\"  [ERROR] experiment '{exp_name}' failed: {exc}\")\n                agent_results[exp_name] = {\n                    \"result\": None,\n                    \"metrics\": None,\n                    \"error\": str(exc),\n                }\n\n        # --- Evaluate all results for this task with a single evaluator call ---\n        print(f\"\\n--- Evaluating {len(agent_results)} agent result(s) ---\")\n        ratings = evaluate_results(\n            client=client,\n            task=task,\n            agent_results=agent_results,\n            task_metadata=task_meta,\n            model=evaluator_model,\n            reasoning=evaluator_reasoning,\n        )\n\n        ratings_path = os.path.join(task_dir, \"ratings.json\")\n        with open(ratings_path, \"w\", encoding=\"utf-8\") as f:\n            json.dump({\"task\": task, \"ratings\": ratings}, f, indent=2, default=str)\n        print(f\"  ratings saved -> {ratings_path}\")\n\n        # --- Build per-task summary (stats + rating for each experiment) ---\n        task_summary: dict[str, Any] = {\n            \"task_idx\": task_idx,\n            \"task\": task,\n            \"difficulty\": task_meta.get(\"difficulty\") if task_meta else None,\n            \"expected_notebooks\": task_meta.get(\"expected_notebooks\") if task_meta else None,\n            \"min_notebooks_expected\": task_meta.get(\"min_notebooks_expected\") if task_meta else None,\n            \"key_finding\": task_meta.get(\"key_finding\") if task_meta else None,\n            \"experiments\": {},\n        }\n        per_experiment_ratings: dict[str, Any] = (ratings.get(\"ratings\") or {})\n        for exp_name, run_data in agent_results.items():\n            entry: dict[str, Any] = {\"error\": run_data[\"error\"]}\n            if run_data[\"metrics\"] is not None:\n                entry[\"stats\"] = _extract_summary_stats(run_data[\"metrics\"])\n            if exp_name in per_experiment_ratings:\n                entry[\"rating\"] = per_experiment_ratings[exp_name]\n            task_summary[\"experiments\"][exp_name] = entry\n\n        all_task_summaries.append(task_summary)\n\n        task_summary_path = os.path.join(task_dir, \"summary.json\")\n        with open(task_summary_path, \"w\", encoding=\"utf-8\") as f:\n            json.dump(task_summary, f, indent=2, default=str)\n        print(f\"  task summary saved -> {task_summary_path}\")\n\n        # --- Print per-task results table ---\n        difficulty_label = f\" [{task_meta['difficulty']}]\" if task_meta else \"\"\n        print(f\"\\n--- Results for task {task_idx}{difficulty_label}: {task} ---\")\n        if task_meta:\n            print(\n                f\"  Expected notebooks ({task_meta['min_notebooks_expected']} min): \"\n                + \", \".join(task_meta[\"expected_notebooks\"])\n            )\n        print(\n            f\"\\n{'Experiment':<35} {'Tokens':>12} {'FnCalls':>10} \"\n            f\"{'Turns':>8} {'Score':>8} {'Coverage':>10}  Rationale\"\n        )\n        print(\"-\" * 115)\n        for exp_name, exp_data in task_summary[\"experiments\"].items():\n            error = exp_data.get(\"error\")\n            if error:\n                print(f\"{exp_name:<35} {'ERROR':>12}  {error[:60]}\")\n                continue\n            stats = exp_data.get(\"stats\", {})\n            rating = exp_data.get(\"rating\", {})\n            score = rating.get(\"score\", \"-\") if isinstance(rating, dict) else \"-\"\n            coverage = rating.get(\"notebook_coverage\", \"-\") if isinstance(rating, dict) else \"-\"\n            rationale = rating.get(\"rationale\", \"\") if isinstance(rating, dict) else \"\"\n            print(\n                f\"{exp_name:<35} \"\n                f\"{str(stats.get('total_tokens', '-')):>12} \"\n                f\"{str(stats.get('num_api_function_calls', '-')):>10} \"\n                f\"{str(stats.get('num_turns', '-')):>8} \"\n                f\"{str(score):>8} \"\n                f\"{str(coverage):>10}  {rationale[:55]}\"\n            )\n        overall = ratings.get(\"overall_comment\", \"\")\n        if overall:\n            print(f\"\\nOverall: {overall}\")\n        print()\n\n    # --- Aggregate stats across all tasks, grouped by function experiment ---\n    by_experiment: dict[str, dict[str, Any]] = {}\n    for exp_name in function_experiments:\n        token_totals, api_fn_call_totals, turn_totals, scores = [], [], [], []\n        for ts in all_task_summaries:\n            exp_data = ts[\"experiments\"].get(exp_name, {})\n            stats = exp_data.get(\"stats\")\n            if stats:\n                token_totals.append(stats[\"total_tokens\"])\n                api_fn_call_totals.append(stats[\"num_api_function_calls\"])\n                turn_totals.append(stats[\"num_turns\"])\n            rating = exp_data.get(\"rating\")\n            if isinstance(rating, dict) and isinstance(rating.get(\"score\"), (int, float)):\n                scores.append(rating[\"score\"])\n\n        by_experiment[exp_name] = {\n            \"num_tasks_completed\": len(token_totals),\n            \"avg_total_tokens\": _safe_avg(token_totals),\n            \"avg_num_api_function_calls\": _safe_avg(api_fn_call_totals),\n            \"avg_num_turns\": _safe_avg(turn_totals),\n            \"avg_rating\": _safe_avg(scores),\n        }\n\n    global_summary: dict[str, Any] = {\n        \"run_id\": run_id,\n        \"agent_model\": agent_model,\n        \"evaluator_model\": evaluator_model,\n        \"evaluator_reasoning\": evaluator_reasoning,\n        \"vault_name\": vault_name,\n        \"num_tasks\": len(tasks),\n        \"by_experiment\": by_experiment,\n        \"per_task\": all_task_summaries,\n    }\n\n    global_summary_path = os.path.join(run_dir, \"global_summary.json\")\n    with open(global_summary_path, \"w\", encoding=\"utf-8\") as f:\n        json.dump(global_summary, f, indent=2, default=str)\n    print(f\"\\n=== Global summary saved -> {global_summary_path} ===\")\n\n    # --- Print aggregate table ---\n    print(\n        f\"\\n{'Experiment':<35} {'AvgTokens':>12} {'AvgFnCalls':>12} \"\n        f\"{'AvgTurns':>10} {'AvgScore':>10}\"\n    )\n    print(\"-\" * 82)\n    for exp_name, agg in by_experiment.items():\n        print(\n            f\"{exp_name:<35} \"\n            f\"{str(agg['avg_total_tokens']):>12} \"\n            f\"{str(agg['avg_num_api_function_calls']):>12} \"\n            f\"{str(agg['avg_num_turns']):>10} \"\n            f\"{str(agg['avg_rating']):>10}\"\n        )\n    print()\n\n\n# ---------------------------------------------------------------------------\n# Entry point\n# ---------------------------------------------------------------------------\n\nif __name__ == \"__main__\":\n    run_experiments()\n"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 8889 | 100 | 75 | 7319 | 2.490s | 0.008s |

---

## Turn 4 — `code_search` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c1cb02c8195b0126c3baf31a4f8`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_WLaQfT1FUnKCkYpznPAuIRWF",
    "output": "{\"ok\": true, \"result\": [\"\\\"\\\"\\\"\\nnotebook_experiments.py\\n\\nRuns AgenticWorkflow (eval_agent) over each function experiment set in FUNCTION_EXPERIMENTS\\nfor a list of tasks. After all agents complete for a task, a separate OpenAI evaluator\\ninstance rates each result 1\\u20135, seeing all agent results together for comparison.\\n\\nFull traces are saved in a structured folder hierarchy. A summary JSON capturing tokens\\nused, API function calls made, and turns taken is saved per task and per function subset.\\n\\nFolder layout:\\n    <output_root>/\\n      <run_id>/\\n        <task_label>/\\n          <experiment_name>/\\n            trace.json\\n            trace.md\\n          ratings.json\\n          summary.json\\n        global_summary.json\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\nimport re\\nimport sys\\nfrom datetime import datetime, timezone\\nfrom typing import Any\\n\\nfrom openai import OpenAI\\n\\n# Ensure the evaluation_agents package is importable when run from the repo root.\\nsys.path.insert(0, os.path.dirname(__file__))\\n\\nfrom eval_agent_functions import AgenticWorkflow, SYSTEM_PROMPT\\nfrom api_functions import FUNCTION_EXPERIMENTS, initialization\\n\\n# ---------------------------------------------------------------------------\\n# Task list with ground-truth metadata for evaluation\\n# ---------------------------------------------------------------------------\\n\\nTASK_SPECS: list[dict] = [\\n    {\\n        # Easy: all relevant notebooks share 'distilbert_feature_extraction' or a\\n        # pooling keyword in their names \\u2014 discoverable by name enumeration alone.\\n        \\\"task\\\": (\\n            \\\"How does the pooling strategy used to extract sentence representations \\\"\\n            \\\"from DistilBERT affect paraphrase detection accuracy on MRPC?\\\"\\n        ),\\n        \\\"difficulty\\\": \\\"easy\\\",\\n        \\\"expected_notebooks\\\": [\\n            \\\"distilbert_feature_extraction_cosine_mrpc\\\",\\n            \\\"distilbert_cls_cosine_mrpc\\\",\\n            \\\"distilbert_max_pool_cosine_mrpc\\\",\\n            \\\"distilbert_no_special_tokens_mean_cosine_mrpc\\\",\\n            \\\"distilbert_last4_mean_cosine_mrpc\\\",\\n            \\\"distilbert_mean_cosine_median_threshold_mrpc\\\",\\n        ],\\n        \\\"min_notebooks_expected\\\": 5,\\n        \\\"discovery_hint\\\": (\\n            \\\"All relevant notebooks share 'distilbert' and a pooling-related keyword \\\"\\n            \\\"(cls, max_pool, mean, last4, no_special_tokens) in their names. \\\"\\n            \\\"A simple name enumeration is sufficient to find them.\\\"\\n        ),\\n        \\\"key_finding\\\": (\\n            \\\"Last-layer mean pooling (with or without special tokens) marginally \\\"\\n            \\\"outperforms CLS-token and max-pool extraction, but differences are small \\\"\\n            \\\"(accuracy ~0.696\\u20130.703 vs ~0.684\\u20130.686 at threshold=0.85). Averaging the \\\"\\n            \\\"last four hidden layers before mean-pooling does not improve over \\\"\\n            \\\"single-layer mean pooling and performs on par with CLS and max-pool. \\\"\\n            \\\"Note: distilbert_mean_cosine_median_threshold_mrpc uses a data-driven \\\"\\n            \\\"median threshold rather than 0.85 and shows substantially lower performance \\\"\\n            \\\"(accuracy ~0.65, F1 ~0.70) \\u2014 this reflects threshold sensitivity, not \\\"\\n            \\\"pooling quality, and should not be interpreted as a pooling result. \\\"\\n            \\\"The agent should report accuracy and F1 per pooling variant at a fixed \\\"\\n            \\\"threshold and note that the overall spread across strategies is narrow.\\\"\\n        ),\\n    },\\n    {\\n        # Medium: notebooks span three families (bi-encoder, distilbert feature\\n        # extraction, HF pipeline, cross-encoder). Code search for 'threshold' or\\n        # description search are needed; name enumeration alone misses cross-family scope.\\n        \\\"task\\\": (\\n            \\\"How sensitive are similarity-based paraphrase classifiers to the choice \\\"\\n            \\\"of decision threshold, and does this vary across model families?\\\"\\n        ),\\n        \\\"difficulty\\\": \\\"medium\\\",\\n        \\\"expected_notebooks\\\": [\\n            \\\"sentence_transformers_bi_encoder_cosine_mrpc\\\",\\n            \\\"st_paraphrase_minilm_l6_cosine_threshold_mrpc\\\",\\n            \\\"st_paraphrase_minilm_l3_cosine_threshold_mrpc\\\",\\n            \\\"st_all_minilm_l6_l2_distance_threshold_mrpc\\\",\\n            \\\"st_all_distilroberta_v1_cosine_threshold_mrpc\\\",\\n            \\\"distilbert_mean_cosine_median_threshold_mrpc\\\",\\n            \\\"hf_pipeline_mrpc_threshold_070\\\",\\n            \\\"quora_cross_encoder_softmax_threshold_065_mrpc\\\",\\n            \\\"paraphrase_score_threshold_zero_shot_mrpc\\\",\\n        ],\\n        \\\"min_notebooks_expected\\\": 6,\\n        \\\"discovery_hint\\\": (\\n            \\\"Relevant notebooks span three families (sentence-transformers bi-encoder, \\\"\\n            \\\"distilbert feature extraction, HF pipeline, cross-encoder). \\\"\\n            \\\"Code search for 'threshold' or description/property search are the most \\\"\\n            \\\"direct routes; name enumeration alone is insufficient without cross-family \\\"\\n            \\\"awareness.\\\"\\n        ),\\n        \\\"key_finding\\\": (\\n            \\\"Threshold choice significantly shifts the precision/recall trade-off. \\\"\\n            \\\"The fine-tuned HF pipeline at threshold=0.70 (acc ~0.848, F1 ~0.890) \\\"\\n            \\\"stays close to its argmax baseline, while bi-encoder cosine models \\\"\\n            \\\"(paraphrase-MiniLM-L6 at 0.78: acc ~0.701, F1 ~0.771; all-distilroberta-v1 \\\"\\n            \\\"at 0.72: acc ~0.723, F1 ~0.806) and the cross-encoder (quora-distilroberta \\\"\\n            \\\"at 0.65: acc ~0.679, F1 ~0.758) degrade more sharply at non-optimal \\\"\\n            \\\"thresholds. Zero-shot NLI models are especially sensitive: applying a \\\"\\n            \\\"threshold of 0.55 (paraphrase_score_threshold_zero_shot_mrpc) yields \\\"\\n            \\\"acc ~0.578, F1 ~0.674. The agent should identify notebooks from multiple \\\"\\n            \\\"families that vary the threshold, report how accuracy and F1 change, and \\\"\\n            \\\"note that the optimal threshold and sensitivity to its choice differ \\\"\\n            \\\"substantially by model family and similarity metric.\\\"\\n        ),\\n    },\\n    {\\n        # Hard: notebooks are spread across four model families with no shared name\\n        # pattern. Must be found via code search for bidirectional processing patterns\\n        # (enc_12/enc_21, margin_12/margin_21) or via description/property search.\\n        \\\"task\\\": (\\n            \\\"How do different strategies for enforcing prediction symmetry affect \\\"\\n            \\\"accuracy when using NLI-based and zero-shot models for paraphrase \\\"\\n            \\\"detection on MRPC?\\\"\\n        ),\\n        \\\"difficulty\\\": \\\"hard\\\",\\n        \\\"expected_notebooks\\\": [\\n            \\\"direct_nli_entailment_mrpc\\\",\\n            \\\"min_direction_margin_mrpc\\\",\\n            \\\"consensus_then_avg_margin_mrpc\\\",\\n            \\\"neutral_penalized_margin_mrpc\\\",\\n            \\\"softmax_gap_mean_mrpc\\\",\\n            \\\"bidirectional_averaged_zero_shot_mrpc\\\",\\n            \\\"hf_pipeline_mrpc_bidirectional_order_average\\\",\\n            \\\"quora_cross_encoder_symmetric_average_mrpc\\\",\\n            \\\"flan_t5_symmetric_prompt_average_mrpc\\\",\\n        ],\\n        \\\"min_notebooks_expected\\\": 6,\\n        \\\"discovery_hint\\\": (\\n            \\\"Relevant notebooks span four families (direct NLI entailment, zero-shot \\\"\\n            \\\"NLI pipeline, HF sequence classification pipeline, cross-encoder). \\\"\\n            \\\"No name pattern unifies them \\u2014 they must be found by searching code for \\\"\\n            \\\"bidirectional processing (enc_12/enc_21, margin_12/margin_21) or via \\\"\\n            \\\"description/property search for symmetry-related concepts.\\\"\\n        ),\\n        \\\"key_finding\\\": (\\n            \\\"The effect of bidirectional symmetry enforcement is highly model-family \\\"\\n            \\\"dependent and does not uniformly improve accuracy. For zero-shot NLI \\\"\\n            \\\"pipelines, bidirectional averaging slightly hurts performance relative to \\\"\\n            \\\"single-direction scoring (acc ~0.613 vs ~0.630). For the fine-tuned HF \\\"\\n            \\\"pipeline, the effect is negligible (acc ~0.850 vs ~0.858). Only for the \\\"\\n            \\\"cross-encoder does bidirectional averaging provide a modest gain \\\"\\n            \\\"(acc ~0.699 vs ~0.679). Among aggregation strategies, average-margin \\\"\\n            \\\"outperforms min-direction by a large margin (acc ~0.703 vs ~0.586 for \\\"\\n            \\\"direct NLI); min-direction is overly conservative and collapses recall. \\\"\\n            \\\"The agent should compare aggregation strategies within each family and \\\"\\n            \\\"note that improvements from bidirectionality are more pronounced for \\\"\\n            \\\"cross-encoders than for NLI or zero-shot models. Flan-T5 \\\"\\n            \\\"(flan_t5_symmetric_prompt_average_mrpc) uses a generative symmetry strategy \\\"\\n            \\\"(averaging yes/no logits for both prompt orderings) and achieves acc ~0.738, \\\"\\n            \\\"F1 ~0.807, representing a distinct symmetry approach outside the NLI/pipeline \\\"\\n            \\\"families.\\\"\\n        ),\\n    },\\n]\\n\\nTASKS: list[str] = [spec[\\\"task\\\"] for spec in TASK_SPECS]\\n\\n# ---------------------------------------------------------------------------\\n# Configuration\\n# ---------------------------------------------------------------------------\\n\\nVAULT_NAME = \\\"tv_experiment_1\\\"\\nAGENT_MODEL = \\\"gpt-5.4\\\"\\nEVALUATOR_MODEL = \\\"gpt-5.4\\\"\\nDEFAULT_EVALUATOR_REASONING: dict = {\\\"effort\\\": \\\"high\\\"}\\nMAX_TURNS = 30\\nOUTPUT_ROOT = \\\"experiment_results\\\"\\n\\nOPENAI_KEY_FILE = \\\"/Users/jinjinzhao/Documents/work_projects/my_keys/my_keys/openai_jinjin.key\\\"\\n\\n# ---------------------------------------------------------------------------\\n# Evaluator\\n# ---------------------------------------------------------------------------\\n\\nEVALUATOR_SYSTEM_PROMPT = \\\"\\\"\\\"\\\\\\nYou are an expert evaluator assessing the quality of AI-generated data analysis responses.\\n\\nYou will receive a user task and the results produced by several agents. Each agent used a\\ndifferent set of API functions to answer the same question against the same data repository.\\n\\nWhen ground-truth metadata is provided (expected notebooks, minimum coverage, key finding),\\nuse it to assess each agent result on three dimensions:\\n\\n  1. Notebook coverage \\u2014 what fraction of the expected notebooks did the agent cite or\\n     retrieve? An agent that finds fewer than the minimum required notebooks should not\\n     score above 3, regardless of the quality of its summary.\\n\\n  2. Factual correctness \\u2014 does the agent's reported finding match the expected key finding?\\n     Penalise results that draw the opposite conclusion or miss the central pattern.\\n\\n  3. Analytical depth \\u2014 does the summary interpret the evidence (not just list numbers),\\n     note cross-family differences, and flag limitations or confounds?\\n\\nScoring guide (apply all three dimensions; coverage and correctness carry the most weight):\\n  5 \\u2014 Meets minimum notebook coverage, correct key finding, insightful analysis\\n  4 \\u2014 Near-minimum coverage or minor factual gap, otherwise complete and correct\\n  3 \\u2014 Below minimum coverage OR incorrect/missing key finding, but some valid evidence\\n  2 \\u2014 Severely under-covered (1\\u20132 notebooks only) or substantially incorrect conclusion\\n  1 \\u2014 Does not address the task, errors dominate, or no relevant notebooks retrieved\\n\\nWhen no ground-truth metadata is provided, fall back to general completeness and accuracy.\\n\\nReturn a JSON object with exactly this shape (no markdown fences):\\n{\\n  \\\"ratings\\\": {\\n    \\\"<function_experiment_name>\\\": {\\n      \\\"score\\\": <int 1\\u20135>,\\n      \\\"notebook_coverage\\\": \\\"<N of M expected notebooks cited>\\\",\\n      \\\"rationale\\\": \\\"<brief explanation referencing coverage, correctness, depth>\\\"\\n    }\\n  },\\n  \\\"overall_comment\\\": \\\"<cross-agent comparison and key observations>\\\"\\n}\\n\\\"\\\"\\\"\\n\\n\\ndef evaluate_results(\\n    client: OpenAI,\\n    task: str,\\n    agent_results: dict[str, dict[str, Any]],\\n    task_metadata: dict | None = None,\\n    model: str = EVALUATOR_MODEL,\\n    reasoning: dict | None = None,\\n) -> dict[str, Any]:\\n    \\\"\\\"\\\"Rate each agent result 1\\u20135 using a single evaluator that sees all results.\\n\\n    Args:\\n        client: OpenAI client.\\n        task: The original task string.\\n        agent_results: {experiment_name: {\\\"result\\\": {...}, \\\"metrics\\\": RunMetrics, \\\"error\\\": str|None}}\\n        task_metadata: Optional ground-truth dict from TASK_SPECS (expected_notebooks,\\n                       min_notebooks_expected, key_finding, difficulty, discovery_hint).\\n        model: Evaluator model name.\\n        reasoning: Optional reasoning parameter dict, e.g. {\\\"effort\\\": \\\"high\\\"}.\\n\\n    Returns:\\n        Parsed ratings dict from the evaluator, or a fallback dict on parse failure.\\n    \\\"\\\"\\\"\\n    result_blocks: list[str] = []\\n    for exp_name, run_data in agent_results.items():\\n        error = run_data.get(\\\"error\\\")\\n        if error:\\n            result_blocks.append(f\\\"### Agent: {exp_name}\\\\n**ERROR:** {error}\\\\n\\\")\\n        else:\\n            result = run_data.get(\\\"result\\\") or {}\\n            rows = result.get(\\\"rows\\\", [])\\n            summary = result.get(\\\"summary\\\", \\\"(no summary)\\\")\\n            result_blocks.append(\\n                f\\\"### Agent: {exp_name}\\\\n\\\"\\n                f\\\"**Summary:** {summary}\\\\n\\\\n\\\"\\n                f\\\"**Result rows ({len(rows)} rows):**\\\\n\\\"\\n                f\\\"```json\\\\n{json.dumps(rows[:20], indent=2, default=str)}\\\\n```\\\\n\\\"\\n            )\\n\\n    ground_truth_block = \\\"\\\"\\n    if task_metadata:\\n        expected = task_metadata.get(\\\"expected_notebooks\\\", [])\\n        min_nb = task_metadata.get(\\\"min_notebooks_expected\\\", \\\"?\\\")\\n        key_finding = task_metadata.get(\\\"key_finding\\\", \\\"\\\")\\n        difficulty = task_metadata.get(\\\"difficulty\\\", \\\"\\\")\\n        ground_truth_block = (\\n            f\\\"## Ground-Truth Reference\\\\n\\\\n\\\"\\n            f\\\"**Task difficulty:** {difficulty}\\\\n\\\\n\\\"\\n            f\\\"**Expected notebooks ({len(expected)} total, minimum {min_nb} required):**\\\\n\\\"\\n            + \\\"\\\\n\\\".join(f\\\"  - {nb}\\\" for nb in expected)\\n            + f\\\"\\\\n\\\\n**Key finding the agent should identify:**\\\\n{key_finding}\\\\n\\\\n\\\"\\n            \\\"Use the expected notebook list to assess coverage: count how many of these \\\"\\n            \\\"names (or close variants) appear in the agent's result rows or summary. \\\"\\n            \\\"An agent that cites fewer than the minimum required should not score above 3.\\\\n\\\\n\\\"\\n        )\\n\\n    user_content = (\\n        f\\\"## Task\\\\n{task}\\\\n\\\\n\\\"\\n        + ground_truth_block\\n        + \\\"## Agent Results\\\\n\\\\n\\\"\\n        + \\\"\\\\n---\\\\n\\\".join(result_blocks)\\n    )\\n\\n    create_kwargs: dict[str, Any] = dict(\\n        model=model,\\n        instructions=EVALUATOR_SYSTEM_PROMPT,\\n        input=[{\\\"role\\\": \\\"user\\\", \\\"content\\\": user_content}],\\n    )\\n    if reasoning is not None:\\n        create_kwargs[\\\"reasoning\\\"] = reasoning\\n\\n    response = client.responses.create(**create_kwargs)\\n\\n    raw_text_parts: list[str] = []\\n    for item in response.output or []:\\n        if getattr(item, \\\"type\\\", None) in (\\\"text\\\", \\\"message\\\"):\\n            part = getattr(item, \\\"text\\\", None) or getattr(item, \\\"content\\\", None) or \\\"\\\"\\n            if isinstance(part, list):\\n                for block in part:\\n                    text = getattr(block, \\\"text\\\", None) or \\\"\\\"\\n                    if isinstance(text, str) and text:\\n                        raw_text_parts.append(text)\\n            elif isinstance(part, str) and part:\\n                raw_text_parts.append(part)\\n    raw_text = \\\"\\\".join(raw_text_parts)\\n\\n    try:\\n        text = raw_text.strip()\\n        # Strip markdown code fences if the model wrapped the JSON.\\n        if text.startswith(\\\"```\\\"):\\n            text = re.sub(r\\\"^```[^\\\\n]*\\\\n\\\", \\\"\\\", text)\\n            text = re.sub(r\\\"\\\\n?```$\\\", \\\"\\\", text).strip()\\n        return json.loads(text)\\n    except json.JSONDecodeError:\\n        return {\\n            \\\"parse_error\\\": \\\"Could not parse JSON from evaluator response\\\",\\n            \\\"raw_response\\\": raw_text,\\n        }\\n\\n\\n# ---------------------------------------------------------------------------\\n# Summary helpers\\n# ---------------------------------------------------------------------------\\n\\ndef _extract_summary_stats(metrics: Any) -> dict[str, Any]:\\n    \\\"\\\"\\\"Pull the key statistics we care about from a RunMetrics object.\\\"\\\"\\\"\\n    s = metrics.summary()\\n    return {\\n        \\\"total_tokens\\\": s[\\\"tokens\\\"][\\\"total\\\"],\\n        \\\"input_tokens\\\": s[\\\"tokens\\\"][\\\"input\\\"],\\n        \\\"output_tokens\\\": s[\\\"tokens\\\"][\\\"output\\\"],\\n        \\\"reasoning_tokens\\\": s[\\\"tokens\\\"][\\\"reasoning\\\"],\\n        # num_turns == total OpenAI API calls == number of turns in the loop\\n        \\\"num_turns\\\": s[\\\"api_calls\\\"],\\n        # num_api_function_calls == tool calls that are not finalize_result or no-tool turns\\n        \\\"num_api_function_calls\\\": sum(\\n            1 for t in metrics.turns\\n            if t.tool_name is not None and t.tool_name != \\\"finalize_result\\\"\\n        ),\\n        \\\"wall_time_s\\\": s[\\\"timing\\\"][\\\"wall_time_s\\\"],\\n    }\\n\\n\\ndef _safe_avg(values: list[float | int]) -> float | None:\\n    return round(sum(values) / len(values), 2) if values else None\\n\\n\\ndef _slugify(text: str, max_len: int = 40) -> str:\\n    slug = re.sub(r\\\"[^a-zA-Z0-9]+\\\", \\\"_\\\", text).strip(\\\"_\\\").lower()\\n    return slug[:max_len]\\n\\n\\n# ---------------------------------------------------------------------------\\n# Main experiment loop\\n# ---------------------------------------------------------------------------\\n\\ndef run_experiments(\\n    tasks: list[str] = TASKS,\\n    task_specs: list[dict] | None = TASK_SPECS,\\n    vault_name: str = VAULT_NAME,\\n    agent_model: str = AGENT_MODEL,\\n    evaluator_model: str = EVALUATOR_MODEL,\\n    evaluator_reasoning: dict | None = DEFAULT_EVALUATOR_REASONING,\\n    max_turns: int = MAX_TURNS,\\n    output_root: str = OUTPUT_ROOT,\\n    function_experiments: dict[str, list[str]] | None = None,\\n) -> None:\\n    \\\"\\\"\\\"Run all experiments and save results.\\n\\n    Args:\\n        tasks: List of task strings to evaluate.\\n        task_specs: Optional list of TASK_SPECS dicts providing ground-truth metadata\\n                    (expected_notebooks, key_finding, difficulty) for the evaluator.\\n                    Must align 1-to-1 with tasks if provided.\\n        vault_name: TableVault database name passed to initialization().\\n        agent_model: Model used by the agentic workflow.\\n        evaluator_model: Model used by the evaluator.\\n        evaluator_reasoning: Reasoning dict for the evaluator (e.g. {\\\"effort\\\": \\\"high\\\"}).\\n                             Pass None to disable reasoning.\\n        max_turns: Maximum turns per agent run.\\n        output_root: Root directory for all output files.\\n        function_experiments: Override FUNCTION_EXPERIMENTS; defaults to the full set.\\n    \\\"\\\"\\\"\\n    if function_experiments is None:\\n        function_experiments = FUNCTION_EXPERIMENTS\\n\\n    with open(OPENAI_KEY_FILE, \\\"r\\\") as f:\\n        os.environ[\\\"OPENAI_API_KEY\\\"] = f.read().strip()\\n    client = OpenAI()\\n\\n    vault = initialization(vault_name)\\n\\n    run_id = datetime.now(timezone.utc).strftime(\\\"%Y%m%dT%H%M%SZ\\\")\\n    run_dir = os.path.join(output_root, run_id)\\n    os.makedirs(run_dir, exist_ok=True)\\n\\n    print(\\n        f\\\"\\\\n=== Experiment run {run_id} | {len(tasks)} task(s) | \\\"\\n        f\\\"{len(function_experiments)} function set(s) ===\\\"\\n    )\\n    print(f\\\"Output directory: {run_dir}\\\\n\\\")\\n\\n    all_task_summaries: list[dict[str, Any]] = []\\n\\n    for task_idx, task in enumerate(tasks):\\n        task_meta = task_specs[task_idx] if task_specs and task_idx < len(task_specs) else None\\n        task_slug = _slugify(task)\\n        task_label = f\\\"task_{task_idx:03d}_{task_slug}\\\"\\n        task_dir = os.path.join(run_dir, task_label)\\n        os.makedirs(task_dir, exist_ok=True)\\n\\n        print(f\\\"\\\\n{'='*70}\\\")\\n        print(f\\\"TASK {task_idx}: {task}\\\")\\n        print(f\\\"{'='*70}\\\\n\\\")\\n\\n        agent_results: dict[str, dict[str, Any]] = {}\\n\\n        # --- Run each function experiment in sequence ---\\n        for exp_name, fn_list in function_experiments.items():\\n            print(f\\\"\\\\n--- [{exp_name}] functions: {fn_list} ---\\\")\\n            exp_dir = os.path.join(task_dir, exp_name)\\n            os.makedirs(exp_dir, exist_ok=True)\\n\\n            try:\\n                wf = AgenticWorkflow(\\n                    client=client,\\n                    model=agent_model,\\n                    system_prompt=SYSTEM_PROMPT,\\n                    vault=vault,\\n                    workflow_key=exp_name,\\n                    max_turns=max_turns,\\n                    trace_output_dir=exp_dir,\\n                    trace_filename_stem=\\\"trace\\\",\\n                    reasoning={\\\"effort\\\": \\\"high\\\"},\\n                )\\n                output = wf.run(task)\\n                agent_results[exp_name] = {\\n                    \\\"result\\\": output[\\\"result\\\"],\\n                    \\\"metrics\\\": output[\\\"metrics\\\"],\\n                    \\\"error\\\": None,\\n                }\\n            except Exception as exc:\\n                print(f\\\"  [ERROR] experiment '{exp_name}' failed: {exc}\\\")\\n                agent_results[exp_name] = {\\n                    \\\"result\\\": None,\\n                    \\\"metrics\\\": None,\\n                    \\\"error\\\": str(exc),\\n                }\\n\\n        # --- Evaluate all results for this task with a single evaluator call ---\\n        print(f\\\"\\\\n--- Evaluating {len(agent_results)} agent result(s) ---\\\")\\n        ratings = evaluate_results(\\n            client=client,\\n            task=task,\\n            agent_results=agent_results,\\n            task_metadata=task_meta,\\n            model=evaluator_model,\\n            reasoning=evaluator_reasoning,\\n        )\\n\\n        ratings_path = os.path.join(task_dir, \\\"ratings.json\\\")\\n        with open(ratings_path, \\\"w\\\", encoding=\\\"utf-8\\\") as f:\\n            json.dump({\\\"task\\\": task, \\\"ratings\\\": ratings}, f, indent=2, default=str)\\n        print(f\\\"  ratings saved -> {ratings_path}\\\")\\n\\n        # --- Build per-task summary (stats + rating for each experiment) ---\\n        task_summary: dict[str, Any] = {\\n            \\\"task_idx\\\": task_idx,\\n            \\\"task\\\": task,\\n            \\\"difficulty\\\": task_meta.get(\\\"difficulty\\\") if task_meta else None,\\n            \\\"expected_notebooks\\\": task_meta.get(\\\"expected_notebooks\\\") if task_meta else None,\\n            \\\"min_notebooks_expected\\\": task_meta.get(\\\"min_notebooks_expected\\\") if task_meta else None,\\n            \\\"key_finding\\\": task_meta.get(\\\"key_finding\\\") if task_meta else None,\\n            \\\"experiments\\\": {},\\n        }\\n        per_experiment_ratings: dict[str, Any] = (ratings.get(\\\"ratings\\\") or {})\\n        for exp_name, run_data in agent_results.items():\\n            entry: dict[str, Any] = {\\\"error\\\": run_data[\\\"error\\\"]}\\n            if run_data[\\\"metrics\\\"] is not None:\\n                entry[\\\"stats\\\"] = _extract_summary_stats(run_data[\\\"metrics\\\"])\\n            if exp_name in per_experiment_ratings:\\n                entry[\\\"rating\\\"] = per_experiment_ratings[exp_name]\\n            task_summary[\\\"experiments\\\"][exp_name] = entry\\n\\n        all_task_summaries.append(task_summary)\\n\\n        task_summary_path = os.path.join(task_dir, \\\"summary.json\\\")\\n        with open(task_summary_path, \\\"w\\\", encoding=\\\"utf-8\\\") as f:\\n            json.dump(task_summary, f, indent=2, default=str)\\n        print(f\\\"  task summary saved -> {task_summary_path}\\\")\\n\\n        # --- Print per-task results table ---\\n        difficulty_label = f\\\" [{task_meta['difficulty']}]\\\" if task_meta else \\\"\\\"\\n        print(f\\\"\\\\n--- Results for task {task_idx}{difficulty_label}: {task} ---\\\")\\n        if task_meta:\\n            print(\\n                f\\\"  Expected notebooks ({task_meta['min_notebooks_expected']} min): \\\"\\n                + \\\", \\\".join(task_meta[\\\"expected_notebooks\\\"])\\n            )\\n        print(\\n            f\\\"\\\\n{'Experiment':<35} {'Tokens':>12} {'FnCalls':>10} \\\"\\n            f\\\"{'Turns':>8} {'Score':>8} {'Coverage':>10}  Rationale\\\"\\n        )\\n        print(\\\"-\\\" * 115)\\n        for exp_name, exp_data in task_summary[\\\"experiments\\\"].items():\\n            error = exp_data.get(\\\"error\\\")\\n            if error:\\n                print(f\\\"{exp_name:<35} {'ERROR':>12}  {error[:60]}\\\")\\n                continue\\n            stats = exp_data.get(\\\"stats\\\", {})\\n            rating = exp_data.get(\\\"rating\\\", {})\\n            score = rating.get(\\\"score\\\", \\\"-\\\") if isinstance(rating, dict) else \\\"-\\\"\\n            coverage = rating.get(\\\"notebook_coverage\\\", \\\"-\\\") if isinstance(rating, dict) else \\\"-\\\"\\n            rationale = rating.get(\\\"rationale\\\", \\\"\\\") if isinstance(rating, dict) else \\\"\\\"\\n            print(\\n                f\\\"{exp_name:<35} \\\"\\n                f\\\"{str(stats.get('total_tokens', '-')):>12} \\\"\\n                f\\\"{str(stats.get('num_api_function_calls', '-')):>10} \\\"\\n                f\\\"{str(stats.get('num_turns', '-')):>8} \\\"\\n                f\\\"{str(score):>8} \\\"\\n                f\\\"{str(coverage):>10}  {rationale[:55]}\\\"\\n            )\\n        overall = ratings.get(\\\"overall_comment\\\", \\\"\\\")\\n        if overall:\\n            print(f\\\"\\\\nOverall: {overall}\\\")\\n        print()\\n\\n    # --- Aggregate stats across all tasks, grouped by function experiment ---\\n    by_experiment: dict[str, dict[str, Any]] = {}\\n    for exp_name in function_experiments:\\n        token_totals, api_fn_call_totals, turn_totals, scores = [], [], [], []\\n        for ts in all_task_summaries:\\n            exp_data = ts[\\\"experiments\\\"].get(exp_name, {})\\n            stats = exp_data.get(\\\"stats\\\")\\n            if stats:\\n                token_totals.append(stats[\\\"total_tokens\\\"])\\n                api_fn_call_totals.append(stats[\\\"num_api_function_calls\\\"])\\n                turn_totals.append(stats[\\\"num_turns\\\"])\\n            rating = exp_data.get(\\\"rating\\\")\\n            if isinstance(rating, dict) and isinstance(rating.get(\\\"score\\\"), (int, float)):\\n                scores.append(rating[\\\"score\\\"])\\n\\n        by_experiment[exp_name] = {\\n            \\\"num_tasks_completed\\\": len(token_totals),\\n            \\\"avg_total_tokens\\\": _safe_avg(token_totals),\\n            \\\"avg_num_api_function_calls\\\": _safe_avg(api_fn_call_totals),\\n            \\\"avg_num_turns\\\": _safe_avg(turn_totals),\\n            \\\"avg_rating\\\": _safe_avg(scores),\\n        }\\n\\n    global_summary: dict[str, Any] = {\\n        \\\"run_id\\\": run_id,\\n        \\\"agent_model\\\": agent_model,\\n        \\\"evaluator_model\\\": evaluator_model,\\n        \\\"evaluator_reasoning\\\": evaluator_reasoning,\\n        \\\"vault_name\\\": vault_name,\\n        \\\"num_tasks\\\": len(tasks),\\n        \\\"by_experiment\\\": by_experiment,\\n        \\\"per_task\\\": all_task_summaries,\\n    }\\n\\n    global_summary_path = os.path.join(run_dir, \\\"global_summary.json\\\")\\n    with open(global_summary_path, \\\"w\\\", encoding=\\\"utf-8\\\") as f:\\n        json.dump(global_summary, f, indent=2, default=str)\\n    print(f\\\"\\\\n=== Global summary saved -> {global_summary_path} ===\\\")\\n\\n    # --- Print aggregate table ---\\n    print(\\n        f\\\"\\\\n{'Experiment':<35} {'AvgTokens':>12} {'AvgFnCalls':>12} \\\"\\n        f\\\"{'AvgTurns':>10} {'AvgScore':>10}\\\"\\n    )\\n    print(\\\"-\\\" * 82)\\n    for exp_name, agg in by_experiment.items():\\n        print(\\n            f\\\"{exp_name:<35} \\\"\\n            f\\\"{str(agg['avg_total_tokens']):>12} \\\"\\n            f\\\"{str(agg['avg_num_api_function_calls']):>12} \\\"\\n            f\\\"{str(agg['avg_num_turns']):>10} \\\"\\n            f\\\"{str(agg['avg_rating']):>10}\\\"\\n        )\\n    print()\\n\\n\\n# ---------------------------------------------------------------------------\\n# Entry point\\n# ---------------------------------------------------------------------------\\n\\nif __name__ == \\\"__main__\\\":\\n    run_experiments()\\n\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c1cb02c8195b0126c3baf31a4f8`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_search",
    "call_id": "call_YDExegJcifzAPweXRA9Ijwl6",
    "arguments": {
      "code": "append_record("
    }
  }
]
```

### Tool Call
**Tool:** `code_search` | **call_id:** `call_YDExegJcifzAPweXRA9Ijwl6`

**Arguments:**
```json
{
  "code": "append_record("
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "hf_pipeline_mrpc_short_maxlen_64",
    "hf_pipeline_mrpc_margin_rule",
    "neutral_penalized_margin_mrpc",
    "st_all_minilm_l6_l2_distance_threshold_mrpc",
    "quora_cross_encoder_prefixed_sentence_tags_mrpc",
    "hf_pipeline_mrpc_raw_logits_softmax",
    "distilbert_max_pool_cosine_mrpc",
    "consensus_then_avg_margin_mrpc",
    "flan_t5_full_answer_logprob_mrpc",
    "softmax_gap_mean_mrpc",
    "quora_cross_encoder_symmetric_average_mrpc",
    "quora_cross_encoder_max_length_64_mrpc",
    "quora_cross_encoder_softmax_threshold_065_mrpc",
    "st_all_minilm_l6_max_seq_len_64_cosine_mrpc",
    "st_paraphrase_minilm_l6_cosine_threshold_mrpc",
    "flan_t5_answer_prefix_yes_no_mrpc",
    "distilbert_mean_cosine_median_threshold_mrpc",
    "distilbert_no_special_tokens_mean_cosine_mrpc",
    "hf_pipeline_mrpc_threshold_070",
    "distilbert_last4_mean_cosine_mrpc",
    "min_direction_margin_mrpc",
    "entailment_logprob_odds_mrpc",
    "st_all_distilroberta_v1_cosine_threshold_mrpc",
    "mrpc_paraphrase_inference_distilbert",
    "flan_t5_contextual_calibrated_yes_no_mrpc",
    "st_paraphrase_minilm_l3_cosine_threshold_mrpc",
    "flan_t5_symmetric_prompt_average_mrpc",
    "distilbert_cls_cosine_mrpc",
    "quora_cross_encoder_text_normalized_mrpc",
    "flan_t5_true_false_first_step_mrpc",
    "hf_pipeline_mrpc_bidirectional_order_average"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 15988 | 99 | 77 | 14418 | 2.311s | 0.048s |

---

## Turn 5 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c1f0560819583af5234f97f91f9`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_YDExegJcifzAPweXRA9Ijwl6",
    "output": "{\"ok\": true, \"result\": [\"hf_pipeline_mrpc_short_maxlen_64\", \"hf_pipeline_mrpc_margin_rule\", \"neutral_penalized_margin_mrpc\", \"st_all_minilm_l6_l2_distance_threshold_mrpc\", \"quora_cross_encoder_prefixed_sentence_tags_mrpc\", \"hf_pipeline_mrpc_raw_logits_softmax\", \"distilbert_max_pool_cosine_mrpc\", \"consensus_then_avg_margin_mrpc\", \"flan_t5_full_answer_logprob_mrpc\", \"softmax_gap_mean_mrpc\", \"quora_cross_encoder_symmetric_average_mrpc\", \"quora_cross_encoder_max_length_64_mrpc\", \"quora_cross_encoder_softmax_threshold_065_mrpc\", \"st_all_minilm_l6_max_seq_len_64_cosine_mrpc\", \"st_paraphrase_minilm_l6_cosine_threshold_mrpc\", \"flan_t5_answer_prefix_yes_no_mrpc\", \"distilbert_mean_cosine_median_threshold_mrpc\", \"distilbert_no_special_tokens_mean_cosine_mrpc\", \"hf_pipeline_mrpc_threshold_070\", \"distilbert_last4_mean_cosine_mrpc\", \"min_direction_margin_mrpc\", \"entailment_logprob_odds_mrpc\", \"st_all_distilroberta_v1_cosine_threshold_mrpc\", \"mrpc_paraphrase_inference_distilbert\", \"flan_t5_contextual_calibrated_yes_no_mrpc\", \"st_paraphrase_minilm_l3_cosine_threshold_mrpc\", \"flan_t5_symmetric_prompt_average_mrpc\", \"distilbert_cls_cosine_mrpc\", \"quora_cross_encoder_text_normalized_mrpc\", \"flan_t5_true_false_first_step_mrpc\", \"hf_pipeline_mrpc_bidirectional_order_average\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c1f0560819583af5234f97f91f9`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "get_code",
    "call_id": "call_rXHHUIjs1qMK9u3iiqya5QSF",
    "arguments": {
      "name": "neutral_penalized_margin_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_rXHHUIjs1qMK9u3iiqya5QSF`

**Arguments:**
```json
{
  "name": "neutral_penalized_margin_mrpc"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "def get_embeddings(text):\n    return client.embeddings.create(\n            input=text,\n            model=\"text-embedding-3-large\"\n        ).data[0].embedding",
    "import torch\nimport numpy as np\nfrom datasets import Dataset\nfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\nfrom tqdm.auto import tqdm\n\ndevice = torch.device(\"mps\" if torch.backends.mps.is_available() else \"cpu\")\nprint(\"device:\", device)\n",
    "model_name = \"typeform/distilbert-base-uncased-mnli\"\n\ntokenizer = AutoTokenizer.from_pretrained(model_name)\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\nmodel.eval()\n\nid2label = model.config.id2label\nlabel2id = {str(v).lower(): int(k) for k, v in id2label.items()}\n\ndef resolve_label_id(label2id_map, candidates):\n    for cand in candidates:\n        if cand in label2id_map:\n            return label2id_map[cand]\n    raise ValueError(f\"Could not resolve label id from candidates={candidates}; available labels={label2id_map}\")\n\ncontradiction_id = resolve_label_id(label2id, [\"contradiction\", \"contradictory\", \"label_0\"])\nneutral_id = resolve_label_id(label2id, [\"neutral\", \"label_1\"])\nentailment_id = resolve_label_id(label2id, [\"entailment\", \"label_2\"])\n\nprint(model_name)\nprint(\"id2label:\", id2label)\nprint({\n    \"contradiction_id\": contradiction_id,\n    \"neutral_id\": neutral_id,\n    \"entailment_id\": entailment_id,\n})\n",
    "ds = vault.query_item_content(\"glue_mrpc_validation\")\nds = Dataset.from_list(ds)\nprint(ds)\nprint(ds[0])\n\nsent1 = ds[\"sentence1\"]\nsent2 = ds[\"sentence2\"]\ny_true = np.array(ds[\"label\"])\n\nprint(\"num_examples:\", len(y_true))\nprint(\"positive_rate:\", y_true.mean())\n",
    "batch_size = 64\nscore_12_all = []\nscore_21_all = []\navg_score_all = []\npreds = []\n\nwith torch.no_grad():\n    for i in tqdm(range(0, len(ds), batch_size)):\n        batch_s1 = sent1[i:i + batch_size]\n        batch_s2 = sent2[i:i + batch_size]\n\n        enc12 = tokenizer(\n            batch_s1,\n            batch_s2,\n            padding=True,\n            truncation=True,\n            max_length=128,\n            return_tensors=\"pt\",\n        )\n        enc12 = {k: v.to(device) for k, v in enc12.items()}\n\n        enc21 = tokenizer(\n            batch_s2,\n            batch_s1,\n            padding=True,\n            truncation=True,\n            max_length=128,\n            return_tensors=\"pt\",\n        )\n        enc21 = {k: v.to(device) for k, v in enc21.items()}\n\n        logits12 = model(**enc12).logits\n        logits21 = model(**enc21).logits\n\n        score12 = logits12[:, entailment_id] - torch.maximum(logits12[:, contradiction_id], logits12[:, neutral_id])\n        score21 = logits21[:, entailment_id] - torch.maximum(logits21[:, contradiction_id], logits21[:, neutral_id])\n        avg_score = (score12 + score21) / 2.0\n        batch_preds = (avg_score > 0).long()\n\n        score_12_all.extend(score12.cpu().numpy())\n        score_21_all.extend(score21.cpu().numpy())\n        avg_score_all.extend(avg_score.cpu().numpy())\n        preds.extend(batch_preds.cpu().numpy())\n\nscore_12_all = np.array(score_12_all)\nscore_21_all = np.array(score_21_all)\navg_score_all = np.array(avg_score_all)\ny_pred = np.array(preds)\n\nprint(\"done\")\nprint(\"score_12 range:\", float(score_12_all.min()), float(score_12_all.max()))\nprint(\"score_21 range:\", float(score_21_all.min()), float(score_21_all.max()))\nprint(\"avg_score range:\", float(avg_score_all.min()), float(avg_score_all.max()))\n",
    "vault.create_record_list(\"mrpc_neutral_penalty_prediction\", column_names=[\"prediction\", \"score_12\", \"score_21\"])\n\nfor i in range(len(y_pred)):\n    vault.append_record(\"mrpc_neutral_penalty_prediction\", \n                        {\n                            \"prediction\": int(y_pred[i]),\n                            \"score_12\": float(score_12_all[i]),\n                            \"score_21\": float(score_21_all[i]),\n                        },\n                       input_items = {\n                           \"glue_mrpc_validation\": [i, i + 1],\n                       }\n                       )\n\ndescription = \"Per-example prediction dataset for the GLUE MRPC validation split, produced by applying the typeform/distilbert-base-uncased-mnli model as a zero-shot paraphrase detector. Each record corresponds to one sentence pair from glue_mrpc_validation and stores: prediction (binary paraphrase decision, where 1 indicates paraphrase and 0 indicates not_paraphrase), score_12 (entailment logit minus max(contradiction, neutral) for sentence1 -> sentence2), and score_21 (the same score for sentence2 -> sentence1). The final prediction is derived from the average of the two directional scores. In this workflow, this dataset captures the model\\u2019s per-example outputs for downstream evaluation, inspection of mistakes, and construction of the overall summary metrics.\"\nembedding = get_embeddings(description)\nvault.create_description(\"mrpc_neutral_penalty_prediction\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"record_type\": \"model predictions\", \"source\": \"glue/mrpc\", \"source_item\": \"glue_mrpc_validation\", \"split\": \"validation\", \"size\": \"408\", \"input_format\": \"sentence pair\", \"label_space\": \"binary\", \"model\": \"typeform/distilbert-base-uncased-mnli\", \"model_family\": \"distilbert\", \"inference_method\": \"neutral-penalized entailment margin\", \"scoring\": \"avg_bidirectional_entailment_minus_max(contradiction,neutral)\", \"prediction_target\": \"paraphrase\", \"domain\": \"news\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"mrpc_neutral_penalty_prediction\", cat, embedding, prop)",
    "acc = accuracy_score(y_true, y_pred)\nf1 = f1_score(y_true, y_pred)\nreport = classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"])\nprint({\"accuracy\": acc, \"f1\": f1})\nprint(classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"]))\n",
    "for i in range(5):\n    print(\"=\" * 80)\n    print(\"sentence1:\", sent1[i])\n    print(\"sentence2:\", sent2[i])\n    print(\"score_12:\", float(score_12_all[i]))\n    print(\"score_21:\", float(score_21_all[i]))\n    print(\"avg_score:\", float(avg_score_all[i]))\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]), \"label:\", \"paraphrase\" if int(y_pred[i]) == 1 else \"not_paraphrase\")\n",
    "mistakes = np.where(y_true != y_pred)[0][:10]\nprint(\"num_errors:\", int((y_true != y_pred).sum()))\n\nfor i in mistakes:\n    print(\"=\" * 80)\n    print(\"idx:\", int(i))\n    print(\"sentence1:\", sent1[i])\n    print(\"sentence2:\", sent2[i])\n    print(\"score_12:\", float(score_12_all[i]))\n    print(\"score_21:\", float(score_21_all[i]))\n    print(\"avg_score:\", float(avg_score_all[i]))\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]))\n",
    "vault.create_record_list(\"neutral_penalized_margin_mrpc_summary\", column_names=[\"accuracy\", \"f1\", \"classification_report\"])\n\n\nsummary = {\n    \"accuracy\": float(acc),\n    \"f1\": float(f1),\n    \"classification_report\": str(report)\n}\n\nvault.append_record(\"neutral_penalized_margin_mrpc_summary\", summary,\n                    input_items = {\n                        \"glue_mrpc_validation\": [0, len(ds)],\n                        \"mrpc_neutral_penalty_prediction\": [0, len(ds)]\n                    })\n\nsummary\n\ndescription = \"Aggregate evaluation summary for the neutral-penalized margin MRPC experiment. This dataset contains a single summary record computed from the GLUE MRPC validation set and the derived mrpc_neutral_penalty_prediction records. Its fields are: accuracy (float, overall prediction accuracy), f1 (float, F1 score for the paraphrase class), and classification_report (string, full sklearn classification report with per-class precision, recall, F1, and support). In this workflow, it serves as the compact experiment-level output used to record and retrieve overall model performance after scoring sentence pairs with the MNLI model and converting the bidirectional entailment-vs.-non-entailment margin into paraphrase predictions.\"\nembedding = get_embeddings(description)\nvault.create_description(\"neutral_penalized_margin_mrpc_summary\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"dataset_role\": \"evaluation summary\", \"source\": \"glue/mrpc\", \"benchmark\": \"GLUE\", \"split\": \"validation\", \"size\": \"408\", \"input_type\": \"sentence pair\", \"label_space\": \"binary paraphrase classification\", \"metrics\": \"accuracy,f1,classification_report\", \"model\": \"typeform/distilbert-base-uncased-mnli\", \"method\": \"neutral-penalized entailment margin\", \"derived_from\": \"mrpc_neutral_penalty_prediction\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"neutral_penalized_margin_mrpc_summary\", cat, embedding, prop)\n\n",
    "description = \"This notebook runs a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the NLI model typeform/distilbert-base-uncased-mnli. Its purpose is to score sentence pairs as paraphrase vs. not paraphrase without task-specific fine-tuning, using a neutral-penalized entailment margin. For each MRPC pair, the notebook evaluates both sentence orders, computes an entailment score minus the larger of the contradiction or neutral scores, averages the two directional margins, and predicts paraphrase when the averaged margin is positive. It then stores per-example predictions and scores in TableVault, links them back to the source validation records, computes evaluation metrics including accuracy, F1, and a classification report, inspects example predictions and errors, and saves dataset-, prediction-, summary-, and process-level metadata and semantic descriptions using OpenAI embeddings.\" # description of whole notebook\nembedding = get_embeddings(description)\nvault.create_description(\"neutral_penalized_margin_mrpc\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"approach\": \"zero-shot NLI transfer\", \"scoring_method\": \"symmetric entailment margin with neutral penalty\", \"model\": \"typeform/distilbert-base-uncased-mnli\", \"dataset\": \"glue/mrpc\", \"split\": \"validation\", \"inputs\": \"sentence pair\", \"framework\": \"PyTorch, Hugging Face Transformers\", \"metrics\": \"accuracy, f1-score, classification report\", \"artifacts\": \"per-example predictions and summary records\", \"storage\": \"TableVault with ArangoDB\", \"embedding_model\": \"text-embedding-3-large\"} #e.g. model: distilbert-base-uncased-MRPC\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"neutral_penalized_margin_mrpc\", cat, embedding, prop)"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 16468 | 106 | 80 | 14898 | 2.614s | 0.023s |

---

## Turn 6 — `get_code` [ERROR]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c2252dc8195abaff7216fcc8523`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_rXHHUIjs1qMK9u3iiqya5QSF",
    "output": "{\"ok\": true, \"result\": [\"def get_embeddings(text):\\n    return client.embeddings.create(\\n            input=text,\\n            model=\\\"text-embedding-3-large\\\"\\n        ).data[0].embedding\", \"import torch\\nimport numpy as np\\nfrom datasets import Dataset\\nfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\\nfrom tqdm.auto import tqdm\\n\\ndevice = torch.device(\\\"mps\\\" if torch.backends.mps.is_available() else \\\"cpu\\\")\\nprint(\\\"device:\\\", device)\\n\", \"model_name = \\\"typeform/distilbert-base-uncased-mnli\\\"\\n\\ntokenizer = AutoTokenizer.from_pretrained(model_name)\\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\\nmodel.eval()\\n\\nid2label = model.config.id2label\\nlabel2id = {str(v).lower(): int(k) for k, v in id2label.items()}\\n\\ndef resolve_label_id(label2id_map, candidates):\\n    for cand in candidates:\\n        if cand in label2id_map:\\n            return label2id_map[cand]\\n    raise ValueError(f\\\"Could not resolve label id from candidates={candidates}; available labels={label2id_map}\\\")\\n\\ncontradiction_id = resolve_label_id(label2id, [\\\"contradiction\\\", \\\"contradictory\\\", \\\"label_0\\\"])\\nneutral_id = resolve_label_id(label2id, [\\\"neutral\\\", \\\"label_1\\\"])\\nentailment_id = resolve_label_id(label2id, [\\\"entailment\\\", \\\"label_2\\\"])\\n\\nprint(model_name)\\nprint(\\\"id2label:\\\", id2label)\\nprint({\\n    \\\"contradiction_id\\\": contradiction_id,\\n    \\\"neutral_id\\\": neutral_id,\\n    \\\"entailment_id\\\": entailment_id,\\n})\\n\", \"ds = vault.query_item_content(\\\"glue_mrpc_validation\\\")\\nds = Dataset.from_list(ds)\\nprint(ds)\\nprint(ds[0])\\n\\nsent1 = ds[\\\"sentence1\\\"]\\nsent2 = ds[\\\"sentence2\\\"]\\ny_true = np.array(ds[\\\"label\\\"])\\n\\nprint(\\\"num_examples:\\\", len(y_true))\\nprint(\\\"positive_rate:\\\", y_true.mean())\\n\", \"batch_size = 64\\nscore_12_all = []\\nscore_21_all = []\\navg_score_all = []\\npreds = []\\n\\nwith torch.no_grad():\\n    for i in tqdm(range(0, len(ds), batch_size)):\\n        batch_s1 = sent1[i:i + batch_size]\\n        batch_s2 = sent2[i:i + batch_size]\\n\\n        enc12 = tokenizer(\\n            batch_s1,\\n            batch_s2,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc12 = {k: v.to(device) for k, v in enc12.items()}\\n\\n        enc21 = tokenizer(\\n            batch_s2,\\n            batch_s1,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc21 = {k: v.to(device) for k, v in enc21.items()}\\n\\n        logits12 = model(**enc12).logits\\n        logits21 = model(**enc21).logits\\n\\n        score12 = logits12[:, entailment_id] - torch.maximum(logits12[:, contradiction_id], logits12[:, neutral_id])\\n        score21 = logits21[:, entailment_id] - torch.maximum(logits21[:, contradiction_id], logits21[:, neutral_id])\\n        avg_score = (score12 + score21) / 2.0\\n        batch_preds = (avg_score > 0).long()\\n\\n        score_12_all.extend(score12.cpu().numpy())\\n        score_21_all.extend(score21.cpu().numpy())\\n        avg_score_all.extend(avg_score.cpu().numpy())\\n        preds.extend(batch_preds.cpu().numpy())\\n\\nscore_12_all = np.array(score_12_all)\\nscore_21_all = np.array(score_21_all)\\navg_score_all = np.array(avg_score_all)\\ny_pred = np.array(preds)\\n\\nprint(\\\"done\\\")\\nprint(\\\"score_12 range:\\\", float(score_12_all.min()), float(score_12_all.max()))\\nprint(\\\"score_21 range:\\\", float(score_21_all.min()), float(score_21_all.max()))\\nprint(\\\"avg_score range:\\\", float(avg_score_all.min()), float(avg_score_all.max()))\\n\", \"vault.create_record_list(\\\"mrpc_neutral_penalty_prediction\\\", column_names=[\\\"prediction\\\", \\\"score_12\\\", \\\"score_21\\\"])\\n\\nfor i in range(len(y_pred)):\\n    vault.append_record(\\\"mrpc_neutral_penalty_prediction\\\", \\n                        {\\n                            \\\"prediction\\\": int(y_pred[i]),\\n                            \\\"score_12\\\": float(score_12_all[i]),\\n                            \\\"score_21\\\": float(score_21_all[i]),\\n                        },\\n                       input_items = {\\n                           \\\"glue_mrpc_validation\\\": [i, i + 1],\\n                       }\\n                       )\\n\\ndescription = \\\"Per-example prediction dataset for the GLUE MRPC validation split, produced by applying the typeform/distilbert-base-uncased-mnli model as a zero-shot paraphrase detector. Each record corresponds to one sentence pair from glue_mrpc_validation and stores: prediction (binary paraphrase decision, where 1 indicates paraphrase and 0 indicates not_paraphrase), score_12 (entailment logit minus max(contradiction, neutral) for sentence1 -> sentence2), and score_21 (the same score for sentence2 -> sentence1). The final prediction is derived from the average of the two directional scores. In this workflow, this dataset captures the model\\\\u2019s per-example outputs for downstream evaluation, inspection of mistakes, and construction of the overall summary metrics.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"mrpc_neutral_penalty_prediction\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"record_type\\\": \\\"model predictions\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"source_item\\\": \\\"glue_mrpc_validation\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"input_format\\\": \\\"sentence pair\\\", \\\"label_space\\\": \\\"binary\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"model_family\\\": \\\"distilbert\\\", \\\"inference_method\\\": \\\"neutral-penalized entailment margin\\\", \\\"scoring\\\": \\\"avg_bidirectional_entailment_minus_max(contradiction,neutral)\\\", \\\"prediction_target\\\": \\\"paraphrase\\\", \\\"domain\\\": \\\"news\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"mrpc_neutral_penalty_prediction\\\", cat, embedding, prop)\", \"acc = accuracy_score(y_true, y_pred)\\nf1 = f1_score(y_true, y_pred)\\nreport = classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"])\\nprint({\\\"accuracy\\\": acc, \\\"f1\\\": f1})\\nprint(classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"]))\\n\", \"for i in range(5):\\n    print(\\\"=\\\" * 80)\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"score_12:\\\", float(score_12_all[i]))\\n    print(\\\"score_21:\\\", float(score_21_all[i]))\\n    print(\\\"avg_score:\\\", float(avg_score_all[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]), \\\"label:\\\", \\\"paraphrase\\\" if int(y_pred[i]) == 1 else \\\"not_paraphrase\\\")\\n\", \"mistakes = np.where(y_true != y_pred)[0][:10]\\nprint(\\\"num_errors:\\\", int((y_true != y_pred).sum()))\\n\\nfor i in mistakes:\\n    print(\\\"=\\\" * 80)\\n    print(\\\"idx:\\\", int(i))\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"score_12:\\\", float(score_12_all[i]))\\n    print(\\\"score_21:\\\", float(score_21_all[i]))\\n    print(\\\"avg_score:\\\", float(avg_score_all[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n\", \"vault.create_record_list(\\\"neutral_penalized_margin_mrpc_summary\\\", column_names=[\\\"accuracy\\\", \\\"f1\\\", \\\"classification_report\\\"])\\n\\n\\nsummary = {\\n    \\\"accuracy\\\": float(acc),\\n    \\\"f1\\\": float(f1),\\n    \\\"classification_report\\\": str(report)\\n}\\n\\nvault.append_record(\\\"neutral_penalized_margin_mrpc_summary\\\", summary,\\n                    input_items = {\\n                        \\\"glue_mrpc_validation\\\": [0, len(ds)],\\n                        \\\"mrpc_neutral_penalty_prediction\\\": [0, len(ds)]\\n                    })\\n\\nsummary\\n\\ndescription = \\\"Aggregate evaluation summary for the neutral-penalized margin MRPC experiment. This dataset contains a single summary record computed from the GLUE MRPC validation set and the derived mrpc_neutral_penalty_prediction records. Its fields are: accuracy (float, overall prediction accuracy), f1 (float, F1 score for the paraphrase class), and classification_report (string, full sklearn classification report with per-class precision, recall, F1, and support). In this workflow, it serves as the compact experiment-level output used to record and retrieve overall model performance after scoring sentence pairs with the MNLI model and converting the bidirectional entailment-vs.-non-entailment margin into paraphrase predictions.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"neutral_penalized_margin_mrpc_summary\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_role\\\": \\\"evaluation summary\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"benchmark\\\": \\\"GLUE\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"input_type\\\": \\\"sentence pair\\\", \\\"label_space\\\": \\\"binary paraphrase classification\\\", \\\"metrics\\\": \\\"accuracy,f1,classification_report\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"method\\\": \\\"neutral-penalized entailment margin\\\", \\\"derived_from\\\": \\\"mrpc_neutral_penalty_prediction\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"neutral_penalized_margin_mrpc_summary\\\", cat, embedding, prop)\\n\\n\", \"description = \\\"This notebook runs a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the NLI model typeform/distilbert-base-uncased-mnli. Its purpose is to score sentence pairs as paraphrase vs. not paraphrase without task-specific fine-tuning, using a neutral-penalized entailment margin. For each MRPC pair, the notebook evaluates both sentence orders, computes an entailment score minus the larger of the contradiction or neutral scores, averages the two directional margins, and predicts paraphrase when the averaged margin is positive. It then stores per-example predictions and scores in TableVault, links them back to the source validation records, computes evaluation metrics including accuracy, F1, and a classification report, inspects example predictions and errors, and saves dataset-, prediction-, summary-, and process-level metadata and semantic descriptions using OpenAI embeddings.\\\" # description of whole notebook\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"neutral_penalized_margin_mrpc\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"approach\\\": \\\"zero-shot NLI transfer\\\", \\\"scoring_method\\\": \\\"symmetric entailment margin with neutral penalty\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"dataset\\\": \\\"glue/mrpc\\\", \\\"split\\\": \\\"validation\\\", \\\"inputs\\\": \\\"sentence pair\\\", \\\"framework\\\": \\\"PyTorch, Hugging Face Transformers\\\", \\\"metrics\\\": \\\"accuracy, f1-score, classification report\\\", \\\"artifacts\\\": \\\"per-example predictions and summary records\\\", \\\"storage\\\": \\\"TableVault with ArangoDB\\\", \\\"embedding_model\\\": \\\"text-embedding-3-large\\\"} #e.g. model: distilbert-base-uncased-MRPC\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"neutral_penalized_margin_mrpc\\\", cat, embedding, prop)\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c2252dc8195abaff7216fcc8523`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "get_code",
    "call_id": "call_kZ902Rp1gJhATXtMQw0PzDhG",
    "arguments": {
      "name": "bidirectional_averaged_zero_shot_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_kZ902Rp1gJhATXtMQw0PzDhG`

**Arguments:**
```json
{
  "name": "bidirectional_averaged_zero_shot_mrpc"
}
```

### Tool Output
```json
{
  "ok": false,
  "error": "Name given isn't a registered code process"
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 19427 | 397 | 368 | 17857 | 6.923s | 0.007s |

### Error
```
Name given isn't a registered code process
```

---

## Turn 7 — `code_search` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c2898e4819592feab4a7cfebef8`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_kZ902Rp1gJhATXtMQw0PzDhG",
    "output": "{\"ok\": false, \"error\": \"Name given isn't a registered code process\"}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c2898e4819592feab4a7cfebef8`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_search",
    "call_id": "call_e3bo1OXTfaHWIvi9RhTkoAlw",
    "arguments": {
      "code": "bidirectional_averaged_zero_shot_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `code_search` | **call_id:** `call_e3bo1OXTfaHWIvi9RhTkoAlw`

**Arguments:**
```json
{
  "code": "bidirectional_averaged_zero_shot_mrpc"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "gent_1775914190",
    "gent_1775874933",
    "gent_1775874373",
    "gent_1775874650",
    "gent_1775914000",
    "gent_1775913615"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 19852 | 60 | 31 | 18282 | 3.799s | 0.048s |

---

## Turn 8 — `code_search` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c2c70ac8195a84a506713fa8617`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_e3bo1OXTfaHWIvi9RhTkoAlw",
    "output": "{\"ok\": true, \"result\": [\"gent_1775914190\", \"gent_1775874933\", \"gent_1775874373\", \"gent_1775874650\", \"gent_1775914000\", \"gent_1775913615\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c2c70ac8195a84a506713fa8617`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_search",
    "call_id": "call_DGEOzgCrzp7y1KKgwQ6ziAWy",
    "arguments": {
      "code": "candidate_labels"
    }
  }
]
```

### Tool Call
**Tool:** `code_search` | **call_id:** `call_DGEOzgCrzp7y1KKgwQ6ziAWy`

**Arguments:**
```json
{
  "code": "candidate_labels"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": []
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 19980 | 43 | 22 | 18410 | 1.795s | 0.009s |

---

## Turn 9 — `code_search` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c2e3c9881959827890d8855324b`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_DGEOzgCrzp7y1KKgwQ6ziAWy",
    "output": "{\"ok\": true, \"result\": []}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c2e3c9881959827890d8855324b`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_search",
    "call_id": "call_9RemDUviMECOGkxWCJfzMlZV",
    "arguments": {
      "code": "zero-shot"
    }
  }
]
```

### Tool Call
**Tool:** `code_search` | **call_id:** `call_9RemDUviMECOGkxWCJfzMlZV`

**Arguments:**
```json
{
  "code": "zero-shot"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "entailment_logprob_odds_mrpc",
    "gent_1775914190",
    "gent_1775874933",
    "gent_1775874373",
    "softmax_gap_mean_mrpc",
    "flan_t5_contextual_calibrated_yes_no_mrpc",
    "neutral_penalized_margin_mrpc",
    "flan_t5_symmetric_prompt_average_mrpc",
    "gent_1775874650",
    "gent_1775913615",
    "gent_1775914000",
    "flan_t5_true_false_first_step_mrpc",
    "consensus_then_avg_margin_mrpc",
    "min_direction_margin_mrpc"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 20044 | 30 | 9 | 18474 | 1.629s | 0.051s |

---

## Turn 10 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c2fed408195b220f1a5416b4cc3`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_9RemDUviMECOGkxWCJfzMlZV",
    "output": "{\"ok\": true, \"result\": [\"entailment_logprob_odds_mrpc\", \"gent_1775914190\", \"gent_1775874933\", \"gent_1775874373\", \"softmax_gap_mean_mrpc\", \"flan_t5_contextual_calibrated_yes_no_mrpc\", \"neutral_penalized_margin_mrpc\", \"flan_t5_symmetric_prompt_average_mrpc\", \"gent_1775874650\", \"gent_1775913615\", \"gent_1775914000\", \"flan_t5_true_false_first_step_mrpc\", \"consensus_then_avg_margin_mrpc\", \"min_direction_margin_mrpc\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c2fed408195b220f1a5416b4cc3`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "get_code",
    "call_id": "call_q1tXfeGs0lcTlaIQTNBQh8RI",
    "arguments": {
      "name": "min_direction_margin_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_q1tXfeGs0lcTlaIQTNBQh8RI`

**Arguments:**
```json
{
  "name": "min_direction_margin_mrpc"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "import torch\nimport numpy as np\nfrom datasets import Dataset\nfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\nfrom tqdm.auto import tqdm\n\ndevice = torch.device(\"mps\" if torch.backends.mps.is_available() else \"cpu\")\nprint(\"device:\", device)\n",
    "def get_embeddings(text):\n    return client.embeddings.create(\n            input=text,\n            model=\"text-embedding-3-large\"\n        ).data[0].embedding",
    "model_name = \"typeform/distilbert-base-uncased-mnli\"\n\ntokenizer = AutoTokenizer.from_pretrained(model_name)\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\nmodel.eval()\n\nid2label = {int(k): v for k, v in model.config.id2label.items()}\nentailment_id = next(i for i, label in id2label.items() if \"entail\" in label.lower())\ncontradiction_id = next(i for i, label in id2label.items() if \"contrad\" in label.lower())\n\nprint(\"model:\", model_name)\nprint(\"id2label:\", id2label)\nprint(\"entailment_id:\", entailment_id, \"label:\", id2label[entailment_id])\nprint(\"contradiction_id:\", contradiction_id, \"label:\", id2label[contradiction_id])\n",
    "ds = vault.query_item_content(\"glue_mrpc_validation\")\nds = Dataset.from_list(ds)\nprint(ds)\nprint(ds[0])\n\nsent1 = ds[\"sentence1\"]\nsent2 = ds[\"sentence2\"]\ny_true = np.array(ds[\"label\"])\n\nprint(\"num_examples:\", len(y_true))\nprint(\"positive_rate:\", float(y_true.mean()))\n",
    "batch_size = 64\nmargin_12_all = []\nmargin_21_all = []\nmin_margin_all = []\n\nwith torch.no_grad():\n    for i in tqdm(range(0, len(ds), batch_size)):\n        batch_s1 = sent1[i:i + batch_size]\n        batch_s2 = sent2[i:i + batch_size]\n\n        enc_12 = tokenizer(\n            batch_s1,\n            batch_s2,\n            padding=True,\n            truncation=True,\n            max_length=128,\n            return_tensors=\"pt\",\n        )\n        enc_21 = tokenizer(\n            batch_s2,\n            batch_s1,\n            padding=True,\n            truncation=True,\n            max_length=128,\n            return_tensors=\"pt\",\n        )\n\n        enc_12 = {k: v.to(device) for k, v in enc_12.items()}\n        enc_21 = {k: v.to(device) for k, v in enc_21.items()}\n\n        logits_12 = model(**enc_12).logits\n        logits_21 = model(**enc_21).logits\n\n        margin_12 = (logits_12[:, entailment_id] - logits_12[:, contradiction_id]).detach().cpu().numpy()\n        margin_21 = (logits_21[:, entailment_id] - logits_21[:, contradiction_id]).detach().cpu().numpy()\n        min_margin = np.minimum(margin_12, margin_21)\n\n        margin_12_all.extend(margin_12.tolist())\n        margin_21_all.extend(margin_21.tolist())\n        min_margin_all.extend(min_margin.tolist())\n\nmargin_12_all = np.array(margin_12_all)\nmargin_21_all = np.array(margin_21_all)\nmin_margin_all = np.array(min_margin_all)\ny_pred = (min_margin_all > 0).astype(int)\n\nprint(\"done\")\nprint(\"predicted_positive_rate:\", float(y_pred.mean()))\n",
    "vault.create_record_list(\"mrpc_min_margin_prediction\", column_names=[\"prediction\", \"min_margin\"])\n\nfor i in range(len(y_pred)):\n    vault.append_record(\"mrpc_min_margin_prediction\", \n                        {\n                            \"prediction\": int(y_pred[i]),\n                            \"min_margin\": float(min_margin_all[i]),\n                        },\n                       input_items = {\n                           \"glue_mrpc_validation\": [i, i + 1],\n                       }\n                       )\n\ndescription = \"mrpc_min_margin_prediction is an example-level prediction dataset derived from the GLUE MRPC validation split. For each sentence pair in glue_mrpc_validation, it stores the binary paraphrase prediction produced by a zero-shot NLI model (typeform/distilbert-base-uncased-mnli) and the confidence score used to make that prediction.\\n\\nEach record corresponds to one MRPC validation example and has two fields: prediction, an integer label where 1 indicates paraphrase and 0 indicates not_paraphrase; and min_margin, a float equal to the minimum of the entailment-versus-contradiction logit margins computed in both input directions, sentence1\\u2192sentence2 and sentence2\\u2192sentence1. The prediction is defined as 1 when min_margin > 0, otherwise 0.\\n\\nIn this workflow, this dataset serves as the per-example output of the min-direction-margin inference step. It is used as the input to downstream evaluation and summarization, including accuracy, F1, classification report generation, and error analysis.\"\nembedding = get_embeddings(description)\nvault.create_description(\"mrpc_min_margin_prediction\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"dataset_type\": \"model predictions\", \"source_dataset\": \"glue_mrpc_validation\", \"source\": \"glue/mrpc\", \"split\": \"validation\", \"size\": \"408\", \"input_type\": \"sentence pair\", \"output_type\": \"binary prediction with confidence margin\", \"output_columns\": \"prediction,min_margin\", \"model\": \"typeform/distilbert-base-uncased-mnli\", \"method\": \"minimum directional entailment-contradiction margin\", \"label_space\": \"0=not_paraphrase,1=paraphrase\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"mrpc_min_margin_prediction\", cat, embedding, prop)",
    "acc = accuracy_score(y_true, y_pred)\nf1 = f1_score(y_true, y_pred)\nreport = classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"])\nprint({\"accuracy\": acc, \"f1\": f1})\nprint(classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"]))\n",
    "for i in range(5):\n    print(\"=\" * 80)\n    print(\"sentence1:\", sent1[i])\n    print(\"sentence2:\", sent2[i])\n    print(\"margin_12:\", float(margin_12_all[i]))\n    print(\"margin_21:\", float(margin_21_all[i]))\n    print(\"min_margin:\", float(min_margin_all[i]))\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]))\n",
    "mistakes = np.where(y_true != y_pred)[0][:10]\nprint(\"num_errors:\", int((y_true != y_pred).sum()))\n\nfor i in mistakes:\n    print(\"=\" * 80)\n    print(\"idx:\", int(i))\n    print(\"sentence1:\", sent1[i])\n    print(\"sentence2:\", sent2[i])\n    print(\"margin_12:\", float(margin_12_all[i]))\n    print(\"margin_21:\", float(margin_21_all[i]))\n    print(\"min_margin:\", float(min_margin_all[i]))\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]))\n",
    "vault.create_record_list(\"min_direction_margin_mrpc_summary\", column_names=[\"accuracy\", \"f1\", \"classification_report\"])\n\n\nsummary = {\n    \"accuracy\": float(acc),\n    \"f1\": float(f1),\n    \"classification_report\": str(report)\n}\n\nvault.append_record(\"min_direction_margin_mrpc_summary\", summary,\n                    input_items = {\n                        \"glue_mrpc_validation\": [0, len(ds)],\n                        \"mrpc_min_margin_prediction\": [0, len(ds)]\n                    })\n\nsummary\n\ndescription = \"Summary dataset for the min_direction_margin_mrpc workflow. It contains experiment-level evaluation results for paraphrase detection on the GLUE MRPC validation set, where predictions are made by scoring each sentence pair in both directions with an MNLI model and using the minimum entailment-minus-contradiction margin as the decision signal. The dataset has one record with three fields: accuracy (float), f1 (float), and classification_report (string). Its role is to store the final aggregated performance summary derived from the source validation examples and the per-example prediction dataset mrpc_min_margin_prediction, so future users can quickly inspect the overall outcome of this notebook without recomputing metrics.\"\nembedding = get_embeddings(description)\nvault.create_description(\"min_direction_margin_mrpc_summary\", description, embedding)\n\nproperties = {\"artifact_type\": \"evaluation summary\", \"task\": \"paraphrase detection\", \"benchmark\": \"GLUE\", \"dataset\": \"MRPC\", \"source\": \"glue_mrpc_validation\", \"split\": \"validation\", \"domain\": \"news\", \"evaluated_examples\": \"408\", \"label_space\": \"binary\", \"model\": \"typeform/distilbert-base-uncased-mnli\", \"inference_method\": \"min directional entailment-contradiction margin\", \"prediction_source\": \"mrpc_min_margin_prediction\", \"metrics\": \"accuracy,f1,classification_report\", \"process\": \"min_direction_margin_mrpc\", \"framework\": \"transformers\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"min_direction_margin_mrpc_summary\", cat, embedding, prop)\n\n",
    "description = \"This notebook evaluates a directional-margin approach to paraphrase detection on the GLUE MRPC validation set. It loads sentence pairs and labels from TableVault, runs the typeform/distilbert-base-uncased-mnli sequence classification model as an NLI-based paraphrase scorer in both directions (sentence1\\u2192sentence2 and sentence2\\u2192sentence1), computes the entailment-minus-contradiction logit margin for each direction, and uses the minimum of the two margins as the final paraphrase score; pairs with positive minimum margin are predicted as paraphrases. The workflow then stores per-example predictions and margins in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, inspects sample predictions and errors, and saves a summary record and notebook-level metadata back to TableVault.\" # description of whole notebook\nembedding = get_embeddings(description)\nvault.create_description(\"min_direction_margin_mrpc\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"method\": \"bidirectional NLI min-direction margin\", \"dataset\": \"glue/mrpc validation\", \"model\": \"typeform/distilbert-base-uncased-mnli\", \"model_family\": \"DistilBERT\", \"inference_type\": \"zero-shot sequence pair classification\", \"label_rule\": \"predict paraphrase when min(entailment-contradiction margin in both directions) > 0\", \"evaluation\": \"accuracy, f1-score, classification report\", \"frameworks\": \"PyTorch, Transformers, Hugging Face Datasets, scikit-learn\", \"storage\": \"TableVault\", \"metadata_embeddings\": \"OpenAI text-embedding-3-large\", \"process_name\": \"min_direction_margin_mrpc\"} #e.g. model: distilbert-base-uncased-MRPC\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"min_direction_margin_mrpc\", cat, embedding, prop)"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 20225 | 157 | 133 | 18655 | 3.533s | 0.023s |

---

## Turn 11 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c337b8481959068b8ff20552965`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_q1tXfeGs0lcTlaIQTNBQh8RI",
    "output": "{\"ok\": true, \"result\": [\"import torch\\nimport numpy as np\\nfrom datasets import Dataset\\nfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\\nfrom tqdm.auto import tqdm\\n\\ndevice = torch.device(\\\"mps\\\" if torch.backends.mps.is_available() else \\\"cpu\\\")\\nprint(\\\"device:\\\", device)\\n\", \"def get_embeddings(text):\\n    return client.embeddings.create(\\n            input=text,\\n            model=\\\"text-embedding-3-large\\\"\\n        ).data[0].embedding\", \"model_name = \\\"typeform/distilbert-base-uncased-mnli\\\"\\n\\ntokenizer = AutoTokenizer.from_pretrained(model_name)\\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\\nmodel.eval()\\n\\nid2label = {int(k): v for k, v in model.config.id2label.items()}\\nentailment_id = next(i for i, label in id2label.items() if \\\"entail\\\" in label.lower())\\ncontradiction_id = next(i for i, label in id2label.items() if \\\"contrad\\\" in label.lower())\\n\\nprint(\\\"model:\\\", model_name)\\nprint(\\\"id2label:\\\", id2label)\\nprint(\\\"entailment_id:\\\", entailment_id, \\\"label:\\\", id2label[entailment_id])\\nprint(\\\"contradiction_id:\\\", contradiction_id, \\\"label:\\\", id2label[contradiction_id])\\n\", \"ds = vault.query_item_content(\\\"glue_mrpc_validation\\\")\\nds = Dataset.from_list(ds)\\nprint(ds)\\nprint(ds[0])\\n\\nsent1 = ds[\\\"sentence1\\\"]\\nsent2 = ds[\\\"sentence2\\\"]\\ny_true = np.array(ds[\\\"label\\\"])\\n\\nprint(\\\"num_examples:\\\", len(y_true))\\nprint(\\\"positive_rate:\\\", float(y_true.mean()))\\n\", \"batch_size = 64\\nmargin_12_all = []\\nmargin_21_all = []\\nmin_margin_all = []\\n\\nwith torch.no_grad():\\n    for i in tqdm(range(0, len(ds), batch_size)):\\n        batch_s1 = sent1[i:i + batch_size]\\n        batch_s2 = sent2[i:i + batch_size]\\n\\n        enc_12 = tokenizer(\\n            batch_s1,\\n            batch_s2,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc_21 = tokenizer(\\n            batch_s2,\\n            batch_s1,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n\\n        enc_12 = {k: v.to(device) for k, v in enc_12.items()}\\n        enc_21 = {k: v.to(device) for k, v in enc_21.items()}\\n\\n        logits_12 = model(**enc_12).logits\\n        logits_21 = model(**enc_21).logits\\n\\n        margin_12 = (logits_12[:, entailment_id] - logits_12[:, contradiction_id]).detach().cpu().numpy()\\n        margin_21 = (logits_21[:, entailment_id] - logits_21[:, contradiction_id]).detach().cpu().numpy()\\n        min_margin = np.minimum(margin_12, margin_21)\\n\\n        margin_12_all.extend(margin_12.tolist())\\n        margin_21_all.extend(margin_21.tolist())\\n        min_margin_all.extend(min_margin.tolist())\\n\\nmargin_12_all = np.array(margin_12_all)\\nmargin_21_all = np.array(margin_21_all)\\nmin_margin_all = np.array(min_margin_all)\\ny_pred = (min_margin_all > 0).astype(int)\\n\\nprint(\\\"done\\\")\\nprint(\\\"predicted_positive_rate:\\\", float(y_pred.mean()))\\n\", \"vault.create_record_list(\\\"mrpc_min_margin_prediction\\\", column_names=[\\\"prediction\\\", \\\"min_margin\\\"])\\n\\nfor i in range(len(y_pred)):\\n    vault.append_record(\\\"mrpc_min_margin_prediction\\\", \\n                        {\\n                            \\\"prediction\\\": int(y_pred[i]),\\n                            \\\"min_margin\\\": float(min_margin_all[i]),\\n                        },\\n                       input_items = {\\n                           \\\"glue_mrpc_validation\\\": [i, i + 1],\\n                       }\\n                       )\\n\\ndescription = \\\"mrpc_min_margin_prediction is an example-level prediction dataset derived from the GLUE MRPC validation split. For each sentence pair in glue_mrpc_validation, it stores the binary paraphrase prediction produced by a zero-shot NLI model (typeform/distilbert-base-uncased-mnli) and the confidence score used to make that prediction.\\\\n\\\\nEach record corresponds to one MRPC validation example and has two fields: prediction, an integer label where 1 indicates paraphrase and 0 indicates not_paraphrase; and min_margin, a float equal to the minimum of the entailment-versus-contradiction logit margins computed in both input directions, sentence1\\\\u2192sentence2 and sentence2\\\\u2192sentence1. The prediction is defined as 1 when min_margin > 0, otherwise 0.\\\\n\\\\nIn this workflow, this dataset serves as the per-example output of the min-direction-margin inference step. It is used as the input to downstream evaluation and summarization, including accuracy, F1, classification report generation, and error analysis.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"mrpc_min_margin_prediction\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_type\\\": \\\"model predictions\\\", \\\"source_dataset\\\": \\\"glue_mrpc_validation\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"input_type\\\": \\\"sentence pair\\\", \\\"output_type\\\": \\\"binary prediction with confidence margin\\\", \\\"output_columns\\\": \\\"prediction,min_margin\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"method\\\": \\\"minimum directional entailment-contradiction margin\\\", \\\"label_space\\\": \\\"0=not_paraphrase,1=paraphrase\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"mrpc_min_margin_prediction\\\", cat, embedding, prop)\", \"acc = accuracy_score(y_true, y_pred)\\nf1 = f1_score(y_true, y_pred)\\nreport = classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"])\\nprint({\\\"accuracy\\\": acc, \\\"f1\\\": f1})\\nprint(classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"]))\\n\", \"for i in range(5):\\n    print(\\\"=\\\" * 80)\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"margin_12:\\\", float(margin_12_all[i]))\\n    print(\\\"margin_21:\\\", float(margin_21_all[i]))\\n    print(\\\"min_margin:\\\", float(min_margin_all[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n\", \"mistakes = np.where(y_true != y_pred)[0][:10]\\nprint(\\\"num_errors:\\\", int((y_true != y_pred).sum()))\\n\\nfor i in mistakes:\\n    print(\\\"=\\\" * 80)\\n    print(\\\"idx:\\\", int(i))\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"margin_12:\\\", float(margin_12_all[i]))\\n    print(\\\"margin_21:\\\", float(margin_21_all[i]))\\n    print(\\\"min_margin:\\\", float(min_margin_all[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n\", \"vault.create_record_list(\\\"min_direction_margin_mrpc_summary\\\", column_names=[\\\"accuracy\\\", \\\"f1\\\", \\\"classification_report\\\"])\\n\\n\\nsummary = {\\n    \\\"accuracy\\\": float(acc),\\n    \\\"f1\\\": float(f1),\\n    \\\"classification_report\\\": str(report)\\n}\\n\\nvault.append_record(\\\"min_direction_margin_mrpc_summary\\\", summary,\\n                    input_items = {\\n                        \\\"glue_mrpc_validation\\\": [0, len(ds)],\\n                        \\\"mrpc_min_margin_prediction\\\": [0, len(ds)]\\n                    })\\n\\nsummary\\n\\ndescription = \\\"Summary dataset for the min_direction_margin_mrpc workflow. It contains experiment-level evaluation results for paraphrase detection on the GLUE MRPC validation set, where predictions are made by scoring each sentence pair in both directions with an MNLI model and using the minimum entailment-minus-contradiction margin as the decision signal. The dataset has one record with three fields: accuracy (float), f1 (float), and classification_report (string). Its role is to store the final aggregated performance summary derived from the source validation examples and the per-example prediction dataset mrpc_min_margin_prediction, so future users can quickly inspect the overall outcome of this notebook without recomputing metrics.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"min_direction_margin_mrpc_summary\\\", description, embedding)\\n\\nproperties = {\\\"artifact_type\\\": \\\"evaluation summary\\\", \\\"task\\\": \\\"paraphrase detection\\\", \\\"benchmark\\\": \\\"GLUE\\\", \\\"dataset\\\": \\\"MRPC\\\", \\\"source\\\": \\\"glue_mrpc_validation\\\", \\\"split\\\": \\\"validation\\\", \\\"domain\\\": \\\"news\\\", \\\"evaluated_examples\\\": \\\"408\\\", \\\"label_space\\\": \\\"binary\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"inference_method\\\": \\\"min directional entailment-contradiction margin\\\", \\\"prediction_source\\\": \\\"mrpc_min_margin_prediction\\\", \\\"metrics\\\": \\\"accuracy,f1,classification_report\\\", \\\"process\\\": \\\"min_direction_margin_mrpc\\\", \\\"framework\\\": \\\"transformers\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"min_direction_margin_mrpc_summary\\\", cat, embedding, prop)\\n\\n\", \"description = \\\"This notebook evaluates a directional-margin approach to paraphrase detection on the GLUE MRPC validation set. It loads sentence pairs and labels from TableVault, runs the typeform/distilbert-base-uncased-mnli sequence classification model as an NLI-based paraphrase scorer in both directions (sentence1\\\\u2192sentence2 and sentence2\\\\u2192sentence1), computes the entailment-minus-contradiction logit margin for each direction, and uses the minimum of the two margins as the final paraphrase score; pairs with positive minimum margin are predicted as paraphrases. The workflow then stores per-example predictions and margins in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, inspects sample predictions and errors, and saves a summary record and notebook-level metadata back to TableVault.\\\" # description of whole notebook\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"min_direction_margin_mrpc\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"method\\\": \\\"bidirectional NLI min-direction margin\\\", \\\"dataset\\\": \\\"glue/mrpc validation\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"model_family\\\": \\\"DistilBERT\\\", \\\"inference_type\\\": \\\"zero-shot sequence pair classification\\\", \\\"label_rule\\\": \\\"predict paraphrase when min(entailment-contradiction margin in both directions) > 0\\\", \\\"evaluation\\\": \\\"accuracy, f1-score, classification report\\\", \\\"frameworks\\\": \\\"PyTorch, Transformers, Hugging Face Datasets, scikit-learn\\\", \\\"storage\\\": \\\"TableVault\\\", \\\"metadata_embeddings\\\": \\\"OpenAI text-embedding-3-large\\\", \\\"process_name\\\": \\\"min_direction_margin_mrpc\\\"} #e.g. model: distilbert-base-uncased-MRPC\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"min_direction_margin_mrpc\\\", cat, embedding, prop)\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c337b8481959068b8ff20552965`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_PJpvjCbd6Nd9U8tcGmsBNXco",
    "arguments": {
      "item_name": "min_direction_margin_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_PJpvjCbd6Nd9U8tcGmsBNXco`

**Arguments:**
```json
{
  "item_name": "min_direction_margin_mrpc_summary",
  "start_position": 0,
  "end_position": 5
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    {
      "accuracy": 0.5857843137254902,
      "f1": 0.5888077858880778,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.43      0.91      0.58       129\n    paraphrase       0.92      0.43      0.59       279\n\n      accuracy                           0.59       408\n     macro avg       0.67      0.67      0.59       408\n  weighted avg       0.76      0.59      0.59       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 23102 | 61 | 25 | 21532 | 1.923s | 0.021s |

---

## Turn 12 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c356dbc81958f1a6508af0074df`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_PJpvjCbd6Nd9U8tcGmsBNXco",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.5857843137254902, \"f1\": 0.5888077858880778, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.43      0.91      0.58       129\\n    paraphrase       0.92      0.43      0.59       279\\n\\n      accuracy                           0.59       408\\n     macro avg       0.67      0.67      0.59       408\\n  weighted avg       0.76      0.59      0.59       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c356dbc81958f1a6508af0074df`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "get_code",
    "call_id": "call_eAMemfUfEDZdMpJnaCYOTIZ1",
    "arguments": {
      "name": "consensus_then_avg_margin_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_eAMemfUfEDZdMpJnaCYOTIZ1`

**Arguments:**
```json
{
  "name": "consensus_then_avg_margin_mrpc"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "def get_embeddings(text):\n    return client.embeddings.create(\n            input=text,\n            model=\"text-embedding-3-large\"\n        ).data[0].embedding",
    "import torch\nimport numpy as np\nfrom datasets import Dataset\nfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\nfrom tqdm.auto import tqdm\n\ndevice = torch.device(\"mps\" if torch.backends.mps.is_available() else \"cpu\")\nprint(\"device:\", device)\n",
    "model_name = \"typeform/distilbert-base-uncased-mnli\"\n\ntokenizer = AutoTokenizer.from_pretrained(model_name)\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\nmodel.eval()\n\nid2label = {int(k): v for k, v in model.config.id2label.items()}\nlabel_lookup = {idx: str(label).lower().strip() for idx, label in id2label.items()}\n\ndef find_label_id(target):\n    matches = [idx for idx, label in label_lookup.items() if label == target]\n    if not matches:\n        raise ValueError(f\"Could not find label id for {target!r} in {label_lookup}\")\n    return matches[0]\n\ncontradiction_id = find_label_id(\"contradiction\")\nentailment_id = find_label_id(\"entailment\")\n\nprint(\"model:\", model_name)\nprint(\"id2label:\", id2label)\nprint(\"contradiction_id:\", contradiction_id)\nprint(\"entailment_id:\", entailment_id)\n",
    "ds = vault.query_item_content(\"glue_mrpc_validation\")\nds = Dataset.from_list(ds)\nprint(ds)\nprint(ds[0])\n\nsent1 = ds[\"sentence1\"]\nsent2 = ds[\"sentence2\"]\ny_true = np.array(ds[\"label\"])\n\nprint(\"num_examples:\", len(y_true))\nprint(\"positive_rate:\", float(y_true.mean()))\n",
    "batch_size = 64\nlogits_12_parts = []\nlogits_21_parts = []\nargmax_12_parts = []\nargmax_21_parts = []\n\nwith torch.no_grad():\n    for i in tqdm(range(0, len(ds), batch_size)):\n        batch_s1 = sent1[i:i + batch_size]\n        batch_s2 = sent2[i:i + batch_size]\n\n        enc_12 = tokenizer(\n            batch_s1,\n            batch_s2,\n            padding=True,\n            truncation=True,\n            max_length=128,\n            return_tensors=\"pt\",\n        )\n        enc_21 = tokenizer(\n            batch_s2,\n            batch_s1,\n            padding=True,\n            truncation=True,\n            max_length=128,\n            return_tensors=\"pt\",\n        )\n\n        enc_12 = {k: v.to(device) for k, v in enc_12.items()}\n        enc_21 = {k: v.to(device) for k, v in enc_21.items()}\n\n        logits_12 = model(**enc_12).logits\n        logits_21 = model(**enc_21).logits\n\n        logits_12_parts.append(logits_12.cpu().numpy())\n        logits_21_parts.append(logits_21.cpu().numpy())\n        argmax_12_parts.append(torch.argmax(logits_12, dim=-1).cpu().numpy())\n        argmax_21_parts.append(torch.argmax(logits_21, dim=-1).cpu().numpy())\n\nlogits_12 = np.concatenate(logits_12_parts, axis=0)\nlogits_21 = np.concatenate(logits_21_parts, axis=0)\nargmax_12 = np.concatenate(argmax_12_parts, axis=0)\nargmax_21 = np.concatenate(argmax_21_parts, axis=0)\n\nprint(\"done\")\nprint(\"logits_12 shape:\", logits_12.shape)\nprint(\"logits_21 shape:\", logits_21.shape)\n",
    "margin_12 = logits_12[:, entailment_id] - logits_12[:, contradiction_id]\nmargin_21 = logits_21[:, entailment_id] - logits_21[:, contradiction_id]\navg_margin = (margin_12 + margin_21) / 2.0\n\ngate = (argmax_12 != contradiction_id) & (argmax_21 != contradiction_id)\ny_pred = ((avg_margin > 0.0) & gate).astype(int)\n\n",
    "vault.create_record_list(\"mrpc_gate_margin_prediction\", column_names=[\"prediction\", \"margin_12\", \"margin_21\", \"gate\"])\n\nfor i in range(len(y_pred)):\n    vault.append_record(\"mrpc_gate_margin_prediction\", \n                        {\n                            \"prediction\": int(y_pred[i]),\n                            \"margin_12\": float(margin_12[i]),\n                            \"margin_21\": float(margin_21[i]),\n                            \"gate\": int(gate[i]),\n                        },\n                       input_items = {\n                           \"glue_mrpc_validation\": [i, i + 1],\n                       }\n                       )\n\ndescription = \"mrpc_gate_margin_prediction is a per-example prediction dataset derived from the GLUE MRPC validation split. For each validation pair (sentence1, sentence2), the notebook runs the NLI model typeform/distilbert-base-uncased-mnli in both input orders, sentence1\\u2192sentence2 and sentence2\\u2192sentence1, and stores the resulting decision signals used for paraphrase classification. The dataset has four fields: prediction (final binary paraphrase prediction, 1 for paraphrase and 0 for not paraphrase), margin_12 (entailment logit minus contradiction logit for sentence1 paired with sentence2), margin_21 (the same margin for the reversed order), and gate (boolean flag that is true only when neither direction\\u2019s argmax label is contradiction). The final prediction is produced by requiring gate = true and the average of margin_12 and margin_21 to be greater than 0. This dataset serves as the main intermediate output of the workflow: it preserves the model\\u2019s directional margin scores and final gated prediction for each MRPC example, and it is then used to compute the summary accuracy, F1, and classification report.\"\nembedding = get_embeddings(description)\nvault.create_description(\"mrpc_gate_margin_prediction\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"dataset_type\": \"model predictions\", \"granularity\": \"pair-level\", \"source\": \"glue/mrpc\", \"input_dataset\": \"glue_mrpc_validation\", \"split\": \"validation\", \"size\": \"408\", \"domain\": \"news\", \"model\": \"typeform/distilbert-base-uncased-mnli\", \"inference_strategy\": \"bidirectional consensus then average entailment-contradiction margin\", \"input_fields\": \"sentence1,sentence2\", \"output_fields\": \"prediction,margin_12,margin_21,gate\", \"label_space\": \"binary\", \"labels\": \"not_paraphrase,paraphrase\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"mrpc_gate_margin_prediction\", cat, embedding, prop)",
    "acc = accuracy_score(y_true, y_pred)\nf1 = f1_score(y_true, y_pred)\nreport = classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"])\nprint({\"accuracy\": acc, \"f1\": f1})\nprint(classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"]))\n",
    "for i in range(5):\n    print(\"=\" * 100)\n    print(\"sentence1:\", sent1[i])\n    print(\"sentence2:\", sent2[i])\n    print(\"dir_12_argmax:\", int(argmax_12[i]), id2label[int(argmax_12[i])])\n    print(\"dir_21_argmax:\", int(argmax_21[i]), id2label[int(argmax_21[i])])\n    print(\"margin_12:\", float(margin_12[i]))\n    print(\"margin_21:\", float(margin_21[i]))\n    print(\"gate:\", bool(gate[i]))\n    print(\"avg_margin:\", float(avg_margin[i]))\n    print(\"true:\", int(y_true[i]))\n    print(\"pred:\", int(y_pred[i]))\n",
    "mistakes = np.where(y_true != y_pred)[0][:10]\nprint(\"num_errors:\", int((y_true != y_pred).sum()))\n\nfor i in mistakes:\n    print(\"=\" * 100)\n    print(\"idx:\", int(i))\n    print(\"sentence1:\", sent1[i])\n    print(\"sentence2:\", sent2[i])\n    print(\"dir_12_argmax:\", int(argmax_12[i]), id2label[int(argmax_12[i])])\n    print(\"dir_21_argmax:\", int(argmax_21[i]), id2label[int(argmax_21[i])])\n    print(\"margin_12:\", float(margin_12[i]))\n    print(\"margin_21:\", float(margin_21[i]))\n    print(\"gate:\", bool(gate[i]))\n    print(\"avg_margin:\", float(avg_margin[i]))\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]))\n",
    "vault.create_record_list(\"consensus_then_avg_margin_mrpc_summary\", column_names=[\"accuracy\", \"f1\", \"classification_report\"])\n\n\nsummary = {\n    \"accuracy\": float(acc),\n    \"f1\": float(f1),\n    \"classification_report\": str(report)\n}\n\nvault.append_record(\"consensus_then_avg_margin_mrpc_summary\", summary,\n                    input_items = {\n                        \"glue_mrpc_validation\": [0, len(ds)],\n                        \"mrpc_gate_margin_prediction\": [0, len(ds)]\n                    })\n\nsummary\n\ndescription = \"Summary dataset for the MRPC validation evaluation of the consensus-then-average-margin inference method. It contains aggregate performance results computed by comparing the generated paraphrase predictions against the true labels from glue_mrpc_validation, using prediction records stored in mrpc_gate_margin_prediction. The dataset is structured as a record list with columns: accuracy (float), f1 (float), and classification_report (string containing the full per-class sklearn classification report for not_paraphrase and paraphrase). In this workflow, it serves as the final evaluation artifact for the notebook, linking the full MRPC validation set and the per-example prediction dataset to a compact summary of model performance.\"\nembedding = get_embeddings(description)\nvault.create_description(\"consensus_then_avg_margin_mrpc_summary\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"dataset_role\": \"evaluation summary\", \"source\": \"glue/mrpc\", \"split\": \"validation\", \"size\": \"408\", \"model\": \"typeform/distilbert-base-uncased-mnli\", \"method\": \"consensus then average entailment-contradiction margin\", \"input_type\": \"sentence pair\", \"output_type\": \"aggregate metrics\", \"metrics\": \"accuracy,f1,classification_report\", \"prediction_source\": \"mrpc_gate_margin_prediction\", \"domain\": \"news\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"consensus_then_avg_margin_mrpc_summary\", cat, embedding, prop)\n\n",
    "description = \"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli natural language inference model. For each sentence pair, it runs inference in both directions (sentence1\\u2192sentence2 and sentence2\\u2192sentence1), computes an entailment-versus-contradiction margin for each direction, averages the two margins, and predicts paraphrase only when neither direction is classified as contradiction and the average margin is positive. The notebook stores per-example predictions, directional margins, and gate decisions in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, logs error analysis examples, and saves dataset-, prediction-, summary-, and notebook-level metadata and embeddings for later retrieval and documentation.\" # description of whole notebook\nembedding = get_embeddings(description)\nvault.create_description(\"consensus_then_avg_margin_mrpc\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"dataset\": \"glue/mrpc\", \"dataset_split\": \"validation\", \"model\": \"typeform/distilbert-base-uncased-mnli\", \"model_type\": \"NLI sequence classification\", \"approach\": \"zero-shot paraphrase detection via NLI\", \"inference_strategy\": \"bidirectional sentence-pair scoring\", \"decision_rule\": \"consensus non-contradiction gate with averaged entailment-contradiction margin\", \"frameworks\": \"transformers, pytorch, datasets, sklearn\", \"metrics\": \"accuracy, f1-score, classification_report\", \"storage\": \"TableVault with ArangoDB\", \"embedding_model\": \"text-embedding-3-large\", \"process_name\": \"consensus_then_avg_margin_mrpc\"} #e.g. model: distilbert-base-uncased-MRPC\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"consensus_then_avg_margin_mrpc\", cat, embedding, prop)"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 23329 | 49 | 23 | 21759 | 1.718s | 0.015s |

---

## Turn 13 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c37266081958c7f53de013c6bd7`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_eAMemfUfEDZdMpJnaCYOTIZ1",
    "output": "{\"ok\": true, \"result\": [\"def get_embeddings(text):\\n    return client.embeddings.create(\\n            input=text,\\n            model=\\\"text-embedding-3-large\\\"\\n        ).data[0].embedding\", \"import torch\\nimport numpy as np\\nfrom datasets import Dataset\\nfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\\nfrom tqdm.auto import tqdm\\n\\ndevice = torch.device(\\\"mps\\\" if torch.backends.mps.is_available() else \\\"cpu\\\")\\nprint(\\\"device:\\\", device)\\n\", \"model_name = \\\"typeform/distilbert-base-uncased-mnli\\\"\\n\\ntokenizer = AutoTokenizer.from_pretrained(model_name)\\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\\nmodel.eval()\\n\\nid2label = {int(k): v for k, v in model.config.id2label.items()}\\nlabel_lookup = {idx: str(label).lower().strip() for idx, label in id2label.items()}\\n\\ndef find_label_id(target):\\n    matches = [idx for idx, label in label_lookup.items() if label == target]\\n    if not matches:\\n        raise ValueError(f\\\"Could not find label id for {target!r} in {label_lookup}\\\")\\n    return matches[0]\\n\\ncontradiction_id = find_label_id(\\\"contradiction\\\")\\nentailment_id = find_label_id(\\\"entailment\\\")\\n\\nprint(\\\"model:\\\", model_name)\\nprint(\\\"id2label:\\\", id2label)\\nprint(\\\"contradiction_id:\\\", contradiction_id)\\nprint(\\\"entailment_id:\\\", entailment_id)\\n\", \"ds = vault.query_item_content(\\\"glue_mrpc_validation\\\")\\nds = Dataset.from_list(ds)\\nprint(ds)\\nprint(ds[0])\\n\\nsent1 = ds[\\\"sentence1\\\"]\\nsent2 = ds[\\\"sentence2\\\"]\\ny_true = np.array(ds[\\\"label\\\"])\\n\\nprint(\\\"num_examples:\\\", len(y_true))\\nprint(\\\"positive_rate:\\\", float(y_true.mean()))\\n\", \"batch_size = 64\\nlogits_12_parts = []\\nlogits_21_parts = []\\nargmax_12_parts = []\\nargmax_21_parts = []\\n\\nwith torch.no_grad():\\n    for i in tqdm(range(0, len(ds), batch_size)):\\n        batch_s1 = sent1[i:i + batch_size]\\n        batch_s2 = sent2[i:i + batch_size]\\n\\n        enc_12 = tokenizer(\\n            batch_s1,\\n            batch_s2,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc_21 = tokenizer(\\n            batch_s2,\\n            batch_s1,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n\\n        enc_12 = {k: v.to(device) for k, v in enc_12.items()}\\n        enc_21 = {k: v.to(device) for k, v in enc_21.items()}\\n\\n        logits_12 = model(**enc_12).logits\\n        logits_21 = model(**enc_21).logits\\n\\n        logits_12_parts.append(logits_12.cpu().numpy())\\n        logits_21_parts.append(logits_21.cpu().numpy())\\n        argmax_12_parts.append(torch.argmax(logits_12, dim=-1).cpu().numpy())\\n        argmax_21_parts.append(torch.argmax(logits_21, dim=-1).cpu().numpy())\\n\\nlogits_12 = np.concatenate(logits_12_parts, axis=0)\\nlogits_21 = np.concatenate(logits_21_parts, axis=0)\\nargmax_12 = np.concatenate(argmax_12_parts, axis=0)\\nargmax_21 = np.concatenate(argmax_21_parts, axis=0)\\n\\nprint(\\\"done\\\")\\nprint(\\\"logits_12 shape:\\\", logits_12.shape)\\nprint(\\\"logits_21 shape:\\\", logits_21.shape)\\n\", \"margin_12 = logits_12[:, entailment_id] - logits_12[:, contradiction_id]\\nmargin_21 = logits_21[:, entailment_id] - logits_21[:, contradiction_id]\\navg_margin = (margin_12 + margin_21) / 2.0\\n\\ngate = (argmax_12 != contradiction_id) & (argmax_21 != contradiction_id)\\ny_pred = ((avg_margin > 0.0) & gate).astype(int)\\n\\n\", \"vault.create_record_list(\\\"mrpc_gate_margin_prediction\\\", column_names=[\\\"prediction\\\", \\\"margin_12\\\", \\\"margin_21\\\", \\\"gate\\\"])\\n\\nfor i in range(len(y_pred)):\\n    vault.append_record(\\\"mrpc_gate_margin_prediction\\\", \\n                        {\\n                            \\\"prediction\\\": int(y_pred[i]),\\n                            \\\"margin_12\\\": float(margin_12[i]),\\n                            \\\"margin_21\\\": float(margin_21[i]),\\n                            \\\"gate\\\": int(gate[i]),\\n                        },\\n                       input_items = {\\n                           \\\"glue_mrpc_validation\\\": [i, i + 1],\\n                       }\\n                       )\\n\\ndescription = \\\"mrpc_gate_margin_prediction is a per-example prediction dataset derived from the GLUE MRPC validation split. For each validation pair (sentence1, sentence2), the notebook runs the NLI model typeform/distilbert-base-uncased-mnli in both input orders, sentence1\\\\u2192sentence2 and sentence2\\\\u2192sentence1, and stores the resulting decision signals used for paraphrase classification. The dataset has four fields: prediction (final binary paraphrase prediction, 1 for paraphrase and 0 for not paraphrase), margin_12 (entailment logit minus contradiction logit for sentence1 paired with sentence2), margin_21 (the same margin for the reversed order), and gate (boolean flag that is true only when neither direction\\\\u2019s argmax label is contradiction). The final prediction is produced by requiring gate = true and the average of margin_12 and margin_21 to be greater than 0. This dataset serves as the main intermediate output of the workflow: it preserves the model\\\\u2019s directional margin scores and final gated prediction for each MRPC example, and it is then used to compute the summary accuracy, F1, and classification report.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"mrpc_gate_margin_prediction\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_type\\\": \\\"model predictions\\\", \\\"granularity\\\": \\\"pair-level\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"input_dataset\\\": \\\"glue_mrpc_validation\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"domain\\\": \\\"news\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"inference_strategy\\\": \\\"bidirectional consensus then average entailment-contradiction margin\\\", \\\"input_fields\\\": \\\"sentence1,sentence2\\\", \\\"output_fields\\\": \\\"prediction,margin_12,margin_21,gate\\\", \\\"label_space\\\": \\\"binary\\\", \\\"labels\\\": \\\"not_paraphrase,paraphrase\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"mrpc_gate_margin_prediction\\\", cat, embedding, prop)\", \"acc = accuracy_score(y_true, y_pred)\\nf1 = f1_score(y_true, y_pred)\\nreport = classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"])\\nprint({\\\"accuracy\\\": acc, \\\"f1\\\": f1})\\nprint(classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"]))\\n\", \"for i in range(5):\\n    print(\\\"=\\\" * 100)\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"dir_12_argmax:\\\", int(argmax_12[i]), id2label[int(argmax_12[i])])\\n    print(\\\"dir_21_argmax:\\\", int(argmax_21[i]), id2label[int(argmax_21[i])])\\n    print(\\\"margin_12:\\\", float(margin_12[i]))\\n    print(\\\"margin_21:\\\", float(margin_21[i]))\\n    print(\\\"gate:\\\", bool(gate[i]))\\n    print(\\\"avg_margin:\\\", float(avg_margin[i]))\\n    print(\\\"true:\\\", int(y_true[i]))\\n    print(\\\"pred:\\\", int(y_pred[i]))\\n\", \"mistakes = np.where(y_true != y_pred)[0][:10]\\nprint(\\\"num_errors:\\\", int((y_true != y_pred).sum()))\\n\\nfor i in mistakes:\\n    print(\\\"=\\\" * 100)\\n    print(\\\"idx:\\\", int(i))\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"dir_12_argmax:\\\", int(argmax_12[i]), id2label[int(argmax_12[i])])\\n    print(\\\"dir_21_argmax:\\\", int(argmax_21[i]), id2label[int(argmax_21[i])])\\n    print(\\\"margin_12:\\\", float(margin_12[i]))\\n    print(\\\"margin_21:\\\", float(margin_21[i]))\\n    print(\\\"gate:\\\", bool(gate[i]))\\n    print(\\\"avg_margin:\\\", float(avg_margin[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n\", \"vault.create_record_list(\\\"consensus_then_avg_margin_mrpc_summary\\\", column_names=[\\\"accuracy\\\", \\\"f1\\\", \\\"classification_report\\\"])\\n\\n\\nsummary = {\\n    \\\"accuracy\\\": float(acc),\\n    \\\"f1\\\": float(f1),\\n    \\\"classification_report\\\": str(report)\\n}\\n\\nvault.append_record(\\\"consensus_then_avg_margin_mrpc_summary\\\", summary,\\n                    input_items = {\\n                        \\\"glue_mrpc_validation\\\": [0, len(ds)],\\n                        \\\"mrpc_gate_margin_prediction\\\": [0, len(ds)]\\n                    })\\n\\nsummary\\n\\ndescription = \\\"Summary dataset for the MRPC validation evaluation of the consensus-then-average-margin inference method. It contains aggregate performance results computed by comparing the generated paraphrase predictions against the true labels from glue_mrpc_validation, using prediction records stored in mrpc_gate_margin_prediction. The dataset is structured as a record list with columns: accuracy (float), f1 (float), and classification_report (string containing the full per-class sklearn classification report for not_paraphrase and paraphrase). In this workflow, it serves as the final evaluation artifact for the notebook, linking the full MRPC validation set and the per-example prediction dataset to a compact summary of model performance.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"consensus_then_avg_margin_mrpc_summary\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_role\\\": \\\"evaluation summary\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"method\\\": \\\"consensus then average entailment-contradiction margin\\\", \\\"input_type\\\": \\\"sentence pair\\\", \\\"output_type\\\": \\\"aggregate metrics\\\", \\\"metrics\\\": \\\"accuracy,f1,classification_report\\\", \\\"prediction_source\\\": \\\"mrpc_gate_margin_prediction\\\", \\\"domain\\\": \\\"news\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"consensus_then_avg_margin_mrpc_summary\\\", cat, embedding, prop)\\n\\n\", \"description = \\\"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli natural language inference model. For each sentence pair, it runs inference in both directions (sentence1\\\\u2192sentence2 and sentence2\\\\u2192sentence1), computes an entailment-versus-contradiction margin for each direction, averages the two margins, and predicts paraphrase only when neither direction is classified as contradiction and the average margin is positive. The notebook stores per-example predictions, directional margins, and gate decisions in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, logs error analysis examples, and saves dataset-, prediction-, summary-, and notebook-level metadata and embeddings for later retrieval and documentation.\\\" # description of whole notebook\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"consensus_then_avg_margin_mrpc\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset\\\": \\\"glue/mrpc\\\", \\\"dataset_split\\\": \\\"validation\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"model_type\\\": \\\"NLI sequence classification\\\", \\\"approach\\\": \\\"zero-shot paraphrase detection via NLI\\\", \\\"inference_strategy\\\": \\\"bidirectional sentence-pair scoring\\\", \\\"decision_rule\\\": \\\"consensus non-contradiction gate with averaged entailment-contradiction margin\\\", \\\"frameworks\\\": \\\"transformers, pytorch, datasets, sklearn\\\", \\\"metrics\\\": \\\"accuracy, f1-score, classification_report\\\", \\\"storage\\\": \\\"TableVault with ArangoDB\\\", \\\"embedding_model\\\": \\\"text-embedding-3-large\\\", \\\"process_name\\\": \\\"consensus_then_avg_margin_mrpc\\\"} #e.g. model: distilbert-base-uncased-MRPC\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"consensus_then_avg_margin_mrpc\\\", cat, embedding, prop)\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c37266081958c7f53de013c6bd7`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "get_code",
    "call_id": "call_xJLPTmrLhvYyqlSnWqWBkVqt",
    "arguments": {
      "name": "softmax_gap_mean_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_xJLPTmrLhvYyqlSnWqWBkVqt`

**Arguments:**
```json
{
  "name": "softmax_gap_mean_mrpc"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "def get_embeddings(text):\n    return client.embeddings.create(\n            input=text,\n            model=\"text-embedding-3-large\"\n        ).data[0].embedding",
    "import torch\nimport numpy as np\nfrom datasets import Dataset\nfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\nfrom tqdm.auto import tqdm\n\ndevice = torch.device(\"mps\" if torch.backends.mps.is_available() else \"cpu\")\nprint(\"device:\", device)",
    "model_name = \"typeform/distilbert-base-uncased-mnli\"\n\ntokenizer = AutoTokenizer.from_pretrained(model_name)\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\nmodel.eval()\n\nid2label = {int(k): v for k, v in model.config.id2label.items()} if hasattr(model.config.id2label, \"items\") else dict(enumerate(model.config.id2label))\nlabel_text = {i: str(v).lower() for i, v in id2label.items()}\nentailment_id = next(i for i, v in label_text.items() if \"entail\" in v)\ncontradiction_id = next(i for i, v in label_text.items() if \"contrad\" in v)\n\nprint(\"model_name:\", model_name)\nprint(\"id2label:\", id2label)\nprint(\"entailment_id:\", entailment_id, \"contradiction_id:\", contradiction_id)",
    "ds = vault.query_item_content(\"glue_mrpc_validation\")\nds = Dataset.from_list(ds)\nprint(ds)\nprint(ds[0])\n\nsent1 = ds[\"sentence1\"]\nsent2 = ds[\"sentence2\"]\ny_true = np.array(ds[\"label\"])\n\nprint(\"num_examples:\", len(y_true))\nprint(\"positive_rate:\", float(y_true.mean()))",
    "batch_size = 64\npreds = []\ngap_12_all = []\ngap_21_all = []\navg_gap_all = []\n\nwith torch.no_grad():\n    for i in tqdm(range(0, len(ds), batch_size)):\n        batch_s1 = sent1[i:i + batch_size]\n        batch_s2 = sent2[i:i + batch_size]\n\n        enc_12 = tokenizer(\n            batch_s1,\n            batch_s2,\n            padding=True,\n            truncation=True,\n            max_length=128,\n            return_tensors=\"pt\",\n        )\n        enc_21 = tokenizer(\n            batch_s2,\n            batch_s1,\n            padding=True,\n            truncation=True,\n            max_length=128,\n            return_tensors=\"pt\",\n        )\n\n        enc_12 = {k: v.to(device) for k, v in enc_12.items()}\n        enc_21 = {k: v.to(device) for k, v in enc_21.items()}\n\n        logits_12 = model(**enc_12).logits\n        logits_21 = model(**enc_21).logits\n\n        probs_12 = torch.softmax(logits_12, dim=-1)\n        probs_21 = torch.softmax(logits_21, dim=-1)\n\n        gap_12 = probs_12[:, entailment_id] - probs_12[:, contradiction_id]\n        gap_21 = probs_21[:, entailment_id] - probs_21[:, contradiction_id]\n        avg_gap = (gap_12 + gap_21) / 2.0\n\n        batch_preds = (avg_gap > 0).long().cpu().numpy()\n\n        preds.extend(batch_preds.tolist())\n        gap_12_all.extend(gap_12.cpu().numpy().tolist())\n        gap_21_all.extend(gap_21.cpu().numpy().tolist())\n        avg_gap_all.extend(avg_gap.cpu().numpy().tolist())\n\ny_pred = np.array(preds)\ngap_12_all = np.array(gap_12_all)\ngap_21_all = np.array(gap_21_all)\navg_gap_all = np.array(avg_gap_all)\n\nprint(\"done\")",
    "vault.create_record_list(\"mrpc_mean_gap_prediction\", column_names=[\"prediction\", \"gap_12\", \"gap_21\"])\n\nfor i in range(len(y_pred)):\n    vault.append_record(\"mrpc_mean_gap_prediction\", \n                        {\n                            \"prediction\": int(y_pred[i]),\n                            \"gap_12\": float(gap_12_all[i]),\n                            \"gap_21\": float(gap_21_all[i]),\n                        },\n                       input_items = {\n                           \"glue_mrpc_validation\": [i, i + 1],\n                       }\n                       )\n\ndescription = \"Per-example prediction dataset for the GLUE MRPC validation split, generated by running the sentence pairs through the typeform/distilbert-base-uncased-mnli model in both input orders. Each record corresponds to one MRPC validation example and is linked to the matching row in glue_mrpc_validation. The dataset has three fields: prediction (binary paraphrase decision, where 1 indicates paraphrase and 0 indicates not paraphrase), gap_12 (entailment probability minus contradiction probability for sentence1\\u2192sentence2), and gap_21 (the same probability gap for sentence2\\u2192sentence1). In this workflow, it serves as the stored per-instance model output used to inspect directional confidence, compare predictions with ground-truth MRPC labels, and build the downstream summary metrics in softmax_gap_mean_mrpc_summary.\"\nembedding = get_embeddings(description)\nvault.create_description(\"mrpc_mean_gap_prediction\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"data_type\": \"model predictions\", \"prediction_type\": \"binary classification\", \"source\": \"glue/mrpc\", \"derived_from\": \"glue_mrpc_validation\", \"split\": \"validation\", \"size\": \"408\", \"input_type\": \"sentence pair\", \"model\": \"typeform/distilbert-base-uncased-mnli\", \"method\": \"mean softmax entailment-contradiction gap over both sentence orders\", \"columns\": \"prediction,gap_12,gap_21\", \"label_space\": \"0=not_paraphrase,1=paraphrase\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"mrpc_mean_gap_prediction\", cat, embedding, prop)",
    "acc = accuracy_score(y_true, y_pred)\nf1 = f1_score(y_true, y_pred)\nreport = classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"])\nprint({\"accuracy\": acc, \"f1\": f1})\nprint(classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"]))",
    "for i in range(5):\n    print(\"=\" * 80)\n    print(\"sentence1:\", sent1[i])\n    print(\"sentence2:\", sent2[i])\n    print(\"gap_12:\", float(gap_12_all[i]))\n    print(\"gap_21:\", float(gap_21_all[i]))\n    print(\"avg_gap:\", float(avg_gap_all[i]))\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]))",
    "mistakes = np.where(y_true != y_pred)[0][:10]\nprint(\"num_errors:\", int((y_true != y_pred).sum()))\n\nfor i in mistakes:\n    print(\"=\" * 80)\n    print(\"idx:\", int(i))\n    print(\"sentence1:\", sent1[i])\n    print(\"sentence2:\", sent2[i])\n    print(\"gap_12:\", float(gap_12_all[i]))\n    print(\"gap_21:\", float(gap_21_all[i]))\n    print(\"avg_gap:\", float(avg_gap_all[i]))\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]))",
    "vault.create_record_list(\"softmax_gap_mean_mrpc_summary\", column_names=[\"accuracy\", \"f1\", \"classification_report\"])\n\n\nsummary = {\n    \"accuracy\": float(acc),\n    \"f1\": float(f1),\n    \"classification_report\": str(report)\n}\n\nvault.append_record(\"softmax_gap_mean_mrpc_summary\", summary,\n                    input_items = {\n                        \"glue_mrpc_validation\": [0, len(ds)],\n                        \"mrpc_mean_gap_prediction\": [0, len(ds)]\n                    })\n\nsummary\n\ndescription = \"Summary dataset for the MRPC validation experiment using an MNLI sequence-classification model and the mean softmax-gap decision rule. It contains a single aggregate record with three fields: accuracy (float), f1 (float), and classification_report (string). These metrics are computed by comparing ground-truth MRPC labels from glue_mrpc_validation against predictions in mrpc_mean_gap_prediction, where each prediction is based on the average of the entailment-minus-contradiction probability gap for both sentence orders (sentence1, sentence2) and (sentence2, sentence1). In this workflow, this dataset serves as the experiment-level evaluation output summarizing model performance over the full validation set.\"\nembedding = get_embeddings(description)\nvault.create_description(\"softmax_gap_mean_mrpc_summary\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"dataset_type\": \"evaluation summary\", \"benchmark\": \"GLUE\", \"source\": \"glue_mrpc_validation\", \"subset\": \"MRPC\", \"split\": \"validation\", \"size\": \"408\", \"model\": \"typeform/distilbert-base-uncased-mnli\", \"inference_method\": \"mean softmax entailment-contradiction gap over both sentence orders\", \"metrics\": \"accuracy,f1,classification_report\", \"input_prediction_dataset\": \"mrpc_mean_gap_prediction\", \"process_name\": \"softmax_gap_mean_mrpc\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"softmax_gap_mean_mrpc_summary\", cat, embedding, prop)\n\n",
    "description = \"This notebook runs a paraphrase detection experiment on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli sequence classification model in an NLI-style formulation. For each sentence pair, it scores both input orders (sentence1, sentence2) and (sentence2, sentence1), computes the softmax probability gap between entailment and contradiction for each order, averages the two gaps, and predicts paraphrase when the mean gap is greater than zero. The workflow loads the MRPC validation examples from TableVault, performs batched inference with Hugging Face Transformers and PyTorch, and stores per-example predictions and gap scores back into TableVault with lineage to the source records. It then evaluates the method with accuracy, F1, and a classification report, inspects sample predictions and errors, and saves an experiment summary plus descriptive metadata and embeddings for the prediction table, summary table, and overall notebook process.\" # description of whole notebook\nembedding = get_embeddings(description)\nvault.create_description(\"softmax_gap_mean_mrpc\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"dataset\": \"glue/mrpc\", \"dataset_split\": \"validation\", \"model\": \"typeform/distilbert-base-uncased-mnli\", \"model_family\": \"distilbert\", \"inference_type\": \"zero-shot NLI\", \"prediction_method\": \"mean entailment-contradiction softmax gap over sentence order swaps\", \"input_format\": \"sentence pair classification\", \"framework\": \"transformers, pytorch\", \"metrics\": \"accuracy, f1-score, classification report\", \"outputs\": \"per-example predictions and summary metrics\", \"tracking\": \"tablevault\", \"vector_embedding_model\": \"text-embedding-3-large\", \"llm_provider\": \"openai\"} #e.g. model: distilbert-base-uncased-MRPC\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"softmax_gap_mean_mrpc\", cat, embedding, prop)"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 26462 | 38 | 13 | 24892 | 1.621s | 0.011s |

---

## Turn 14 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c38cca8819590d59ec1a2d6e904`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_xJLPTmrLhvYyqlSnWqWBkVqt",
    "output": "{\"ok\": true, \"result\": [\"def get_embeddings(text):\\n    return client.embeddings.create(\\n            input=text,\\n            model=\\\"text-embedding-3-large\\\"\\n        ).data[0].embedding\", \"import torch\\nimport numpy as np\\nfrom datasets import Dataset\\nfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\\nfrom tqdm.auto import tqdm\\n\\ndevice = torch.device(\\\"mps\\\" if torch.backends.mps.is_available() else \\\"cpu\\\")\\nprint(\\\"device:\\\", device)\", \"model_name = \\\"typeform/distilbert-base-uncased-mnli\\\"\\n\\ntokenizer = AutoTokenizer.from_pretrained(model_name)\\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\\nmodel.eval()\\n\\nid2label = {int(k): v for k, v in model.config.id2label.items()} if hasattr(model.config.id2label, \\\"items\\\") else dict(enumerate(model.config.id2label))\\nlabel_text = {i: str(v).lower() for i, v in id2label.items()}\\nentailment_id = next(i for i, v in label_text.items() if \\\"entail\\\" in v)\\ncontradiction_id = next(i for i, v in label_text.items() if \\\"contrad\\\" in v)\\n\\nprint(\\\"model_name:\\\", model_name)\\nprint(\\\"id2label:\\\", id2label)\\nprint(\\\"entailment_id:\\\", entailment_id, \\\"contradiction_id:\\\", contradiction_id)\", \"ds = vault.query_item_content(\\\"glue_mrpc_validation\\\")\\nds = Dataset.from_list(ds)\\nprint(ds)\\nprint(ds[0])\\n\\nsent1 = ds[\\\"sentence1\\\"]\\nsent2 = ds[\\\"sentence2\\\"]\\ny_true = np.array(ds[\\\"label\\\"])\\n\\nprint(\\\"num_examples:\\\", len(y_true))\\nprint(\\\"positive_rate:\\\", float(y_true.mean()))\", \"batch_size = 64\\npreds = []\\ngap_12_all = []\\ngap_21_all = []\\navg_gap_all = []\\n\\nwith torch.no_grad():\\n    for i in tqdm(range(0, len(ds), batch_size)):\\n        batch_s1 = sent1[i:i + batch_size]\\n        batch_s2 = sent2[i:i + batch_size]\\n\\n        enc_12 = tokenizer(\\n            batch_s1,\\n            batch_s2,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc_21 = tokenizer(\\n            batch_s2,\\n            batch_s1,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n\\n        enc_12 = {k: v.to(device) for k, v in enc_12.items()}\\n        enc_21 = {k: v.to(device) for k, v in enc_21.items()}\\n\\n        logits_12 = model(**enc_12).logits\\n        logits_21 = model(**enc_21).logits\\n\\n        probs_12 = torch.softmax(logits_12, dim=-1)\\n        probs_21 = torch.softmax(logits_21, dim=-1)\\n\\n        gap_12 = probs_12[:, entailment_id] - probs_12[:, contradiction_id]\\n        gap_21 = probs_21[:, entailment_id] - probs_21[:, contradiction_id]\\n        avg_gap = (gap_12 + gap_21) / 2.0\\n\\n        batch_preds = (avg_gap > 0).long().cpu().numpy()\\n\\n        preds.extend(batch_preds.tolist())\\n        gap_12_all.extend(gap_12.cpu().numpy().tolist())\\n        gap_21_all.extend(gap_21.cpu().numpy().tolist())\\n        avg_gap_all.extend(avg_gap.cpu().numpy().tolist())\\n\\ny_pred = np.array(preds)\\ngap_12_all = np.array(gap_12_all)\\ngap_21_all = np.array(gap_21_all)\\navg_gap_all = np.array(avg_gap_all)\\n\\nprint(\\\"done\\\")\", \"vault.create_record_list(\\\"mrpc_mean_gap_prediction\\\", column_names=[\\\"prediction\\\", \\\"gap_12\\\", \\\"gap_21\\\"])\\n\\nfor i in range(len(y_pred)):\\n    vault.append_record(\\\"mrpc_mean_gap_prediction\\\", \\n                        {\\n                            \\\"prediction\\\": int(y_pred[i]),\\n                            \\\"gap_12\\\": float(gap_12_all[i]),\\n                            \\\"gap_21\\\": float(gap_21_all[i]),\\n                        },\\n                       input_items = {\\n                           \\\"glue_mrpc_validation\\\": [i, i + 1],\\n                       }\\n                       )\\n\\ndescription = \\\"Per-example prediction dataset for the GLUE MRPC validation split, generated by running the sentence pairs through the typeform/distilbert-base-uncased-mnli model in both input orders. Each record corresponds to one MRPC validation example and is linked to the matching row in glue_mrpc_validation. The dataset has three fields: prediction (binary paraphrase decision, where 1 indicates paraphrase and 0 indicates not paraphrase), gap_12 (entailment probability minus contradiction probability for sentence1\\\\u2192sentence2), and gap_21 (the same probability gap for sentence2\\\\u2192sentence1). In this workflow, it serves as the stored per-instance model output used to inspect directional confidence, compare predictions with ground-truth MRPC labels, and build the downstream summary metrics in softmax_gap_mean_mrpc_summary.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"mrpc_mean_gap_prediction\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"data_type\\\": \\\"model predictions\\\", \\\"prediction_type\\\": \\\"binary classification\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"derived_from\\\": \\\"glue_mrpc_validation\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"input_type\\\": \\\"sentence pair\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"method\\\": \\\"mean softmax entailment-contradiction gap over both sentence orders\\\", \\\"columns\\\": \\\"prediction,gap_12,gap_21\\\", \\\"label_space\\\": \\\"0=not_paraphrase,1=paraphrase\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"mrpc_mean_gap_prediction\\\", cat, embedding, prop)\", \"acc = accuracy_score(y_true, y_pred)\\nf1 = f1_score(y_true, y_pred)\\nreport = classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"])\\nprint({\\\"accuracy\\\": acc, \\\"f1\\\": f1})\\nprint(classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"]))\", \"for i in range(5):\\n    print(\\\"=\\\" * 80)\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"gap_12:\\\", float(gap_12_all[i]))\\n    print(\\\"gap_21:\\\", float(gap_21_all[i]))\\n    print(\\\"avg_gap:\\\", float(avg_gap_all[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\", \"mistakes = np.where(y_true != y_pred)[0][:10]\\nprint(\\\"num_errors:\\\", int((y_true != y_pred).sum()))\\n\\nfor i in mistakes:\\n    print(\\\"=\\\" * 80)\\n    print(\\\"idx:\\\", int(i))\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"gap_12:\\\", float(gap_12_all[i]))\\n    print(\\\"gap_21:\\\", float(gap_21_all[i]))\\n    print(\\\"avg_gap:\\\", float(avg_gap_all[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\", \"vault.create_record_list(\\\"softmax_gap_mean_mrpc_summary\\\", column_names=[\\\"accuracy\\\", \\\"f1\\\", \\\"classification_report\\\"])\\n\\n\\nsummary = {\\n    \\\"accuracy\\\": float(acc),\\n    \\\"f1\\\": float(f1),\\n    \\\"classification_report\\\": str(report)\\n}\\n\\nvault.append_record(\\\"softmax_gap_mean_mrpc_summary\\\", summary,\\n                    input_items = {\\n                        \\\"glue_mrpc_validation\\\": [0, len(ds)],\\n                        \\\"mrpc_mean_gap_prediction\\\": [0, len(ds)]\\n                    })\\n\\nsummary\\n\\ndescription = \\\"Summary dataset for the MRPC validation experiment using an MNLI sequence-classification model and the mean softmax-gap decision rule. It contains a single aggregate record with three fields: accuracy (float), f1 (float), and classification_report (string). These metrics are computed by comparing ground-truth MRPC labels from glue_mrpc_validation against predictions in mrpc_mean_gap_prediction, where each prediction is based on the average of the entailment-minus-contradiction probability gap for both sentence orders (sentence1, sentence2) and (sentence2, sentence1). In this workflow, this dataset serves as the experiment-level evaluation output summarizing model performance over the full validation set.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"softmax_gap_mean_mrpc_summary\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_type\\\": \\\"evaluation summary\\\", \\\"benchmark\\\": \\\"GLUE\\\", \\\"source\\\": \\\"glue_mrpc_validation\\\", \\\"subset\\\": \\\"MRPC\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"inference_method\\\": \\\"mean softmax entailment-contradiction gap over both sentence orders\\\", \\\"metrics\\\": \\\"accuracy,f1,classification_report\\\", \\\"input_prediction_dataset\\\": \\\"mrpc_mean_gap_prediction\\\", \\\"process_name\\\": \\\"softmax_gap_mean_mrpc\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"softmax_gap_mean_mrpc_summary\\\", cat, embedding, prop)\\n\\n\", \"description = \\\"This notebook runs a paraphrase detection experiment on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli sequence classification model in an NLI-style formulation. For each sentence pair, it scores both input orders (sentence1, sentence2) and (sentence2, sentence1), computes the softmax probability gap between entailment and contradiction for each order, averages the two gaps, and predicts paraphrase when the mean gap is greater than zero. The workflow loads the MRPC validation examples from TableVault, performs batched inference with Hugging Face Transformers and PyTorch, and stores per-example predictions and gap scores back into TableVault with lineage to the source records. It then evaluates the method with accuracy, F1, and a classification report, inspects sample predictions and errors, and saves an experiment summary plus descriptive metadata and embeddings for the prediction table, summary table, and overall notebook process.\\\" # description of whole notebook\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"softmax_gap_mean_mrpc\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset\\\": \\\"glue/mrpc\\\", \\\"dataset_split\\\": \\\"validation\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"model_family\\\": \\\"distilbert\\\", \\\"inference_type\\\": \\\"zero-shot NLI\\\", \\\"prediction_method\\\": \\\"mean entailment-contradiction softmax gap over sentence order swaps\\\", \\\"input_format\\\": \\\"sentence pair classification\\\", \\\"framework\\\": \\\"transformers, pytorch\\\", \\\"metrics\\\": \\\"accuracy, f1-score, classification report\\\", \\\"outputs\\\": \\\"per-example predictions and summary metrics\\\", \\\"tracking\\\": \\\"tablevault\\\", \\\"vector_embedding_model\\\": \\\"text-embedding-3-large\\\", \\\"llm_provider\\\": \\\"openai\\\"} #e.g. model: distilbert-base-uncased-MRPC\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"softmax_gap_mean_mrpc\\\", cat, embedding, prop)\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c38cca8819590d59ec1a2d6e904`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "get_code",
    "call_id": "call_Q16lFoQeFyEI4NZzFDHNt5LR",
    "arguments": {
      "name": "entailment_logprob_odds_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_Q16lFoQeFyEI4NZzFDHNt5LR`

**Arguments:**
```json
{
  "name": "entailment_logprob_odds_mrpc"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "import torch\nimport numpy as np\nfrom datasets import Dataset\nfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\nfrom tqdm.auto import tqdm\n",
    "def get_embeddings(text):\n    return client.embeddings.create(\n            input=text,\n            model=\"text-embedding-3-large\"\n        ).data[0].embedding",
    "device = torch.device(\"mps\" if torch.backends.mps.is_available() else \"cpu\")\nprint(\"device:\", device)\n",
    "model_name = \"typeform/distilbert-base-uncased-mnli\"\n\ntokenizer = AutoTokenizer.from_pretrained(model_name)\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\nmodel.eval()\n\nid2label = model.config.id2label\nlabel2id = model.config.label2id\n\ndef _normalize_label(x):\n    return str(x).strip().lower().replace(\"-\", \"_\").replace(\" \", \"_\")\n\nnorm_label2id = {_normalize_label(k): int(v) for k, v in label2id.items()}\n\nif \"entailment\" in norm_label2id:\n    entailment_id = norm_label2id[\"entailment\"]\nelse:\n    entailment_id = next(i for i, lab in id2label.items() if _normalize_label(lab) == \"entailment\")\n\nif \"contradiction\" in norm_label2id:\n    contradiction_id = norm_label2id[\"contradiction\"]\nelse:\n    contradiction_id = next(i for i, lab in id2label.items() if _normalize_label(lab) == \"contradiction\")\n\nprint(model_name)\nprint(\"id2label:\", id2label)\nprint(\"entailment_id:\", entailment_id, \"contradiction_id:\", contradiction_id)\n",
    "ds = vault.query_item_content(\"glue_mrpc_validation\")\nds = Dataset.from_list(ds)\nprint(ds)\nprint(ds[0])\n\nsent1 = ds[\"sentence1\"]\nsent2 = ds[\"sentence2\"]\ny_true = np.array(ds[\"label\"])\n\nprint(\"num_examples:\", len(y_true))\nprint(\"positive_rate:\", float(y_true.mean()))\n",
    "batch_size = 64\ndir12_scores = []\ndir21_scores = []\navg_scores = []\npreds = []\n\nwith torch.no_grad():\n    for i in tqdm(range(0, len(ds), batch_size)):\n        batch_s1 = sent1[i:i + batch_size]\n        batch_s2 = sent2[i:i + batch_size]\n\n        enc12 = tokenizer(\n            batch_s1,\n            batch_s2,\n            padding=True,\n            truncation=True,\n            max_length=128,\n            return_tensors=\"pt\",\n        )\n        enc21 = tokenizer(\n            batch_s2,\n            batch_s1,\n            padding=True,\n            truncation=True,\n            max_length=128,\n            return_tensors=\"pt\",\n        )\n\n        enc12 = {k: v.to(device) for k, v in enc12.items()}\n        enc21 = {k: v.to(device) for k, v in enc21.items()}\n\n        logits12 = model(**enc12).logits\n        logits21 = model(**enc21).logits\n\n        log_probs12 = torch.log_softmax(logits12, dim=-1)\n        log_probs21 = torch.log_softmax(logits21, dim=-1)\n\n        score12 = (log_probs12[:, entailment_id] - log_probs12[:, contradiction_id]).detach().cpu().numpy()\n        score21 = (log_probs21[:, entailment_id] - log_probs21[:, contradiction_id]).detach().cpu().numpy()\n        score_avg = 0.5 * (score12 + score21)\n        batch_preds = (score_avg > 0).astype(np.int64)\n\n        dir12_scores.extend(score12.tolist())\n        dir21_scores.extend(score21.tolist())\n        avg_scores.extend(score_avg.tolist())\n        preds.extend(batch_preds.tolist())\n\ndir12_scores = np.array(dir12_scores)\ndir21_scores = np.array(dir21_scores)\navg_scores = np.array(avg_scores)\ny_pred = np.array(preds)\n\nprint(\"done\")\nprint(\"pred_positive_rate:\", float(y_pred.mean()))\n",
    "vault.create_record_list(\"mrpc_entailment_prediction\", column_names=[\"prediction\", \"dir12\", \"dir21\"])\n\nfor i in range(len(y_pred)):\n    vault.append_record(\"mrpc_entailment_prediction\", \n                        {\n                            \"prediction\": int(y_pred[i]),\n                            \"dir12\": float(dir12_scores[i]),\n                            \"dir21\": float(dir21_scores[i]),\n                        },\n                       input_items = {\n                           \"glue_mrpc_validation\": [i, i + 1],\n                       }\n                       )\n\ndescription = \"mrpc_entailment_prediction contains per-example prediction outputs for the GLUE MRPC validation set generated with the typeform/distilbert-base-uncased-mnli NLI model. Each record corresponds to one validation pair from glue_mrpc_validation and stores three fields: prediction (binary paraphrase decision obtained by thresholding the averaged score at 0), dir12 (entailment-minus-contradiction log-probability score for sentence1 \\u2192 sentence2), and dir21 (the same score for sentence2 \\u2192 sentence1). The dataset is aligned one-to-one with the source MRPC examples through input item indexing. Its role in this workflow is to capture the model\\u2019s directional entailment-based evidence and final paraphrase prediction for downstream evaluation, error analysis, and summary metric computation.\"\nembedding = get_embeddings(description)\nvault.create_description(\"mrpc_entailment_prediction\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"method\": \"mnli entailment vs contradiction logprob odds\", \"dataset_type\": \"model predictions\", \"source\": \"glue/mrpc\", \"input_dataset\": \"glue_mrpc_validation\", \"split\": \"validation\", \"size\": \"408\", \"model\": \"typeform/distilbert-base-uncased-mnli\", \"prediction_target\": \"mrpc label\", \"labels\": \"0=not_paraphrase,1=paraphrase\", \"features\": \"prediction,dir12,dir21\", \"pair_ordering\": \"sentence1->sentence2 and sentence2->sentence1\", \"text_fields\": \"sentence1,sentence2\", \"domain\": \"news\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"mrpc_entailment_prediction\", cat, embedding, prop)",
    "acc = accuracy_score(y_true, y_pred)\nf1 = f1_score(y_true, y_pred)\nreport = classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"])\nprint({\"accuracy\": acc, \"f1\": f1})\nprint(classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"]))\n",
    "for i in range(5):\n    print(\"=\" * 80)\n    print(\"sentence1:\", sent1[i])\n    print(\"sentence2:\", sent2[i])\n    print(\"dir12_log_odds:\", float(dir12_scores[i]))\n    print(\"dir21_log_odds:\", float(dir21_scores[i]))\n    print(\"avg_log_odds:\", float(avg_scores[i]))\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]))\n",
    "mistakes = np.where(y_true != y_pred)[0][:10]\nprint(\"num_errors:\", int((y_true != y_pred).sum()))\n\nfor i in mistakes:\n    print(\"=\" * 80)\n    print(\"idx:\", int(i))\n    print(\"sentence1:\", sent1[i])\n    print(\"sentence2:\", sent2[i])\n    print(\"dir12_log_odds:\", float(dir12_scores[i]))\n    print(\"dir21_log_odds:\", float(dir21_scores[i]))\n    print(\"avg_log_odds:\", float(avg_scores[i]))\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]))\n",
    "vault.create_record_list(\"entailment_logprob_odds_mrpc_summary\", column_names=[\"accuracy\", \"f1\", \"classification_report\"])\n\n\nsummary = {\n    \"accuracy\": float(acc),\n    \"f1\": float(f1),\n    \"classification_report\": str(report)\n}\n\nvault.append_record(\"entailment_logprob_odds_mrpc_summary\", summary,\n                    input_items = {\n                        \"glue_mrpc_validation\": [0, len(ds)],\n                        \"mrpc_entailment_prediction\": [0, len(ds)]\n                    })\n\nsummary\n\ndescription = \"Summary dataset for the MRPC entailment-logprob-odds experiment on the GLUE MRPC validation split. It contains evaluation results for paraphrase predictions produced from a zero-shot NLI model (typeform/distilbert-base-uncased-mnli), where each sentence pair is scored using the average entailment-vs-contradiction log-odds across both input orders. Structure: one record with columns accuracy (float), f1 (float), and classification_report (string). Its role in this workflow is to provide a compact experiment-level summary of model performance, derived from the full per-example outputs in mrpc_entailment_prediction and the ground-truth labels in glue_mrpc_validation.\"\nembedding = get_embeddings(description)\nvault.create_description(\"entailment_logprob_odds_mrpc_summary\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"dataset_type\": \"evaluation summary\", \"source\": \"glue/mrpc\", \"source_table\": \"glue_mrpc_validation\", \"split\": \"validation\", \"size\": \"408\", \"input_type\": \"sentence pair\", \"labels\": \"not_paraphrase,paraphrase\", \"model\": \"typeform/distilbert-base-uncased-mnli\", \"method\": \"entailment_minus_contradiction_logprob_odds_avg_bidirectional\", \"metrics\": \"accuracy,f1,classification_report\", \"domain\": \"news\", \"process\": \"entailment_logprob_odds_mrpc\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"entailment_logprob_odds_mrpc_summary\", cat, embedding, prop)\n\n",
    "description = \"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using an NLI model. It loads sentence pairs and labels from TableVault, applies the typeform/distilbert-base-uncased-mnli sequence classification model, and treats paraphrase detection as entailment scoring: for each pair, it computes the log-probability difference between entailment and contradiction for both sentence orders (sentence1\\u2192sentence2 and sentence2\\u2192sentence1), averages the two directional scores, and predicts paraphrase when the averaged score is positive. The notebook stores per-example predictions and directional entailment log-odds in TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves both dataset-level summaries and notebook-level metadata/descriptions with OpenAI embeddings for documentation and retrieval.\" # description of whole notebook\nembedding = get_embeddings(description)\nvault.create_description(\"entailment_logprob_odds_mrpc\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"approach\": \"NLI entailment-vs-contradiction log-probability odds\", \"model\": \"typeform/distilbert-base-uncased-mnli\", \"model_family\": \"DistilBERT MNLI sequence classification\", \"dataset\": \"glue/mrpc\", \"dataset_split\": \"validation\", \"input_type\": \"sentence pair\", \"prediction_rule\": \"average bidirectional entailment log-odds > 0\", \"evaluation\": \"accuracy, f1-score, classification report\", \"metrics\": \"accuracy, f1\", \"artifacts\": \"per-example predictions, directional scores, summary metrics\", \"tracking\": \"TableVault\", \"embedding_model\": \"text-embedding-3-large\", \"frameworks\": \"transformers, torch, sklearn, datasets\", \"process_name\": \"entailment_logprob_odds_mrpc\"} #e.g. model: distilbert-base-uncased-MRPC\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"entailment_logprob_odds_mrpc\", cat, embedding, prop)"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 29250 | 57 | 29 | 27680 | 2.180s | 0.023s |

---

## Turn 15 — `code_search` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c3b04408195bd3946db0af3262f`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_Q16lFoQeFyEI4NZzFDHNt5LR",
    "output": "{\"ok\": true, \"result\": [\"import torch\\nimport numpy as np\\nfrom datasets import Dataset\\nfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\\nfrom tqdm.auto import tqdm\\n\", \"def get_embeddings(text):\\n    return client.embeddings.create(\\n            input=text,\\n            model=\\\"text-embedding-3-large\\\"\\n        ).data[0].embedding\", \"device = torch.device(\\\"mps\\\" if torch.backends.mps.is_available() else \\\"cpu\\\")\\nprint(\\\"device:\\\", device)\\n\", \"model_name = \\\"typeform/distilbert-base-uncased-mnli\\\"\\n\\ntokenizer = AutoTokenizer.from_pretrained(model_name)\\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\\nmodel.eval()\\n\\nid2label = model.config.id2label\\nlabel2id = model.config.label2id\\n\\ndef _normalize_label(x):\\n    return str(x).strip().lower().replace(\\\"-\\\", \\\"_\\\").replace(\\\" \\\", \\\"_\\\")\\n\\nnorm_label2id = {_normalize_label(k): int(v) for k, v in label2id.items()}\\n\\nif \\\"entailment\\\" in norm_label2id:\\n    entailment_id = norm_label2id[\\\"entailment\\\"]\\nelse:\\n    entailment_id = next(i for i, lab in id2label.items() if _normalize_label(lab) == \\\"entailment\\\")\\n\\nif \\\"contradiction\\\" in norm_label2id:\\n    contradiction_id = norm_label2id[\\\"contradiction\\\"]\\nelse:\\n    contradiction_id = next(i for i, lab in id2label.items() if _normalize_label(lab) == \\\"contradiction\\\")\\n\\nprint(model_name)\\nprint(\\\"id2label:\\\", id2label)\\nprint(\\\"entailment_id:\\\", entailment_id, \\\"contradiction_id:\\\", contradiction_id)\\n\", \"ds = vault.query_item_content(\\\"glue_mrpc_validation\\\")\\nds = Dataset.from_list(ds)\\nprint(ds)\\nprint(ds[0])\\n\\nsent1 = ds[\\\"sentence1\\\"]\\nsent2 = ds[\\\"sentence2\\\"]\\ny_true = np.array(ds[\\\"label\\\"])\\n\\nprint(\\\"num_examples:\\\", len(y_true))\\nprint(\\\"positive_rate:\\\", float(y_true.mean()))\\n\", \"batch_size = 64\\ndir12_scores = []\\ndir21_scores = []\\navg_scores = []\\npreds = []\\n\\nwith torch.no_grad():\\n    for i in tqdm(range(0, len(ds), batch_size)):\\n        batch_s1 = sent1[i:i + batch_size]\\n        batch_s2 = sent2[i:i + batch_size]\\n\\n        enc12 = tokenizer(\\n            batch_s1,\\n            batch_s2,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc21 = tokenizer(\\n            batch_s2,\\n            batch_s1,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n\\n        enc12 = {k: v.to(device) for k, v in enc12.items()}\\n        enc21 = {k: v.to(device) for k, v in enc21.items()}\\n\\n        logits12 = model(**enc12).logits\\n        logits21 = model(**enc21).logits\\n\\n        log_probs12 = torch.log_softmax(logits12, dim=-1)\\n        log_probs21 = torch.log_softmax(logits21, dim=-1)\\n\\n        score12 = (log_probs12[:, entailment_id] - log_probs12[:, contradiction_id]).detach().cpu().numpy()\\n        score21 = (log_probs21[:, entailment_id] - log_probs21[:, contradiction_id]).detach().cpu().numpy()\\n        score_avg = 0.5 * (score12 + score21)\\n        batch_preds = (score_avg > 0).astype(np.int64)\\n\\n        dir12_scores.extend(score12.tolist())\\n        dir21_scores.extend(score21.tolist())\\n        avg_scores.extend(score_avg.tolist())\\n        preds.extend(batch_preds.tolist())\\n\\ndir12_scores = np.array(dir12_scores)\\ndir21_scores = np.array(dir21_scores)\\navg_scores = np.array(avg_scores)\\ny_pred = np.array(preds)\\n\\nprint(\\\"done\\\")\\nprint(\\\"pred_positive_rate:\\\", float(y_pred.mean()))\\n\", \"vault.create_record_list(\\\"mrpc_entailment_prediction\\\", column_names=[\\\"prediction\\\", \\\"dir12\\\", \\\"dir21\\\"])\\n\\nfor i in range(len(y_pred)):\\n    vault.append_record(\\\"mrpc_entailment_prediction\\\", \\n                        {\\n                            \\\"prediction\\\": int(y_pred[i]),\\n                            \\\"dir12\\\": float(dir12_scores[i]),\\n                            \\\"dir21\\\": float(dir21_scores[i]),\\n                        },\\n                       input_items = {\\n                           \\\"glue_mrpc_validation\\\": [i, i + 1],\\n                       }\\n                       )\\n\\ndescription = \\\"mrpc_entailment_prediction contains per-example prediction outputs for the GLUE MRPC validation set generated with the typeform/distilbert-base-uncased-mnli NLI model. Each record corresponds to one validation pair from glue_mrpc_validation and stores three fields: prediction (binary paraphrase decision obtained by thresholding the averaged score at 0), dir12 (entailment-minus-contradiction log-probability score for sentence1 \\\\u2192 sentence2), and dir21 (the same score for sentence2 \\\\u2192 sentence1). The dataset is aligned one-to-one with the source MRPC examples through input item indexing. Its role in this workflow is to capture the model\\\\u2019s directional entailment-based evidence and final paraphrase prediction for downstream evaluation, error analysis, and summary metric computation.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"mrpc_entailment_prediction\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"method\\\": \\\"mnli entailment vs contradiction logprob odds\\\", \\\"dataset_type\\\": \\\"model predictions\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"input_dataset\\\": \\\"glue_mrpc_validation\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"prediction_target\\\": \\\"mrpc label\\\", \\\"labels\\\": \\\"0=not_paraphrase,1=paraphrase\\\", \\\"features\\\": \\\"prediction,dir12,dir21\\\", \\\"pair_ordering\\\": \\\"sentence1->sentence2 and sentence2->sentence1\\\", \\\"text_fields\\\": \\\"sentence1,sentence2\\\", \\\"domain\\\": \\\"news\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"mrpc_entailment_prediction\\\", cat, embedding, prop)\", \"acc = accuracy_score(y_true, y_pred)\\nf1 = f1_score(y_true, y_pred)\\nreport = classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"])\\nprint({\\\"accuracy\\\": acc, \\\"f1\\\": f1})\\nprint(classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"]))\\n\", \"for i in range(5):\\n    print(\\\"=\\\" * 80)\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"dir12_log_odds:\\\", float(dir12_scores[i]))\\n    print(\\\"dir21_log_odds:\\\", float(dir21_scores[i]))\\n    print(\\\"avg_log_odds:\\\", float(avg_scores[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n\", \"mistakes = np.where(y_true != y_pred)[0][:10]\\nprint(\\\"num_errors:\\\", int((y_true != y_pred).sum()))\\n\\nfor i in mistakes:\\n    print(\\\"=\\\" * 80)\\n    print(\\\"idx:\\\", int(i))\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"dir12_log_odds:\\\", float(dir12_scores[i]))\\n    print(\\\"dir21_log_odds:\\\", float(dir21_scores[i]))\\n    print(\\\"avg_log_odds:\\\", float(avg_scores[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n\", \"vault.create_record_list(\\\"entailment_logprob_odds_mrpc_summary\\\", column_names=[\\\"accuracy\\\", \\\"f1\\\", \\\"classification_report\\\"])\\n\\n\\nsummary = {\\n    \\\"accuracy\\\": float(acc),\\n    \\\"f1\\\": float(f1),\\n    \\\"classification_report\\\": str(report)\\n}\\n\\nvault.append_record(\\\"entailment_logprob_odds_mrpc_summary\\\", summary,\\n                    input_items = {\\n                        \\\"glue_mrpc_validation\\\": [0, len(ds)],\\n                        \\\"mrpc_entailment_prediction\\\": [0, len(ds)]\\n                    })\\n\\nsummary\\n\\ndescription = \\\"Summary dataset for the MRPC entailment-logprob-odds experiment on the GLUE MRPC validation split. It contains evaluation results for paraphrase predictions produced from a zero-shot NLI model (typeform/distilbert-base-uncased-mnli), where each sentence pair is scored using the average entailment-vs-contradiction log-odds across both input orders. Structure: one record with columns accuracy (float), f1 (float), and classification_report (string). Its role in this workflow is to provide a compact experiment-level summary of model performance, derived from the full per-example outputs in mrpc_entailment_prediction and the ground-truth labels in glue_mrpc_validation.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"entailment_logprob_odds_mrpc_summary\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_type\\\": \\\"evaluation summary\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"source_table\\\": \\\"glue_mrpc_validation\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"input_type\\\": \\\"sentence pair\\\", \\\"labels\\\": \\\"not_paraphrase,paraphrase\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"method\\\": \\\"entailment_minus_contradiction_logprob_odds_avg_bidirectional\\\", \\\"metrics\\\": \\\"accuracy,f1,classification_report\\\", \\\"domain\\\": \\\"news\\\", \\\"process\\\": \\\"entailment_logprob_odds_mrpc\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"entailment_logprob_odds_mrpc_summary\\\", cat, embedding, prop)\\n\\n\", \"description = \\\"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using an NLI model. It loads sentence pairs and labels from TableVault, applies the typeform/distilbert-base-uncased-mnli sequence classification model, and treats paraphrase detection as entailment scoring: for each pair, it computes the log-probability difference between entailment and contradiction for both sentence orders (sentence1\\\\u2192sentence2 and sentence2\\\\u2192sentence1), averages the two directional scores, and predicts paraphrase when the averaged score is positive. The notebook stores per-example predictions and directional entailment log-odds in TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves both dataset-level summaries and notebook-level metadata/descriptions with OpenAI embeddings for documentation and retrieval.\\\" # description of whole notebook\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"entailment_logprob_odds_mrpc\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"approach\\\": \\\"NLI entailment-vs-contradiction log-probability odds\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"model_family\\\": \\\"DistilBERT MNLI sequence classification\\\", \\\"dataset\\\": \\\"glue/mrpc\\\", \\\"dataset_split\\\": \\\"validation\\\", \\\"input_type\\\": \\\"sentence pair\\\", \\\"prediction_rule\\\": \\\"average bidirectional entailment log-odds > 0\\\", \\\"evaluation\\\": \\\"accuracy, f1-score, classification report\\\", \\\"metrics\\\": \\\"accuracy, f1\\\", \\\"artifacts\\\": \\\"per-example predictions, directional scores, summary metrics\\\", \\\"tracking\\\": \\\"TableVault\\\", \\\"embedding_model\\\": \\\"text-embedding-3-large\\\", \\\"frameworks\\\": \\\"transformers, torch, sklearn, datasets\\\", \\\"process_name\\\": \\\"entailment_logprob_odds_mrpc\\\"} #e.g. model: distilbert-base-uncased-MRPC\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"entailment_logprob_odds_mrpc\\\", cat, embedding, prop)\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c3b04408195bd3946db0af3262f`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_search",
    "call_id": "call_oCPH8HPhiMcHZuCiZwfeLApn",
    "arguments": {
      "code": "direct_nli"
    }
  }
]
```

### Tool Call
**Tool:** `code_search` | **call_id:** `call_oCPH8HPhiMcHZuCiZwfeLApn`

**Arguments:**
```json
{
  "code": "direct_nli"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": []
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 32216 | 62 | 40 | 30646 | 3.228s | 0.009s |

---

## Turn 16 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c3e3db88195a10ca1f980bc53ab`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_oCPH8HPhiMcHZuCiZwfeLApn",
    "output": "{\"ok\": true, \"result\": []}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c3e3db88195a10ca1f980bc53ab`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_KVqSio9oAlf7keCdITFsge20",
    "arguments": {
      "item_name": "entailment_logprob_odds_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_KVqSio9oAlf7keCdITFsge20`

**Arguments:**
```json
{
  "item_name": "entailment_logprob_odds_mrpc_summary",
  "start_position": 0,
  "end_position": 5
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    {
      "accuracy": 0.7034313725490197,
      "f1": 0.7729831144465291,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.53      0.63      0.57       129\n    paraphrase       0.81      0.74      0.77       279\n\n      accuracy                           0.70       408\n     macro avg       0.67      0.68      0.67       408\n  weighted avg       0.72      0.70      0.71       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 32299 | 137 | 97 | 30729 | 3.144s | 0.016s |

---

## Turn 17 — `code_search` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c41635881958c1a51b6b63662cd`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_KVqSio9oAlf7keCdITFsge20",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.7034313725490197, \"f1\": 0.7729831144465291, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.53      0.63      0.57       129\\n    paraphrase       0.81      0.74      0.77       279\\n\\n      accuracy                           0.70       408\\n     macro avg       0.67      0.68      0.67       408\\n  weighted avg       0.72      0.70      0.71       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c41635881958c1a51b6b63662cd`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_search",
    "call_id": "call_838xQAyQnwzNC0GSVPbKRSeS",
    "arguments": {
      "code": "paraphrase_score_threshold_zero_shot_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `code_search` | **call_id:** `call_838xQAyQnwzNC0GSVPbKRSeS`

**Arguments:**
```json
{
  "code": "paraphrase_score_threshold_zero_shot_mrpc"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "gent_1775914190",
    "gent_1775874933",
    "gent_1775874373",
    "gent_1775874650",
    "gent_1775914000",
    "gent_1775913615"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 32602 | 261 | 232 | 31032 | 4.850s | 0.026s |

---

## Turn 18 — `code_search` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c46491081958a8755bf7c9114d1`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_838xQAyQnwzNC0GSVPbKRSeS",
    "output": "{\"ok\": true, \"result\": [\"gent_1775914190\", \"gent_1775874933\", \"gent_1775874373\", \"gent_1775874650\", \"gent_1775914000\", \"gent_1775913615\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c46491081958a8755bf7c9114d1`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_search",
    "call_id": "call_9i3ypY4tDR0iCBAK1yqFBWCf",
    "arguments": {
      "code": "zero_shot_classification"
    }
  }
]
```

### Tool Call
**Tool:** `code_search` | **call_id:** `call_9i3ypY4tDR0iCBAK1yqFBWCf`

**Arguments:**
```json
{
  "code": "zero_shot_classification"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": []
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 32931 | 44 | 20 | 31361 | 2.690s | 0.006s |

---

## Turn 19 — `code_search` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c48f8008195b065402c85146e17`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_9i3ypY4tDR0iCBAK1yqFBWCf",
    "output": "{\"ok\": true, \"result\": []}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c48f8008195b065402c85146e17`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_search",
    "call_id": "call_O65Nwv3CZIa7iPDb96SLuFor",
    "arguments": {
      "code": "zero-shot-classification"
    }
  }
]
```

### Tool Call
**Tool:** `code_search` | **call_id:** `call_O65Nwv3CZIa7iPDb96SLuFor`

**Arguments:**
```json
{
  "code": "zero-shot-classification"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "entailment_logprob_odds_mrpc",
    "gent_1775914190",
    "gent_1775874933",
    "gent_1775874373",
    "softmax_gap_mean_mrpc",
    "flan_t5_contextual_calibrated_yes_no_mrpc",
    "neutral_penalized_margin_mrpc",
    "flan_t5_symmetric_prompt_average_mrpc",
    "gent_1775874650",
    "gent_1775913615",
    "gent_1775914000",
    "flan_t5_true_false_first_step_mrpc",
    "consensus_then_avg_margin_mrpc",
    "min_direction_margin_mrpc"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 32996 | 41 | 18 | 31426 | 1.632s | 0.050s |

---

## Turn 20 — `code_search` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c4aa7348195ab330354da16c58d`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_O65Nwv3CZIa7iPDb96SLuFor",
    "output": "{\"ok\": true, \"result\": [\"entailment_logprob_odds_mrpc\", \"gent_1775914190\", \"gent_1775874933\", \"gent_1775874373\", \"softmax_gap_mean_mrpc\", \"flan_t5_contextual_calibrated_yes_no_mrpc\", \"neutral_penalized_margin_mrpc\", \"flan_t5_symmetric_prompt_average_mrpc\", \"gent_1775874650\", \"gent_1775913615\", \"gent_1775914000\", \"flan_t5_true_false_first_step_mrpc\", \"consensus_then_avg_margin_mrpc\", \"min_direction_margin_mrpc\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c4aa7348195ab330354da16c58d`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_search",
    "call_id": "call_SPV3lS4ZLNsXnB94UL5gRL5F",
    "arguments": {
      "code": "pipeline("
    }
  }
]
```

### Tool Call
**Tool:** `code_search` | **call_id:** `call_SPV3lS4ZLNsXnB94UL5gRL5F`

**Arguments:**
```json
{
  "code": "pipeline("
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "gent_1775914190",
    "gent_1775874933",
    "hf_pipeline_mrpc_short_maxlen_64",
    "mrpc_paraphrase_inference_distilbert",
    "gent_1775874373",
    "hf_pipeline_mrpc_margin_rule",
    "gent_1775874650",
    "hf_pipeline_mrpc_raw_logits_softmax",
    "gent_1775913615",
    "distilbert_max_pool_cosine_mrpc",
    "gent_1775914000",
    "quora_cross_encoder_text_normalized_mrpc",
    "distilbert_no_special_tokens_mean_cosine_mrpc",
    "hf_pipeline_mrpc_threshold_070",
    "hf_pipeline_mrpc_bidirectional_order_average"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 33188 | 43 | 22 | 31618 | 1.837s | 0.041s |

---

## Turn 21 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c4d77b08195990640c7f4193c41`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_SPV3lS4ZLNsXnB94UL5gRL5F",
    "output": "{\"ok\": true, \"result\": [\"gent_1775914190\", \"gent_1775874933\", \"hf_pipeline_mrpc_short_maxlen_64\", \"mrpc_paraphrase_inference_distilbert\", \"gent_1775874373\", \"hf_pipeline_mrpc_margin_rule\", \"gent_1775874650\", \"hf_pipeline_mrpc_raw_logits_softmax\", \"gent_1775913615\", \"distilbert_max_pool_cosine_mrpc\", \"gent_1775914000\", \"quora_cross_encoder_text_normalized_mrpc\", \"distilbert_no_special_tokens_mean_cosine_mrpc\", \"hf_pipeline_mrpc_threshold_070\", \"hf_pipeline_mrpc_bidirectional_order_average\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c4d77b08195990640c7f4193c41`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "get_code",
    "call_id": "call_qCYZkPPswuikb2ZaKAKakmO7",
    "arguments": {
      "name": "mrpc_paraphrase_inference_distilbert"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_qCYZkPPswuikb2ZaKAKakmO7`

**Arguments:**
```json
{
  "name": "mrpc_paraphrase_inference_distilbert"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "def get_embeddings(text):\n    return client.embeddings.create(\n            input=text,\n            model=\"text-embedding-3-large\"\n        ).data[0].embedding",
    "model_name = \"textattack/distilbert-base-uncased-MRPC\"\n\ntokenizer = AutoTokenizer.from_pretrained(model_name)\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\nmodel.eval()\n\nid2label = model.config.id2label\nprint(model_name)\nprint(id2label)",
    "ds = load_dataset(\"glue\", \"mrpc\", split=\"validation\")\nprint(ds)\nprint(ds[0])",
    "vault.create_record_list(\"glue_mrpc_validation\", column_names=[\"sentence1\", \"sentence2\", \"label\", \"idx\"])\nfor row in ds:\n    vault.append_record(\"glue_mrpc_validation\", row)\n\ndescription = \"glue_mrpc_validation is the validation split of the GLUE MRPC (Microsoft Research Paraphrase Corpus) dataset stored in TableVault for this notebook. Each record contains sentence1, sentence2, label, and idx, where sentence1 and sentence2 are a pair of sentences, label is a binary paraphrase target (1 = paraphrase, 0 = not paraphrase), and idx is the example identifier from the original dataset. This dataset is the ground-truth evaluation input for the workflow: the sentence pairs are tokenized and passed to the pretrained textattack/distilbert-base-uncased-MRPC model, and the labels are used to compute accuracy, F1, error cases, and the final classification report. It serves as the source dataset linked to downstream prediction, mistake-analysis, and summary output records.\"\nembedding = get_embeddings(description)\nvault.create_description(\"glue_mrpc_validation\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"benchmark\": \"GLUE\", \"dataset\": \"MRPC\", \"source\": \"glue/mrpc\", \"split\": \"validation\", \"size\": \"408\", \"language\": \"English\", \"modality\": \"text\", \"input_type\": \"sentence pair\", \"labels\": \"0:not_paraphrase,1:paraphrase\", \"domain\": \"news\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"glue_mrpc_validation\", cat, embedding, prop)\n",
    "ds = vault.query_item_content(\"glue_mrpc_validation\")\nds = Dataset.from_list(ds)\n\nsent1 = ds[\"sentence1\"]\nsent2 = ds[\"sentence2\"]\ny_true = np.array(ds[\"label\"])\nprint(\"num_examples:\", len(y_true))\nprint(\"positive_rate:\", y_true.mean())",
    "ds",
    "batch_size = 64\nvault.create_record_list(\"mrpc_distilbert_predictions\", column_names=[\"prediction\"])\n\nwith torch.no_grad():\n    for i in tqdm(range(0, len(ds), batch_size)):\n        batch_s1 = sent1[i:i + batch_size]\n        batch_s2 = sent2[i:i + batch_size]\n\n        enc = tokenizer(\n            batch_s1,\n            batch_s2,\n            padding=True,\n            truncation=True,\n            max_length=128,\n            return_tensors=\"pt\",\n        )\n        enc = {k: v.to(device) for k, v in enc.items()}\n\n        logits = model(**enc).logits\n        batch_preds = torch.argmax(logits, dim=-1).cpu().numpy()\n        for j in range(len(batch_preds)):\n            vault.append_record(\"mrpc_distilbert_predictions\", {\"prediction\": int(batch_preds[j])}, \n                               input_items = {\"glue_mrpc_validation\": [i + j, i + j + 1]}\n                               )\n\npreds = vault.query_item_content(\"mrpc_distilbert_predictions\")\n\ndescription = \"Model prediction outputs for the GLUE MRPC validation set generated by the textattack/distilbert-base-uncased-MRPC sequence classification model. Each record corresponds to one sentence-pair example in glue_mrpc_validation and stores the model\\u2019s predicted class label for paraphrase detection. The dataset has a single field, prediction, which is an integer class ID (0 = not paraphrase, 1 = paraphrase). In this workflow, it serves as the inference output table linked back to the source validation examples and is used to compute evaluation metrics, compare predictions with ground-truth labels, and identify error cases.\"\nembedding = get_embeddings(description)\nvault.create_description(\"mrpc_distilbert_predictions\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"dataset_role\": \"model predictions\", \"prediction_type\": \"binary sequence classification\", \"source_dataset\": \"glue/mrpc\", \"benchmark\": \"GLUE\", \"split\": \"validation\", \"size\": \"408\", \"model\": \"textattack/distilbert-base-uncased-MRPC\", \"model_family\": \"DistilBERT\", \"input_format\": \"sentence pair\", \"label_space\": \"0=not_paraphrase,1=paraphrase\", \"output_column\": \"prediction\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"mrpc_distilbert_predictions\", cat, embedding, prop)\n\n    \npreds = [pred[\"prediction\"] for pred in preds]\n\ny_pred = np.array(preds)\nprint(\"done\")",
    "acc = accuracy_score(y_true, y_pred)\nf1 = f1_score(y_true, y_pred)\nreport = classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"])\n\nprint({\"accuracy\": acc, \"f1\": f1})\nprint(classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"]))",
    "for i in range(5):\n    print(\"=\" * 80)\n    print(\"sentence1:\", sent1[i])\n    print(\"sentence2:\", sent2[i])\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]), \"label:\", id2label[int(y_pred[i])])",
    "mistakes = np.where(y_true != y_pred)[0][:10]\nprint(\"num_errors:\", int((y_true != y_pred).sum()))\n\nvault.create_record_list(\"mrpc_paraphrase_inference_distilbert_mistakes\", column_names=[\"idx\", \"sentence1\", \"sentence2\", \"true\", \"pred\"])\n\nfor i in mistakes:\n    print(\"=\" * 80)\n    print(\"idx:\", int(i))\n    print(\"sentence1:\", sent1[i])\n    print(\"sentence2:\", sent2[i])\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]))\n\n    vault.append_record(\"mrpc_paraphrase_inference_distilbert_mistakes\", {\n            \"idx\": int(i),\n            \"sentence1\": sent1[i],\n            \"sentence2\": sent2[i],\n            \"true\": int(y_true[i]),\n            \"pred\": int(y_pred[i]),\n        },\n        input_items = {\n            \"glue_mrpc_validation\": [int(i), int(i)+ 1],\n            \"mrpc_distilbert_predictions\": [int(i), int(i)+ 1]\n        }\n    )\n\ndescription = \"Subset of error cases from the GLUE MRPC validation run using the textattack/distilbert-base-uncased-MRPC model. Each record captures one misclassified sentence pair and includes the fields: idx (validation-set position), sentence1, sentence2, true (ground-truth binary label), and pred (model-predicted binary label). This dataset is created by selecting the first 10 examples where the model prediction differs from the true label, and each record is linked back to the corresponding source example in glue_mrpc_validation and its entry in mrpc_distilbert_predictions. Its role in the workflow is error analysis: it provides a compact, inspectable sample of model failures for diagnosing paraphrase detection mistakes.\"\nembedding = get_embeddings(description)\nvault.create_description(\"mrpc_paraphrase_inference_distilbert_mistakes\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"dataset_type\": \"error analysis subset\", \"subset\": \"model mistakes\", \"source\": \"glue/mrpc\", \"split\": \"validation\", \"model\": \"textattack/distilbert-base-uncased-MRPC\", \"framework\": \"transformers\", \"input_format\": \"sentence pair\", \"label_space\": \"0=not_paraphrase, 1=paraphrase\", \"content\": \"misclassified validation examples with true and predicted labels\", \"size\": \"10\", \"sampling\": \"first 10 misclassifications\", \"parent_datasets\": \"glue_mrpc_validation,mrpc_distilbert_predictions\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"mrpc_paraphrase_inference_distilbert_mistakes\", cat, embedding, prop)\n",
    "vault.create_record_list(\"mrpc_paraphrase_inference_distilbert_output\", column_names=[\"accuracy\", \"f1\", \"classification_report\"])\n\n\nsummary = {\n    \"accuracy\": float(acc),\n    \"f1\": float(f1),\n    \"classification_report\": str(report)\n}\n\nvault.append_record(\"mrpc_paraphrase_inference_distilbert_output\", summary,\n                    input_items = {\n                        \"glue_mrpc_validation\": [0, len(ds)],\n                        \"mrpc_distilbert_predictions\": [0, len(ds)]\n                    })\n\nsummary\n\ndescription = \"This dataset contains the final evaluation summary for the textattack/distilbert-base-uncased-MRPC model on the GLUE MRPC validation split. It is a small output table with one record summarizing model performance over the full validation dataset.\\n\\nFields:\\n- accuracy: overall classification accuracy on the validation set\\n- f1: F1 score for the paraphrase classification task\\n- classification_report: full text report from sklearn including precision, recall, F1, and support for the not_paraphrase and paraphrase classes\\n\\nIn this workflow, this dataset serves as the final results artifact. It is created after running batched inference on sentence pairs, comparing predictions against ground-truth labels, and aggregating the metrics. The record is linked to the full validation input dataset and the prediction dataset so a user can trace the reported metrics back to the underlying examples and model outputs.\"\nembedding = get_embeddings(description)\nvault.create_description(\"mrpc_paraphrase_inference_distilbert_output\", description, embedding)\n\nproperties = {\"artifact_type\": \"evaluation_output\", \"task\": \"paraphrase_detection\", \"source_dataset\": \"glue/mrpc\", \"split\": \"validation\", \"evaluation_examples\": \"408\", \"input_format\": \"sentence_pair\", \"model\": \"textattack/distilbert-base-uncased-MRPC\", \"framework\": \"transformers\", \"metrics\": \"accuracy,f1,classification_report\", \"labels\": \"not_paraphrase,paraphrase\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"mrpc_paraphrase_inference_distilbert_output\", cat, embedding, prop)",
    "description = \"This notebook runs a paraphrase detection inference workflow on the GLUE MRPC validation set using the pretrained Hugging Face model textattack/distilbert-base-uncased-MRPC. It loads sentence pairs and labels from the dataset, performs batched tokenization and prediction with DistilBERT on the available device, and evaluates results with accuracy, F1, and a full classification report. The workflow stores the source validation records, model predictions, error examples, and final summary metrics in TableVault so the inputs, outputs, and lineage between them are traceable. It also creates semantic descriptions and property metadata embeddings for the dataset, prediction table, mistakes table, output summary, and overall notebook process. Overall, the notebook is designed to both benchmark a pretrained MRPC paraphrase classifier and document the complete inference pipeline in a searchable experiment vault.\" # description of whole notebook\nembedding = get_embeddings(description)\nvault.create_description(\"mrpc_paraphrase_inference_distilbert\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"problem_type\": \"binary text pair classification\", \"model\": \"textattack/distilbert-base-uncased-MRPC\", \"model_family\": \"DistilBERT\", \"dataset\": \"glue/mrpc\", \"dataset_split\": \"validation\", \"framework\": \"PyTorch\", \"library\": \"Hugging Face Transformers\", \"evaluation\": \"accuracy, f1-score, classification report\", \"inference_type\": \"batched inference\", \"tracking\": \"TableVault\", \"embedding_model\": \"text-embedding-3-large\", \"device\": \"mps_or_cpu\", \"outputs\": \"predictions, mistakes, summary metrics\", \"domain\": \"natural language processing\"} #e.g. model: distilbert-base-uncased-MRPC\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"mrpc_paraphrase_inference_distilbert\", cat, embedding, prop)"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 33394 | 52 | 23 | 31824 | 3.295s | 0.016s |

---

## Turn 22 — `code_search` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c4fd7688195b9b2ca4f75d74d18`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_qCYZkPPswuikb2ZaKAKakmO7",
    "output": "{\"ok\": true, \"result\": [\"def get_embeddings(text):\\n    return client.embeddings.create(\\n            input=text,\\n            model=\\\"text-embedding-3-large\\\"\\n        ).data[0].embedding\", \"model_name = \\\"textattack/distilbert-base-uncased-MRPC\\\"\\n\\ntokenizer = AutoTokenizer.from_pretrained(model_name)\\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\\nmodel.eval()\\n\\nid2label = model.config.id2label\\nprint(model_name)\\nprint(id2label)\", \"ds = load_dataset(\\\"glue\\\", \\\"mrpc\\\", split=\\\"validation\\\")\\nprint(ds)\\nprint(ds[0])\", \"vault.create_record_list(\\\"glue_mrpc_validation\\\", column_names=[\\\"sentence1\\\", \\\"sentence2\\\", \\\"label\\\", \\\"idx\\\"])\\nfor row in ds:\\n    vault.append_record(\\\"glue_mrpc_validation\\\", row)\\n\\ndescription = \\\"glue_mrpc_validation is the validation split of the GLUE MRPC (Microsoft Research Paraphrase Corpus) dataset stored in TableVault for this notebook. Each record contains sentence1, sentence2, label, and idx, where sentence1 and sentence2 are a pair of sentences, label is a binary paraphrase target (1 = paraphrase, 0 = not paraphrase), and idx is the example identifier from the original dataset. This dataset is the ground-truth evaluation input for the workflow: the sentence pairs are tokenized and passed to the pretrained textattack/distilbert-base-uncased-MRPC model, and the labels are used to compute accuracy, F1, error cases, and the final classification report. It serves as the source dataset linked to downstream prediction, mistake-analysis, and summary output records.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"glue_mrpc_validation\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"benchmark\\\": \\\"GLUE\\\", \\\"dataset\\\": \\\"MRPC\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"language\\\": \\\"English\\\", \\\"modality\\\": \\\"text\\\", \\\"input_type\\\": \\\"sentence pair\\\", \\\"labels\\\": \\\"0:not_paraphrase,1:paraphrase\\\", \\\"domain\\\": \\\"news\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"glue_mrpc_validation\\\", cat, embedding, prop)\\n\", \"ds = vault.query_item_content(\\\"glue_mrpc_validation\\\")\\nds = Dataset.from_list(ds)\\n\\nsent1 = ds[\\\"sentence1\\\"]\\nsent2 = ds[\\\"sentence2\\\"]\\ny_true = np.array(ds[\\\"label\\\"])\\nprint(\\\"num_examples:\\\", len(y_true))\\nprint(\\\"positive_rate:\\\", y_true.mean())\", \"ds\", \"batch_size = 64\\nvault.create_record_list(\\\"mrpc_distilbert_predictions\\\", column_names=[\\\"prediction\\\"])\\n\\nwith torch.no_grad():\\n    for i in tqdm(range(0, len(ds), batch_size)):\\n        batch_s1 = sent1[i:i + batch_size]\\n        batch_s2 = sent2[i:i + batch_size]\\n\\n        enc = tokenizer(\\n            batch_s1,\\n            batch_s2,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc = {k: v.to(device) for k, v in enc.items()}\\n\\n        logits = model(**enc).logits\\n        batch_preds = torch.argmax(logits, dim=-1).cpu().numpy()\\n        for j in range(len(batch_preds)):\\n            vault.append_record(\\\"mrpc_distilbert_predictions\\\", {\\\"prediction\\\": int(batch_preds[j])}, \\n                               input_items = {\\\"glue_mrpc_validation\\\": [i + j, i + j + 1]}\\n                               )\\n\\npreds = vault.query_item_content(\\\"mrpc_distilbert_predictions\\\")\\n\\ndescription = \\\"Model prediction outputs for the GLUE MRPC validation set generated by the textattack/distilbert-base-uncased-MRPC sequence classification model. Each record corresponds to one sentence-pair example in glue_mrpc_validation and stores the model\\\\u2019s predicted class label for paraphrase detection. The dataset has a single field, prediction, which is an integer class ID (0 = not paraphrase, 1 = paraphrase). In this workflow, it serves as the inference output table linked back to the source validation examples and is used to compute evaluation metrics, compare predictions with ground-truth labels, and identify error cases.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"mrpc_distilbert_predictions\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_role\\\": \\\"model predictions\\\", \\\"prediction_type\\\": \\\"binary sequence classification\\\", \\\"source_dataset\\\": \\\"glue/mrpc\\\", \\\"benchmark\\\": \\\"GLUE\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"textattack/distilbert-base-uncased-MRPC\\\", \\\"model_family\\\": \\\"DistilBERT\\\", \\\"input_format\\\": \\\"sentence pair\\\", \\\"label_space\\\": \\\"0=not_paraphrase,1=paraphrase\\\", \\\"output_column\\\": \\\"prediction\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"mrpc_distilbert_predictions\\\", cat, embedding, prop)\\n\\n    \\npreds = [pred[\\\"prediction\\\"] for pred in preds]\\n\\ny_pred = np.array(preds)\\nprint(\\\"done\\\")\", \"acc = accuracy_score(y_true, y_pred)\\nf1 = f1_score(y_true, y_pred)\\nreport = classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"])\\n\\nprint({\\\"accuracy\\\": acc, \\\"f1\\\": f1})\\nprint(classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"]))\", \"for i in range(5):\\n    print(\\\"=\\\" * 80)\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]), \\\"label:\\\", id2label[int(y_pred[i])])\", \"mistakes = np.where(y_true != y_pred)[0][:10]\\nprint(\\\"num_errors:\\\", int((y_true != y_pred).sum()))\\n\\nvault.create_record_list(\\\"mrpc_paraphrase_inference_distilbert_mistakes\\\", column_names=[\\\"idx\\\", \\\"sentence1\\\", \\\"sentence2\\\", \\\"true\\\", \\\"pred\\\"])\\n\\nfor i in mistakes:\\n    print(\\\"=\\\" * 80)\\n    print(\\\"idx:\\\", int(i))\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n\\n    vault.append_record(\\\"mrpc_paraphrase_inference_distilbert_mistakes\\\", {\\n            \\\"idx\\\": int(i),\\n            \\\"sentence1\\\": sent1[i],\\n            \\\"sentence2\\\": sent2[i],\\n            \\\"true\\\": int(y_true[i]),\\n            \\\"pred\\\": int(y_pred[i]),\\n        },\\n        input_items = {\\n            \\\"glue_mrpc_validation\\\": [int(i), int(i)+ 1],\\n            \\\"mrpc_distilbert_predictions\\\": [int(i), int(i)+ 1]\\n        }\\n    )\\n\\ndescription = \\\"Subset of error cases from the GLUE MRPC validation run using the textattack/distilbert-base-uncased-MRPC model. Each record captures one misclassified sentence pair and includes the fields: idx (validation-set position), sentence1, sentence2, true (ground-truth binary label), and pred (model-predicted binary label). This dataset is created by selecting the first 10 examples where the model prediction differs from the true label, and each record is linked back to the corresponding source example in glue_mrpc_validation and its entry in mrpc_distilbert_predictions. Its role in the workflow is error analysis: it provides a compact, inspectable sample of model failures for diagnosing paraphrase detection mistakes.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"mrpc_paraphrase_inference_distilbert_mistakes\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_type\\\": \\\"error analysis subset\\\", \\\"subset\\\": \\\"model mistakes\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"split\\\": \\\"validation\\\", \\\"model\\\": \\\"textattack/distilbert-base-uncased-MRPC\\\", \\\"framework\\\": \\\"transformers\\\", \\\"input_format\\\": \\\"sentence pair\\\", \\\"label_space\\\": \\\"0=not_paraphrase, 1=paraphrase\\\", \\\"content\\\": \\\"misclassified validation examples with true and predicted labels\\\", \\\"size\\\": \\\"10\\\", \\\"sampling\\\": \\\"first 10 misclassifications\\\", \\\"parent_datasets\\\": \\\"glue_mrpc_validation,mrpc_distilbert_predictions\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"mrpc_paraphrase_inference_distilbert_mistakes\\\", cat, embedding, prop)\\n\", \"vault.create_record_list(\\\"mrpc_paraphrase_inference_distilbert_output\\\", column_names=[\\\"accuracy\\\", \\\"f1\\\", \\\"classification_report\\\"])\\n\\n\\nsummary = {\\n    \\\"accuracy\\\": float(acc),\\n    \\\"f1\\\": float(f1),\\n    \\\"classification_report\\\": str(report)\\n}\\n\\nvault.append_record(\\\"mrpc_paraphrase_inference_distilbert_output\\\", summary,\\n                    input_items = {\\n                        \\\"glue_mrpc_validation\\\": [0, len(ds)],\\n                        \\\"mrpc_distilbert_predictions\\\": [0, len(ds)]\\n                    })\\n\\nsummary\\n\\ndescription = \\\"This dataset contains the final evaluation summary for the textattack/distilbert-base-uncased-MRPC model on the GLUE MRPC validation split. It is a small output table with one record summarizing model performance over the full validation dataset.\\\\n\\\\nFields:\\\\n- accuracy: overall classification accuracy on the validation set\\\\n- f1: F1 score for the paraphrase classification task\\\\n- classification_report: full text report from sklearn including precision, recall, F1, and support for the not_paraphrase and paraphrase classes\\\\n\\\\nIn this workflow, this dataset serves as the final results artifact. It is created after running batched inference on sentence pairs, comparing predictions against ground-truth labels, and aggregating the metrics. The record is linked to the full validation input dataset and the prediction dataset so a user can trace the reported metrics back to the underlying examples and model outputs.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"mrpc_paraphrase_inference_distilbert_output\\\", description, embedding)\\n\\nproperties = {\\\"artifact_type\\\": \\\"evaluation_output\\\", \\\"task\\\": \\\"paraphrase_detection\\\", \\\"source_dataset\\\": \\\"glue/mrpc\\\", \\\"split\\\": \\\"validation\\\", \\\"evaluation_examples\\\": \\\"408\\\", \\\"input_format\\\": \\\"sentence_pair\\\", \\\"model\\\": \\\"textattack/distilbert-base-uncased-MRPC\\\", \\\"framework\\\": \\\"transformers\\\", \\\"metrics\\\": \\\"accuracy,f1,classification_report\\\", \\\"labels\\\": \\\"not_paraphrase,paraphrase\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"mrpc_paraphrase_inference_distilbert_output\\\", cat, embedding, prop)\", \"description = \\\"This notebook runs a paraphrase detection inference workflow on the GLUE MRPC validation set using the pretrained Hugging Face model textattack/distilbert-base-uncased-MRPC. It loads sentence pairs and labels from the dataset, performs batched tokenization and prediction with DistilBERT on the available device, and evaluates results with accuracy, F1, and a full classification report. The workflow stores the source validation records, model predictions, error examples, and final summary metrics in TableVault so the inputs, outputs, and lineage between them are traceable. It also creates semantic descriptions and property metadata embeddings for the dataset, prediction table, mistakes table, output summary, and overall notebook process. Overall, the notebook is designed to both benchmark a pretrained MRPC paraphrase classifier and document the complete inference pipeline in a searchable experiment vault.\\\" # description of whole notebook\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"mrpc_paraphrase_inference_distilbert\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"problem_type\\\": \\\"binary text pair classification\\\", \\\"model\\\": \\\"textattack/distilbert-base-uncased-MRPC\\\", \\\"model_family\\\": \\\"DistilBERT\\\", \\\"dataset\\\": \\\"glue/mrpc\\\", \\\"dataset_split\\\": \\\"validation\\\", \\\"framework\\\": \\\"PyTorch\\\", \\\"library\\\": \\\"Hugging Face Transformers\\\", \\\"evaluation\\\": \\\"accuracy, f1-score, classification report\\\", \\\"inference_type\\\": \\\"batched inference\\\", \\\"tracking\\\": \\\"TableVault\\\", \\\"embedding_model\\\": \\\"text-embedding-3-large\\\", \\\"device\\\": \\\"mps_or_cpu\\\", \\\"outputs\\\": \\\"predictions, mistakes, summary metrics\\\", \\\"domain\\\": \\\"natural language processing\\\"} #e.g. model: distilbert-base-uncased-MRPC\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"mrpc_paraphrase_inference_distilbert\\\", cat, embedding, prop)\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c4fd7688195b9b2ca4f75d74d18`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_search",
    "call_id": "call_9LpF1mcYh0nCl7bowsj2SAyt",
    "arguments": {
      "code": "candidate_labels = [\"paraphrase\", \"not paraphrase\"]"
    }
  }
]
```

### Tool Call
**Tool:** `code_search` | **call_id:** `call_9LpF1mcYh0nCl7bowsj2SAyt`

**Arguments:**
```json
{
  "code": "candidate_labels = [\"paraphrase\", \"not paraphrase\"]"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": []
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 36461 | 69 | 36 | 34891 | 2.031s | 0.067s |

---

## Turn 23 — `code_search` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c51ee64819591b73526b4679381`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_9LpF1mcYh0nCl7bowsj2SAyt",
    "output": "{\"ok\": true, \"result\": []}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c51ee64819591b73526b4679381`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_search",
    "call_id": "call_iAt6EeJWTiQLgKRxevTKNd2x",
    "arguments": {
      "code": "bart-large-mnli"
    }
  }
]
```

### Tool Call
**Tool:** `code_search` | **call_id:** `call_iAt6EeJWTiQLgKRxevTKNd2x`

**Arguments:**
```json
{
  "code": "bart-large-mnli"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": []
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 36551 | 40 | 16 | 34981 | 1.571s | 0.041s |

---

## Turn 24 — `code_search` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c538d00819581a04b471ae5fb4f`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_iAt6EeJWTiQLgKRxevTKNd2x",
    "output": "{\"ok\": true, \"result\": []}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c538d00819581a04b471ae5fb4f`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_search",
    "call_id": "call_YBt1wpuYem9Ms8ZMFZ13gNRX",
    "arguments": {
      "code": "task=\"zero-shot-classification\""
    }
  }
]
```

### Tool Call
**Tool:** `code_search` | **call_id:** `call_YBt1wpuYem9Ms8ZMFZ13gNRX`

**Arguments:**
```json
{
  "code": "task=\"zero-shot-classification\""
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "entailment_logprob_odds_mrpc",
    "gent_1775914190",
    "gent_1775874933",
    "gent_1775874373",
    "softmax_gap_mean_mrpc",
    "flan_t5_contextual_calibrated_yes_no_mrpc",
    "neutral_penalized_margin_mrpc",
    "flan_t5_symmetric_prompt_average_mrpc",
    "gent_1775874650",
    "gent_1775913615",
    "gent_1775914000",
    "flan_t5_true_false_first_step_mrpc",
    "consensus_then_avg_margin_mrpc",
    "min_direction_margin_mrpc"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 36612 | 118 | 92 | 35042 | 3.030s | 0.060s |

---

## Turn 25 — `code_search` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c56a32c8195b6d49b7598f29caa`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_YBt1wpuYem9Ms8ZMFZ13gNRX",
    "output": "{\"ok\": true, \"result\": [\"entailment_logprob_odds_mrpc\", \"gent_1775914190\", \"gent_1775874933\", \"gent_1775874373\", \"softmax_gap_mean_mrpc\", \"flan_t5_contextual_calibrated_yes_no_mrpc\", \"neutral_penalized_margin_mrpc\", \"flan_t5_symmetric_prompt_average_mrpc\", \"gent_1775874650\", \"gent_1775913615\", \"gent_1775914000\", \"flan_t5_true_false_first_step_mrpc\", \"consensus_then_avg_margin_mrpc\", \"min_direction_margin_mrpc\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c56a32c8195b6d49b7598f29caa`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_search",
    "call_id": "call_mFePxPEl14ouMuPIQbvIHQGn",
    "arguments": {
      "code": "hypothesis_template"
    }
  }
]
```

### Tool Call
**Tool:** `code_search` | **call_id:** `call_mFePxPEl14ouMuPIQbvIHQGn`

**Arguments:**
```json
{
  "code": "hypothesis_template"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": []
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 36881 | 80 | 58 | 35311 | 2.499s | 0.005s |

---

## Turn 26 — `code_search` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c5925a081959b1b1335b708488c`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_mFePxPEl14ouMuPIQbvIHQGn",
    "output": "{\"ok\": true, \"result\": []}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c5925a081959b1b1335b708488c`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_search",
    "call_id": "call_R9qrUaWu6hFCwvxEaj9ODt8g",
    "arguments": {
      "code": "zero shot"
    }
  }
]
```

### Tool Call
**Tool:** `code_search` | **call_id:** `call_R9qrUaWu6hFCwvxEaj9ODt8g`

**Arguments:**
```json
{
  "code": "zero shot"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "entailment_logprob_odds_mrpc",
    "gent_1775914190",
    "gent_1775874933",
    "gent_1775874373",
    "softmax_gap_mean_mrpc",
    "flan_t5_contextual_calibrated_yes_no_mrpc",
    "neutral_penalized_margin_mrpc",
    "flan_t5_symmetric_prompt_average_mrpc",
    "gent_1775874650",
    "gent_1775913615",
    "gent_1775914000",
    "flan_t5_true_false_first_step_mrpc",
    "consensus_then_avg_margin_mrpc",
    "min_direction_margin_mrpc"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 36982 | 44 | 23 | 35412 | 4.603s | 0.049s |

---

## Turn 27 — `get_item` [ERROR]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c5dcabc819590351faeb92e1fd3`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_R9qrUaWu6hFCwvxEaj9ODt8g",
    "output": "{\"ok\": true, \"result\": [\"entailment_logprob_odds_mrpc\", \"gent_1775914190\", \"gent_1775874933\", \"gent_1775874373\", \"softmax_gap_mean_mrpc\", \"flan_t5_contextual_calibrated_yes_no_mrpc\", \"neutral_penalized_margin_mrpc\", \"flan_t5_symmetric_prompt_average_mrpc\", \"gent_1775874650\", \"gent_1775913615\", \"gent_1775914000\", \"flan_t5_true_false_first_step_mrpc\", \"consensus_then_avg_margin_mrpc\", \"min_direction_margin_mrpc\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c5dcabc819590351faeb92e1fd3`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_3A2xKop9Unel1N1Q0n6E8zCO",
    "arguments": {
      "item_name": "bidirectional_averaged_zero_shot_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_3A2xKop9Unel1N1Q0n6E8zCO`

**Arguments:**
```json
{
  "item_name": "bidirectional_averaged_zero_shot_mrpc_summary",
  "start_position": 0,
  "end_position": 5
}
```

### Tool Output
```json
{
  "ok": false,
  "error": "Name given isn't a registered item list"
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 37177 | 126 | 85 | 35607 | 2.818s | 0.004s |

### Error
```
Name given isn't a registered item list
```

---

## Turn 28 — `code_search` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c609cf88195b4edd32b89f438cd`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_3A2xKop9Unel1N1Q0n6E8zCO",
    "output": "{\"ok\": false, \"error\": \"Name given isn't a registered item list\"}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c609cf88195b4edd32b89f438cd`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_search",
    "call_id": "call_F5WLs4PBJD9DLyXE7W3wag6s",
    "arguments": {
      "code": "bidirectional averaging"
    }
  }
]
```

### Tool Call
**Tool:** `code_search` | **call_id:** `call_F5WLs4PBJD9DLyXE7W3wag6s`

**Arguments:**
```json
{
  "code": "bidirectional averaging"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "entailment_logprob_odds_mrpc",
    "gent_1775914190",
    "gent_1775874933",
    "gent_1775874373",
    "gent_1775874650",
    "gent_1775913615",
    "gent_1775914000",
    "consensus_then_avg_margin_mrpc",
    "hf_pipeline_mrpc_bidirectional_order_average"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 37331 | 52 | 30 | 35761 | 4.535s | 0.050s |

---

## Turn 29 — `code_search` [ok]

### Model Input
**previous_response_id:** `resp_0024ef54afa3d6830069da5c6533548195955be8d74b3cc9bb`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_F5WLs4PBJD9DLyXE7W3wag6s",
    "output": "{\"ok\": true, \"result\": [\"entailment_logprob_odds_mrpc\", \"gent_1775914190\", \"gent_1775874933\", \"gent_1775874373\", \"gent_1775874650\", \"gent_1775913615\", \"gent_1775914000\", \"consensus_then_avg_margin_mrpc\", \"hf_pipeline_mrpc_bidirectional_order_average\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0024ef54afa3d6830069da5c6533548195955be8d74b3cc9bb`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_search",
    "call_id": "call_sgEDNJG58OHKi4ZevEJTwzjz",
    "arguments": {
      "code": "from transformers import pipeline"
    }
  }
]
```

### Tool Call
**Tool:** `code_search` | **call_id:** `call_sgEDNJG58OHKi4ZevEJTwzjz`

**Arguments:**
```json
{
  "code": "from transformers import pipeline"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "gent_1775914190",
    "gent_1775874933",
    "hf_pipeline_mrpc_short_maxlen_64",
    "gent_1775874373",
    "gent_1775874650",
    "hf_pipeline_mrpc_raw_logits_softmax",
    "gent_1775914000",
    "gent_1775913615",
    "hf_pipeline_mrpc_threshold_070",
    "hf_pipeline_mrpc_bidirectional_order_average"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 37481 | 84 | 61 | 35911 | 3.504s | 0.081s |

---

# Run Summary

**Run ended with error:**
```
Max turns reached before finalize_result.
```

**Metrics Summary:**
```json
{
  "tokens": {
    "input": 779926,
    "output": 2733,
    "reasoning": 1941,
    "total": 782659,
    "system_estimate": 1570,
    "conversation": 732925
  },
  "code": {
    "executions": 0,
    "failed_executions": 0,
    "total_lines": 0
  },
  "timing": {
    "api_latency_s": 84.387,
    "exec_latency_s": 0.944,
    "wall_time_s": 85.331
  },
  "api_calls": 30,
  "cost": null
}
```
