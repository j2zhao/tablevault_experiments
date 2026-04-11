# Agent Trace — 20260411T142949Z

**Model:** `gpt-5.4`  
**Timestamp:** 2026-04-11T14:29:49.590473+00:00  
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

## Turn 0 — `get_item_names` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5adda86c81988ef697868ca7d173`

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
**response_id:** `resp_0c2409105c899fb80069da5adda86c81988ef697868ca7d173`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "get_item_names",
    "call_id": "call_bUips5Tt2756gGewsDTmlTCL",
    "arguments": {
      "item_type": "record_list"
    }
  }
]
```

### Tool Call
**Tool:** `get_item_names` | **call_id:** `call_bUips5Tt2756gGewsDTmlTCL`

**Arguments:**
```json
{
  "item_type": "record_list"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "consensus_then_avg_margin_mrpc_summary",
    "cosine_mrpc_max_pool_similarity_prediction",
    "cosine_mrpc_mean_similarity_prediction",
    "cosine_mrpc_threshold_score",
    "distilbert_cls_cosine_mrpc_summary",
    "distilbert_cross_text_prediction",
    "distilbert_cross_text_prediction_cutoff",
    "distilbert_last4_mean_cosine_mrpc_summary",
    "distilbert_margin_score_prediction_values",
    "distilbert_max_pool_cosine_mrpc_summary",
    "distilbert_mean_cosine_median_threshold_mrpc_summary",
    "distilbert_no_special_tokens_mean_cosine_mrpc_summary",
    "distilbert_quora_softmax_prediction",
    "distilbert_swap_prediction_values",
    "distilbert_symmetric_average_prediction",
    "distilbert-normalized-text-prediction",
    "entailment_logprob_odds_mrpc_summary",
    "flan_prediction_and_logit_prefix",
    "flan_prediction_logit_calibrated",
    "flan_prediction_scored",
    "flan_t5_answer_prefix_yes_no_mrpcc_summary",
    "flan_t5_contextual_calibrated_yes_no_mrpc_summary",
    "flan_t5_full_answer_logprob_mrpc_summary",
    "flan_t5_symmetric_prompt_average_mrpc_summary",
    "flan_t5_true_false_first_step_mrpc_summary",
    "glue_mrpc_validation",
    "google_flan_prediction_and_logits",
    "google_flan_prediction_swapped",
    "hf_pipeline_mrpc_bidirectional_order_average_summary",
    "hf_pipeline_mrpc_margin_rule_summary",
    "hf_pipeline_mrpc_raw_logits_softmax_summary",
    "hf_pipeline_mrpc_short_maxlen_64_summary",
    "hf_pipeline_mrpc_threshold_070_summary",
    "min_direction_margin_mrpc_summary",
    "minilm_cosine_threshold_prediction",
    "mrpc_distilbert_predictions",
    "mrpc_entailment_prediction",
    "mrpc_gate_margin_prediction",
    "mrpc_mean_gap_prediction",
    "mrpc_min_margin_prediction",
    "mrpc_neutral_penalty_prediction",
    "mrpc_paraphrase_inference_distilbert_mistakes",
    "mrpc_paraphrase_inference_distilbert_output",
    "neutral_penalized_margin_mrpc_summary",
    "no_special_cosine_mrpc_similarity_prediction",
    "pipeline_distilbert_shortened",
    "pipeline_distilbert_softmax_probs",
    "pipeline_distilbert_threshold",
    "quora_cross_encoder_max_length_64_mrpc_summary",
    "quora_cross_encoder_prefixed_sentence_tags_mrpc_summary",
    "quora_cross_encoder_softmax_threshold_065_mrpc_summary",
    "quora_cross_encoder_symmetric_average_mrpc_summary",
    "quora_cross_encoder_text_normalized_mrpc_summary",
    "sentence_transformers_mrpc_prediction_distance",
    "sentence_transformers_mrpc_prediction_max64",
    "sentence_transformers_mrpc_prediction_threshold",
    "sentence_transformers_mrpc_prediction_threshold_2",
    "softmax_gap_mean_mrpc_summary",
    "st_all_distilroberta_v1_cosine_threshold_mrpc_summary",
    "st_all_minilm_l6_l2_distance_threshold_mrpc_summary",
    "st_all_minilm_l6_max_seq_len_64_cosine_mrpc_summary",
    "st_paraphrase_minilm_l3_cosine_threshold_mrpc_summary",
    "st_paraphrase_minilm_l6_cosine_threshold_mrpc_summary",
    "threshold_cosine_mrpc_similarity_prediction"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 1580 | 115 | 92 | 0 | 2.521s | 0.025s |

---

## Turn 1 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5ae0365481989b6639192014a83b`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_bUips5Tt2756gGewsDTmlTCL",
    "output": "{\"ok\": true, \"result\": [\"consensus_then_avg_margin_mrpc_summary\", \"cosine_mrpc_max_pool_similarity_prediction\", \"cosine_mrpc_mean_similarity_prediction\", \"cosine_mrpc_threshold_score\", \"distilbert_cls_cosine_mrpc_summary\", \"distilbert_cross_text_prediction\", \"distilbert_cross_text_prediction_cutoff\", \"distilbert_last4_mean_cosine_mrpc_summary\", \"distilbert_margin_score_prediction_values\", \"distilbert_max_pool_cosine_mrpc_summary\", \"distilbert_mean_cosine_median_threshold_mrpc_summary\", \"distilbert_no_special_tokens_mean_cosine_mrpc_summary\", \"distilbert_quora_softmax_prediction\", \"distilbert_swap_prediction_values\", \"distilbert_symmetric_average_prediction\", \"distilbert-normalized-text-prediction\", \"entailment_logprob_odds_mrpc_summary\", \"flan_prediction_and_logit_prefix\", \"flan_prediction_logit_calibrated\", \"flan_prediction_scored\", \"flan_t5_answer_prefix_yes_no_mrpcc_summary\", \"flan_t5_contextual_calibrated_yes_no_mrpc_summary\", \"flan_t5_full_answer_logprob_mrpc_summary\", \"flan_t5_symmetric_prompt_average_mrpc_summary\", \"flan_t5_true_false_first_step_mrpc_summary\", \"glue_mrpc_validation\", \"google_flan_prediction_and_logits\", \"google_flan_prediction_swapped\", \"hf_pipeline_mrpc_bidirectional_order_average_summary\", \"hf_pipeline_mrpc_margin_rule_summary\", \"hf_pipeline_mrpc_raw_logits_softmax_summary\", \"hf_pipeline_mrpc_short_maxlen_64_summary\", \"hf_pipeline_mrpc_threshold_070_summary\", \"min_direction_margin_mrpc_summary\", \"minilm_cosine_threshold_prediction\", \"mrpc_distilbert_predictions\", \"mrpc_entailment_prediction\", \"mrpc_gate_margin_prediction\", \"mrpc_mean_gap_prediction\", \"mrpc_min_margin_prediction\", \"mrpc_neutral_penalty_prediction\", \"mrpc_paraphrase_inference_distilbert_mistakes\", \"mrpc_paraphrase_inference_distilbert_output\", \"neutral_penalized_margin_mrpc_summary\", \"no_special_cosine_mrpc_similarity_prediction\", \"pipeline_distilbert_shortened\", \"pipeline_distilbert_softmax_probs\", \"pipeline_distilbert_threshold\", \"quora_cross_encoder_max_length_64_mrpc_summary\", \"quora_cross_encoder_prefixed_sentence_tags_mrpc_summary\", \"quora_cross_encoder_softmax_threshold_065_mrpc_summary\", \"quora_cross_encoder_symmetric_average_mrpc_summary\", \"quora_cross_encoder_text_normalized_mrpc_summary\", \"sentence_transformers_mrpc_prediction_distance\", \"sentence_transformers_mrpc_prediction_max64\", \"sentence_transformers_mrpc_prediction_threshold\", \"sentence_transformers_mrpc_prediction_threshold_2\", \"softmax_gap_mean_mrpc_summary\", \"st_all_distilroberta_v1_cosine_threshold_mrpc_summary\", \"st_all_minilm_l6_l2_distance_threshold_mrpc_summary\", \"st_all_minilm_l6_max_seq_len_64_cosine_mrpc_summary\", \"st_paraphrase_minilm_l3_cosine_threshold_mrpc_summary\", \"st_paraphrase_minilm_l6_cosine_threshold_mrpc_summary\", \"threshold_cosine_mrpc_similarity_prediction\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5ae0365481989b6639192014a83b`

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
    "call_id": "call_oYAZ26j1mQ7oavocbXzP7EgU",
    "arguments": {
      "item_name": "hf_pipeline_mrpc_raw_logits_softmax_summary",
      "start_position": 0,
      "end_position": 10
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_oYAZ26j1mQ7oavocbXzP7EgU`

**Arguments:**
```json
{
  "item_name": "hf_pipeline_mrpc_raw_logits_softmax_summary",
  "start_position": 0,
  "end_position": 10
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    {
      "accuracy": 0.8578431372549019,
      "f1": 0.9026845637583892,
      "classification_report": "              precision    recall  f1-score   support\n\n     LABEL_0       0.89      0.63      0.74       129\n     LABEL_1       0.85      0.96      0.90       279\n\n    accuracy                           0.86       408\n   macro avg       0.87      0.80      0.82       408\nweighted avg       0.86      0.86      0.85       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 2401 | 203 | 164 | 692 | 3.791s | 0.019s |

---

## Turn 2 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5ae403f081989cce1f46c199c2f4`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_oYAZ26j1mQ7oavocbXzP7EgU",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.8578431372549019, \"f1\": 0.9026845637583892, \"classification_report\": \"              precision    recall  f1-score   support\\n\\n     LABEL_0       0.89      0.63      0.74       129\\n     LABEL_1       0.85      0.96      0.90       279\\n\\n    accuracy                           0.86       408\\n   macro avg       0.87      0.80      0.82       408\\nweighted avg       0.86      0.86      0.85       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5ae403f081989cce1f46c199c2f4`

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
    "call_id": "call_gqQ0Sur2Ls76u4tj4wIEfOlm",
    "arguments": {
      "item_name": "hf_pipeline_mrpc_bidirectional_order_average_summary",
      "start_position": 0,
      "end_position": 10
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_gqQ0Sur2Ls76u4tj4wIEfOlm`

**Arguments:**
```json
{
  "item_name": "hf_pipeline_mrpc_bidirectional_order_average_summary",
  "start_position": 0,
  "end_position": 10
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    {
      "accuracy": 0.8504901960784313,
      "f1": 0.897822445561139,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.88      0.61      0.72       129\n    paraphrase       0.84      0.96      0.90       279\n\n      accuracy                           0.85       408\n     macro avg       0.86      0.79      0.81       408\n  weighted avg       0.85      0.85      0.84       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 2770 | 91 | 52 | 1061 | 2.052s | 0.012s |

---

## Turn 3 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5ae6153881989f737ebce52f949f`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_gqQ0Sur2Ls76u4tj4wIEfOlm",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.8504901960784313, \"f1\": 0.897822445561139, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.88      0.61      0.72       129\\n    paraphrase       0.84      0.96      0.90       279\\n\\n      accuracy                           0.85       408\\n     macro avg       0.86      0.79      0.81       408\\n  weighted avg       0.85      0.85      0.84       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5ae6153881989f737ebce52f949f`

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
    "call_id": "call_CFVjfsPTgQBGchxJfUYKic6q",
    "arguments": {
      "item_name": "hf_pipeline_mrpc_margin_rule_summary",
      "start_position": 0,
      "end_position": 10
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_CFVjfsPTgQBGchxJfUYKic6q`

**Arguments:**
```json
{
  "item_name": "hf_pipeline_mrpc_margin_rule_summary",
  "start_position": 0,
  "end_position": 10
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    {
      "accuracy": 0.8627450980392157,
      "f1": 0.9044368600682594,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.86      0.67      0.76       129\n    paraphrase       0.86      0.95      0.90       279\n\n      accuracy                           0.86       408\n     macro avg       0.86      0.81      0.83       408\n  weighted avg       0.86      0.86      0.86       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 3026 | 49 | 12 | 1317 | 1.506s | 0.023s |

---

## Turn 4 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5ae797fc8198bcda6917b96f0f02`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_CFVjfsPTgQBGchxJfUYKic6q",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.8627450980392157, \"f1\": 0.9044368600682594, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.86      0.67      0.76       129\\n    paraphrase       0.86      0.95      0.90       279\\n\\n      accuracy                           0.86       408\\n     macro avg       0.86      0.81      0.83       408\\n  weighted avg       0.86      0.86      0.86       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5ae797fc8198bcda6917b96f0f02`

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
    "call_id": "call_4nF3cjXYoUrSGamFL94ax3CO",
    "arguments": {
      "item_name": "hf_pipeline_mrpc_threshold_070_summary",
      "start_position": 0,
      "end_position": 10
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_4nF3cjXYoUrSGamFL94ax3CO`

**Arguments:**
```json
{
  "item_name": "hf_pipeline_mrpc_threshold_070_summary",
  "start_position": 0,
  "end_position": 10
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    {
      "accuracy": 0.8480392156862745,
      "f1": 0.8896797153024911,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase     0.7680    0.7442    0.7559       129\n    paraphrase     0.8834    0.8961    0.8897       279\n\n      accuracy                         0.8480       408\n     macro avg     0.8257    0.8201    0.8228       408\n  weighted avg     0.8469    0.8480    0.8474       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 3241 | 48 | 10 | 1532 | 1.606s | 0.017s |

---

## Turn 5 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5ae93f948198a160e81df3bda476`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_4nF3cjXYoUrSGamFL94ax3CO",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.8480392156862745, \"f1\": 0.8896797153024911, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase     0.7680    0.7442    0.7559       129\\n    paraphrase     0.8834    0.8961    0.8897       279\\n\\n      accuracy                         0.8480       408\\n     macro avg     0.8257    0.8201    0.8228       408\\n  weighted avg     0.8469    0.8480    0.8474       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5ae93f948198a160e81df3bda476`

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
    "call_id": "call_ey17xzraKhhFGoU5eKQZWc2t",
    "arguments": {
      "item_name": "flan_t5_full_answer_logprob_mrpc_summary",
      "start_position": 0,
      "end_position": 10
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_ey17xzraKhhFGoU5eKQZWc2t`

**Arguments:**
```json
{
  "item_name": "flan_t5_full_answer_logprob_mrpc_summary",
  "start_position": 0,
  "end_position": 10
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    {
      "accuracy": 0.6495098039215687,
      "f1": 0.6911447084233261,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.47      0.81      0.59       129\n    paraphrase       0.87      0.57      0.69       279\n\n      accuracy                           0.65       408\n     macro avg       0.67      0.69      0.64       408\n  weighted avg       0.74      0.65      0.66       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 3468 | 64 | 23 | 1759 | 1.516s | 0.007s |

---

## Turn 6 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5aeac83c81989919007248820712`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_ey17xzraKhhFGoU5eKQZWc2t",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.6495098039215687, \"f1\": 0.6911447084233261, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.47      0.81      0.59       129\\n    paraphrase       0.87      0.57      0.69       279\\n\\n      accuracy                           0.65       408\\n     macro avg       0.67      0.69      0.64       408\\n  weighted avg       0.74      0.65      0.66       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5aeac83c81989919007248820712`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_OwXQowOJBSi84ZvbeIbTdJhK",
    "arguments": {
      "item_name": "flan_t5_symmetric_prompt_average_mrpc_summary",
      "start_position": 0,
      "end_position": 10
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_OwXQowOJBSi84ZvbeIbTdJhK`

**Arguments:**
```json
{
  "item_name": "flan_t5_symmetric_prompt_average_mrpc_summary",
  "start_position": 0,
  "end_position": 10
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    {
      "accuracy": 0.7377450980392157,
      "f1": 0.8065099457504521,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.58      0.60      0.59       129\n    paraphrase       0.81      0.80      0.81       279\n\n      accuracy                           0.74       408\n     macro avg       0.70      0.70      0.70       408\n  weighted avg       0.74      0.74      0.74       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 3698 | 39 | 0 | 1989 | 1.190s | 0.007s |

---

## Turn 7 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5aebf3e481988367bbf2c6ce0358`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_OwXQowOJBSi84ZvbeIbTdJhK",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.7377450980392157, \"f1\": 0.8065099457504521, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.58      0.60      0.59       129\\n    paraphrase       0.81      0.80      0.81       279\\n\\n      accuracy                           0.74       408\\n     macro avg       0.70      0.70      0.70       408\\n  weighted avg       0.74      0.74      0.74       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5aebf3e481988367bbf2c6ce0358`

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
    "call_id": "call_MI6Nx0hwxtgS0AIhhdSf704l",
    "arguments": {
      "item_name": "consensus_then_avg_margin_mrpc_summary",
      "start_position": 0,
      "end_position": 10
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_MI6Nx0hwxtgS0AIhhdSf704l`

**Arguments:**
```json
{
  "item_name": "consensus_then_avg_margin_mrpc_summary",
  "start_position": 0,
  "end_position": 10
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    {
      "accuracy": 0.7009803921568627,
      "f1": 0.769811320754717,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.52      0.64      0.57       129\n    paraphrase       0.81      0.73      0.77       279\n\n      accuracy                           0.70       408\n     macro avg       0.67      0.68      0.67       408\n  weighted avg       0.72      0.70      0.71       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 3903 | 180 | 142 | 2194 | 2.913s | 0.025s |

---

## Turn 8 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5aeee7888198b1fa050a6361693b`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_MI6Nx0hwxtgS0AIhhdSf704l",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.7009803921568627, \"f1\": 0.769811320754717, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.52      0.64      0.57       129\\n    paraphrase       0.81      0.73      0.77       279\\n\\n      accuracy                           0.70       408\\n     macro avg       0.67      0.68      0.67       408\\n  weighted avg       0.72      0.70      0.71       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5aeee7888198b1fa050a6361693b`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_S0ux9xeSjDZaxF9NykN0ixxr",
    "arguments": {
      "item_name": "entailment_logprob_odds_mrpc_summary",
      "start_position": 0,
      "end_position": 10
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_S0ux9xeSjDZaxF9NykN0ixxr`

**Arguments:**
```json
{
  "item_name": "entailment_logprob_odds_mrpc_summary",
  "start_position": 0,
  "end_position": 10
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
| 4248 | 38 | 0 | 2539 | 1.392s | 0.011s |

---

## Turn 9 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5af04b8081988736087e320356e2`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_S0ux9xeSjDZaxF9NykN0ixxr",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.7034313725490197, \"f1\": 0.7729831144465291, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.53      0.63      0.57       129\\n    paraphrase       0.81      0.74      0.77       279\\n\\n      accuracy                           0.70       408\\n     macro avg       0.67      0.68      0.67       408\\n  weighted avg       0.72      0.70      0.71       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5af04b8081988736087e320356e2`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_bDsg7iOojAxsAxzIIyUm7Dbm",
    "arguments": {
      "item_name": "min_direction_margin_mrpc_summary",
      "start_position": 0,
      "end_position": 10
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_bDsg7iOojAxsAxzIIyUm7Dbm`

**Arguments:**
```json
{
  "item_name": "min_direction_margin_mrpc_summary",
  "start_position": 0,
  "end_position": 10
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
| 4452 | 34 | 0 | 2743 | 1.213s | 0.007s |

---

## Turn 10 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5af180e881989a9e2320ed0ed9ed`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_bDsg7iOojAxsAxzIIyUm7Dbm",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.5857843137254902, \"f1\": 0.5888077858880778, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.43      0.91      0.58       129\\n    paraphrase       0.92      0.43      0.59       279\\n\\n      accuracy                           0.59       408\\n     macro avg       0.67      0.67      0.59       408\\n  weighted avg       0.76      0.59      0.59       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5af180e881989a9e2320ed0ed9ed`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_Dw0h5OVJfrZ4Pj1XfefXB7MB",
    "arguments": {
      "item_name": "neutral_penalized_margin_mrpc_summary",
      "start_position": 0,
      "end_position": 10
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_Dw0h5OVJfrZ4Pj1XfefXB7MB`

**Arguments:**
```json
{
  "item_name": "neutral_penalized_margin_mrpc_summary",
  "start_position": 0,
  "end_position": 10
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    {
      "accuracy": 0.5563725490196079,
      "f1": 0.5322997416020672,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.41      0.96      0.58       129\n    paraphrase       0.95      0.37      0.53       279\n\n      accuracy                           0.56       408\n     macro avg       0.68      0.67      0.56       408\n  weighted avg       0.78      0.56      0.55       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 4652 | 36 | 0 | 2943 | 1.296s | 0.012s |

---

## Turn 11 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5af2d23c8198a5962941f1c86151`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_Dw0h5OVJfrZ4Pj1XfefXB7MB",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.5563725490196079, \"f1\": 0.5322997416020672, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.41      0.96      0.58       129\\n    paraphrase       0.95      0.37      0.53       279\\n\\n      accuracy                           0.56       408\\n     macro avg       0.68      0.67      0.56       408\\n  weighted avg       0.78      0.56      0.55       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5af2d23c8198a5962941f1c86151`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_ma6a6bAWrkmp3TMZP4XiOJss",
    "arguments": {
      "item_name": "softmax_gap_mean_mrpc_summary",
      "start_position": 0,
      "end_position": 10
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_ma6a6bAWrkmp3TMZP4XiOJss`

**Arguments:**
```json
{
  "item_name": "softmax_gap_mean_mrpc_summary",
  "start_position": 0,
  "end_position": 10
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    {
      "accuracy": 0.7181372549019608,
      "f1": 0.7905282331511839,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.55      0.59      0.57       129\n    paraphrase       0.80      0.78      0.79       279\n\n      accuracy                           0.72       408\n     macro avg       0.68      0.68      0.68       408\n  weighted avg       0.72      0.72      0.72       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 4854 | 35 | 0 | 3145 | 1.146s | 0.014s |

---

## Turn 12 — `get_code_names` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5af3fb9c8198aab00d70f4ff289a`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_ma6a6bAWrkmp3TMZP4XiOJss",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.7181372549019608, \"f1\": 0.7905282331511839, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.55      0.59      0.57       129\\n    paraphrase       0.80      0.78      0.79       279\\n\\n      accuracy                           0.72       408\\n     macro avg       0.68      0.68      0.68       408\\n  weighted avg       0.72      0.72      0.72       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5af3fb9c8198aab00d70f4ff289a`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "get_code_names",
    "call_id": "call_A1nfgdEGSRxaUJ9ECgMnbv7O",
    "arguments": {}
  }
]
```

### Tool Call
**Tool:** `get_code_names` | **call_id:** `call_A1nfgdEGSRxaUJ9ECgMnbv7O`

**Arguments:**
```json
{}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "consensus_then_avg_margin_mrpc",
    "distilbert_cls_cosine_mrpc",
    "distilbert_last4_mean_cosine_mrpc",
    "distilbert_max_pool_cosine_mrpc",
    "distilbert_mean_cosine_median_threshold_mrpc",
    "distilbert_no_special_tokens_mean_cosine_mrpc",
    "entailment_logprob_odds_mrpc",
    "flan_t5_answer_prefix_yes_no_mrpc",
    "flan_t5_contextual_calibrated_yes_no_mrpc",
    "flan_t5_full_answer_logprob_mrpc",
    "flan_t5_symmetric_prompt_average_mrpc",
    "flan_t5_true_false_first_step_mrpc",
    "gent_1775874373",
    "gent_1775874650",
    "gent_1775874933",
    "gent_1775913615",
    "gent_1775914000",
    "gent_1775914190",
    "hf_pipeline_mrpc_bidirectional_order_average",
    "hf_pipeline_mrpc_margin_rule",
    "hf_pipeline_mrpc_raw_logits_softmax",
    "hf_pipeline_mrpc_short_maxlen_64",
    "hf_pipeline_mrpc_threshold_070",
    "min_direction_margin_mrpc",
    "mrpc_paraphrase_inference_distilbert",
    "neutral_penalized_margin_mrpc",
    "quora_cross_encoder_max_length_64_mrpc",
    "quora_cross_encoder_prefixed_sentence_tags_mrpc",
    "quora_cross_encoder_softmax_threshold_065_mrpc",
    "quora_cross_encoder_symmetric_average_mrpc",
    "quora_cross_encoder_text_normalized_mrpc",
    "softmax_gap_mean_mrpc",
    "st_all_distilroberta_v1_cosine_threshold_mrpc",
    "st_all_minilm_l6_l2_distance_threshold_mrpc",
    "st_all_minilm_l6_max_seq_len_64_cosine_mrpc",
    "st_paraphrase_minilm_l3_cosine_threshold_mrpc",
    "st_paraphrase_minilm_l6_cosine_threshold_mrpc"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 5055 | 62 | 45 | 3346 | 1.930s | 0.024s |

---

## Turn 13 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5af5efc48198914fd465df4eb6cd`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_A1nfgdEGSRxaUJ9ECgMnbv7O",
    "output": "{\"ok\": true, \"result\": [\"consensus_then_avg_margin_mrpc\", \"distilbert_cls_cosine_mrpc\", \"distilbert_last4_mean_cosine_mrpc\", \"distilbert_max_pool_cosine_mrpc\", \"distilbert_mean_cosine_median_threshold_mrpc\", \"distilbert_no_special_tokens_mean_cosine_mrpc\", \"entailment_logprob_odds_mrpc\", \"flan_t5_answer_prefix_yes_no_mrpc\", \"flan_t5_contextual_calibrated_yes_no_mrpc\", \"flan_t5_full_answer_logprob_mrpc\", \"flan_t5_symmetric_prompt_average_mrpc\", \"flan_t5_true_false_first_step_mrpc\", \"gent_1775874373\", \"gent_1775874650\", \"gent_1775874933\", \"gent_1775913615\", \"gent_1775914000\", \"gent_1775914190\", \"hf_pipeline_mrpc_bidirectional_order_average\", \"hf_pipeline_mrpc_margin_rule\", \"hf_pipeline_mrpc_raw_logits_softmax\", \"hf_pipeline_mrpc_short_maxlen_64\", \"hf_pipeline_mrpc_threshold_070\", \"min_direction_margin_mrpc\", \"mrpc_paraphrase_inference_distilbert\", \"neutral_penalized_margin_mrpc\", \"quora_cross_encoder_max_length_64_mrpc\", \"quora_cross_encoder_prefixed_sentence_tags_mrpc\", \"quora_cross_encoder_softmax_threshold_065_mrpc\", \"quora_cross_encoder_symmetric_average_mrpc\", \"quora_cross_encoder_text_normalized_mrpc\", \"softmax_gap_mean_mrpc\", \"st_all_distilroberta_v1_cosine_threshold_mrpc\", \"st_all_minilm_l6_l2_distance_threshold_mrpc\", \"st_all_minilm_l6_max_seq_len_64_cosine_mrpc\", \"st_paraphrase_minilm_l3_cosine_threshold_mrpc\", \"st_paraphrase_minilm_l6_cosine_threshold_mrpc\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5af5efc48198914fd465df4eb6cd`

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
    "call_id": "call_MLQs2mhLYs2KvznZiryNhOVR",
    "arguments": {
      "name": "hf_pipeline_mrpc_raw_logits_softmax"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_MLQs2mhLYs2KvznZiryNhOVR`

**Arguments:**
```json
{
  "name": "hf_pipeline_mrpc_raw_logits_softmax"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "def get_embeddings(text):\n    return client.embeddings.create(\n            input=text,\n            model=\"text-embedding-3-large\"\n        ).data[0].embedding",
    "import torch\nimport numpy as np\nfrom datasets import Dataset\nfrom transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\nfrom tqdm.auto import tqdm",
    "device = torch.device(\"mps\" if torch.backends.mps.is_available() else \"cpu\")\nprint(\"device:\", device)",
    "model_name = \"textattack/distilbert-base-uncased-MRPC\"\n\ntokenizer = AutoTokenizer.from_pretrained(model_name)\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\nmodel.eval()\n\nid2label = {int(k): v for k, v in model.config.id2label.items()}\nlabel2id = {str(k): int(v) for k, v in model.config.label2id.items()}\nnum_labels = model.config.num_labels\n\nclf_pipe = pipeline(\n    \"text-classification\",\n    model=model,\n    tokenizer=tokenizer,\n    device=device,\n    function_to_apply=\"none\",\n    top_k=None,\n)\n\nprint(model_name)\nprint(\"id2label:\", id2label)\nprint(\"label2id:\", label2id)",
    "ds = vault.query_item_content(\"glue_mrpc_validation\")\nds = Dataset.from_list(ds)\nprint(ds)\nprint(ds[0])\n\nsent1 = ds[\"sentence1\"]\nsent2 = ds[\"sentence2\"]\ny_true = np.array(ds[\"label\"])\ninputs = [{\"text\": s1, \"text_pair\": s2} for s1, s2 in zip(sent1, sent2)]\n\nprint(\"num_examples:\", len(y_true))\nprint(\"positive_rate:\", y_true.mean())",
    "def stable_softmax(x, axis=-1):\n    x = x - np.max(x, axis=axis, keepdims=True)\n    exp_x = np.exp(x)\n    return exp_x / np.sum(exp_x, axis=axis, keepdims=True)\n\ndef label_to_index(label):\n    label = str(label)\n    if label in label2id:\n        return int(label2id[label])\n    if label.startswith(\"LABEL_\"):\n        return int(label.split(\"_\")[-1])\n    if label.isdigit():\n        return int(label)\n    raise KeyError(f\"Unknown label from pipeline output: {label}\")\n\nbatch_size = 64\nraw_logits = np.zeros((len(inputs), num_labels), dtype=np.float32)\n\nfor start in tqdm(range(0, len(inputs), batch_size)):\n    batch_inputs = inputs[start:start + batch_size]\n    batch_outputs = clf_pipe(\n        batch_inputs,\n        batch_size=batch_size,\n        truncation=True,\n        max_length=128,\n    )\n\n    for row_offset, example_outputs in enumerate(batch_outputs):\n        row_idx = start + row_offset\n        for item in example_outputs:\n            cls_idx = label_to_index(item[\"label\"])\n            raw_logits[row_idx, cls_idx] = float(item[\"score\"])\n\nprobs = stable_softmax(raw_logits, axis=-1)\ny_pred = np.argmax(probs, axis=-1)\npositive_probs = probs[:, 1]\n\nprint(\"done\")\nprint(\"raw_logits_shape:\", raw_logits.shape)\nprint(\"probs_shape:\", probs.shape)",
    "\nvault.create_record_list(\"pipeline_distilbert_softmax_probs\", column_names=[\"prediction\", \"positive_probs\"])\n\nfor i in range(len(y_pred)):\n    vault.append_record(\"pipeline_distilbert_softmax_probs\", \n                        {\n                            \"prediction\": int(y_pred[i]),\n                            \"positive_probs\": float(positive_probs[i]),\n                        },\n                       input_items = {\n                           \"glue_mrpc_validation\": [i, i + 1],\n                       }\n                       )\n\ndescription = \"Per-example inference outputs for the GLUE MRPC validation set produced by the Hugging Face text-classification pipeline using textattack/distilbert-base-uncased-MRPC. Each record corresponds to one input sentence pair from glue_mrpc_validation and stores the model\\u2019s predicted class and the softmax probability of the positive/paraphrase class. The dataset is structured as one row per validation example with fields for prediction (integer class label from argmax) and the positive-class probability (intended as positive_probs; in the appended records this is written as paraphrase_probs). In this workflow, this dataset serves as the main prediction artifact linking model outputs back to the source validation examples and is used downstream to compute accuracy, F1, and the classification report summary.\"\nembedding = get_embeddings(description)\nvault.create_description(\"pipeline_distilbert_softmax_probs\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"dataset\": \"GLUE MRPC\", \"source\": \"glue/mrpc\", \"split\": \"validation\", \"size\": \"408\", \"model\": \"textattack/distilbert-base-uncased-MRPC\", \"framework\": \"huggingface transformers pipeline\", \"input_type\": \"sentence pair\", \"output_type\": \"predicted label and positive-class softmax probability\", \"score_type\": \"softmax probabilities from raw logits\", \"prediction_target\": \"paraphrase label\", \"upstream_table\": \"glue_mrpc_validation\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"pipeline_distilbert_softmax_probs\", cat, embedding, prop)",
    "acc = accuracy_score(y_true, y_pred)\nf1 = f1_score(y_true, y_pred)\ntarget_names = [id2label[i] for i in range(num_labels)]\nreport = classification_report(y_true, y_pred, target_names=target_names)\nprint({\"accuracy\": acc, \"f1\": f1})\nprint(classification_report(y_true, y_pred, target_names=target_names))",
    "for i in range(5):\n    print(\"=\" * 80)\n    print(\"sentence1:\", sent1[i])\n    print(\"sentence2:\", sent2[i])\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]), \"label:\", id2label[int(y_pred[i])])\n    print(\"raw_logits:\", raw_logits[i].tolist())\n    print(\"prob_positive:\", float(positive_probs[i]))",
    "mistakes = np.where(y_true != y_pred)[0][:10]\nprint(\"num_errors:\", int((y_true != y_pred).sum()))\n\nfor i in mistakes:\n    print(\"=\" * 80)\n    print(\"idx:\", int(i))\n    print(\"sentence1:\", sent1[i])\n    print(\"sentence2:\", sent2[i])\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]))\n    print(\"raw_logits:\", raw_logits[i].tolist())\n    print(\"prob_positive:\", float(positive_probs[i]))",
    "\nvault.create_record_list(\"hf_pipeline_mrpc_raw_logits_softmax_summary\", column_names=[\"accuracy\", \"f1\", \"classification_report\"])\n\n\nsummary = {\n    \"accuracy\": float(acc),\n    \"f1\": float(f1),\n    \"classification_report\": str(report)\n}\n\nvault.append_record(\"hf_pipeline_mrpc_raw_logits_softmax_summary\", summary,\n                    input_items = {\n                        \"glue_mrpc_validation\": [0, len(ds)],\n                        \"pipeline_distilbert_softmax_probs\": [0, len(ds)]\n                    })\n\nsummary\n\ndescription = \"This dataset stores the aggregate evaluation summary for the DistilBERT MRPC inference run on the GLUE MRPC validation set after converting pipeline raw logits to softmax probabilities. It contains one summary record with three fields: accuracy (overall prediction accuracy), f1 (binary F1 score for paraphrase detection), and classification_report (the full sklearn text report with per-class precision, recall, F1, support, and overall averages). In this workflow, it serves as the experiment-level performance snapshot, linking the source validation examples and the per-example prediction dataset pipeline_distilbert_softmax_probs so that users can quickly inspect overall model quality without recomputing metrics.\"\nembedding = get_embeddings(description)\nvault.create_description(\"hf_pipeline_mrpc_raw_logits_softmax_summary\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"problem_type\": \"binary sentence-pair classification\", \"dataset_role\": \"evaluation summary\", \"metrics\": \"accuracy, f1, classification_report\", \"split\": \"validation\", \"size\": \"408\", \"source\": \"glue/mrpc\", \"input_dataset\": \"glue_mrpc_validation\", \"model\": \"textattack/distilbert-base-uncased-MRPC\", \"framework\": \"huggingface transformers pipeline\", \"prediction_type\": \"raw logits converted with softmax\", \"labels\": \"not_equivalent, equivalent\", \"domain\": \"news\", \"process_name\": \"hf_pipeline_mrpc_raw_logits_softmax\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"hf_pipeline_mrpc_raw_logits_softmax_summary\", cat, embedding, prop)\n\n",
    "description = \"This notebook runs a Hugging Face inference workflow for the GLUE MRPC validation set to evaluate paraphrase detection. It loads the textattack/distilbert-base-uncased-MRPC sequence classification model and tokenizer, performs batched prediction on sentence pairs using the transformers text-classification pipeline with raw model outputs (logits), converts those logits to probabilities with a stable softmax, and derives predicted labels and paraphrase probabilities. The notebook then compares predictions against the ground-truth MRPC labels, computes evaluation metrics including accuracy, F1, and a classification report, inspects example predictions and errors, and stores both per-example outputs and aggregate summary results in TableVault. It also creates semantic descriptions and property metadata using OpenAI text embeddings so the generated artifacts and the overall notebook process can be indexed and discovered later.\" # description of whole notebook\nembedding = get_embeddings(description)\nvault.create_description(\"hf_pipeline_mrpc_raw_logits_softmax\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"problem_type\": \"binary text classification\", \"model\": \"textattack/distilbert-base-uncased-MRPC\", \"dataset\": \"glue/mrpc validation\", \"framework\": \"huggingface transformers pipeline\", \"inference_output\": \"raw logits and softmax probabilities\", \"metrics\": \"accuracy, f1-score, classification report\", \"storage\": \"tablevault\", \"embedding_model\": \"text-embedding-3-large\", \"split\": \"validation\", \"device\": \"mps or cpu\", \"process_name\": \"hf_pipeline_mrpc_raw_logits_softmax\"} #e.g. model: distilbert-base-uncased-MRPC\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"hf_pipeline_mrpc_raw_logits_softmax\", cat, embedding, prop)"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 5547 | 51 | 24 | 3838 | 1.718s | 0.024s |

---

## Turn 14 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5af7d1848198aa95b564870d97ba`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_MLQs2mhLYs2KvznZiryNhOVR",
    "output": "{\"ok\": true, \"result\": [\"def get_embeddings(text):\\n    return client.embeddings.create(\\n            input=text,\\n            model=\\\"text-embedding-3-large\\\"\\n        ).data[0].embedding\", \"import torch\\nimport numpy as np\\nfrom datasets import Dataset\\nfrom transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification\\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\\nfrom tqdm.auto import tqdm\", \"device = torch.device(\\\"mps\\\" if torch.backends.mps.is_available() else \\\"cpu\\\")\\nprint(\\\"device:\\\", device)\", \"model_name = \\\"textattack/distilbert-base-uncased-MRPC\\\"\\n\\ntokenizer = AutoTokenizer.from_pretrained(model_name)\\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\\nmodel.eval()\\n\\nid2label = {int(k): v for k, v in model.config.id2label.items()}\\nlabel2id = {str(k): int(v) for k, v in model.config.label2id.items()}\\nnum_labels = model.config.num_labels\\n\\nclf_pipe = pipeline(\\n    \\\"text-classification\\\",\\n    model=model,\\n    tokenizer=tokenizer,\\n    device=device,\\n    function_to_apply=\\\"none\\\",\\n    top_k=None,\\n)\\n\\nprint(model_name)\\nprint(\\\"id2label:\\\", id2label)\\nprint(\\\"label2id:\\\", label2id)\", \"ds = vault.query_item_content(\\\"glue_mrpc_validation\\\")\\nds = Dataset.from_list(ds)\\nprint(ds)\\nprint(ds[0])\\n\\nsent1 = ds[\\\"sentence1\\\"]\\nsent2 = ds[\\\"sentence2\\\"]\\ny_true = np.array(ds[\\\"label\\\"])\\ninputs = [{\\\"text\\\": s1, \\\"text_pair\\\": s2} for s1, s2 in zip(sent1, sent2)]\\n\\nprint(\\\"num_examples:\\\", len(y_true))\\nprint(\\\"positive_rate:\\\", y_true.mean())\", \"def stable_softmax(x, axis=-1):\\n    x = x - np.max(x, axis=axis, keepdims=True)\\n    exp_x = np.exp(x)\\n    return exp_x / np.sum(exp_x, axis=axis, keepdims=True)\\n\\ndef label_to_index(label):\\n    label = str(label)\\n    if label in label2id:\\n        return int(label2id[label])\\n    if label.startswith(\\\"LABEL_\\\"):\\n        return int(label.split(\\\"_\\\")[-1])\\n    if label.isdigit():\\n        return int(label)\\n    raise KeyError(f\\\"Unknown label from pipeline output: {label}\\\")\\n\\nbatch_size = 64\\nraw_logits = np.zeros((len(inputs), num_labels), dtype=np.float32)\\n\\nfor start in tqdm(range(0, len(inputs), batch_size)):\\n    batch_inputs = inputs[start:start + batch_size]\\n    batch_outputs = clf_pipe(\\n        batch_inputs,\\n        batch_size=batch_size,\\n        truncation=True,\\n        max_length=128,\\n    )\\n\\n    for row_offset, example_outputs in enumerate(batch_outputs):\\n        row_idx = start + row_offset\\n        for item in example_outputs:\\n            cls_idx = label_to_index(item[\\\"label\\\"])\\n            raw_logits[row_idx, cls_idx] = float(item[\\\"score\\\"])\\n\\nprobs = stable_softmax(raw_logits, axis=-1)\\ny_pred = np.argmax(probs, axis=-1)\\npositive_probs = probs[:, 1]\\n\\nprint(\\\"done\\\")\\nprint(\\\"raw_logits_shape:\\\", raw_logits.shape)\\nprint(\\\"probs_shape:\\\", probs.shape)\", \"\\nvault.create_record_list(\\\"pipeline_distilbert_softmax_probs\\\", column_names=[\\\"prediction\\\", \\\"positive_probs\\\"])\\n\\nfor i in range(len(y_pred)):\\n    vault.append_record(\\\"pipeline_distilbert_softmax_probs\\\", \\n                        {\\n                            \\\"prediction\\\": int(y_pred[i]),\\n                            \\\"positive_probs\\\": float(positive_probs[i]),\\n                        },\\n                       input_items = {\\n                           \\\"glue_mrpc_validation\\\": [i, i + 1],\\n                       }\\n                       )\\n\\ndescription = \\\"Per-example inference outputs for the GLUE MRPC validation set produced by the Hugging Face text-classification pipeline using textattack/distilbert-base-uncased-MRPC. Each record corresponds to one input sentence pair from glue_mrpc_validation and stores the model\\\\u2019s predicted class and the softmax probability of the positive/paraphrase class. The dataset is structured as one row per validation example with fields for prediction (integer class label from argmax) and the positive-class probability (intended as positive_probs; in the appended records this is written as paraphrase_probs). In this workflow, this dataset serves as the main prediction artifact linking model outputs back to the source validation examples and is used downstream to compute accuracy, F1, and the classification report summary.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"pipeline_distilbert_softmax_probs\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset\\\": \\\"GLUE MRPC\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"textattack/distilbert-base-uncased-MRPC\\\", \\\"framework\\\": \\\"huggingface transformers pipeline\\\", \\\"input_type\\\": \\\"sentence pair\\\", \\\"output_type\\\": \\\"predicted label and positive-class softmax probability\\\", \\\"score_type\\\": \\\"softmax probabilities from raw logits\\\", \\\"prediction_target\\\": \\\"paraphrase label\\\", \\\"upstream_table\\\": \\\"glue_mrpc_validation\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"pipeline_distilbert_softmax_probs\\\", cat, embedding, prop)\", \"acc = accuracy_score(y_true, y_pred)\\nf1 = f1_score(y_true, y_pred)\\ntarget_names = [id2label[i] for i in range(num_labels)]\\nreport = classification_report(y_true, y_pred, target_names=target_names)\\nprint({\\\"accuracy\\\": acc, \\\"f1\\\": f1})\\nprint(classification_report(y_true, y_pred, target_names=target_names))\", \"for i in range(5):\\n    print(\\\"=\\\" * 80)\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]), \\\"label:\\\", id2label[int(y_pred[i])])\\n    print(\\\"raw_logits:\\\", raw_logits[i].tolist())\\n    print(\\\"prob_positive:\\\", float(positive_probs[i]))\", \"mistakes = np.where(y_true != y_pred)[0][:10]\\nprint(\\\"num_errors:\\\", int((y_true != y_pred).sum()))\\n\\nfor i in mistakes:\\n    print(\\\"=\\\" * 80)\\n    print(\\\"idx:\\\", int(i))\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n    print(\\\"raw_logits:\\\", raw_logits[i].tolist())\\n    print(\\\"prob_positive:\\\", float(positive_probs[i]))\", \"\\nvault.create_record_list(\\\"hf_pipeline_mrpc_raw_logits_softmax_summary\\\", column_names=[\\\"accuracy\\\", \\\"f1\\\", \\\"classification_report\\\"])\\n\\n\\nsummary = {\\n    \\\"accuracy\\\": float(acc),\\n    \\\"f1\\\": float(f1),\\n    \\\"classification_report\\\": str(report)\\n}\\n\\nvault.append_record(\\\"hf_pipeline_mrpc_raw_logits_softmax_summary\\\", summary,\\n                    input_items = {\\n                        \\\"glue_mrpc_validation\\\": [0, len(ds)],\\n                        \\\"pipeline_distilbert_softmax_probs\\\": [0, len(ds)]\\n                    })\\n\\nsummary\\n\\ndescription = \\\"This dataset stores the aggregate evaluation summary for the DistilBERT MRPC inference run on the GLUE MRPC validation set after converting pipeline raw logits to softmax probabilities. It contains one summary record with three fields: accuracy (overall prediction accuracy), f1 (binary F1 score for paraphrase detection), and classification_report (the full sklearn text report with per-class precision, recall, F1, support, and overall averages). In this workflow, it serves as the experiment-level performance snapshot, linking the source validation examples and the per-example prediction dataset pipeline_distilbert_softmax_probs so that users can quickly inspect overall model quality without recomputing metrics.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"hf_pipeline_mrpc_raw_logits_softmax_summary\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"problem_type\\\": \\\"binary sentence-pair classification\\\", \\\"dataset_role\\\": \\\"evaluation summary\\\", \\\"metrics\\\": \\\"accuracy, f1, classification_report\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"input_dataset\\\": \\\"glue_mrpc_validation\\\", \\\"model\\\": \\\"textattack/distilbert-base-uncased-MRPC\\\", \\\"framework\\\": \\\"huggingface transformers pipeline\\\", \\\"prediction_type\\\": \\\"raw logits converted with softmax\\\", \\\"labels\\\": \\\"not_equivalent, equivalent\\\", \\\"domain\\\": \\\"news\\\", \\\"process_name\\\": \\\"hf_pipeline_mrpc_raw_logits_softmax\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"hf_pipeline_mrpc_raw_logits_softmax_summary\\\", cat, embedding, prop)\\n\\n\", \"description = \\\"This notebook runs a Hugging Face inference workflow for the GLUE MRPC validation set to evaluate paraphrase detection. It loads the textattack/distilbert-base-uncased-MRPC sequence classification model and tokenizer, performs batched prediction on sentence pairs using the transformers text-classification pipeline with raw model outputs (logits), converts those logits to probabilities with a stable softmax, and derives predicted labels and paraphrase probabilities. The notebook then compares predictions against the ground-truth MRPC labels, computes evaluation metrics including accuracy, F1, and a classification report, inspects example predictions and errors, and stores both per-example outputs and aggregate summary results in TableVault. It also creates semantic descriptions and property metadata using OpenAI text embeddings so the generated artifacts and the overall notebook process can be indexed and discovered later.\\\" # description of whole notebook\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"hf_pipeline_mrpc_raw_logits_softmax\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"problem_type\\\": \\\"binary text classification\\\", \\\"model\\\": \\\"textattack/distilbert-base-uncased-MRPC\\\", \\\"dataset\\\": \\\"glue/mrpc validation\\\", \\\"framework\\\": \\\"huggingface transformers pipeline\\\", \\\"inference_output\\\": \\\"raw logits and softmax probabilities\\\", \\\"metrics\\\": \\\"accuracy, f1-score, classification report\\\", \\\"storage\\\": \\\"tablevault\\\", \\\"embedding_model\\\": \\\"text-embedding-3-large\\\", \\\"split\\\": \\\"validation\\\", \\\"device\\\": \\\"mps or cpu\\\", \\\"process_name\\\": \\\"hf_pipeline_mrpc_raw_logits_softmax\\\"} #e.g. model: distilbert-base-uncased-MRPC\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"hf_pipeline_mrpc_raw_logits_softmax\\\", cat, embedding, prop)\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5af7d1848198aa95b564870d97ba`

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
    "call_id": "call_h43bleIeNDPYI6g7fByxsuqL",
    "arguments": {
      "name": "flan_t5_symmetric_prompt_average_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_h43bleIeNDPYI6g7fByxsuqL`

**Arguments:**
```json
{
  "name": "flan_t5_symmetric_prompt_average_mrpc"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "def get_embeddings(text):\n    return client.embeddings.create(\n            input=text,\n            model=\"text-embedding-3-large\"\n        ).data[0].embedding",
    "import torch\nimport numpy as np\nfrom datasets import Dataset\nfrom transformers import AutoTokenizer, AutoModelForSeq2SeqLM\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\nfrom tqdm.auto import tqdm\n\ndevice = torch.device(\"mps\" if torch.backends.mps.is_available() else \"cpu\")\nprint(\"device:\", device)\n",
    "model_name = \"google/flan-t5-small\"\n\ntokenizer = AutoTokenizer.from_pretrained(model_name)\nmodel = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)\nmodel.eval()\n\nlabel_names = {0: \"not_paraphrase\", 1: \"paraphrase\"}\nprint(model_name)\nprint(\"vocab_size:\", model.config.vocab_size)\n",
    "def get_single_token_id(text):\n    candidates = [text, text.lower(), f\" {text}\", f\" {text.lower()}\"]\n    for cand in candidates:\n        ids = tokenizer.encode(cand, add_special_tokens=False)\n        if len(ids) == 1:\n            token = tokenizer.convert_ids_to_tokens(ids)[0]\n            print({\"requested\": text, \"matched_text\": cand, \"token_id\": ids[0], \"token\": token})\n            return ids[0]\n    raise ValueError(f\"Could not find a single-token form for {text!r}\")\n\nyes_token_id = get_single_token_id(\"yes\")\nno_token_id = get_single_token_id(\"no\")\n\ndecoder_start_token_id = model.config.decoder_start_token_id\nif decoder_start_token_id is None:\n    decoder_start_token_id = tokenizer.pad_token_id\n\nprint(\"decoder_start_token_id:\", decoder_start_token_id)\nprint(\"pad_token_id:\", tokenizer.pad_token_id)\n",
    "ds = vault.query_item_content(\"glue_mrpc_validation\")\nds = Dataset.from_list(ds)\nprint(ds)\nprint(ds[0])\n\nsent1 = ds[\"sentence1\"]\nsent2 = ds[\"sentence2\"]\ny_true = np.array(ds[\"label\"])\n\nprint(\"num_examples:\", len(y_true))\nprint(\"positive_rate:\", y_true.mean())\n",
    "def build_prompt(sentence_a, sentence_b):\n    return (\n        \"Are the following two sentences paraphrases? Answer yes or no.\\n\"\n        f\"Sentence 1: {sentence_a}\\n\"\n        f\"Sentence 2: {sentence_b}\"\n    )\n\nbatch_size = 32\npreds = []\nforward_yes_logits = []\nforward_no_logits = []\nswapped_yes_logits = []\nswapped_no_logits = []\n\nwith torch.no_grad():\n    for i in tqdm(range(0, len(ds), batch_size)):\n        batch_s1 = sent1[i:i + batch_size]\n        batch_s2 = sent2[i:i + batch_size]\n\n        prompts_forward = [build_prompt(a, b) for a, b in zip(batch_s1, batch_s2)]\n        prompts_swapped = [build_prompt(b, a) for a, b in zip(batch_s1, batch_s2)]\n\n        enc_forward = tokenizer(\n            prompts_forward,\n            padding=True,\n            truncation=True,\n            max_length=256,\n            return_tensors=\"pt\",\n        )\n        enc_swapped = tokenizer(\n            prompts_swapped,\n            padding=True,\n            truncation=True,\n            max_length=256,\n            return_tensors=\"pt\",\n        )\n\n        enc_forward = {k: v.to(device) for k, v in enc_forward.items()}\n        enc_swapped = {k: v.to(device) for k, v in enc_swapped.items()}\n\n        decoder_input_ids = torch.full(\n            (len(batch_s1), 1),\n            decoder_start_token_id,\n            dtype=torch.long,\n            device=device,\n        )\n\n        logits_forward = model(**enc_forward, decoder_input_ids=decoder_input_ids).logits[:, 0, :]\n        logits_swapped = model(**enc_swapped, decoder_input_ids=decoder_input_ids).logits[:, 0, :]\n\n        yes_forward = logits_forward[:, yes_token_id]\n        no_forward = logits_forward[:, no_token_id]\n        yes_swapped = logits_swapped[:, yes_token_id]\n        no_swapped = logits_swapped[:, no_token_id]\n\n        avg_yes_batch = (yes_forward + yes_swapped) / 2.0\n        avg_no_batch = (no_forward + no_swapped) / 2.0\n        batch_preds = (avg_yes_batch > avg_no_batch).long().cpu().numpy()\n\n        preds.extend(batch_preds.tolist())\n        forward_yes_logits.extend(yes_forward.cpu().numpy().tolist())\n        forward_no_logits.extend(no_forward.cpu().numpy().tolist())\n        swapped_yes_logits.extend(yes_swapped.cpu().numpy().tolist())\n        swapped_no_logits.extend(no_swapped.cpu().numpy().tolist())\n\ny_pred = np.array(preds)\nforward_yes_logits = np.array(forward_yes_logits)\nforward_no_logits = np.array(forward_no_logits)\nswapped_yes_logits = np.array(swapped_yes_logits)\nswapped_no_logits = np.array(swapped_no_logits)\navg_yes_logits = (forward_yes_logits + swapped_yes_logits) / 2.0\navg_no_logits = (forward_no_logits + swapped_no_logits) / 2.0\n\nprint(\"done\")\n",
    "\nvault.create_record_list(\"google_flan_prediction_swapped\", column_names=[\"prediction\", \"yes_logits\", \"no_logits\", \"swapped_yes_logits\", \"swapped_no_logits\"])\n\nfor i in range(len(y_pred)):\n    vault.append_record(\"google_flan_prediction_swapped\", \n                        {\n                            \"prediction\": int(y_pred[i]),\n                            \"yes_logits\": float(forward_yes_logits[i]),\n                            \"no_logits\": float(forward_no_logits[i]),\n                            \"swapped_yes_logits\": float(swapped_yes_logits[i]),\n                            \"swapped_no_logits\": float(swapped_no_logits[i]),\n                        },\n                       input_items = {\n                           \"glue_mrpc_validation\": [i, i + 1],\n                       }\n                       )\n\ndescription = \"Per-example prediction outputs from google/flan-t5-small on the GLUE MRPC validation set using a yes/no paraphrase prompt evaluated in both original and swapped sentence order. Each record is aligned to one input example from glue_mrpc_validation and contains: prediction (binary paraphrase decision after averaging forward and swapped logits), yes_logits (forward-order logit for \\u201cyes\\u201d), no_logits (forward-order logit for \\u201cno\\u201d), swapped_yes_logits (swapped-order logit for \\u201cyes\\u201d), and swapped_no_logits (swapped-order logit for \\u201cno\\u201d). This dataset is used as the intermediate model-output table in the workflow, supporting order-symmetric paraphrase prediction, error analysis, and computation of final evaluation metrics in the summary dataset.\"\nembedding = get_embeddings(description)\nvault.create_description(\"google_flan_prediction_swapped\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"dataset_role\": \"model predictions\", \"source\": \"glue/mrpc\", \"split\": \"validation\", \"size\": \"408\", \"model\": \"google/flan-t5-small\", \"prompting\": \"yes/no question\", \"inference_method\": \"symmetric swapped-prompt average\", \"prediction_type\": \"binary classification\", \"output_columns\": \"prediction, yes_logits, no_logits, swapped_yes_logits, swapped_no_logits\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"google_flan_prediction_swapped\", cat, embedding, prop)",
    "acc = accuracy_score(y_true, y_pred)\nf1 = f1_score(y_true, y_pred)\nreport = classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"], zero_division=0)\nprint({\"accuracy\": acc, \"f1\": f1})\nprint(classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"], zero_division=0))\n",
    "for i in range(5):\n    print(\"=\" * 80)\n    print(\"sentence1:\", sent1[i])\n    print(\"sentence2:\", sent2[i])\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]), \"label:\", label_names[int(y_pred[i])])\n    print(\n        {\n            \"forward_yes_logit\": float(forward_yes_logits[i]),\n            \"forward_no_logit\": float(forward_no_logits[i]),\n            \"swapped_yes_logit\": float(swapped_yes_logits[i]),\n            \"swapped_no_logit\": float(swapped_no_logits[i]),\n            \"avg_yes_logit\": float(avg_yes_logits[i]),\n            \"avg_no_logit\": float(avg_no_logits[i]),\n        }\n    )\n",
    "mistakes = np.where(y_true != y_pred)[0][:10]\nprint(\"num_errors:\", int((y_true != y_pred).sum()))\n\nfor i in mistakes:\n    print(\"=\" * 80)\n    print(\"idx:\", int(i))\n    print(\"sentence1:\", sent1[i])\n    print(\"sentence2:\", sent2[i])\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]))\n    print(\n        {\n            \"forward_yes_logit\": float(forward_yes_logits[i]),\n            \"forward_no_logit\": float(forward_no_logits[i]),\n            \"swapped_yes_logit\": float(swapped_yes_logits[i]),\n            \"swapped_no_logit\": float(swapped_no_logits[i]),\n            \"avg_yes_logit\": float(avg_yes_logits[i]),\n            \"avg_no_logit\": float(avg_no_logits[i]),\n        }\n    )\n",
    "\nvault.create_record_list(\"flan_t5_symmetric_prompt_average_mrpc_summary\", column_names=[\"accuracy\", \"f1\", \"classification_report\"])\n\n\nsummary = {\n    \"accuracy\": float(acc),\n    \"f1\": float(f1),\n    \"classification_report\": str(report)\n}\n\nvault.append_record(\"flan_t5_symmetric_prompt_average_mrpc_summary\", summary,\n                    input_items = {\n                        \"glue_mrpc_validation\": [0, len(ds)],\n                        \"google_flan_prediction_swapped\": [0, len(ds)]\n                    })\n\nsummary\n\ndescription = \"Summary dataset for the FLAN-T5 symmetric-prompt MRPC evaluation run. It contains a single aggregate record describing model performance on the full glue_mrpc_validation split, computed from predictions stored in google_flan_prediction_swapped. The fields are: accuracy (float, overall classification accuracy), f1 (float, binary F1 score for paraphrase detection), and classification_report (string, the full scikit-learn classification report with precision, recall, F1, and support for both not_paraphrase and paraphrase classes). Its role in this workflow is to provide a compact experiment-level evaluation artifact that links the source validation examples and prediction outputs to final metrics for the notebook/process flan_t5_symmetric_prompt_average_mrpc.\"\nembedding = get_embeddings(description)\nvault.create_description(\"flan_t5_symmetric_prompt_average_mrpc_summary\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"dataset_type\": \"evaluation summary\", \"source\": \"glue/mrpc\", \"split\": \"validation\", \"size\": \"408\", \"model\": \"google/flan-t5-small\", \"prompting_method\": \"symmetric prompt averaging\", \"prediction_target\": \"binary yes/no\", \"metrics\": \"accuracy,f1,classification_report\", \"input_items\": \"glue_mrpc_validation,google_flan_prediction_swapped\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"flan_t5_symmetric_prompt_average_mrpc_summary\", cat, embedding, prop)\n\n",
    "description = \"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using google/flan-t5-small. It frames MRPC as a yes/no text-to-text classification task by prompting the model with two sentences and asking whether they are paraphrases. To reduce order sensitivity, each sentence pair is scored twice\\u2014once in the original order and once with the sentences swapped\\u2014and the first-token logits for yes and no are averaged across both prompts to produce the final prediction. The notebook loads the validation data from TableVault, runs batched inference with Hugging Face Transformers on MPS or CPU, computes accuracy, F1, and a classification report, inspects example predictions and errors, and stores per-example predictions, logits, summary metrics, and metadata back into TableVault with embedding-based descriptions.\" # description of whole notebook\nembedding = get_embeddings(description)\nvault.create_description(\"flan_t5_symmetric_prompt_average_mrpc\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"dataset\": \"glue/mrpc\", \"dataset_split\": \"validation\", \"model\": \"google/flan-t5-small\", \"model_family\": \"flan-t5\", \"inference_method\": \"zero-shot seq2seq first-token logit comparison\", \"prompt_strategy\": \"symmetric prompt averaging with sentence order swap\", \"labels\": \"yes/no mapped to paraphrase/not_paraphrase\", \"evaluation\": \"accuracy, f1-score, classification_report\", \"frameworks\": \"transformers, pytorch, datasets, sklearn\", \"storage\": \"tablevault\", \"database\": \"arangodb\", \"embedding_model\": \"text-embedding-3-large\", \"process_name\": \"flan_t5_symmetric_prompt_average_mrpc\"} #e.g. model: distilbert-base-uncased-MRPC\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"flan_t5_symmetric_prompt_average_mrpc\", cat, embedding, prop)"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 8118 | 97 | 68 | 6409 | 2.331s | 0.025s |

---

## Turn 15 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5afa0cd08198b8df6e57ea56c3b8`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_h43bleIeNDPYI6g7fByxsuqL",
    "output": "{\"ok\": true, \"result\": [\"def get_embeddings(text):\\n    return client.embeddings.create(\\n            input=text,\\n            model=\\\"text-embedding-3-large\\\"\\n        ).data[0].embedding\", \"import torch\\nimport numpy as np\\nfrom datasets import Dataset\\nfrom transformers import AutoTokenizer, AutoModelForSeq2SeqLM\\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\\nfrom tqdm.auto import tqdm\\n\\ndevice = torch.device(\\\"mps\\\" if torch.backends.mps.is_available() else \\\"cpu\\\")\\nprint(\\\"device:\\\", device)\\n\", \"model_name = \\\"google/flan-t5-small\\\"\\n\\ntokenizer = AutoTokenizer.from_pretrained(model_name)\\nmodel = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)\\nmodel.eval()\\n\\nlabel_names = {0: \\\"not_paraphrase\\\", 1: \\\"paraphrase\\\"}\\nprint(model_name)\\nprint(\\\"vocab_size:\\\", model.config.vocab_size)\\n\", \"def get_single_token_id(text):\\n    candidates = [text, text.lower(), f\\\" {text}\\\", f\\\" {text.lower()}\\\"]\\n    for cand in candidates:\\n        ids = tokenizer.encode(cand, add_special_tokens=False)\\n        if len(ids) == 1:\\n            token = tokenizer.convert_ids_to_tokens(ids)[0]\\n            print({\\\"requested\\\": text, \\\"matched_text\\\": cand, \\\"token_id\\\": ids[0], \\\"token\\\": token})\\n            return ids[0]\\n    raise ValueError(f\\\"Could not find a single-token form for {text!r}\\\")\\n\\nyes_token_id = get_single_token_id(\\\"yes\\\")\\nno_token_id = get_single_token_id(\\\"no\\\")\\n\\ndecoder_start_token_id = model.config.decoder_start_token_id\\nif decoder_start_token_id is None:\\n    decoder_start_token_id = tokenizer.pad_token_id\\n\\nprint(\\\"decoder_start_token_id:\\\", decoder_start_token_id)\\nprint(\\\"pad_token_id:\\\", tokenizer.pad_token_id)\\n\", \"ds = vault.query_item_content(\\\"glue_mrpc_validation\\\")\\nds = Dataset.from_list(ds)\\nprint(ds)\\nprint(ds[0])\\n\\nsent1 = ds[\\\"sentence1\\\"]\\nsent2 = ds[\\\"sentence2\\\"]\\ny_true = np.array(ds[\\\"label\\\"])\\n\\nprint(\\\"num_examples:\\\", len(y_true))\\nprint(\\\"positive_rate:\\\", y_true.mean())\\n\", \"def build_prompt(sentence_a, sentence_b):\\n    return (\\n        \\\"Are the following two sentences paraphrases? Answer yes or no.\\\\n\\\"\\n        f\\\"Sentence 1: {sentence_a}\\\\n\\\"\\n        f\\\"Sentence 2: {sentence_b}\\\"\\n    )\\n\\nbatch_size = 32\\npreds = []\\nforward_yes_logits = []\\nforward_no_logits = []\\nswapped_yes_logits = []\\nswapped_no_logits = []\\n\\nwith torch.no_grad():\\n    for i in tqdm(range(0, len(ds), batch_size)):\\n        batch_s1 = sent1[i:i + batch_size]\\n        batch_s2 = sent2[i:i + batch_size]\\n\\n        prompts_forward = [build_prompt(a, b) for a, b in zip(batch_s1, batch_s2)]\\n        prompts_swapped = [build_prompt(b, a) for a, b in zip(batch_s1, batch_s2)]\\n\\n        enc_forward = tokenizer(\\n            prompts_forward,\\n            padding=True,\\n            truncation=True,\\n            max_length=256,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc_swapped = tokenizer(\\n            prompts_swapped,\\n            padding=True,\\n            truncation=True,\\n            max_length=256,\\n            return_tensors=\\\"pt\\\",\\n        )\\n\\n        enc_forward = {k: v.to(device) for k, v in enc_forward.items()}\\n        enc_swapped = {k: v.to(device) for k, v in enc_swapped.items()}\\n\\n        decoder_input_ids = torch.full(\\n            (len(batch_s1), 1),\\n            decoder_start_token_id,\\n            dtype=torch.long,\\n            device=device,\\n        )\\n\\n        logits_forward = model(**enc_forward, decoder_input_ids=decoder_input_ids).logits[:, 0, :]\\n        logits_swapped = model(**enc_swapped, decoder_input_ids=decoder_input_ids).logits[:, 0, :]\\n\\n        yes_forward = logits_forward[:, yes_token_id]\\n        no_forward = logits_forward[:, no_token_id]\\n        yes_swapped = logits_swapped[:, yes_token_id]\\n        no_swapped = logits_swapped[:, no_token_id]\\n\\n        avg_yes_batch = (yes_forward + yes_swapped) / 2.0\\n        avg_no_batch = (no_forward + no_swapped) / 2.0\\n        batch_preds = (avg_yes_batch > avg_no_batch).long().cpu().numpy()\\n\\n        preds.extend(batch_preds.tolist())\\n        forward_yes_logits.extend(yes_forward.cpu().numpy().tolist())\\n        forward_no_logits.extend(no_forward.cpu().numpy().tolist())\\n        swapped_yes_logits.extend(yes_swapped.cpu().numpy().tolist())\\n        swapped_no_logits.extend(no_swapped.cpu().numpy().tolist())\\n\\ny_pred = np.array(preds)\\nforward_yes_logits = np.array(forward_yes_logits)\\nforward_no_logits = np.array(forward_no_logits)\\nswapped_yes_logits = np.array(swapped_yes_logits)\\nswapped_no_logits = np.array(swapped_no_logits)\\navg_yes_logits = (forward_yes_logits + swapped_yes_logits) / 2.0\\navg_no_logits = (forward_no_logits + swapped_no_logits) / 2.0\\n\\nprint(\\\"done\\\")\\n\", \"\\nvault.create_record_list(\\\"google_flan_prediction_swapped\\\", column_names=[\\\"prediction\\\", \\\"yes_logits\\\", \\\"no_logits\\\", \\\"swapped_yes_logits\\\", \\\"swapped_no_logits\\\"])\\n\\nfor i in range(len(y_pred)):\\n    vault.append_record(\\\"google_flan_prediction_swapped\\\", \\n                        {\\n                            \\\"prediction\\\": int(y_pred[i]),\\n                            \\\"yes_logits\\\": float(forward_yes_logits[i]),\\n                            \\\"no_logits\\\": float(forward_no_logits[i]),\\n                            \\\"swapped_yes_logits\\\": float(swapped_yes_logits[i]),\\n                            \\\"swapped_no_logits\\\": float(swapped_no_logits[i]),\\n                        },\\n                       input_items = {\\n                           \\\"glue_mrpc_validation\\\": [i, i + 1],\\n                       }\\n                       )\\n\\ndescription = \\\"Per-example prediction outputs from google/flan-t5-small on the GLUE MRPC validation set using a yes/no paraphrase prompt evaluated in both original and swapped sentence order. Each record is aligned to one input example from glue_mrpc_validation and contains: prediction (binary paraphrase decision after averaging forward and swapped logits), yes_logits (forward-order logit for \\\\u201cyes\\\\u201d), no_logits (forward-order logit for \\\\u201cno\\\\u201d), swapped_yes_logits (swapped-order logit for \\\\u201cyes\\\\u201d), and swapped_no_logits (swapped-order logit for \\\\u201cno\\\\u201d). This dataset is used as the intermediate model-output table in the workflow, supporting order-symmetric paraphrase prediction, error analysis, and computation of final evaluation metrics in the summary dataset.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"google_flan_prediction_swapped\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_role\\\": \\\"model predictions\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"google/flan-t5-small\\\", \\\"prompting\\\": \\\"yes/no question\\\", \\\"inference_method\\\": \\\"symmetric swapped-prompt average\\\", \\\"prediction_type\\\": \\\"binary classification\\\", \\\"output_columns\\\": \\\"prediction, yes_logits, no_logits, swapped_yes_logits, swapped_no_logits\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"google_flan_prediction_swapped\\\", cat, embedding, prop)\", \"acc = accuracy_score(y_true, y_pred)\\nf1 = f1_score(y_true, y_pred)\\nreport = classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"], zero_division=0)\\nprint({\\\"accuracy\\\": acc, \\\"f1\\\": f1})\\nprint(classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"], zero_division=0))\\n\", \"for i in range(5):\\n    print(\\\"=\\\" * 80)\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]), \\\"label:\\\", label_names[int(y_pred[i])])\\n    print(\\n        {\\n            \\\"forward_yes_logit\\\": float(forward_yes_logits[i]),\\n            \\\"forward_no_logit\\\": float(forward_no_logits[i]),\\n            \\\"swapped_yes_logit\\\": float(swapped_yes_logits[i]),\\n            \\\"swapped_no_logit\\\": float(swapped_no_logits[i]),\\n            \\\"avg_yes_logit\\\": float(avg_yes_logits[i]),\\n            \\\"avg_no_logit\\\": float(avg_no_logits[i]),\\n        }\\n    )\\n\", \"mistakes = np.where(y_true != y_pred)[0][:10]\\nprint(\\\"num_errors:\\\", int((y_true != y_pred).sum()))\\n\\nfor i in mistakes:\\n    print(\\\"=\\\" * 80)\\n    print(\\\"idx:\\\", int(i))\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n    print(\\n        {\\n            \\\"forward_yes_logit\\\": float(forward_yes_logits[i]),\\n            \\\"forward_no_logit\\\": float(forward_no_logits[i]),\\n            \\\"swapped_yes_logit\\\": float(swapped_yes_logits[i]),\\n            \\\"swapped_no_logit\\\": float(swapped_no_logits[i]),\\n            \\\"avg_yes_logit\\\": float(avg_yes_logits[i]),\\n            \\\"avg_no_logit\\\": float(avg_no_logits[i]),\\n        }\\n    )\\n\", \"\\nvault.create_record_list(\\\"flan_t5_symmetric_prompt_average_mrpc_summary\\\", column_names=[\\\"accuracy\\\", \\\"f1\\\", \\\"classification_report\\\"])\\n\\n\\nsummary = {\\n    \\\"accuracy\\\": float(acc),\\n    \\\"f1\\\": float(f1),\\n    \\\"classification_report\\\": str(report)\\n}\\n\\nvault.append_record(\\\"flan_t5_symmetric_prompt_average_mrpc_summary\\\", summary,\\n                    input_items = {\\n                        \\\"glue_mrpc_validation\\\": [0, len(ds)],\\n                        \\\"google_flan_prediction_swapped\\\": [0, len(ds)]\\n                    })\\n\\nsummary\\n\\ndescription = \\\"Summary dataset for the FLAN-T5 symmetric-prompt MRPC evaluation run. It contains a single aggregate record describing model performance on the full glue_mrpc_validation split, computed from predictions stored in google_flan_prediction_swapped. The fields are: accuracy (float, overall classification accuracy), f1 (float, binary F1 score for paraphrase detection), and classification_report (string, the full scikit-learn classification report with precision, recall, F1, and support for both not_paraphrase and paraphrase classes). Its role in this workflow is to provide a compact experiment-level evaluation artifact that links the source validation examples and prediction outputs to final metrics for the notebook/process flan_t5_symmetric_prompt_average_mrpc.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"flan_t5_symmetric_prompt_average_mrpc_summary\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_type\\\": \\\"evaluation summary\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"google/flan-t5-small\\\", \\\"prompting_method\\\": \\\"symmetric prompt averaging\\\", \\\"prediction_target\\\": \\\"binary yes/no\\\", \\\"metrics\\\": \\\"accuracy,f1,classification_report\\\", \\\"input_items\\\": \\\"glue_mrpc_validation,google_flan_prediction_swapped\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"flan_t5_symmetric_prompt_average_mrpc_summary\\\", cat, embedding, prop)\\n\\n\", \"description = \\\"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using google/flan-t5-small. It frames MRPC as a yes/no text-to-text classification task by prompting the model with two sentences and asking whether they are paraphrases. To reduce order sensitivity, each sentence pair is scored twice\\\\u2014once in the original order and once with the sentences swapped\\\\u2014and the first-token logits for yes and no are averaged across both prompts to produce the final prediction. The notebook loads the validation data from TableVault, runs batched inference with Hugging Face Transformers on MPS or CPU, computes accuracy, F1, and a classification report, inspects example predictions and errors, and stores per-example predictions, logits, summary metrics, and metadata back into TableVault with embedding-based descriptions.\\\" # description of whole notebook\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"flan_t5_symmetric_prompt_average_mrpc\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset\\\": \\\"glue/mrpc\\\", \\\"dataset_split\\\": \\\"validation\\\", \\\"model\\\": \\\"google/flan-t5-small\\\", \\\"model_family\\\": \\\"flan-t5\\\", \\\"inference_method\\\": \\\"zero-shot seq2seq first-token logit comparison\\\", \\\"prompt_strategy\\\": \\\"symmetric prompt averaging with sentence order swap\\\", \\\"labels\\\": \\\"yes/no mapped to paraphrase/not_paraphrase\\\", \\\"evaluation\\\": \\\"accuracy, f1-score, classification_report\\\", \\\"frameworks\\\": \\\"transformers, pytorch, datasets, sklearn\\\", \\\"storage\\\": \\\"tablevault\\\", \\\"database\\\": \\\"arangodb\\\", \\\"embedding_model\\\": \\\"text-embedding-3-large\\\", \\\"process_name\\\": \\\"flan_t5_symmetric_prompt_average_mrpc\\\"} #e.g. model: distilbert-base-uncased-MRPC\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"flan_t5_symmetric_prompt_average_mrpc\\\", cat, embedding, prop)\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5afa0cd08198b8df6e57ea56c3b8`

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
    "call_id": "call_QMlgsrkWvcwzIhBl0z7h1s97",
    "arguments": {
      "name": "flan_t5_full_answer_logprob_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_QMlgsrkWvcwzIhBl0z7h1s97`

**Arguments:**
```json
{
  "name": "flan_t5_full_answer_logprob_mrpc"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "def get_embeddings(text):\n    return client.embeddings.create(\n            input=text,\n            model=\"text-embedding-3-large\"\n        ).data[0].embedding",
    "model_name = \"google/flan-t5-small\"\n\ntokenizer = AutoTokenizer.from_pretrained(model_name)\nmodel = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)\nmodel.eval()\n\ndecoder_start_token_id = model.config.decoder_start_token_id\nif decoder_start_token_id is None:\n    decoder_start_token_id = tokenizer.pad_token_id\n\neos_token_id = tokenizer.eos_token_id\nassert eos_token_id is not None, \"Tokenizer must define eos_token_id for sequence scoring.\"\n\ncandidate_token_ids = {\n    \"yes\": tokenizer(\"yes\", add_special_tokens=False).input_ids + [eos_token_id],\n    \"no\": tokenizer(\"no\", add_special_tokens=False).input_ids + [eos_token_id],\n}\n\nprint(model_name)\nprint(\"decoder_start_token_id:\", decoder_start_token_id)\nprint(\"eos_token_id:\", eos_token_id)\nprint({k: {\"ids\": v, \"decoded\": tokenizer.decode(v)} for k, v in candidate_token_ids.items()})\n",
    "ds = vault.query_item_content(\"glue_mrpc_validation\")\nds = Dataset.from_list(ds)\nprint(ds)\nprint(ds[0])\n\nsent1 = ds[\"sentence1\"]\nsent2 = ds[\"sentence2\"]\ny_true = np.array(ds[\"label\"])\n\ndef build_prompt(s1, s2):\n    return (\n        \"Are these two sentences paraphrases? Answer yes or no.\\n\"\n        f\"Sentence 1: {s1}\\n\"\n        f\"Sentence 2: {s2}\\n\"\n        \"Answer:\"\n    )\n\nprompts = [build_prompt(a, b) for a, b in zip(sent1, sent2)]\n\nprint(\"num_examples:\", len(y_true))\nprint(\"positive_rate:\", y_true.mean())\nprint(\"sample_prompt:\\n\", prompts[0])\n",
    "def score_candidate(enc, candidate_ids):\n    batch_size = enc[\"input_ids\"].shape[0]\n    target_ids = torch.tensor(candidate_ids, dtype=torch.long, device=device).unsqueeze(0).expand(batch_size, -1)\n    target_len = target_ids.shape[1]\n\n    decoder_input_ids = torch.full(\n        (batch_size, target_len),\n        fill_value=decoder_start_token_id,\n        dtype=torch.long,\n        device=device,\n    )\n    if target_len > 1:\n        decoder_input_ids[:, 1:] = target_ids[:, :-1]\n\n    outputs = model(**enc, decoder_input_ids=decoder_input_ids)\n    log_probs = torch.log_softmax(outputs.logits, dim=-1)\n    token_log_probs = log_probs.gather(dim=-1, index=target_ids.unsqueeze(-1)).squeeze(-1)\n    seq_log_probs = token_log_probs.sum(dim=-1)\n    return seq_log_probs\n\nbatch_size = 32\npreds = []\nyes_scores_all = []\nno_scores_all = []\n\nwith torch.inference_mode():\n    for i in tqdm(range(0, len(prompts), batch_size)):\n        batch_prompts = prompts[i:i + batch_size]\n\n        enc = tokenizer(\n            batch_prompts,\n            padding=True,\n            truncation=True,\n            max_length=256,\n            return_tensors=\"pt\",\n        )\n        enc = {k: v.to(device) for k, v in enc.items()}\n\n        yes_scores = score_candidate(enc, candidate_token_ids[\"yes\"])\n        no_scores = score_candidate(enc, candidate_token_ids[\"no\"])\n\n        batch_preds = (yes_scores > no_scores).long().cpu().numpy()\n\n        preds.extend(batch_preds.tolist())\n        yes_scores_all.extend(yes_scores.cpu().numpy().tolist())\n        no_scores_all.extend(no_scores.cpu().numpy().tolist())\n\ny_pred = np.array(preds)\nyes_scores_all = np.array(yes_scores_all)\nno_scores_all = np.array(no_scores_all)\nprint(\"done\")\n",
    "\nvault.create_record_list(\"flan_prediction_scored\", column_names=[\"prediction\", \"yes_scores\", \"no_scores\"])\n\nfor i in range(len(y_pred)):\n    vault.append_record(\"flan_prediction_scored\", \n                        {\n                            \"prediction\": int(y_pred[i]),\n                            \"yes_scores\": float(yes_scores_all[i]),\n                            \"no_scores\": float(no_scores_all[i]),\n                        },\n                       input_items = {\n                           \"glue_mrpc_validation\": [i, i + 1],\n                       }\n                       )\n\ndescription = \"flan_prediction_scored is a per-example prediction dataset generated by running google/flan-t5-small on the GLUE MRPC validation set with a yes/no paraphrase prompt. Each record corresponds to one input pair from glue_mrpc_validation and stores the model\\u2019s binary prediction and the sequence log-probability scores for the two candidate answers. The fields are: prediction (integer label, where 1 indicates yes/paraphrase and 0 indicates no/not paraphrase), yes_scores (float log-probability of the full answer token sequence for \\u201cyes\\u201d), and no_scores (float log-probability of the full answer token sequence for \\u201cno\\u201d). In this workflow, this dataset serves as the scored inference output used to inspect example-level model behavior and to compute downstream summary metrics such as accuracy, F1, and the classification report.\"\nembedding = get_embeddings(description)\nvault.create_description(\"flan_prediction_scored\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"record_type\": \"model prediction scores\", \"source\": \"glue/mrpc\", \"derived_from\": \"glue_mrpc_validation\", \"split\": \"validation\", \"size\": \"408\", \"model\": \"google/flan-t5-small\", \"model_family\": \"flan-t5\", \"scoring_method\": \"full answer logprob\", \"prompt_format\": \"yes/no question answering\", \"input_type\": \"sentence pair\", \"output_fields\": \"prediction, yes_scores, no_scores\", \"label_space\": \"yes/no\", \"domain\": \"news\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"flan_prediction_scored\", cat, embedding, prop)",
    "acc = accuracy_score(y_true, y_pred)\nf1 = f1_score(y_true, y_pred)\nreport = classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"])\nprint({\"accuracy\": acc, \"f1\": f1})\nprint(classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"]))\n",
    "for i in range(5):\n    print(\"=\" * 80)\n    print(\"sentence1:\", sent1[i])\n    print(\"sentence2:\", sent2[i])\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]), \"answer:\", \"yes\" if int(y_pred[i]) == 1 else \"no\")\n    print(\"yes_logprob:\", float(yes_scores_all[i]), \"no_logprob:\", float(no_scores_all[i]))\n",
    "mistakes = np.where(y_true != y_pred)[0][:10]\nprint(\"num_errors:\", int((y_true != y_pred).sum()))\n\nfor i in mistakes:\n    print(\"=\" * 80)\n    print(\"idx:\", int(i))\n    print(\"sentence1:\", sent1[i])\n    print(\"sentence2:\", sent2[i])\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]))\n    print(\"yes_logprob:\", float(yes_scores_all[i]), \"no_logprob:\", float(no_scores_all[i]))\n",
    "\nvault.create_record_list(\"flan_t5_full_answer_logprob_mrpc_summary\", column_names=[\"accuracy\", \"f1\", \"classification_report\"])\n\n\nsummary = {\n    \"accuracy\": float(acc),\n    \"f1\": float(f1),\n    \"classification_report\": str(report)\n}\n\nvault.append_record(\"flan_t5_full_answer_logprob_mrpc_summary\", summary,\n                    input_items = {\n                        \"glue_mrpc_validation\": [0, len(ds)],\n                        \"flan_prediction_scored\": [0, len(ds)]\n                    })\n\nsummary\n\ndescription = \"flan_t5_full_answer_logprob_mrpc_summary is an experiment-level summary dataset for evaluating google/flan-t5-small on the GLUE MRPC validation split using prompt-based yes/no paraphrase prediction with full-answer log-probability scoring. It contains a single record with three fields: accuracy (float), f1 (float), and classification_report (string from sklearn with per-class precision, recall, f1, and support for not_paraphrase and paraphrase). This dataset is produced after generating example-level predictions in flan_prediction_scored and comparing them against the ground-truth MRPC labels. Its role in the workflow is to store the aggregate evaluation results for the entire validation run, linking the underlying input dataset (glue_mrpc_validation) and the per-example prediction dataset (flan_prediction_scored).\"\nembedding = get_embeddings(description)\nvault.create_description(\"flan_t5_full_answer_logprob_mrpc_summary\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"dataset_type\": \"evaluation summary\", \"source\": \"glue/mrpc\", \"dataset\": \"MRPC\", \"split\": \"validation\", \"size\": \"408\", \"model\": \"google/flan-t5-small\", \"inference_method\": \"full answer log probability scoring\", \"label_space\": \"yes/no\", \"input_format\": \"sentence pair prompt\", \"metrics\": \"accuracy,f1,classification_report\", \"language\": \"English\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"flan_t5_full_answer_logprob_mrpc_summary\", cat, embedding, prop)\n\n",
    "description = \"This notebook runs a prompt-based paraphrase detection experiment on the GLUE MRPC validation set using google/flan-t5-small. For each sentence pair, it builds an instruction prompt asking whether the two sentences are paraphrases and scores the full decoder log probability of the candidate answers \\u201cyes\\u201d and \\u201cno\\u201d (including EOS). The predicted label is chosen by comparing these two sequence log probabilities.\\n\\nThe workflow loads MRPC validation data from TableVault, tokenizes prompts, performs batched inference with FLAN-T5, records per-example predictions and yes/no scores, and evaluates performance with accuracy, F1, and a classification report. It also prints sample predictions and error cases for qualitative inspection.\\n\\nResults are written back to TableVault as a scored prediction record list and a summary record list, with dataset lineage links and embedding-based descriptions/metadata for both the outputs and the overall notebook process.\" # description of whole notebook\nembedding = get_embeddings(description)\nvault.create_description(\"flan_t5_full_answer_logprob_mrpc\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"dataset\": \"glue/mrpc\", \"split\": \"validation\", \"model\": \"google/flan-t5-small\", \"model_family\": \"flan-t5\", \"approach\": \"prompt-based binary classification via seq2seq log-probability scoring\", \"label_space\": \"yes/no\", \"scoring_method\": \"full answer log probability comparison\", \"frameworks\": \"transformers, pytorch, datasets, scikit-learn\", \"evaluation\": \"accuracy, f1-score, classification report\", \"artifact_outputs\": \"per-example predictions and summary metrics\", \"tracking\": \"tablevault\", \"embedding_model\": \"text-embedding-3-large\"} #e.g. model: distilbert-base-uncased-MRPC\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"flan_t5_full_answer_logprob_mrpc\", cat, embedding, prop)"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 11477 | 56 | 27 | 9768 | 1.610s | 0.009s |

---

## Turn 16 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5afba45c81989307200313d74058`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_QMlgsrkWvcwzIhBl0z7h1s97",
    "output": "{\"ok\": true, \"result\": [\"def get_embeddings(text):\\n    return client.embeddings.create(\\n            input=text,\\n            model=\\\"text-embedding-3-large\\\"\\n        ).data[0].embedding\", \"model_name = \\\"google/flan-t5-small\\\"\\n\\ntokenizer = AutoTokenizer.from_pretrained(model_name)\\nmodel = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)\\nmodel.eval()\\n\\ndecoder_start_token_id = model.config.decoder_start_token_id\\nif decoder_start_token_id is None:\\n    decoder_start_token_id = tokenizer.pad_token_id\\n\\neos_token_id = tokenizer.eos_token_id\\nassert eos_token_id is not None, \\\"Tokenizer must define eos_token_id for sequence scoring.\\\"\\n\\ncandidate_token_ids = {\\n    \\\"yes\\\": tokenizer(\\\"yes\\\", add_special_tokens=False).input_ids + [eos_token_id],\\n    \\\"no\\\": tokenizer(\\\"no\\\", add_special_tokens=False).input_ids + [eos_token_id],\\n}\\n\\nprint(model_name)\\nprint(\\\"decoder_start_token_id:\\\", decoder_start_token_id)\\nprint(\\\"eos_token_id:\\\", eos_token_id)\\nprint({k: {\\\"ids\\\": v, \\\"decoded\\\": tokenizer.decode(v)} for k, v in candidate_token_ids.items()})\\n\", \"ds = vault.query_item_content(\\\"glue_mrpc_validation\\\")\\nds = Dataset.from_list(ds)\\nprint(ds)\\nprint(ds[0])\\n\\nsent1 = ds[\\\"sentence1\\\"]\\nsent2 = ds[\\\"sentence2\\\"]\\ny_true = np.array(ds[\\\"label\\\"])\\n\\ndef build_prompt(s1, s2):\\n    return (\\n        \\\"Are these two sentences paraphrases? Answer yes or no.\\\\n\\\"\\n        f\\\"Sentence 1: {s1}\\\\n\\\"\\n        f\\\"Sentence 2: {s2}\\\\n\\\"\\n        \\\"Answer:\\\"\\n    )\\n\\nprompts = [build_prompt(a, b) for a, b in zip(sent1, sent2)]\\n\\nprint(\\\"num_examples:\\\", len(y_true))\\nprint(\\\"positive_rate:\\\", y_true.mean())\\nprint(\\\"sample_prompt:\\\\n\\\", prompts[0])\\n\", \"def score_candidate(enc, candidate_ids):\\n    batch_size = enc[\\\"input_ids\\\"].shape[0]\\n    target_ids = torch.tensor(candidate_ids, dtype=torch.long, device=device).unsqueeze(0).expand(batch_size, -1)\\n    target_len = target_ids.shape[1]\\n\\n    decoder_input_ids = torch.full(\\n        (batch_size, target_len),\\n        fill_value=decoder_start_token_id,\\n        dtype=torch.long,\\n        device=device,\\n    )\\n    if target_len > 1:\\n        decoder_input_ids[:, 1:] = target_ids[:, :-1]\\n\\n    outputs = model(**enc, decoder_input_ids=decoder_input_ids)\\n    log_probs = torch.log_softmax(outputs.logits, dim=-1)\\n    token_log_probs = log_probs.gather(dim=-1, index=target_ids.unsqueeze(-1)).squeeze(-1)\\n    seq_log_probs = token_log_probs.sum(dim=-1)\\n    return seq_log_probs\\n\\nbatch_size = 32\\npreds = []\\nyes_scores_all = []\\nno_scores_all = []\\n\\nwith torch.inference_mode():\\n    for i in tqdm(range(0, len(prompts), batch_size)):\\n        batch_prompts = prompts[i:i + batch_size]\\n\\n        enc = tokenizer(\\n            batch_prompts,\\n            padding=True,\\n            truncation=True,\\n            max_length=256,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc = {k: v.to(device) for k, v in enc.items()}\\n\\n        yes_scores = score_candidate(enc, candidate_token_ids[\\\"yes\\\"])\\n        no_scores = score_candidate(enc, candidate_token_ids[\\\"no\\\"])\\n\\n        batch_preds = (yes_scores > no_scores).long().cpu().numpy()\\n\\n        preds.extend(batch_preds.tolist())\\n        yes_scores_all.extend(yes_scores.cpu().numpy().tolist())\\n        no_scores_all.extend(no_scores.cpu().numpy().tolist())\\n\\ny_pred = np.array(preds)\\nyes_scores_all = np.array(yes_scores_all)\\nno_scores_all = np.array(no_scores_all)\\nprint(\\\"done\\\")\\n\", \"\\nvault.create_record_list(\\\"flan_prediction_scored\\\", column_names=[\\\"prediction\\\", \\\"yes_scores\\\", \\\"no_scores\\\"])\\n\\nfor i in range(len(y_pred)):\\n    vault.append_record(\\\"flan_prediction_scored\\\", \\n                        {\\n                            \\\"prediction\\\": int(y_pred[i]),\\n                            \\\"yes_scores\\\": float(yes_scores_all[i]),\\n                            \\\"no_scores\\\": float(no_scores_all[i]),\\n                        },\\n                       input_items = {\\n                           \\\"glue_mrpc_validation\\\": [i, i + 1],\\n                       }\\n                       )\\n\\ndescription = \\\"flan_prediction_scored is a per-example prediction dataset generated by running google/flan-t5-small on the GLUE MRPC validation set with a yes/no paraphrase prompt. Each record corresponds to one input pair from glue_mrpc_validation and stores the model\\\\u2019s binary prediction and the sequence log-probability scores for the two candidate answers. The fields are: prediction (integer label, where 1 indicates yes/paraphrase and 0 indicates no/not paraphrase), yes_scores (float log-probability of the full answer token sequence for \\\\u201cyes\\\\u201d), and no_scores (float log-probability of the full answer token sequence for \\\\u201cno\\\\u201d). In this workflow, this dataset serves as the scored inference output used to inspect example-level model behavior and to compute downstream summary metrics such as accuracy, F1, and the classification report.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"flan_prediction_scored\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"record_type\\\": \\\"model prediction scores\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"derived_from\\\": \\\"glue_mrpc_validation\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"google/flan-t5-small\\\", \\\"model_family\\\": \\\"flan-t5\\\", \\\"scoring_method\\\": \\\"full answer logprob\\\", \\\"prompt_format\\\": \\\"yes/no question answering\\\", \\\"input_type\\\": \\\"sentence pair\\\", \\\"output_fields\\\": \\\"prediction, yes_scores, no_scores\\\", \\\"label_space\\\": \\\"yes/no\\\", \\\"domain\\\": \\\"news\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"flan_prediction_scored\\\", cat, embedding, prop)\", \"acc = accuracy_score(y_true, y_pred)\\nf1 = f1_score(y_true, y_pred)\\nreport = classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"])\\nprint({\\\"accuracy\\\": acc, \\\"f1\\\": f1})\\nprint(classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"]))\\n\", \"for i in range(5):\\n    print(\\\"=\\\" * 80)\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]), \\\"answer:\\\", \\\"yes\\\" if int(y_pred[i]) == 1 else \\\"no\\\")\\n    print(\\\"yes_logprob:\\\", float(yes_scores_all[i]), \\\"no_logprob:\\\", float(no_scores_all[i]))\\n\", \"mistakes = np.where(y_true != y_pred)[0][:10]\\nprint(\\\"num_errors:\\\", int((y_true != y_pred).sum()))\\n\\nfor i in mistakes:\\n    print(\\\"=\\\" * 80)\\n    print(\\\"idx:\\\", int(i))\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n    print(\\\"yes_logprob:\\\", float(yes_scores_all[i]), \\\"no_logprob:\\\", float(no_scores_all[i]))\\n\", \"\\nvault.create_record_list(\\\"flan_t5_full_answer_logprob_mrpc_summary\\\", column_names=[\\\"accuracy\\\", \\\"f1\\\", \\\"classification_report\\\"])\\n\\n\\nsummary = {\\n    \\\"accuracy\\\": float(acc),\\n    \\\"f1\\\": float(f1),\\n    \\\"classification_report\\\": str(report)\\n}\\n\\nvault.append_record(\\\"flan_t5_full_answer_logprob_mrpc_summary\\\", summary,\\n                    input_items = {\\n                        \\\"glue_mrpc_validation\\\": [0, len(ds)],\\n                        \\\"flan_prediction_scored\\\": [0, len(ds)]\\n                    })\\n\\nsummary\\n\\ndescription = \\\"flan_t5_full_answer_logprob_mrpc_summary is an experiment-level summary dataset for evaluating google/flan-t5-small on the GLUE MRPC validation split using prompt-based yes/no paraphrase prediction with full-answer log-probability scoring. It contains a single record with three fields: accuracy (float), f1 (float), and classification_report (string from sklearn with per-class precision, recall, f1, and support for not_paraphrase and paraphrase). This dataset is produced after generating example-level predictions in flan_prediction_scored and comparing them against the ground-truth MRPC labels. Its role in the workflow is to store the aggregate evaluation results for the entire validation run, linking the underlying input dataset (glue_mrpc_validation) and the per-example prediction dataset (flan_prediction_scored).\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"flan_t5_full_answer_logprob_mrpc_summary\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_type\\\": \\\"evaluation summary\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"dataset\\\": \\\"MRPC\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"google/flan-t5-small\\\", \\\"inference_method\\\": \\\"full answer log probability scoring\\\", \\\"label_space\\\": \\\"yes/no\\\", \\\"input_format\\\": \\\"sentence pair prompt\\\", \\\"metrics\\\": \\\"accuracy,f1,classification_report\\\", \\\"language\\\": \\\"English\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"flan_t5_full_answer_logprob_mrpc_summary\\\", cat, embedding, prop)\\n\\n\", \"description = \\\"This notebook runs a prompt-based paraphrase detection experiment on the GLUE MRPC validation set using google/flan-t5-small. For each sentence pair, it builds an instruction prompt asking whether the two sentences are paraphrases and scores the full decoder log probability of the candidate answers \\\\u201cyes\\\\u201d and \\\\u201cno\\\\u201d (including EOS). The predicted label is chosen by comparing these two sequence log probabilities.\\\\n\\\\nThe workflow loads MRPC validation data from TableVault, tokenizes prompts, performs batched inference with FLAN-T5, records per-example predictions and yes/no scores, and evaluates performance with accuracy, F1, and a classification report. It also prints sample predictions and error cases for qualitative inspection.\\\\n\\\\nResults are written back to TableVault as a scored prediction record list and a summary record list, with dataset lineage links and embedding-based descriptions/metadata for both the outputs and the overall notebook process.\\\" # description of whole notebook\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"flan_t5_full_answer_logprob_mrpc\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset\\\": \\\"glue/mrpc\\\", \\\"split\\\": \\\"validation\\\", \\\"model\\\": \\\"google/flan-t5-small\\\", \\\"model_family\\\": \\\"flan-t5\\\", \\\"approach\\\": \\\"prompt-based binary classification via seq2seq log-probability scoring\\\", \\\"label_space\\\": \\\"yes/no\\\", \\\"scoring_method\\\": \\\"full answer log probability comparison\\\", \\\"frameworks\\\": \\\"transformers, pytorch, datasets, scikit-learn\\\", \\\"evaluation\\\": \\\"accuracy, f1-score, classification report\\\", \\\"artifact_outputs\\\": \\\"per-example predictions and summary metrics\\\", \\\"tracking\\\": \\\"tablevault\\\", \\\"embedding_model\\\": \\\"text-embedding-3-large\\\"} #e.g. model: distilbert-base-uncased-MRPC\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"flan_t5_full_answer_logprob_mrpc\\\", cat, embedding, prop)\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5afba45c81989307200313d74058`

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
    "call_id": "call_0Oplqfm6TLzmK9ukqchIzDHt",
    "arguments": {
      "name": "entailment_logprob_odds_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_0Oplqfm6TLzmK9ukqchIzDHt`

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
| 14336 | 96 | 68 | 12627 | 2.452s | 0.022s |

---

## Turn 17 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5afe1efc819893d17efa65fe19fd`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_0Oplqfm6TLzmK9ukqchIzDHt",
    "output": "{\"ok\": true, \"result\": [\"import torch\\nimport numpy as np\\nfrom datasets import Dataset\\nfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\\nfrom tqdm.auto import tqdm\\n\", \"def get_embeddings(text):\\n    return client.embeddings.create(\\n            input=text,\\n            model=\\\"text-embedding-3-large\\\"\\n        ).data[0].embedding\", \"device = torch.device(\\\"mps\\\" if torch.backends.mps.is_available() else \\\"cpu\\\")\\nprint(\\\"device:\\\", device)\\n\", \"model_name = \\\"typeform/distilbert-base-uncased-mnli\\\"\\n\\ntokenizer = AutoTokenizer.from_pretrained(model_name)\\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\\nmodel.eval()\\n\\nid2label = model.config.id2label\\nlabel2id = model.config.label2id\\n\\ndef _normalize_label(x):\\n    return str(x).strip().lower().replace(\\\"-\\\", \\\"_\\\").replace(\\\" \\\", \\\"_\\\")\\n\\nnorm_label2id = {_normalize_label(k): int(v) for k, v in label2id.items()}\\n\\nif \\\"entailment\\\" in norm_label2id:\\n    entailment_id = norm_label2id[\\\"entailment\\\"]\\nelse:\\n    entailment_id = next(i for i, lab in id2label.items() if _normalize_label(lab) == \\\"entailment\\\")\\n\\nif \\\"contradiction\\\" in norm_label2id:\\n    contradiction_id = norm_label2id[\\\"contradiction\\\"]\\nelse:\\n    contradiction_id = next(i for i, lab in id2label.items() if _normalize_label(lab) == \\\"contradiction\\\")\\n\\nprint(model_name)\\nprint(\\\"id2label:\\\", id2label)\\nprint(\\\"entailment_id:\\\", entailment_id, \\\"contradiction_id:\\\", contradiction_id)\\n\", \"ds = vault.query_item_content(\\\"glue_mrpc_validation\\\")\\nds = Dataset.from_list(ds)\\nprint(ds)\\nprint(ds[0])\\n\\nsent1 = ds[\\\"sentence1\\\"]\\nsent2 = ds[\\\"sentence2\\\"]\\ny_true = np.array(ds[\\\"label\\\"])\\n\\nprint(\\\"num_examples:\\\", len(y_true))\\nprint(\\\"positive_rate:\\\", float(y_true.mean()))\\n\", \"batch_size = 64\\ndir12_scores = []\\ndir21_scores = []\\navg_scores = []\\npreds = []\\n\\nwith torch.no_grad():\\n    for i in tqdm(range(0, len(ds), batch_size)):\\n        batch_s1 = sent1[i:i + batch_size]\\n        batch_s2 = sent2[i:i + batch_size]\\n\\n        enc12 = tokenizer(\\n            batch_s1,\\n            batch_s2,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc21 = tokenizer(\\n            batch_s2,\\n            batch_s1,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n\\n        enc12 = {k: v.to(device) for k, v in enc12.items()}\\n        enc21 = {k: v.to(device) for k, v in enc21.items()}\\n\\n        logits12 = model(**enc12).logits\\n        logits21 = model(**enc21).logits\\n\\n        log_probs12 = torch.log_softmax(logits12, dim=-1)\\n        log_probs21 = torch.log_softmax(logits21, dim=-1)\\n\\n        score12 = (log_probs12[:, entailment_id] - log_probs12[:, contradiction_id]).detach().cpu().numpy()\\n        score21 = (log_probs21[:, entailment_id] - log_probs21[:, contradiction_id]).detach().cpu().numpy()\\n        score_avg = 0.5 * (score12 + score21)\\n        batch_preds = (score_avg > 0).astype(np.int64)\\n\\n        dir12_scores.extend(score12.tolist())\\n        dir21_scores.extend(score21.tolist())\\n        avg_scores.extend(score_avg.tolist())\\n        preds.extend(batch_preds.tolist())\\n\\ndir12_scores = np.array(dir12_scores)\\ndir21_scores = np.array(dir21_scores)\\navg_scores = np.array(avg_scores)\\ny_pred = np.array(preds)\\n\\nprint(\\\"done\\\")\\nprint(\\\"pred_positive_rate:\\\", float(y_pred.mean()))\\n\", \"vault.create_record_list(\\\"mrpc_entailment_prediction\\\", column_names=[\\\"prediction\\\", \\\"dir12\\\", \\\"dir21\\\"])\\n\\nfor i in range(len(y_pred)):\\n    vault.append_record(\\\"mrpc_entailment_prediction\\\", \\n                        {\\n                            \\\"prediction\\\": int(y_pred[i]),\\n                            \\\"dir12\\\": float(dir12_scores[i]),\\n                            \\\"dir21\\\": float(dir21_scores[i]),\\n                        },\\n                       input_items = {\\n                           \\\"glue_mrpc_validation\\\": [i, i + 1],\\n                       }\\n                       )\\n\\ndescription = \\\"mrpc_entailment_prediction contains per-example prediction outputs for the GLUE MRPC validation set generated with the typeform/distilbert-base-uncased-mnli NLI model. Each record corresponds to one validation pair from glue_mrpc_validation and stores three fields: prediction (binary paraphrase decision obtained by thresholding the averaged score at 0), dir12 (entailment-minus-contradiction log-probability score for sentence1 \\\\u2192 sentence2), and dir21 (the same score for sentence2 \\\\u2192 sentence1). The dataset is aligned one-to-one with the source MRPC examples through input item indexing. Its role in this workflow is to capture the model\\\\u2019s directional entailment-based evidence and final paraphrase prediction for downstream evaluation, error analysis, and summary metric computation.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"mrpc_entailment_prediction\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"method\\\": \\\"mnli entailment vs contradiction logprob odds\\\", \\\"dataset_type\\\": \\\"model predictions\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"input_dataset\\\": \\\"glue_mrpc_validation\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"prediction_target\\\": \\\"mrpc label\\\", \\\"labels\\\": \\\"0=not_paraphrase,1=paraphrase\\\", \\\"features\\\": \\\"prediction,dir12,dir21\\\", \\\"pair_ordering\\\": \\\"sentence1->sentence2 and sentence2->sentence1\\\", \\\"text_fields\\\": \\\"sentence1,sentence2\\\", \\\"domain\\\": \\\"news\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"mrpc_entailment_prediction\\\", cat, embedding, prop)\", \"acc = accuracy_score(y_true, y_pred)\\nf1 = f1_score(y_true, y_pred)\\nreport = classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"])\\nprint({\\\"accuracy\\\": acc, \\\"f1\\\": f1})\\nprint(classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"]))\\n\", \"for i in range(5):\\n    print(\\\"=\\\" * 80)\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"dir12_log_odds:\\\", float(dir12_scores[i]))\\n    print(\\\"dir21_log_odds:\\\", float(dir21_scores[i]))\\n    print(\\\"avg_log_odds:\\\", float(avg_scores[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n\", \"mistakes = np.where(y_true != y_pred)[0][:10]\\nprint(\\\"num_errors:\\\", int((y_true != y_pred).sum()))\\n\\nfor i in mistakes:\\n    print(\\\"=\\\" * 80)\\n    print(\\\"idx:\\\", int(i))\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"dir12_log_odds:\\\", float(dir12_scores[i]))\\n    print(\\\"dir21_log_odds:\\\", float(dir21_scores[i]))\\n    print(\\\"avg_log_odds:\\\", float(avg_scores[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n\", \"vault.create_record_list(\\\"entailment_logprob_odds_mrpc_summary\\\", column_names=[\\\"accuracy\\\", \\\"f1\\\", \\\"classification_report\\\"])\\n\\n\\nsummary = {\\n    \\\"accuracy\\\": float(acc),\\n    \\\"f1\\\": float(f1),\\n    \\\"classification_report\\\": str(report)\\n}\\n\\nvault.append_record(\\\"entailment_logprob_odds_mrpc_summary\\\", summary,\\n                    input_items = {\\n                        \\\"glue_mrpc_validation\\\": [0, len(ds)],\\n                        \\\"mrpc_entailment_prediction\\\": [0, len(ds)]\\n                    })\\n\\nsummary\\n\\ndescription = \\\"Summary dataset for the MRPC entailment-logprob-odds experiment on the GLUE MRPC validation split. It contains evaluation results for paraphrase predictions produced from a zero-shot NLI model (typeform/distilbert-base-uncased-mnli), where each sentence pair is scored using the average entailment-vs-contradiction log-odds across both input orders. Structure: one record with columns accuracy (float), f1 (float), and classification_report (string). Its role in this workflow is to provide a compact experiment-level summary of model performance, derived from the full per-example outputs in mrpc_entailment_prediction and the ground-truth labels in glue_mrpc_validation.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"entailment_logprob_odds_mrpc_summary\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_type\\\": \\\"evaluation summary\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"source_table\\\": \\\"glue_mrpc_validation\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"input_type\\\": \\\"sentence pair\\\", \\\"labels\\\": \\\"not_paraphrase,paraphrase\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"method\\\": \\\"entailment_minus_contradiction_logprob_odds_avg_bidirectional\\\", \\\"metrics\\\": \\\"accuracy,f1,classification_report\\\", \\\"domain\\\": \\\"news\\\", \\\"process\\\": \\\"entailment_logprob_odds_mrpc\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"entailment_logprob_odds_mrpc_summary\\\", cat, embedding, prop)\\n\\n\", \"description = \\\"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using an NLI model. It loads sentence pairs and labels from TableVault, applies the typeform/distilbert-base-uncased-mnli sequence classification model, and treats paraphrase detection as entailment scoring: for each pair, it computes the log-probability difference between entailment and contradiction for both sentence orders (sentence1\\\\u2192sentence2 and sentence2\\\\u2192sentence1), averages the two directional scores, and predicts paraphrase when the averaged score is positive. The notebook stores per-example predictions and directional entailment log-odds in TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves both dataset-level summaries and notebook-level metadata/descriptions with OpenAI embeddings for documentation and retrieval.\\\" # description of whole notebook\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"entailment_logprob_odds_mrpc\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"approach\\\": \\\"NLI entailment-vs-contradiction log-probability odds\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"model_family\\\": \\\"DistilBERT MNLI sequence classification\\\", \\\"dataset\\\": \\\"glue/mrpc\\\", \\\"dataset_split\\\": \\\"validation\\\", \\\"input_type\\\": \\\"sentence pair\\\", \\\"prediction_rule\\\": \\\"average bidirectional entailment log-odds > 0\\\", \\\"evaluation\\\": \\\"accuracy, f1-score, classification report\\\", \\\"metrics\\\": \\\"accuracy, f1\\\", \\\"artifacts\\\": \\\"per-example predictions, directional scores, summary metrics\\\", \\\"tracking\\\": \\\"TableVault\\\", \\\"embedding_model\\\": \\\"text-embedding-3-large\\\", \\\"frameworks\\\": \\\"transformers, torch, sklearn, datasets\\\", \\\"process_name\\\": \\\"entailment_logprob_odds_mrpc\\\"} #e.g. model: distilbert-base-uncased-MRPC\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"entailment_logprob_odds_mrpc\\\", cat, embedding, prop)\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5afe1efc819893d17efa65fe19fd`

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
    "call_id": "call_ugTPwIYuJmprQ8Uzu6QLoGCS",
    "arguments": {
      "name": "softmax_gap_mean_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_ugTPwIYuJmprQ8Uzu6QLoGCS`

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
| 17341 | 96 | 71 | 15632 | 3.049s | 0.020s |

---

## Turn 18 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5b0136648198b051ec78107bac83`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_ugTPwIYuJmprQ8Uzu6QLoGCS",
    "output": "{\"ok\": true, \"result\": [\"def get_embeddings(text):\\n    return client.embeddings.create(\\n            input=text,\\n            model=\\\"text-embedding-3-large\\\"\\n        ).data[0].embedding\", \"import torch\\nimport numpy as np\\nfrom datasets import Dataset\\nfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\\nfrom tqdm.auto import tqdm\\n\\ndevice = torch.device(\\\"mps\\\" if torch.backends.mps.is_available() else \\\"cpu\\\")\\nprint(\\\"device:\\\", device)\", \"model_name = \\\"typeform/distilbert-base-uncased-mnli\\\"\\n\\ntokenizer = AutoTokenizer.from_pretrained(model_name)\\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\\nmodel.eval()\\n\\nid2label = {int(k): v for k, v in model.config.id2label.items()} if hasattr(model.config.id2label, \\\"items\\\") else dict(enumerate(model.config.id2label))\\nlabel_text = {i: str(v).lower() for i, v in id2label.items()}\\nentailment_id = next(i for i, v in label_text.items() if \\\"entail\\\" in v)\\ncontradiction_id = next(i for i, v in label_text.items() if \\\"contrad\\\" in v)\\n\\nprint(\\\"model_name:\\\", model_name)\\nprint(\\\"id2label:\\\", id2label)\\nprint(\\\"entailment_id:\\\", entailment_id, \\\"contradiction_id:\\\", contradiction_id)\", \"ds = vault.query_item_content(\\\"glue_mrpc_validation\\\")\\nds = Dataset.from_list(ds)\\nprint(ds)\\nprint(ds[0])\\n\\nsent1 = ds[\\\"sentence1\\\"]\\nsent2 = ds[\\\"sentence2\\\"]\\ny_true = np.array(ds[\\\"label\\\"])\\n\\nprint(\\\"num_examples:\\\", len(y_true))\\nprint(\\\"positive_rate:\\\", float(y_true.mean()))\", \"batch_size = 64\\npreds = []\\ngap_12_all = []\\ngap_21_all = []\\navg_gap_all = []\\n\\nwith torch.no_grad():\\n    for i in tqdm(range(0, len(ds), batch_size)):\\n        batch_s1 = sent1[i:i + batch_size]\\n        batch_s2 = sent2[i:i + batch_size]\\n\\n        enc_12 = tokenizer(\\n            batch_s1,\\n            batch_s2,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc_21 = tokenizer(\\n            batch_s2,\\n            batch_s1,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n\\n        enc_12 = {k: v.to(device) for k, v in enc_12.items()}\\n        enc_21 = {k: v.to(device) for k, v in enc_21.items()}\\n\\n        logits_12 = model(**enc_12).logits\\n        logits_21 = model(**enc_21).logits\\n\\n        probs_12 = torch.softmax(logits_12, dim=-1)\\n        probs_21 = torch.softmax(logits_21, dim=-1)\\n\\n        gap_12 = probs_12[:, entailment_id] - probs_12[:, contradiction_id]\\n        gap_21 = probs_21[:, entailment_id] - probs_21[:, contradiction_id]\\n        avg_gap = (gap_12 + gap_21) / 2.0\\n\\n        batch_preds = (avg_gap > 0).long().cpu().numpy()\\n\\n        preds.extend(batch_preds.tolist())\\n        gap_12_all.extend(gap_12.cpu().numpy().tolist())\\n        gap_21_all.extend(gap_21.cpu().numpy().tolist())\\n        avg_gap_all.extend(avg_gap.cpu().numpy().tolist())\\n\\ny_pred = np.array(preds)\\ngap_12_all = np.array(gap_12_all)\\ngap_21_all = np.array(gap_21_all)\\navg_gap_all = np.array(avg_gap_all)\\n\\nprint(\\\"done\\\")\", \"vault.create_record_list(\\\"mrpc_mean_gap_prediction\\\", column_names=[\\\"prediction\\\", \\\"gap_12\\\", \\\"gap_21\\\"])\\n\\nfor i in range(len(y_pred)):\\n    vault.append_record(\\\"mrpc_mean_gap_prediction\\\", \\n                        {\\n                            \\\"prediction\\\": int(y_pred[i]),\\n                            \\\"gap_12\\\": float(gap_12_all[i]),\\n                            \\\"gap_21\\\": float(gap_21_all[i]),\\n                        },\\n                       input_items = {\\n                           \\\"glue_mrpc_validation\\\": [i, i + 1],\\n                       }\\n                       )\\n\\ndescription = \\\"Per-example prediction dataset for the GLUE MRPC validation split, generated by running the sentence pairs through the typeform/distilbert-base-uncased-mnli model in both input orders. Each record corresponds to one MRPC validation example and is linked to the matching row in glue_mrpc_validation. The dataset has three fields: prediction (binary paraphrase decision, where 1 indicates paraphrase and 0 indicates not paraphrase), gap_12 (entailment probability minus contradiction probability for sentence1\\\\u2192sentence2), and gap_21 (the same probability gap for sentence2\\\\u2192sentence1). In this workflow, it serves as the stored per-instance model output used to inspect directional confidence, compare predictions with ground-truth MRPC labels, and build the downstream summary metrics in softmax_gap_mean_mrpc_summary.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"mrpc_mean_gap_prediction\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"data_type\\\": \\\"model predictions\\\", \\\"prediction_type\\\": \\\"binary classification\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"derived_from\\\": \\\"glue_mrpc_validation\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"input_type\\\": \\\"sentence pair\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"method\\\": \\\"mean softmax entailment-contradiction gap over both sentence orders\\\", \\\"columns\\\": \\\"prediction,gap_12,gap_21\\\", \\\"label_space\\\": \\\"0=not_paraphrase,1=paraphrase\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"mrpc_mean_gap_prediction\\\", cat, embedding, prop)\", \"acc = accuracy_score(y_true, y_pred)\\nf1 = f1_score(y_true, y_pred)\\nreport = classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"])\\nprint({\\\"accuracy\\\": acc, \\\"f1\\\": f1})\\nprint(classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"]))\", \"for i in range(5):\\n    print(\\\"=\\\" * 80)\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"gap_12:\\\", float(gap_12_all[i]))\\n    print(\\\"gap_21:\\\", float(gap_21_all[i]))\\n    print(\\\"avg_gap:\\\", float(avg_gap_all[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\", \"mistakes = np.where(y_true != y_pred)[0][:10]\\nprint(\\\"num_errors:\\\", int((y_true != y_pred).sum()))\\n\\nfor i in mistakes:\\n    print(\\\"=\\\" * 80)\\n    print(\\\"idx:\\\", int(i))\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"gap_12:\\\", float(gap_12_all[i]))\\n    print(\\\"gap_21:\\\", float(gap_21_all[i]))\\n    print(\\\"avg_gap:\\\", float(avg_gap_all[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\", \"vault.create_record_list(\\\"softmax_gap_mean_mrpc_summary\\\", column_names=[\\\"accuracy\\\", \\\"f1\\\", \\\"classification_report\\\"])\\n\\n\\nsummary = {\\n    \\\"accuracy\\\": float(acc),\\n    \\\"f1\\\": float(f1),\\n    \\\"classification_report\\\": str(report)\\n}\\n\\nvault.append_record(\\\"softmax_gap_mean_mrpc_summary\\\", summary,\\n                    input_items = {\\n                        \\\"glue_mrpc_validation\\\": [0, len(ds)],\\n                        \\\"mrpc_mean_gap_prediction\\\": [0, len(ds)]\\n                    })\\n\\nsummary\\n\\ndescription = \\\"Summary dataset for the MRPC validation experiment using an MNLI sequence-classification model and the mean softmax-gap decision rule. It contains a single aggregate record with three fields: accuracy (float), f1 (float), and classification_report (string). These metrics are computed by comparing ground-truth MRPC labels from glue_mrpc_validation against predictions in mrpc_mean_gap_prediction, where each prediction is based on the average of the entailment-minus-contradiction probability gap for both sentence orders (sentence1, sentence2) and (sentence2, sentence1). In this workflow, this dataset serves as the experiment-level evaluation output summarizing model performance over the full validation set.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"softmax_gap_mean_mrpc_summary\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_type\\\": \\\"evaluation summary\\\", \\\"benchmark\\\": \\\"GLUE\\\", \\\"source\\\": \\\"glue_mrpc_validation\\\", \\\"subset\\\": \\\"MRPC\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"inference_method\\\": \\\"mean softmax entailment-contradiction gap over both sentence orders\\\", \\\"metrics\\\": \\\"accuracy,f1,classification_report\\\", \\\"input_prediction_dataset\\\": \\\"mrpc_mean_gap_prediction\\\", \\\"process_name\\\": \\\"softmax_gap_mean_mrpc\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"softmax_gap_mean_mrpc_summary\\\", cat, embedding, prop)\\n\\n\", \"description = \\\"This notebook runs a paraphrase detection experiment on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli sequence classification model in an NLI-style formulation. For each sentence pair, it scores both input orders (sentence1, sentence2) and (sentence2, sentence1), computes the softmax probability gap between entailment and contradiction for each order, averages the two gaps, and predicts paraphrase when the mean gap is greater than zero. The workflow loads the MRPC validation examples from TableVault, performs batched inference with Hugging Face Transformers and PyTorch, and stores per-example predictions and gap scores back into TableVault with lineage to the source records. It then evaluates the method with accuracy, F1, and a classification report, inspects sample predictions and errors, and saves an experiment summary plus descriptive metadata and embeddings for the prediction table, summary table, and overall notebook process.\\\" # description of whole notebook\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"softmax_gap_mean_mrpc\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset\\\": \\\"glue/mrpc\\\", \\\"dataset_split\\\": \\\"validation\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"model_family\\\": \\\"distilbert\\\", \\\"inference_type\\\": \\\"zero-shot NLI\\\", \\\"prediction_method\\\": \\\"mean entailment-contradiction softmax gap over sentence order swaps\\\", \\\"input_format\\\": \\\"sentence pair classification\\\", \\\"framework\\\": \\\"transformers, pytorch\\\", \\\"metrics\\\": \\\"accuracy, f1-score, classification report\\\", \\\"outputs\\\": \\\"per-example predictions and summary metrics\\\", \\\"tracking\\\": \\\"tablevault\\\", \\\"vector_embedding_model\\\": \\\"text-embedding-3-large\\\", \\\"llm_provider\\\": \\\"openai\\\"} #e.g. model: distilbert-base-uncased-MRPC\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"softmax_gap_mean_mrpc\\\", cat, embedding, prop)\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5b0136648198b051ec78107bac83`

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
    "call_id": "call_vlyv4k6uTITOMvUeXPvqQ7GU",
    "arguments": {
      "name": "min_direction_margin_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_vlyv4k6uTITOMvUeXPvqQ7GU`

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
| 20187 | 38 | 14 | 18478 | 1.312s | 0.025s |

---

## Turn 19 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5b028a6c8198b92e2cf9082f204f`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_vlyv4k6uTITOMvUeXPvqQ7GU",
    "output": "{\"ok\": true, \"result\": [\"import torch\\nimport numpy as np\\nfrom datasets import Dataset\\nfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\\nfrom tqdm.auto import tqdm\\n\\ndevice = torch.device(\\\"mps\\\" if torch.backends.mps.is_available() else \\\"cpu\\\")\\nprint(\\\"device:\\\", device)\\n\", \"def get_embeddings(text):\\n    return client.embeddings.create(\\n            input=text,\\n            model=\\\"text-embedding-3-large\\\"\\n        ).data[0].embedding\", \"model_name = \\\"typeform/distilbert-base-uncased-mnli\\\"\\n\\ntokenizer = AutoTokenizer.from_pretrained(model_name)\\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\\nmodel.eval()\\n\\nid2label = {int(k): v for k, v in model.config.id2label.items()}\\nentailment_id = next(i for i, label in id2label.items() if \\\"entail\\\" in label.lower())\\ncontradiction_id = next(i for i, label in id2label.items() if \\\"contrad\\\" in label.lower())\\n\\nprint(\\\"model:\\\", model_name)\\nprint(\\\"id2label:\\\", id2label)\\nprint(\\\"entailment_id:\\\", entailment_id, \\\"label:\\\", id2label[entailment_id])\\nprint(\\\"contradiction_id:\\\", contradiction_id, \\\"label:\\\", id2label[contradiction_id])\\n\", \"ds = vault.query_item_content(\\\"glue_mrpc_validation\\\")\\nds = Dataset.from_list(ds)\\nprint(ds)\\nprint(ds[0])\\n\\nsent1 = ds[\\\"sentence1\\\"]\\nsent2 = ds[\\\"sentence2\\\"]\\ny_true = np.array(ds[\\\"label\\\"])\\n\\nprint(\\\"num_examples:\\\", len(y_true))\\nprint(\\\"positive_rate:\\\", float(y_true.mean()))\\n\", \"batch_size = 64\\nmargin_12_all = []\\nmargin_21_all = []\\nmin_margin_all = []\\n\\nwith torch.no_grad():\\n    for i in tqdm(range(0, len(ds), batch_size)):\\n        batch_s1 = sent1[i:i + batch_size]\\n        batch_s2 = sent2[i:i + batch_size]\\n\\n        enc_12 = tokenizer(\\n            batch_s1,\\n            batch_s2,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc_21 = tokenizer(\\n            batch_s2,\\n            batch_s1,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n\\n        enc_12 = {k: v.to(device) for k, v in enc_12.items()}\\n        enc_21 = {k: v.to(device) for k, v in enc_21.items()}\\n\\n        logits_12 = model(**enc_12).logits\\n        logits_21 = model(**enc_21).logits\\n\\n        margin_12 = (logits_12[:, entailment_id] - logits_12[:, contradiction_id]).detach().cpu().numpy()\\n        margin_21 = (logits_21[:, entailment_id] - logits_21[:, contradiction_id]).detach().cpu().numpy()\\n        min_margin = np.minimum(margin_12, margin_21)\\n\\n        margin_12_all.extend(margin_12.tolist())\\n        margin_21_all.extend(margin_21.tolist())\\n        min_margin_all.extend(min_margin.tolist())\\n\\nmargin_12_all = np.array(margin_12_all)\\nmargin_21_all = np.array(margin_21_all)\\nmin_margin_all = np.array(min_margin_all)\\ny_pred = (min_margin_all > 0).astype(int)\\n\\nprint(\\\"done\\\")\\nprint(\\\"predicted_positive_rate:\\\", float(y_pred.mean()))\\n\", \"vault.create_record_list(\\\"mrpc_min_margin_prediction\\\", column_names=[\\\"prediction\\\", \\\"min_margin\\\"])\\n\\nfor i in range(len(y_pred)):\\n    vault.append_record(\\\"mrpc_min_margin_prediction\\\", \\n                        {\\n                            \\\"prediction\\\": int(y_pred[i]),\\n                            \\\"min_margin\\\": float(min_margin_all[i]),\\n                        },\\n                       input_items = {\\n                           \\\"glue_mrpc_validation\\\": [i, i + 1],\\n                       }\\n                       )\\n\\ndescription = \\\"mrpc_min_margin_prediction is an example-level prediction dataset derived from the GLUE MRPC validation split. For each sentence pair in glue_mrpc_validation, it stores the binary paraphrase prediction produced by a zero-shot NLI model (typeform/distilbert-base-uncased-mnli) and the confidence score used to make that prediction.\\\\n\\\\nEach record corresponds to one MRPC validation example and has two fields: prediction, an integer label where 1 indicates paraphrase and 0 indicates not_paraphrase; and min_margin, a float equal to the minimum of the entailment-versus-contradiction logit margins computed in both input directions, sentence1\\\\u2192sentence2 and sentence2\\\\u2192sentence1. The prediction is defined as 1 when min_margin > 0, otherwise 0.\\\\n\\\\nIn this workflow, this dataset serves as the per-example output of the min-direction-margin inference step. It is used as the input to downstream evaluation and summarization, including accuracy, F1, classification report generation, and error analysis.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"mrpc_min_margin_prediction\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_type\\\": \\\"model predictions\\\", \\\"source_dataset\\\": \\\"glue_mrpc_validation\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"input_type\\\": \\\"sentence pair\\\", \\\"output_type\\\": \\\"binary prediction with confidence margin\\\", \\\"output_columns\\\": \\\"prediction,min_margin\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"method\\\": \\\"minimum directional entailment-contradiction margin\\\", \\\"label_space\\\": \\\"0=not_paraphrase,1=paraphrase\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"mrpc_min_margin_prediction\\\", cat, embedding, prop)\", \"acc = accuracy_score(y_true, y_pred)\\nf1 = f1_score(y_true, y_pred)\\nreport = classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"])\\nprint({\\\"accuracy\\\": acc, \\\"f1\\\": f1})\\nprint(classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"]))\\n\", \"for i in range(5):\\n    print(\\\"=\\\" * 80)\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"margin_12:\\\", float(margin_12_all[i]))\\n    print(\\\"margin_21:\\\", float(margin_21_all[i]))\\n    print(\\\"min_margin:\\\", float(min_margin_all[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n\", \"mistakes = np.where(y_true != y_pred)[0][:10]\\nprint(\\\"num_errors:\\\", int((y_true != y_pred).sum()))\\n\\nfor i in mistakes:\\n    print(\\\"=\\\" * 80)\\n    print(\\\"idx:\\\", int(i))\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"margin_12:\\\", float(margin_12_all[i]))\\n    print(\\\"margin_21:\\\", float(margin_21_all[i]))\\n    print(\\\"min_margin:\\\", float(min_margin_all[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n\", \"vault.create_record_list(\\\"min_direction_margin_mrpc_summary\\\", column_names=[\\\"accuracy\\\", \\\"f1\\\", \\\"classification_report\\\"])\\n\\n\\nsummary = {\\n    \\\"accuracy\\\": float(acc),\\n    \\\"f1\\\": float(f1),\\n    \\\"classification_report\\\": str(report)\\n}\\n\\nvault.append_record(\\\"min_direction_margin_mrpc_summary\\\", summary,\\n                    input_items = {\\n                        \\\"glue_mrpc_validation\\\": [0, len(ds)],\\n                        \\\"mrpc_min_margin_prediction\\\": [0, len(ds)]\\n                    })\\n\\nsummary\\n\\ndescription = \\\"Summary dataset for the min_direction_margin_mrpc workflow. It contains experiment-level evaluation results for paraphrase detection on the GLUE MRPC validation set, where predictions are made by scoring each sentence pair in both directions with an MNLI model and using the minimum entailment-minus-contradiction margin as the decision signal. The dataset has one record with three fields: accuracy (float), f1 (float), and classification_report (string). Its role is to store the final aggregated performance summary derived from the source validation examples and the per-example prediction dataset mrpc_min_margin_prediction, so future users can quickly inspect the overall outcome of this notebook without recomputing metrics.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"min_direction_margin_mrpc_summary\\\", description, embedding)\\n\\nproperties = {\\\"artifact_type\\\": \\\"evaluation summary\\\", \\\"task\\\": \\\"paraphrase detection\\\", \\\"benchmark\\\": \\\"GLUE\\\", \\\"dataset\\\": \\\"MRPC\\\", \\\"source\\\": \\\"glue_mrpc_validation\\\", \\\"split\\\": \\\"validation\\\", \\\"domain\\\": \\\"news\\\", \\\"evaluated_examples\\\": \\\"408\\\", \\\"label_space\\\": \\\"binary\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"inference_method\\\": \\\"min directional entailment-contradiction margin\\\", \\\"prediction_source\\\": \\\"mrpc_min_margin_prediction\\\", \\\"metrics\\\": \\\"accuracy,f1,classification_report\\\", \\\"process\\\": \\\"min_direction_margin_mrpc\\\", \\\"framework\\\": \\\"transformers\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"min_direction_margin_mrpc_summary\\\", cat, embedding, prop)\\n\\n\", \"description = \\\"This notebook evaluates a directional-margin approach to paraphrase detection on the GLUE MRPC validation set. It loads sentence pairs and labels from TableVault, runs the typeform/distilbert-base-uncased-mnli sequence classification model as an NLI-based paraphrase scorer in both directions (sentence1\\\\u2192sentence2 and sentence2\\\\u2192sentence1), computes the entailment-minus-contradiction logit margin for each direction, and uses the minimum of the two margins as the final paraphrase score; pairs with positive minimum margin are predicted as paraphrases. The workflow then stores per-example predictions and margins in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, inspects sample predictions and errors, and saves a summary record and notebook-level metadata back to TableVault.\\\" # description of whole notebook\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"min_direction_margin_mrpc\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"method\\\": \\\"bidirectional NLI min-direction margin\\\", \\\"dataset\\\": \\\"glue/mrpc validation\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"model_family\\\": \\\"DistilBERT\\\", \\\"inference_type\\\": \\\"zero-shot sequence pair classification\\\", \\\"label_rule\\\": \\\"predict paraphrase when min(entailment-contradiction margin in both directions) > 0\\\", \\\"evaluation\\\": \\\"accuracy, f1-score, classification report\\\", \\\"frameworks\\\": \\\"PyTorch, Transformers, Hugging Face Datasets, scikit-learn\\\", \\\"storage\\\": \\\"TableVault\\\", \\\"metadata_embeddings\\\": \\\"OpenAI text-embedding-3-large\\\", \\\"process_name\\\": \\\"min_direction_margin_mrpc\\\"} #e.g. model: distilbert-base-uncased-MRPC\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"min_direction_margin_mrpc\\\", cat, embedding, prop)\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5b028a6c8198b92e2cf9082f204f`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_code",
    "call_id": "call_DeWlDQmvfuTOj5XJGAFt9NHE",
    "arguments": {
      "name": "consensus_then_avg_margin_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_DeWlDQmvfuTOj5XJGAFt9NHE`

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
| 22945 | 24 | 0 | 21236 | 1.230s | 0.006s |

---

## Turn 20 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5b03c5048198a8188482ac21c9d2`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_DeWlDQmvfuTOj5XJGAFt9NHE",
    "output": "{\"ok\": true, \"result\": [\"def get_embeddings(text):\\n    return client.embeddings.create(\\n            input=text,\\n            model=\\\"text-embedding-3-large\\\"\\n        ).data[0].embedding\", \"import torch\\nimport numpy as np\\nfrom datasets import Dataset\\nfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\\nfrom tqdm.auto import tqdm\\n\\ndevice = torch.device(\\\"mps\\\" if torch.backends.mps.is_available() else \\\"cpu\\\")\\nprint(\\\"device:\\\", device)\\n\", \"model_name = \\\"typeform/distilbert-base-uncased-mnli\\\"\\n\\ntokenizer = AutoTokenizer.from_pretrained(model_name)\\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\\nmodel.eval()\\n\\nid2label = {int(k): v for k, v in model.config.id2label.items()}\\nlabel_lookup = {idx: str(label).lower().strip() for idx, label in id2label.items()}\\n\\ndef find_label_id(target):\\n    matches = [idx for idx, label in label_lookup.items() if label == target]\\n    if not matches:\\n        raise ValueError(f\\\"Could not find label id for {target!r} in {label_lookup}\\\")\\n    return matches[0]\\n\\ncontradiction_id = find_label_id(\\\"contradiction\\\")\\nentailment_id = find_label_id(\\\"entailment\\\")\\n\\nprint(\\\"model:\\\", model_name)\\nprint(\\\"id2label:\\\", id2label)\\nprint(\\\"contradiction_id:\\\", contradiction_id)\\nprint(\\\"entailment_id:\\\", entailment_id)\\n\", \"ds = vault.query_item_content(\\\"glue_mrpc_validation\\\")\\nds = Dataset.from_list(ds)\\nprint(ds)\\nprint(ds[0])\\n\\nsent1 = ds[\\\"sentence1\\\"]\\nsent2 = ds[\\\"sentence2\\\"]\\ny_true = np.array(ds[\\\"label\\\"])\\n\\nprint(\\\"num_examples:\\\", len(y_true))\\nprint(\\\"positive_rate:\\\", float(y_true.mean()))\\n\", \"batch_size = 64\\nlogits_12_parts = []\\nlogits_21_parts = []\\nargmax_12_parts = []\\nargmax_21_parts = []\\n\\nwith torch.no_grad():\\n    for i in tqdm(range(0, len(ds), batch_size)):\\n        batch_s1 = sent1[i:i + batch_size]\\n        batch_s2 = sent2[i:i + batch_size]\\n\\n        enc_12 = tokenizer(\\n            batch_s1,\\n            batch_s2,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc_21 = tokenizer(\\n            batch_s2,\\n            batch_s1,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n\\n        enc_12 = {k: v.to(device) for k, v in enc_12.items()}\\n        enc_21 = {k: v.to(device) for k, v in enc_21.items()}\\n\\n        logits_12 = model(**enc_12).logits\\n        logits_21 = model(**enc_21).logits\\n\\n        logits_12_parts.append(logits_12.cpu().numpy())\\n        logits_21_parts.append(logits_21.cpu().numpy())\\n        argmax_12_parts.append(torch.argmax(logits_12, dim=-1).cpu().numpy())\\n        argmax_21_parts.append(torch.argmax(logits_21, dim=-1).cpu().numpy())\\n\\nlogits_12 = np.concatenate(logits_12_parts, axis=0)\\nlogits_21 = np.concatenate(logits_21_parts, axis=0)\\nargmax_12 = np.concatenate(argmax_12_parts, axis=0)\\nargmax_21 = np.concatenate(argmax_21_parts, axis=0)\\n\\nprint(\\\"done\\\")\\nprint(\\\"logits_12 shape:\\\", logits_12.shape)\\nprint(\\\"logits_21 shape:\\\", logits_21.shape)\\n\", \"margin_12 = logits_12[:, entailment_id] - logits_12[:, contradiction_id]\\nmargin_21 = logits_21[:, entailment_id] - logits_21[:, contradiction_id]\\navg_margin = (margin_12 + margin_21) / 2.0\\n\\ngate = (argmax_12 != contradiction_id) & (argmax_21 != contradiction_id)\\ny_pred = ((avg_margin > 0.0) & gate).astype(int)\\n\\n\", \"vault.create_record_list(\\\"mrpc_gate_margin_prediction\\\", column_names=[\\\"prediction\\\", \\\"margin_12\\\", \\\"margin_21\\\", \\\"gate\\\"])\\n\\nfor i in range(len(y_pred)):\\n    vault.append_record(\\\"mrpc_gate_margin_prediction\\\", \\n                        {\\n                            \\\"prediction\\\": int(y_pred[i]),\\n                            \\\"margin_12\\\": float(margin_12[i]),\\n                            \\\"margin_21\\\": float(margin_21[i]),\\n                            \\\"gate\\\": int(gate[i]),\\n                        },\\n                       input_items = {\\n                           \\\"glue_mrpc_validation\\\": [i, i + 1],\\n                       }\\n                       )\\n\\ndescription = \\\"mrpc_gate_margin_prediction is a per-example prediction dataset derived from the GLUE MRPC validation split. For each validation pair (sentence1, sentence2), the notebook runs the NLI model typeform/distilbert-base-uncased-mnli in both input orders, sentence1\\\\u2192sentence2 and sentence2\\\\u2192sentence1, and stores the resulting decision signals used for paraphrase classification. The dataset has four fields: prediction (final binary paraphrase prediction, 1 for paraphrase and 0 for not paraphrase), margin_12 (entailment logit minus contradiction logit for sentence1 paired with sentence2), margin_21 (the same margin for the reversed order), and gate (boolean flag that is true only when neither direction\\\\u2019s argmax label is contradiction). The final prediction is produced by requiring gate = true and the average of margin_12 and margin_21 to be greater than 0. This dataset serves as the main intermediate output of the workflow: it preserves the model\\\\u2019s directional margin scores and final gated prediction for each MRPC example, and it is then used to compute the summary accuracy, F1, and classification report.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"mrpc_gate_margin_prediction\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_type\\\": \\\"model predictions\\\", \\\"granularity\\\": \\\"pair-level\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"input_dataset\\\": \\\"glue_mrpc_validation\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"domain\\\": \\\"news\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"inference_strategy\\\": \\\"bidirectional consensus then average entailment-contradiction margin\\\", \\\"input_fields\\\": \\\"sentence1,sentence2\\\", \\\"output_fields\\\": \\\"prediction,margin_12,margin_21,gate\\\", \\\"label_space\\\": \\\"binary\\\", \\\"labels\\\": \\\"not_paraphrase,paraphrase\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"mrpc_gate_margin_prediction\\\", cat, embedding, prop)\", \"acc = accuracy_score(y_true, y_pred)\\nf1 = f1_score(y_true, y_pred)\\nreport = classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"])\\nprint({\\\"accuracy\\\": acc, \\\"f1\\\": f1})\\nprint(classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"]))\\n\", \"for i in range(5):\\n    print(\\\"=\\\" * 100)\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"dir_12_argmax:\\\", int(argmax_12[i]), id2label[int(argmax_12[i])])\\n    print(\\\"dir_21_argmax:\\\", int(argmax_21[i]), id2label[int(argmax_21[i])])\\n    print(\\\"margin_12:\\\", float(margin_12[i]))\\n    print(\\\"margin_21:\\\", float(margin_21[i]))\\n    print(\\\"gate:\\\", bool(gate[i]))\\n    print(\\\"avg_margin:\\\", float(avg_margin[i]))\\n    print(\\\"true:\\\", int(y_true[i]))\\n    print(\\\"pred:\\\", int(y_pred[i]))\\n\", \"mistakes = np.where(y_true != y_pred)[0][:10]\\nprint(\\\"num_errors:\\\", int((y_true != y_pred).sum()))\\n\\nfor i in mistakes:\\n    print(\\\"=\\\" * 100)\\n    print(\\\"idx:\\\", int(i))\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"dir_12_argmax:\\\", int(argmax_12[i]), id2label[int(argmax_12[i])])\\n    print(\\\"dir_21_argmax:\\\", int(argmax_21[i]), id2label[int(argmax_21[i])])\\n    print(\\\"margin_12:\\\", float(margin_12[i]))\\n    print(\\\"margin_21:\\\", float(margin_21[i]))\\n    print(\\\"gate:\\\", bool(gate[i]))\\n    print(\\\"avg_margin:\\\", float(avg_margin[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n\", \"vault.create_record_list(\\\"consensus_then_avg_margin_mrpc_summary\\\", column_names=[\\\"accuracy\\\", \\\"f1\\\", \\\"classification_report\\\"])\\n\\n\\nsummary = {\\n    \\\"accuracy\\\": float(acc),\\n    \\\"f1\\\": float(f1),\\n    \\\"classification_report\\\": str(report)\\n}\\n\\nvault.append_record(\\\"consensus_then_avg_margin_mrpc_summary\\\", summary,\\n                    input_items = {\\n                        \\\"glue_mrpc_validation\\\": [0, len(ds)],\\n                        \\\"mrpc_gate_margin_prediction\\\": [0, len(ds)]\\n                    })\\n\\nsummary\\n\\ndescription = \\\"Summary dataset for the MRPC validation evaluation of the consensus-then-average-margin inference method. It contains aggregate performance results computed by comparing the generated paraphrase predictions against the true labels from glue_mrpc_validation, using prediction records stored in mrpc_gate_margin_prediction. The dataset is structured as a record list with columns: accuracy (float), f1 (float), and classification_report (string containing the full per-class sklearn classification report for not_paraphrase and paraphrase). In this workflow, it serves as the final evaluation artifact for the notebook, linking the full MRPC validation set and the per-example prediction dataset to a compact summary of model performance.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"consensus_then_avg_margin_mrpc_summary\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_role\\\": \\\"evaluation summary\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"method\\\": \\\"consensus then average entailment-contradiction margin\\\", \\\"input_type\\\": \\\"sentence pair\\\", \\\"output_type\\\": \\\"aggregate metrics\\\", \\\"metrics\\\": \\\"accuracy,f1,classification_report\\\", \\\"prediction_source\\\": \\\"mrpc_gate_margin_prediction\\\", \\\"domain\\\": \\\"news\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"consensus_then_avg_margin_mrpc_summary\\\", cat, embedding, prop)\\n\\n\", \"description = \\\"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli natural language inference model. For each sentence pair, it runs inference in both directions (sentence1\\\\u2192sentence2 and sentence2\\\\u2192sentence1), computes an entailment-versus-contradiction margin for each direction, averages the two margins, and predicts paraphrase only when neither direction is classified as contradiction and the average margin is positive. The notebook stores per-example predictions, directional margins, and gate decisions in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, logs error analysis examples, and saves dataset-, prediction-, summary-, and notebook-level metadata and embeddings for later retrieval and documentation.\\\" # description of whole notebook\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"consensus_then_avg_margin_mrpc\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset\\\": \\\"glue/mrpc\\\", \\\"dataset_split\\\": \\\"validation\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"model_type\\\": \\\"NLI sequence classification\\\", \\\"approach\\\": \\\"zero-shot paraphrase detection via NLI\\\", \\\"inference_strategy\\\": \\\"bidirectional sentence-pair scoring\\\", \\\"decision_rule\\\": \\\"consensus non-contradiction gate with averaged entailment-contradiction margin\\\", \\\"frameworks\\\": \\\"transformers, pytorch, datasets, sklearn\\\", \\\"metrics\\\": \\\"accuracy, f1-score, classification_report\\\", \\\"storage\\\": \\\"TableVault with ArangoDB\\\", \\\"embedding_model\\\": \\\"text-embedding-3-large\\\", \\\"process_name\\\": \\\"consensus_then_avg_margin_mrpc\\\"} #e.g. model: distilbert-base-uncased-MRPC\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"consensus_then_avg_margin_mrpc\\\", cat, embedding, prop)\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5b03c5048198a8188482ac21c9d2`

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
    "call_id": "call_9foJXdNBQM1WQ2FfHD6jHnmk",
    "arguments": {
      "name": "neutral_penalized_margin_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_9foJXdNBQM1WQ2FfHD6jHnmk`

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
| 26053 | 40 | 14 | 24344 | 1.706s | 0.023s |

---

## Turn 21 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5b0582e8819885d85a7e378f43b4`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_9foJXdNBQM1WQ2FfHD6jHnmk",
    "output": "{\"ok\": true, \"result\": [\"def get_embeddings(text):\\n    return client.embeddings.create(\\n            input=text,\\n            model=\\\"text-embedding-3-large\\\"\\n        ).data[0].embedding\", \"import torch\\nimport numpy as np\\nfrom datasets import Dataset\\nfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\\nfrom tqdm.auto import tqdm\\n\\ndevice = torch.device(\\\"mps\\\" if torch.backends.mps.is_available() else \\\"cpu\\\")\\nprint(\\\"device:\\\", device)\\n\", \"model_name = \\\"typeform/distilbert-base-uncased-mnli\\\"\\n\\ntokenizer = AutoTokenizer.from_pretrained(model_name)\\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\\nmodel.eval()\\n\\nid2label = model.config.id2label\\nlabel2id = {str(v).lower(): int(k) for k, v in id2label.items()}\\n\\ndef resolve_label_id(label2id_map, candidates):\\n    for cand in candidates:\\n        if cand in label2id_map:\\n            return label2id_map[cand]\\n    raise ValueError(f\\\"Could not resolve label id from candidates={candidates}; available labels={label2id_map}\\\")\\n\\ncontradiction_id = resolve_label_id(label2id, [\\\"contradiction\\\", \\\"contradictory\\\", \\\"label_0\\\"])\\nneutral_id = resolve_label_id(label2id, [\\\"neutral\\\", \\\"label_1\\\"])\\nentailment_id = resolve_label_id(label2id, [\\\"entailment\\\", \\\"label_2\\\"])\\n\\nprint(model_name)\\nprint(\\\"id2label:\\\", id2label)\\nprint({\\n    \\\"contradiction_id\\\": contradiction_id,\\n    \\\"neutral_id\\\": neutral_id,\\n    \\\"entailment_id\\\": entailment_id,\\n})\\n\", \"ds = vault.query_item_content(\\\"glue_mrpc_validation\\\")\\nds = Dataset.from_list(ds)\\nprint(ds)\\nprint(ds[0])\\n\\nsent1 = ds[\\\"sentence1\\\"]\\nsent2 = ds[\\\"sentence2\\\"]\\ny_true = np.array(ds[\\\"label\\\"])\\n\\nprint(\\\"num_examples:\\\", len(y_true))\\nprint(\\\"positive_rate:\\\", y_true.mean())\\n\", \"batch_size = 64\\nscore_12_all = []\\nscore_21_all = []\\navg_score_all = []\\npreds = []\\n\\nwith torch.no_grad():\\n    for i in tqdm(range(0, len(ds), batch_size)):\\n        batch_s1 = sent1[i:i + batch_size]\\n        batch_s2 = sent2[i:i + batch_size]\\n\\n        enc12 = tokenizer(\\n            batch_s1,\\n            batch_s2,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc12 = {k: v.to(device) for k, v in enc12.items()}\\n\\n        enc21 = tokenizer(\\n            batch_s2,\\n            batch_s1,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc21 = {k: v.to(device) for k, v in enc21.items()}\\n\\n        logits12 = model(**enc12).logits\\n        logits21 = model(**enc21).logits\\n\\n        score12 = logits12[:, entailment_id] - torch.maximum(logits12[:, contradiction_id], logits12[:, neutral_id])\\n        score21 = logits21[:, entailment_id] - torch.maximum(logits21[:, contradiction_id], logits21[:, neutral_id])\\n        avg_score = (score12 + score21) / 2.0\\n        batch_preds = (avg_score > 0).long()\\n\\n        score_12_all.extend(score12.cpu().numpy())\\n        score_21_all.extend(score21.cpu().numpy())\\n        avg_score_all.extend(avg_score.cpu().numpy())\\n        preds.extend(batch_preds.cpu().numpy())\\n\\nscore_12_all = np.array(score_12_all)\\nscore_21_all = np.array(score_21_all)\\navg_score_all = np.array(avg_score_all)\\ny_pred = np.array(preds)\\n\\nprint(\\\"done\\\")\\nprint(\\\"score_12 range:\\\", float(score_12_all.min()), float(score_12_all.max()))\\nprint(\\\"score_21 range:\\\", float(score_21_all.min()), float(score_21_all.max()))\\nprint(\\\"avg_score range:\\\", float(avg_score_all.min()), float(avg_score_all.max()))\\n\", \"vault.create_record_list(\\\"mrpc_neutral_penalty_prediction\\\", column_names=[\\\"prediction\\\", \\\"score_12\\\", \\\"score_21\\\"])\\n\\nfor i in range(len(y_pred)):\\n    vault.append_record(\\\"mrpc_neutral_penalty_prediction\\\", \\n                        {\\n                            \\\"prediction\\\": int(y_pred[i]),\\n                            \\\"score_12\\\": float(score_12_all[i]),\\n                            \\\"score_21\\\": float(score_21_all[i]),\\n                        },\\n                       input_items = {\\n                           \\\"glue_mrpc_validation\\\": [i, i + 1],\\n                       }\\n                       )\\n\\ndescription = \\\"Per-example prediction dataset for the GLUE MRPC validation split, produced by applying the typeform/distilbert-base-uncased-mnli model as a zero-shot paraphrase detector. Each record corresponds to one sentence pair from glue_mrpc_validation and stores: prediction (binary paraphrase decision, where 1 indicates paraphrase and 0 indicates not_paraphrase), score_12 (entailment logit minus max(contradiction, neutral) for sentence1 -> sentence2), and score_21 (the same score for sentence2 -> sentence1). The final prediction is derived from the average of the two directional scores. In this workflow, this dataset captures the model\\\\u2019s per-example outputs for downstream evaluation, inspection of mistakes, and construction of the overall summary metrics.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"mrpc_neutral_penalty_prediction\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"record_type\\\": \\\"model predictions\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"source_item\\\": \\\"glue_mrpc_validation\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"input_format\\\": \\\"sentence pair\\\", \\\"label_space\\\": \\\"binary\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"model_family\\\": \\\"distilbert\\\", \\\"inference_method\\\": \\\"neutral-penalized entailment margin\\\", \\\"scoring\\\": \\\"avg_bidirectional_entailment_minus_max(contradiction,neutral)\\\", \\\"prediction_target\\\": \\\"paraphrase\\\", \\\"domain\\\": \\\"news\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"mrpc_neutral_penalty_prediction\\\", cat, embedding, prop)\", \"acc = accuracy_score(y_true, y_pred)\\nf1 = f1_score(y_true, y_pred)\\nreport = classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"])\\nprint({\\\"accuracy\\\": acc, \\\"f1\\\": f1})\\nprint(classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"]))\\n\", \"for i in range(5):\\n    print(\\\"=\\\" * 80)\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"score_12:\\\", float(score_12_all[i]))\\n    print(\\\"score_21:\\\", float(score_21_all[i]))\\n    print(\\\"avg_score:\\\", float(avg_score_all[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]), \\\"label:\\\", \\\"paraphrase\\\" if int(y_pred[i]) == 1 else \\\"not_paraphrase\\\")\\n\", \"mistakes = np.where(y_true != y_pred)[0][:10]\\nprint(\\\"num_errors:\\\", int((y_true != y_pred).sum()))\\n\\nfor i in mistakes:\\n    print(\\\"=\\\" * 80)\\n    print(\\\"idx:\\\", int(i))\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"score_12:\\\", float(score_12_all[i]))\\n    print(\\\"score_21:\\\", float(score_21_all[i]))\\n    print(\\\"avg_score:\\\", float(avg_score_all[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n\", \"vault.create_record_list(\\\"neutral_penalized_margin_mrpc_summary\\\", column_names=[\\\"accuracy\\\", \\\"f1\\\", \\\"classification_report\\\"])\\n\\n\\nsummary = {\\n    \\\"accuracy\\\": float(acc),\\n    \\\"f1\\\": float(f1),\\n    \\\"classification_report\\\": str(report)\\n}\\n\\nvault.append_record(\\\"neutral_penalized_margin_mrpc_summary\\\", summary,\\n                    input_items = {\\n                        \\\"glue_mrpc_validation\\\": [0, len(ds)],\\n                        \\\"mrpc_neutral_penalty_prediction\\\": [0, len(ds)]\\n                    })\\n\\nsummary\\n\\ndescription = \\\"Aggregate evaluation summary for the neutral-penalized margin MRPC experiment. This dataset contains a single summary record computed from the GLUE MRPC validation set and the derived mrpc_neutral_penalty_prediction records. Its fields are: accuracy (float, overall prediction accuracy), f1 (float, F1 score for the paraphrase class), and classification_report (string, full sklearn classification report with per-class precision, recall, F1, and support). In this workflow, it serves as the compact experiment-level output used to record and retrieve overall model performance after scoring sentence pairs with the MNLI model and converting the bidirectional entailment-vs.-non-entailment margin into paraphrase predictions.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"neutral_penalized_margin_mrpc_summary\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_role\\\": \\\"evaluation summary\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"benchmark\\\": \\\"GLUE\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"input_type\\\": \\\"sentence pair\\\", \\\"label_space\\\": \\\"binary paraphrase classification\\\", \\\"metrics\\\": \\\"accuracy,f1,classification_report\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"method\\\": \\\"neutral-penalized entailment margin\\\", \\\"derived_from\\\": \\\"mrpc_neutral_penalty_prediction\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"neutral_penalized_margin_mrpc_summary\\\", cat, embedding, prop)\\n\\n\", \"description = \\\"This notebook runs a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the NLI model typeform/distilbert-base-uncased-mnli. Its purpose is to score sentence pairs as paraphrase vs. not paraphrase without task-specific fine-tuning, using a neutral-penalized entailment margin. For each MRPC pair, the notebook evaluates both sentence orders, computes an entailment score minus the larger of the contradiction or neutral scores, averages the two directional margins, and predicts paraphrase when the averaged margin is positive. It then stores per-example predictions and scores in TableVault, links them back to the source validation records, computes evaluation metrics including accuracy, F1, and a classification report, inspects example predictions and errors, and saves dataset-, prediction-, summary-, and process-level metadata and semantic descriptions using OpenAI embeddings.\\\" # description of whole notebook\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"neutral_penalized_margin_mrpc\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"approach\\\": \\\"zero-shot NLI transfer\\\", \\\"scoring_method\\\": \\\"symmetric entailment margin with neutral penalty\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"dataset\\\": \\\"glue/mrpc\\\", \\\"split\\\": \\\"validation\\\", \\\"inputs\\\": \\\"sentence pair\\\", \\\"framework\\\": \\\"PyTorch, Hugging Face Transformers\\\", \\\"metrics\\\": \\\"accuracy, f1-score, classification report\\\", \\\"artifacts\\\": \\\"per-example predictions and summary records\\\", \\\"storage\\\": \\\"TableVault with ArangoDB\\\", \\\"embedding_model\\\": \\\"text-embedding-3-large\\\"} #e.g. model: distilbert-base-uncased-MRPC\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"neutral_penalized_margin_mrpc\\\", cat, embedding, prop)\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5b0582e8819885d85a7e378f43b4`

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
    "call_id": "call_LuzV5rPaYuBLdXxPwekZKokd",
    "arguments": {
      "item_name": "google_flan_prediction_and_logits",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_LuzV5rPaYuBLdXxPwekZKokd`

**Arguments:**
```json
{
  "item_name": "google_flan_prediction_and_logits",
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
      "prediction": 1,
      "true_logits": -4.720203399658203,
      "false_logits": -5.303816318511963
    },
    {
      "prediction": 0,
      "true_logits": -6.741540431976318,
      "false_logits": -6.069624900817871
    },
    {
      "prediction": 0,
      "true_logits": -6.652932167053223,
      "false_logits": -6.596719264984131
    },
    {
      "prediction": 0,
      "true_logits": -7.249307632446289,
      "false_logits": -7.079233646392822
    },
    {
      "prediction": 0,
      "true_logits": -4.714442729949951,
      "false_logits": -4.304520606994629
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 28946 | 552 | 516 | 27237 | 8.994s | 0.021s |

---

## Turn 22 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5b0e8748819881ce4e8994b09e31`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_LuzV5rPaYuBLdXxPwekZKokd",
    "output": "{\"ok\": true, \"result\": [{\"prediction\": 1, \"true_logits\": -4.720203399658203, \"false_logits\": -5.303816318511963}, {\"prediction\": 0, \"true_logits\": -6.741540431976318, \"false_logits\": -6.069624900817871}, {\"prediction\": 0, \"true_logits\": -6.652932167053223, \"false_logits\": -6.596719264984131}, {\"prediction\": 0, \"true_logits\": -7.249307632446289, \"false_logits\": -7.079233646392822}, {\"prediction\": 0, \"true_logits\": -4.714442729949951, \"false_logits\": -4.304520606994629}]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5b0e8748819881ce4e8994b09e31`

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
    "call_id": "call_lFxB4XMwnENiGbv80aAgTX2p",
    "arguments": {
      "item_name": "flan_t5_answer_prefix_yes_no_mrpcc_summary",
      "start_position": 0,
      "end_position": 10
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_lFxB4XMwnENiGbv80aAgTX2p`

**Arguments:**
```json
{
  "item_name": "flan_t5_answer_prefix_yes_no_mrpcc_summary",
  "start_position": 0,
  "end_position": 10
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    {
      "accuracy": 0.6372549019607843,
      "f1": 0.6877637130801688,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.46      0.75      0.57       129\n    paraphrase       0.84      0.58      0.69       279\n\n      accuracy                           0.64       408\n     macro avg       0.65      0.67      0.63       408\n  weighted avg       0.72      0.64      0.65       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 29678 | 4824 | 4782 | 27969 | 70.220s | 0.021s |

---

## Turn 23 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5b54c8908198bdd23ebc1e57a6c3`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_lFxB4XMwnENiGbv80aAgTX2p",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.6372549019607843, \"f1\": 0.6877637130801688, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.46      0.75      0.57       129\\n    paraphrase       0.84      0.58      0.69       279\\n\\n      accuracy                           0.64       408\\n     macro avg       0.65      0.67      0.63       408\\n  weighted avg       0.72      0.64      0.65       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5b54c8908198bdd23ebc1e57a6c3`

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
    "call_id": "call_KQV2nqlk0L0Jq8VMHnVXgdAX",
    "arguments": {
      "name": "flan_t5_answer_prefix_yes_no_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_KQV2nqlk0L0Jq8VMHnVXgdAX`

**Arguments:**
```json
{
  "name": "flan_t5_answer_prefix_yes_no_mrpc"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "model_name = \"google/flan-t5-small\"\n\ntokenizer = AutoTokenizer.from_pretrained(model_name)\nmodel = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)\nmodel.eval()\n\ndef get_single_token_id(text):\n    ids = tokenizer(text, add_special_tokens=False).input_ids\n    if len(ids) != 1:\n        raise ValueError(f\"{text!r} is not a single token: {ids} -> {tokenizer.convert_ids_to_tokens(ids)}\")\n    return ids[0]\n\nyes_token_id = get_single_token_id(\"yes\")\nno_token_id = get_single_token_id(\"no\")\n\nanswer_prefix = \"Answer:\"\nanswer_prefix_ids = tokenizer(answer_prefix, add_special_tokens=False).input_ids\ndecoder_start_token_id = model.config.decoder_start_token_id\n\nprint(\"model:\", model_name)\nprint(\"decoder_start_token_id:\", decoder_start_token_id)\nprint(\"yes_token_id:\", yes_token_id, \"token:\", tokenizer.convert_ids_to_tokens([yes_token_id]))\nprint(\"no_token_id:\", no_token_id, \"token:\", tokenizer.convert_ids_to_tokens([no_token_id]))\nprint(\"answer_prefix_ids:\", answer_prefix_ids, \"tokens:\", tokenizer.convert_ids_to_tokens(answer_prefix_ids))\n",
    "ds = vault.query_item_content(\"glue_mrpc_validation\")\nds = Dataset.from_list(ds)\nprint(ds)\nprint(ds[0])\n\nsent1 = ds[\"sentence1\"]\nsent2 = ds[\"sentence2\"]\ny_true = np.array(ds[\"label\"])\n\nprompts = [\n    f\"Do these two sentences have the same meaning? Sentence 1: {s1} Sentence 2: {s2}\"\n    for s1, s2 in zip(sent1, sent2)\n]\n\nprint(\"num_examples:\", len(ds))\nprint(\"positive_rate:\", float(y_true.mean()))\nprint(\"sample_prompt:\", prompts[0])\n",
    "batch_size = 16\npreds = []\nyes_logits_all = []\nno_logits_all = []\n\ndecoder_prefix_ids = [decoder_start_token_id] + answer_prefix_ids\ndecoder_prefix = torch.tensor(decoder_prefix_ids, dtype=torch.long, device=device)\n\nwith torch.no_grad():\n    for i in tqdm(range(0, len(prompts), batch_size)):\n        batch_prompts = prompts[i:i + batch_size]\n\n        enc = tokenizer(\n            batch_prompts,\n            padding=True,\n            truncation=True,\n            max_length=256,\n            return_tensors=\"pt\",\n        )\n        enc = {k: v.to(device) for k, v in enc.items()}\n\n        batch_decoder_input_ids = decoder_prefix.unsqueeze(0).repeat(len(batch_prompts), 1)\n\n        logits = model(**enc, decoder_input_ids=batch_decoder_input_ids).logits\n        step_logits = logits[:, -1, :]\n\n        batch_yes_logits = step_logits[:, yes_token_id]\n        batch_no_logits = step_logits[:, no_token_id]\n        batch_preds = (batch_yes_logits > batch_no_logits).long().cpu().numpy()\n\n        preds.extend(batch_preds.tolist())\n        yes_logits_all.extend(batch_yes_logits.detach().cpu().numpy().tolist())\n        no_logits_all.extend(batch_no_logits.detach().cpu().numpy().tolist())\n\ny_pred = np.array(preds)\nyes_logits_all = np.array(yes_logits_all)\nno_logits_all = np.array(no_logits_all)\n\nprint(\"done\")\nprint(\"num_predicted_positive:\", int(y_pred.sum()))\n",
    "\nvault.create_record_list(\"flan_prediction_and_logit_prefix\", column_names=[\"prediction\",\"yes_logits\", \"no_logits\"])\n\nfor i in range(len(y_pred)):\n    vault.append_record(\"flan_prediction_and_logit_prefix\", \n                        {\n                            \"prediction\": int(y_pred[i]),\n                            \"yes_logits\": float(yes_logits_all[i]),\n                            \"no_logits\": float(no_logits_all[i]),\n                        },\n                       input_items = {\n                           \"glue_mrpc_validation\": [i, i + 1],\n                       }\n                       )\n\ndescription = \"This dataset stores per-example inference outputs from google/flan-t5-small on the GLUE MRPC validation set using a prompted yes/no paraphrase detection setup. Each record corresponds to one input pair from glue_mrpc_validation and contains three fields: prediction (binary label, where 1 indicates the model preferred \\u201cyes\\u201d and 0 indicates it preferred \\u201cno\\u201d), yes_logits (the decoder logit for the token \\u201cyes\\u201d at the answer position), and no_logits (the decoder logit for the token \\u201cno\\u201d at the answer position). Predictions are produced by prompting the model with the two sentences, forcing the decoder prefix \\u201cAnswer:\\u201d, and selecting the higher of the yes/no logits. In this workflow, the dataset serves as the main model output table for downstream evaluation, error analysis, and summary metric generation, while preserving a row-level link back to the original MRPC validation examples.\"\nembedding = get_embeddings(description)\nvault.create_description(\"flan_prediction_and_logit_prefix\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"dataset_type\": \"model predictions and logits\", \"source\": \"glue/mrpc\", \"split\": \"validation\", \"size\": \"408\", \"model\": \"google/flan-t5-small\", \"prompt_type\": \"yes/no question answering\", \"decoder_prefix\": \"Answer:\", \"label_space\": \"binary\", \"output_columns\": \"prediction, yes_logits, no_logits\", \"input_fields\": \"sentence1, sentence2\", \"prediction_target\": \"paraphrase label\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"flan_prediction_and_logit_prefix\", cat, embedding, prop)",
    "acc = accuracy_score(y_true, y_pred)\nf1 = f1_score(y_true, y_pred)\nreport = classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"], zero_division=0)\nprint({\"accuracy\": acc, \"f1\": f1})\nprint(classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"], zero_division=0))\n",
    "for i in range(5):\n    print(\"=\" * 100)\n    print(\"idx:\", i)\n    print(\"prompt:\", prompts[i])\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]))\n    print(\"yes_logit:\", float(yes_logits_all[i]), \"no_logit:\", float(no_logits_all[i]))\n\nmistakes = np.where(y_true != y_pred)[0][:10]\nprint(\"num_errors:\", int((y_true != y_pred).sum()))\n\nfor i in mistakes:\n    print(\"=\" * 100)\n    print(\"idx:\", int(i))\n    print(\"prompt:\", prompts[i])\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]))\n    print(\"yes_logit:\", float(yes_logits_all[i]), \"no_logit:\", float(no_logits_all[i]))\n",
    "vault.create_record_list(\"flan_t5_answer_prefix_yes_no_mrpcc_summary\", column_names=[\"accuracy\", \"f1\", \"classification_report\"])\n\n\nsummary = {\n    \"accuracy\": float(acc),\n    \"f1\": float(f1),\n    \"classification_report\": str(report)\n}\n\nvault.append_record(\"flan_t5_answer_prefix_yes_no_mrpcc_summary\", summary,\n                    input_items = {\n                        \"glue_mrpc_validation\": [0, len(ds)],\n                        \"flan_prediction_and_logit_prefix\": [0, len(ds)]\n                    })\n\nsummary\n\ndescription = \"Summary dataset for the FLAN-T5-small MRPC validation run using answer-prefix yes/no scoring. It contains aggregate evaluation results computed from predictions on the glue_mrpc_validation dataset, based on comparing the model\\u2019s logits for the tokens \\u201cyes\\u201d and \\u201cno\\u201d after the decoder prefix \\u201cAnswer:\\u201d. The dataset structure has three fields: accuracy (float), f1 (float), and classification_report (string with per-class precision/recall/F1/support). In this workflow, it serves as the experiment-level summary record for the notebook, linking the full validation input set and the per-example prediction/logit dataset flan_prediction_and_logit_prefix into a single compact performance summary.\"\nembedding = get_embeddings(description)\nvault.create_description(\"flan_t5_answer_prefix_yes_no_mrpcc_summary\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"benchmark\": \"GLUE\", \"source\": \"glue/mrpc\", \"split\": \"validation\", \"size\": \"408\", \"model\": \"google/flan-t5-small\", \"model_family\": \"flan-t5\", \"input_type\": \"sentence pair\", \"prompt_type\": \"yes/no question with answer prefix\", \"evaluation_method\": \"decoder next-token yes/no logits\", \"output_type\": \"evaluation summary metrics\", \"metrics\": \"accuracy,f1,classification_report\", \"label_space\": \"not_paraphrase,paraphrase\", \"prediction_source\": \"flan_prediction_and_logit_prefix\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"flan_t5_answer_prefix_yes_no_mrpcc_summary\", cat, embedding, prop)\n\n\n",
    "description = \"This notebook evaluates google/flan-t5-small on the GLUE MRPC validation set for binary paraphrase detection. It loads sentence pairs and labels from TableVault, converts each pair into a natural-language prompt asking whether the two sentences have the same meaning, and runs FLAN-T5 as a seq2seq model on MPS or CPU. Using the decoder prefix Answer:, it compares the next-token logits for yes and no to make a classification without full text generation. The workflow saves per-example predictions and yes/no logits to TableVault, computes accuracy, F1, and a classification report, reviews sample predictions and errors, and stores both dataset-level outputs and experiment summary metadata/descriptions back into TableVault for tracking and retrieval.\" # description of whole notebook\nembedding = get_embeddings(description)\nvault.create_description(\"flan_t5_answer_prefix_yes_no_mrpc\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"problem_type\": \"binary text classification\", \"dataset\": \"glue/mrpc\", \"dataset_split\": \"validation\", \"model\": \"google/flan-t5-small\", \"model_family\": \"FLAN-T5\", \"framework\": \"transformers, pytorch\", \"inference_method\": \"generative seq2seq yes/no logit comparison\", \"prompt_format\": \"instruction prompt with answer prefix 'Answer:'\", \"label_space\": \"yes/no\", \"evaluation\": \"accuracy, f1-score, classification_report\", \"artifacts\": \"predictions, yes_logits, no_logits, summary metrics\", \"storage\": \"TableVault\", \"device\": \"mps_or_cpu\"} #e.g. model: distilbert-base-uncased-MRPC\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"flan_t5_answer_prefix_yes_no_mrpc\", cat, embedding, prop)"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 34667 | 42 | 13 | 32958 | 1.661s | 0.010s |

---

## Turn 24 — `finalize_result` [ok]

### Model Input
**previous_response_id:** `resp_0c2409105c899fb80069da5b566d988198aadd18c17a89b472`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_KQV2nqlk0L0Jq8VMHnVXgdAX",
    "output": "{\"ok\": true, \"result\": [\"model_name = \\\"google/flan-t5-small\\\"\\n\\ntokenizer = AutoTokenizer.from_pretrained(model_name)\\nmodel = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)\\nmodel.eval()\\n\\ndef get_single_token_id(text):\\n    ids = tokenizer(text, add_special_tokens=False).input_ids\\n    if len(ids) != 1:\\n        raise ValueError(f\\\"{text!r} is not a single token: {ids} -> {tokenizer.convert_ids_to_tokens(ids)}\\\")\\n    return ids[0]\\n\\nyes_token_id = get_single_token_id(\\\"yes\\\")\\nno_token_id = get_single_token_id(\\\"no\\\")\\n\\nanswer_prefix = \\\"Answer:\\\"\\nanswer_prefix_ids = tokenizer(answer_prefix, add_special_tokens=False).input_ids\\ndecoder_start_token_id = model.config.decoder_start_token_id\\n\\nprint(\\\"model:\\\", model_name)\\nprint(\\\"decoder_start_token_id:\\\", decoder_start_token_id)\\nprint(\\\"yes_token_id:\\\", yes_token_id, \\\"token:\\\", tokenizer.convert_ids_to_tokens([yes_token_id]))\\nprint(\\\"no_token_id:\\\", no_token_id, \\\"token:\\\", tokenizer.convert_ids_to_tokens([no_token_id]))\\nprint(\\\"answer_prefix_ids:\\\", answer_prefix_ids, \\\"tokens:\\\", tokenizer.convert_ids_to_tokens(answer_prefix_ids))\\n\", \"ds = vault.query_item_content(\\\"glue_mrpc_validation\\\")\\nds = Dataset.from_list(ds)\\nprint(ds)\\nprint(ds[0])\\n\\nsent1 = ds[\\\"sentence1\\\"]\\nsent2 = ds[\\\"sentence2\\\"]\\ny_true = np.array(ds[\\\"label\\\"])\\n\\nprompts = [\\n    f\\\"Do these two sentences have the same meaning? Sentence 1: {s1} Sentence 2: {s2}\\\"\\n    for s1, s2 in zip(sent1, sent2)\\n]\\n\\nprint(\\\"num_examples:\\\", len(ds))\\nprint(\\\"positive_rate:\\\", float(y_true.mean()))\\nprint(\\\"sample_prompt:\\\", prompts[0])\\n\", \"batch_size = 16\\npreds = []\\nyes_logits_all = []\\nno_logits_all = []\\n\\ndecoder_prefix_ids = [decoder_start_token_id] + answer_prefix_ids\\ndecoder_prefix = torch.tensor(decoder_prefix_ids, dtype=torch.long, device=device)\\n\\nwith torch.no_grad():\\n    for i in tqdm(range(0, len(prompts), batch_size)):\\n        batch_prompts = prompts[i:i + batch_size]\\n\\n        enc = tokenizer(\\n            batch_prompts,\\n            padding=True,\\n            truncation=True,\\n            max_length=256,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc = {k: v.to(device) for k, v in enc.items()}\\n\\n        batch_decoder_input_ids = decoder_prefix.unsqueeze(0).repeat(len(batch_prompts), 1)\\n\\n        logits = model(**enc, decoder_input_ids=batch_decoder_input_ids).logits\\n        step_logits = logits[:, -1, :]\\n\\n        batch_yes_logits = step_logits[:, yes_token_id]\\n        batch_no_logits = step_logits[:, no_token_id]\\n        batch_preds = (batch_yes_logits > batch_no_logits).long().cpu().numpy()\\n\\n        preds.extend(batch_preds.tolist())\\n        yes_logits_all.extend(batch_yes_logits.detach().cpu().numpy().tolist())\\n        no_logits_all.extend(batch_no_logits.detach().cpu().numpy().tolist())\\n\\ny_pred = np.array(preds)\\nyes_logits_all = np.array(yes_logits_all)\\nno_logits_all = np.array(no_logits_all)\\n\\nprint(\\\"done\\\")\\nprint(\\\"num_predicted_positive:\\\", int(y_pred.sum()))\\n\", \"\\nvault.create_record_list(\\\"flan_prediction_and_logit_prefix\\\", column_names=[\\\"prediction\\\",\\\"yes_logits\\\", \\\"no_logits\\\"])\\n\\nfor i in range(len(y_pred)):\\n    vault.append_record(\\\"flan_prediction_and_logit_prefix\\\", \\n                        {\\n                            \\\"prediction\\\": int(y_pred[i]),\\n                            \\\"yes_logits\\\": float(yes_logits_all[i]),\\n                            \\\"no_logits\\\": float(no_logits_all[i]),\\n                        },\\n                       input_items = {\\n                           \\\"glue_mrpc_validation\\\": [i, i + 1],\\n                       }\\n                       )\\n\\ndescription = \\\"This dataset stores per-example inference outputs from google/flan-t5-small on the GLUE MRPC validation set using a prompted yes/no paraphrase detection setup. Each record corresponds to one input pair from glue_mrpc_validation and contains three fields: prediction (binary label, where 1 indicates the model preferred \\\\u201cyes\\\\u201d and 0 indicates it preferred \\\\u201cno\\\\u201d), yes_logits (the decoder logit for the token \\\\u201cyes\\\\u201d at the answer position), and no_logits (the decoder logit for the token \\\\u201cno\\\\u201d at the answer position). Predictions are produced by prompting the model with the two sentences, forcing the decoder prefix \\\\u201cAnswer:\\\\u201d, and selecting the higher of the yes/no logits. In this workflow, the dataset serves as the main model output table for downstream evaluation, error analysis, and summary metric generation, while preserving a row-level link back to the original MRPC validation examples.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"flan_prediction_and_logit_prefix\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_type\\\": \\\"model predictions and logits\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"google/flan-t5-small\\\", \\\"prompt_type\\\": \\\"yes/no question answering\\\", \\\"decoder_prefix\\\": \\\"Answer:\\\", \\\"label_space\\\": \\\"binary\\\", \\\"output_columns\\\": \\\"prediction, yes_logits, no_logits\\\", \\\"input_fields\\\": \\\"sentence1, sentence2\\\", \\\"prediction_target\\\": \\\"paraphrase label\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"flan_prediction_and_logit_prefix\\\", cat, embedding, prop)\", \"acc = accuracy_score(y_true, y_pred)\\nf1 = f1_score(y_true, y_pred)\\nreport = classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"], zero_division=0)\\nprint({\\\"accuracy\\\": acc, \\\"f1\\\": f1})\\nprint(classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"], zero_division=0))\\n\", \"for i in range(5):\\n    print(\\\"=\\\" * 100)\\n    print(\\\"idx:\\\", i)\\n    print(\\\"prompt:\\\", prompts[i])\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n    print(\\\"yes_logit:\\\", float(yes_logits_all[i]), \\\"no_logit:\\\", float(no_logits_all[i]))\\n\\nmistakes = np.where(y_true != y_pred)[0][:10]\\nprint(\\\"num_errors:\\\", int((y_true != y_pred).sum()))\\n\\nfor i in mistakes:\\n    print(\\\"=\\\" * 100)\\n    print(\\\"idx:\\\", int(i))\\n    print(\\\"prompt:\\\", prompts[i])\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n    print(\\\"yes_logit:\\\", float(yes_logits_all[i]), \\\"no_logit:\\\", float(no_logits_all[i]))\\n\", \"vault.create_record_list(\\\"flan_t5_answer_prefix_yes_no_mrpcc_summary\\\", column_names=[\\\"accuracy\\\", \\\"f1\\\", \\\"classification_report\\\"])\\n\\n\\nsummary = {\\n    \\\"accuracy\\\": float(acc),\\n    \\\"f1\\\": float(f1),\\n    \\\"classification_report\\\": str(report)\\n}\\n\\nvault.append_record(\\\"flan_t5_answer_prefix_yes_no_mrpcc_summary\\\", summary,\\n                    input_items = {\\n                        \\\"glue_mrpc_validation\\\": [0, len(ds)],\\n                        \\\"flan_prediction_and_logit_prefix\\\": [0, len(ds)]\\n                    })\\n\\nsummary\\n\\ndescription = \\\"Summary dataset for the FLAN-T5-small MRPC validation run using answer-prefix yes/no scoring. It contains aggregate evaluation results computed from predictions on the glue_mrpc_validation dataset, based on comparing the model\\\\u2019s logits for the tokens \\\\u201cyes\\\\u201d and \\\\u201cno\\\\u201d after the decoder prefix \\\\u201cAnswer:\\\\u201d. The dataset structure has three fields: accuracy (float), f1 (float), and classification_report (string with per-class precision/recall/F1/support). In this workflow, it serves as the experiment-level summary record for the notebook, linking the full validation input set and the per-example prediction/logit dataset flan_prediction_and_logit_prefix into a single compact performance summary.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"flan_t5_answer_prefix_yes_no_mrpcc_summary\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"benchmark\\\": \\\"GLUE\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"google/flan-t5-small\\\", \\\"model_family\\\": \\\"flan-t5\\\", \\\"input_type\\\": \\\"sentence pair\\\", \\\"prompt_type\\\": \\\"yes/no question with answer prefix\\\", \\\"evaluation_method\\\": \\\"decoder next-token yes/no logits\\\", \\\"output_type\\\": \\\"evaluation summary metrics\\\", \\\"metrics\\\": \\\"accuracy,f1,classification_report\\\", \\\"label_space\\\": \\\"not_paraphrase,paraphrase\\\", \\\"prediction_source\\\": \\\"flan_prediction_and_logit_prefix\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"flan_t5_answer_prefix_yes_no_mrpcc_summary\\\", cat, embedding, prop)\\n\\n\\n\", \"description = \\\"This notebook evaluates google/flan-t5-small on the GLUE MRPC validation set for binary paraphrase detection. It loads sentence pairs and labels from TableVault, converts each pair into a natural-language prompt asking whether the two sentences have the same meaning, and runs FLAN-T5 as a seq2seq model on MPS or CPU. Using the decoder prefix Answer:, it compares the next-token logits for yes and no to make a classification without full text generation. The workflow saves per-example predictions and yes/no logits to TableVault, computes accuracy, F1, and a classification report, reviews sample predictions and errors, and stores both dataset-level outputs and experiment summary metadata/descriptions back into TableVault for tracking and retrieval.\\\" # description of whole notebook\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"flan_t5_answer_prefix_yes_no_mrpc\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"problem_type\\\": \\\"binary text classification\\\", \\\"dataset\\\": \\\"glue/mrpc\\\", \\\"dataset_split\\\": \\\"validation\\\", \\\"model\\\": \\\"google/flan-t5-small\\\", \\\"model_family\\\": \\\"FLAN-T5\\\", \\\"framework\\\": \\\"transformers, pytorch\\\", \\\"inference_method\\\": \\\"generative seq2seq yes/no logit comparison\\\", \\\"prompt_format\\\": \\\"instruction prompt with answer prefix 'Answer:'\\\", \\\"label_space\\\": \\\"yes/no\\\", \\\"evaluation\\\": \\\"accuracy, f1-score, classification_report\\\", \\\"artifacts\\\": \\\"predictions, yes_logits, no_logits, summary metrics\\\", \\\"storage\\\": \\\"TableVault\\\", \\\"device\\\": \\\"mps_or_cpu\\\"} #e.g. model: distilbert-base-uncased-MRPC\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"flan_t5_answer_prefix_yes_no_mrpc\\\", cat, embedding, prop)\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0c2409105c899fb80069da5b566d988198aadd18c17a89b472`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "finalize_result",
    "call_id": "call_XV3nEdsAviv04LjsCR0b5nhb",
    "arguments": {
      "summary": "{\"rows\":[{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"soft average\",\"strategy\":\"mean softmax entailment-contradiction gap over both sentence orders\",\"accuracy\":0.7181,\"f1\":0.7905,\"not_paraphrase_recall\":0.59,\"paraphrase_recall\":0.78},{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"soft average\",\"strategy\":\"mean log-probability odds (entailment - contradiction) over both sentence orders\",\"accuracy\":0.7034,\"f1\":0.773,\"not_paraphrase_recall\":0.63,\"paraphrase_recall\":0.74},{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"soft average + gate\",\"strategy\":\"average directional margin, but predict paraphrase only if neither direction is contradiction\",\"accuracy\":0.701,\"f1\":0.7698,\"not_paraphrase_recall\":0.64,\"paraphrase_recall\":0.73},{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"hard conservative\",\"strategy\":\"minimum directional entailment-contradiction margin must be positive\",\"accuracy\":0.5858,\"f1\":0.5888,\"not_paraphrase_recall\":0.91,\"paraphrase_recall\":0.43},{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"hard conservative\",\"strategy\":\"average bidirectional entailment minus max(contradiction, neutral)\",\"accuracy\":0.5564,\"f1\":0.5323,\"not_paraphrase_recall\":0.96,\"paraphrase_recall\":0.37},{\"model_family\":\"Prompted zero-shot\",\"model\":\"google/flan-t5-small\",\"symmetry_style\":\"none\",\"strategy\":\"single-order answer-prefix yes/no next-token logits\",\"accuracy\":0.6373,\"f1\":0.6878,\"not_paraphrase_recall\":0.75,\"paraphrase_recall\":0.58},{\"model_family\":\"Prompted zero-shot\",\"model\":\"google/flan-t5-small\",\"symmetry_style\":\"none\",\"strategy\":\"single-order full-answer log-probability scoring\",\"accuracy\":0.6495,\"f1\":0.6911,\"not_paraphrase_recall\":0.81,\"paraphrase_recall\":0.57},{\"model_family\":\"Prompted zero-shot\",\"model\":\"google/flan-t5-small\",\"symmetry_style\":\"soft average\",\"strategy\":\"swapped-prompt average of yes/no logits\",\"accuracy\":0.7377,\"f1\":0.8065,\"not_paraphrase_recall\":0.6,\"paraphrase_recall\":0.8}],\"summary\":\"Across the 408-example MRPC validation split, the repository shows that symmetry is most helpful when enforced softly by averaging predictions across sentence order, not by hard agreement constraints. For the NLI-transfer model typeform/distilbert-base-uncased-mnli, the best symmetric rule is the mean softmax entailment-minus-contradiction gap over both directions (accuracy 0.7181, F1 0.7905). Two other soft bidirectional rules\u2014mean log-probability odds (0.7034) and consensus-plus-average margin (0.7010)\u2014are only slightly worse. In contrast, stricter symmetry rules that require both directions to stay positive or that heavily penalize non-entailment sharply reduce accuracy: min-direction margin falls to 0.5858 and neutral-penalized averaging to 0.5564. Their classification reports show why: they become overly conservative, driving not_paraphrase recall up to 0.91-0.96 while collapsing paraphrase recall to 0.43-0.37 on a paraphrase-heavy split (279/408 positives). For the prompted zero-shot model google/flan-t5-small, explicit symmetry enforcement is clearly beneficial: swapped-prompt averaging reaches 0.7377 accuracy and 0.8065 F1, outperforming two single-order baselines at 0.6373 and 0.6495 accuracy. The gain is mainly from much better paraphrase recall (0.80 vs 0.57-0.58), although negative recall falls to about 0.60. Overall, the evidence suggests a consistent pattern: mild bidirectional averaging is the safest and often best way to enforce symmetry, whereas hard consensus/min-style constraints over-correct toward negative predictions and hurt MRPC accuracy. The table should be read as experiment-level evidence from single stored runs, not repeated trials; moreover, the FLAN comparisons also differ somewhat in prompt/scoring setup, and the repository does not contain a stored one-direction NLI summary, so causal claims about symmetry alone should be treated cautiously.\"}"
    }
  }
]
```

### Tool Call
**Tool:** `finalize_result` | **call_id:** `call_XV3nEdsAviv04LjsCR0b5nhb`

**Arguments:**
```json
{
  "summary": "{\"rows\":[{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"soft average\",\"strategy\":\"mean softmax entailment-contradiction gap over both sentence orders\",\"accuracy\":0.7181,\"f1\":0.7905,\"not_paraphrase_recall\":0.59,\"paraphrase_recall\":0.78},{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"soft average\",\"strategy\":\"mean log-probability odds (entailment - contradiction) over both sentence orders\",\"accuracy\":0.7034,\"f1\":0.773,\"not_paraphrase_recall\":0.63,\"paraphrase_recall\":0.74},{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"soft average + gate\",\"strategy\":\"average directional margin, but predict paraphrase only if neither direction is contradiction\",\"accuracy\":0.701,\"f1\":0.7698,\"not_paraphrase_recall\":0.64,\"paraphrase_recall\":0.73},{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"hard conservative\",\"strategy\":\"minimum directional entailment-contradiction margin must be positive\",\"accuracy\":0.5858,\"f1\":0.5888,\"not_paraphrase_recall\":0.91,\"paraphrase_recall\":0.43},{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"hard conservative\",\"strategy\":\"average bidirectional entailment minus max(contradiction, neutral)\",\"accuracy\":0.5564,\"f1\":0.5323,\"not_paraphrase_recall\":0.96,\"paraphrase_recall\":0.37},{\"model_family\":\"Prompted zero-shot\",\"model\":\"google/flan-t5-small\",\"symmetry_style\":\"none\",\"strategy\":\"single-order answer-prefix yes/no next-token logits\",\"accuracy\":0.6373,\"f1\":0.6878,\"not_paraphrase_recall\":0.75,\"paraphrase_recall\":0.58},{\"model_family\":\"Prompted zero-shot\",\"model\":\"google/flan-t5-small\",\"symmetry_style\":\"none\",\"strategy\":\"single-order full-answer log-probability scoring\",\"accuracy\":0.6495,\"f1\":0.6911,\"not_paraphrase_recall\":0.81,\"paraphrase_recall\":0.57},{\"model_family\":\"Prompted zero-shot\",\"model\":\"google/flan-t5-small\",\"symmetry_style\":\"soft average\",\"strategy\":\"swapped-prompt average of yes/no logits\",\"accuracy\":0.7377,\"f1\":0.8065,\"not_paraphrase_recall\":0.6,\"paraphrase_recall\":0.8}],\"summary\":\"Across the 408-example MRPC validation split, the repository shows that symmetry is most helpful when enforced softly by averaging predictions across sentence order, not by hard agreement constraints. For the NLI-transfer model typeform/distilbert-base-uncased-mnli, the best symmetric rule is the mean softmax entailment-minus-contradiction gap over both directions (accuracy 0.7181, F1 0.7905). Two other soft bidirectional rules\u2014mean log-probability odds (0.7034) and consensus-plus-average margin (0.7010)\u2014are only slightly worse. In contrast, stricter symmetry rules that require both directions to stay positive or that heavily penalize non-entailment sharply reduce accuracy: min-direction margin falls to 0.5858 and neutral-penalized averaging to 0.5564. Their classification reports show why: they become overly conservative, driving not_paraphrase recall up to 0.91-0.96 while collapsing paraphrase recall to 0.43-0.37 on a paraphrase-heavy split (279/408 positives). For the prompted zero-shot model google/flan-t5-small, explicit symmetry enforcement is clearly beneficial: swapped-prompt averaging reaches 0.7377 accuracy and 0.8065 F1, outperforming two single-order baselines at 0.6373 and 0.6495 accuracy. The gain is mainly from much better paraphrase recall (0.80 vs 0.57-0.58), although negative recall falls to about 0.60. Overall, the evidence suggests a consistent pattern: mild bidirectional averaging is the safest and often best way to enforce symmetry, whereas hard consensus/min-style constraints over-correct toward negative predictions and hurt MRPC accuracy. The table should be read as experiment-level evidence from single stored runs, not repeated trials; moreover, the FLAN comparisons also differ somewhat in prompt/scoring setup, and the repository does not contain a stored one-direction NLI summary, so causal claims about symmetry alone should be treated cautiously.\"}"
}
```

### Tool Output
```json
{
  "summary": "{\"rows\":[{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"soft average\",\"strategy\":\"mean softmax entailment-contradiction gap over both sentence orders\",\"accuracy\":0.7181,\"f1\":0.7905,\"not_paraphrase_recall\":0.59,\"paraphrase_recall\":0.78},{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"soft average\",\"strategy\":\"mean log-probability odds (entailment - contradiction) over both sentence orders\",\"accuracy\":0.7034,\"f1\":0.773,\"not_paraphrase_recall\":0.63,\"paraphrase_recall\":0.74},{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"soft average + gate\",\"strategy\":\"average directional margin, but predict paraphrase only if neither direction is contradiction\",\"accuracy\":0.701,\"f1\":0.7698,\"not_paraphrase_recall\":0.64,\"paraphrase_recall\":0.73},{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"hard conservative\",\"strategy\":\"minimum directional entailment-contradiction margin must be positive\",\"accuracy\":0.5858,\"f1\":0.5888,\"not_paraphrase_recall\":0.91,\"paraphrase_recall\":0.43},{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"hard conservative\",\"strategy\":\"average bidirectional entailment minus max(contradiction, neutral)\",\"accuracy\":0.5564,\"f1\":0.5323,\"not_paraphrase_recall\":0.96,\"paraphrase_recall\":0.37},{\"model_family\":\"Prompted zero-shot\",\"model\":\"google/flan-t5-small\",\"symmetry_style\":\"none\",\"strategy\":\"single-order answer-prefix yes/no next-token logits\",\"accuracy\":0.6373,\"f1\":0.6878,\"not_paraphrase_recall\":0.75,\"paraphrase_recall\":0.58},{\"model_family\":\"Prompted zero-shot\",\"model\":\"google/flan-t5-small\",\"symmetry_style\":\"none\",\"strategy\":\"single-order full-answer log-probability scoring\",\"accuracy\":0.6495,\"f1\":0.6911,\"not_paraphrase_recall\":0.81,\"paraphrase_recall\":0.57},{\"model_family\":\"Prompted zero-shot\",\"model\":\"google/flan-t5-small\",\"symmetry_style\":\"soft average\",\"strategy\":\"swapped-prompt average of yes/no logits\",\"accuracy\":0.7377,\"f1\":0.8065,\"not_paraphrase_recall\":0.6,\"paraphrase_recall\":0.8}],\"summary\":\"Across the 408-example MRPC validation split, the repository shows that symmetry is most helpful when enforced softly by averaging predictions across sentence order, not by hard agreement constraints. For the NLI-transfer model typeform/distilbert-base-uncased-mnli, the best symmetric rule is the mean softmax entailment-minus-contradiction gap over both directions (accuracy 0.7181, F1 0.7905). Two other soft bidirectional rules\u2014mean log-probability odds (0.7034) and consensus-plus-average margin (0.7010)\u2014are only slightly worse. In contrast, stricter symmetry rules that require both directions to stay positive or that heavily penalize non-entailment sharply reduce accuracy: min-direction margin falls to 0.5858 and neutral-penalized averaging to 0.5564. Their classification reports show why: they become overly conservative, driving not_paraphrase recall up to 0.91-0.96 while collapsing paraphrase recall to 0.43-0.37 on a paraphrase-heavy split (279/408 positives). For the prompted zero-shot model google/flan-t5-small, explicit symmetry enforcement is clearly beneficial: swapped-prompt averaging reaches 0.7377 accuracy and 0.8065 F1, outperforming two single-order baselines at 0.6373 and 0.6495 accuracy. The gain is mainly from much better paraphrase recall (0.80 vs 0.57-0.58), although negative recall falls to about 0.60. Overall, the evidence suggests a consistent pattern: mild bidirectional averaging is the safest and often best way to enforce symmetry, whereas hard consensus/min-style constraints over-correct toward negative predictions and hurt MRPC accuracy. The table should be read as experiment-level evidence from single stored runs, not repeated trials; moreover, the FLAN comparisons also differ somewhat in prompt/scoring setup, and the repository does not contain a stored one-direction NLI summary, so causal claims about symmetry alone should be treated cautiously.\"}"
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 37344 | 4609 | 3523 | 35635 | 61.589s | 0.000s |

---

# Run Summary

**Final Result:**
```json
{
  "summary": "{\"rows\":[{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"soft average\",\"strategy\":\"mean softmax entailment-contradiction gap over both sentence orders\",\"accuracy\":0.7181,\"f1\":0.7905,\"not_paraphrase_recall\":0.59,\"paraphrase_recall\":0.78},{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"soft average\",\"strategy\":\"mean log-probability odds (entailment - contradiction) over both sentence orders\",\"accuracy\":0.7034,\"f1\":0.773,\"not_paraphrase_recall\":0.63,\"paraphrase_recall\":0.74},{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"soft average + gate\",\"strategy\":\"average directional margin, but predict paraphrase only if neither direction is contradiction\",\"accuracy\":0.701,\"f1\":0.7698,\"not_paraphrase_recall\":0.64,\"paraphrase_recall\":0.73},{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"hard conservative\",\"strategy\":\"minimum directional entailment-contradiction margin must be positive\",\"accuracy\":0.5858,\"f1\":0.5888,\"not_paraphrase_recall\":0.91,\"paraphrase_recall\":0.43},{\"model_family\":\"NLI transfer\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"symmetry_style\":\"hard conservative\",\"strategy\":\"average bidirectional entailment minus max(contradiction, neutral)\",\"accuracy\":0.5564,\"f1\":0.5323,\"not_paraphrase_recall\":0.96,\"paraphrase_recall\":0.37},{\"model_family\":\"Prompted zero-shot\",\"model\":\"google/flan-t5-small\",\"symmetry_style\":\"none\",\"strategy\":\"single-order answer-prefix yes/no next-token logits\",\"accuracy\":0.6373,\"f1\":0.6878,\"not_paraphrase_recall\":0.75,\"paraphrase_recall\":0.58},{\"model_family\":\"Prompted zero-shot\",\"model\":\"google/flan-t5-small\",\"symmetry_style\":\"none\",\"strategy\":\"single-order full-answer log-probability scoring\",\"accuracy\":0.6495,\"f1\":0.6911,\"not_paraphrase_recall\":0.81,\"paraphrase_recall\":0.57},{\"model_family\":\"Prompted zero-shot\",\"model\":\"google/flan-t5-small\",\"symmetry_style\":\"soft average\",\"strategy\":\"swapped-prompt average of yes/no logits\",\"accuracy\":0.7377,\"f1\":0.8065,\"not_paraphrase_recall\":0.6,\"paraphrase_recall\":0.8}],\"summary\":\"Across the 408-example MRPC validation split, the repository shows that symmetry is most helpful when enforced softly by averaging predictions across sentence order, not by hard agreement constraints. For the NLI-transfer model typeform/distilbert-base-uncased-mnli, the best symmetric rule is the mean softmax entailment-minus-contradiction gap over both directions (accuracy 0.7181, F1 0.7905). Two other soft bidirectional rules\u2014mean log-probability odds (0.7034) and consensus-plus-average margin (0.7010)\u2014are only slightly worse. In contrast, stricter symmetry rules that require both directions to stay positive or that heavily penalize non-entailment sharply reduce accuracy: min-direction margin falls to 0.5858 and neutral-penalized averaging to 0.5564. Their classification reports show why: they become overly conservative, driving not_paraphrase recall up to 0.91-0.96 while collapsing paraphrase recall to 0.43-0.37 on a paraphrase-heavy split (279/408 positives). For the prompted zero-shot model google/flan-t5-small, explicit symmetry enforcement is clearly beneficial: swapped-prompt averaging reaches 0.7377 accuracy and 0.8065 F1, outperforming two single-order baselines at 0.6373 and 0.6495 accuracy. The gain is mainly from much better paraphrase recall (0.80 vs 0.57-0.58), although negative recall falls to about 0.60. Overall, the evidence suggests a consistent pattern: mild bidirectional averaging is the safest and often best way to enforce symmetry, whereas hard consensus/min-style constraints over-correct toward negative predictions and hurt MRPC accuracy. The table should be read as experiment-level evidence from single stored runs, not repeated trials; moreover, the FLAN comparisons also differ somewhat in prompt/scoring setup, and the repository does not contain a stored one-direction NLI summary, so causal claims about symmetry alone should be treated cautiously.\"}"
}
```

**Metrics Summary:**
```json
{
  "tokens": {
    "input": 303987,
    "output": 11519,
    "reasoning": 9660,
    "total": 315506,
    "system_estimate": 1709,
    "conversation": 261391
  },
  "code": {
    "executions": 0,
    "failed_executions": 0,
    "total_lines": 0
  },
  "timing": {
    "api_latency_s": 181.946,
    "exec_latency_s": 0.407,
    "wall_time_s": 182.354
  },
  "api_calls": 25,
  "cost": null
}
```
