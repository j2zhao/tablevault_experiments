# Agent Trace — 20260411T132950Z

**Model:** `gpt-5.4`  
**Timestamp:** 2026-04-11T13:29:50.702995+00:00  
**Task:** How does the pooling strategy used to extract sentence representations from DistilBERT affect paraphrase detection accuracy on MRPC?

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
**previous_response_id:** `resp_0aa6a9b5a2e2caf30069da4ccef54c819797045e5f20b7817d`

**Pending messages:**
```json
[
  {
    "role": "user",
    "content": "How does the pooling strategy used to extract sentence representations from DistilBERT affect paraphrase detection accuracy on MRPC?"
  }
]
```

### Model Output
**response_id:** `resp_0aa6a9b5a2e2caf30069da4ccef54c819797045e5f20b7817d`

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
    "call_id": "call_5ZqJtIj6eryuX8QCZgJt30w4",
    "arguments": {
      "item_type": "record_list"
    }
  }
]
```

### Tool Call
**Tool:** `get_item_names` | **call_id:** `call_5ZqJtIj6eryuX8QCZgJt30w4`

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
| 1432 | 49 | 26 | 0 | 3.027s | 0.018s |

---

## Turn 1 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0aa6a9b5a2e2caf30069da4cd1dc688197a543dd7659b6a921`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_5ZqJtIj6eryuX8QCZgJt30w4",
    "output": "{\"ok\": true, \"result\": [\"consensus_then_avg_margin_mrpc_summary\", \"cosine_mrpc_max_pool_similarity_prediction\", \"cosine_mrpc_mean_similarity_prediction\", \"cosine_mrpc_threshold_score\", \"distilbert_cls_cosine_mrpc_summary\", \"distilbert_cross_text_prediction\", \"distilbert_cross_text_prediction_cutoff\", \"distilbert_last4_mean_cosine_mrpc_summary\", \"distilbert_margin_score_prediction_values\", \"distilbert_max_pool_cosine_mrpc_summary\", \"distilbert_mean_cosine_median_threshold_mrpc_summary\", \"distilbert_no_special_tokens_mean_cosine_mrpc_summary\", \"distilbert_quora_softmax_prediction\", \"distilbert_swap_prediction_values\", \"distilbert_symmetric_average_prediction\", \"distilbert-normalized-text-prediction\", \"entailment_logprob_odds_mrpc_summary\", \"flan_prediction_and_logit_prefix\", \"flan_prediction_logit_calibrated\", \"flan_prediction_scored\", \"flan_t5_answer_prefix_yes_no_mrpcc_summary\", \"flan_t5_contextual_calibrated_yes_no_mrpc_summary\", \"flan_t5_full_answer_logprob_mrpc_summary\", \"flan_t5_symmetric_prompt_average_mrpc_summary\", \"flan_t5_true_false_first_step_mrpc_summary\", \"glue_mrpc_validation\", \"google_flan_prediction_and_logits\", \"google_flan_prediction_swapped\", \"hf_pipeline_mrpc_bidirectional_order_average_summary\", \"hf_pipeline_mrpc_margin_rule_summary\", \"hf_pipeline_mrpc_raw_logits_softmax_summary\", \"hf_pipeline_mrpc_short_maxlen_64_summary\", \"hf_pipeline_mrpc_threshold_070_summary\", \"min_direction_margin_mrpc_summary\", \"minilm_cosine_threshold_prediction\", \"mrpc_distilbert_predictions\", \"mrpc_entailment_prediction\", \"mrpc_gate_margin_prediction\", \"mrpc_mean_gap_prediction\", \"mrpc_min_margin_prediction\", \"mrpc_neutral_penalty_prediction\", \"mrpc_paraphrase_inference_distilbert_mistakes\", \"mrpc_paraphrase_inference_distilbert_output\", \"neutral_penalized_margin_mrpc_summary\", \"no_special_cosine_mrpc_similarity_prediction\", \"pipeline_distilbert_shortened\", \"pipeline_distilbert_softmax_probs\", \"pipeline_distilbert_threshold\", \"quora_cross_encoder_max_length_64_mrpc_summary\", \"quora_cross_encoder_prefixed_sentence_tags_mrpc_summary\", \"quora_cross_encoder_softmax_threshold_065_mrpc_summary\", \"quora_cross_encoder_symmetric_average_mrpc_summary\", \"quora_cross_encoder_text_normalized_mrpc_summary\", \"sentence_transformers_mrpc_prediction_distance\", \"sentence_transformers_mrpc_prediction_max64\", \"sentence_transformers_mrpc_prediction_threshold\", \"sentence_transformers_mrpc_prediction_threshold_2\", \"softmax_gap_mean_mrpc_summary\", \"st_all_distilroberta_v1_cosine_threshold_mrpc_summary\", \"st_all_minilm_l6_l2_distance_threshold_mrpc_summary\", \"st_all_minilm_l6_max_seq_len_64_cosine_mrpc_summary\", \"st_paraphrase_minilm_l3_cosine_threshold_mrpc_summary\", \"st_paraphrase_minilm_l6_cosine_threshold_mrpc_summary\", \"threshold_cosine_mrpc_similarity_prediction\"]}"
  }
]
```

### Model Output
**response_id:** `resp_0aa6a9b5a2e2caf30069da4cd1dc688197a543dd7659b6a921`

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
    "call_id": "call_LDdvvNPY2TVZSauQANivoPxe",
    "arguments": {
      "item_name": "distilbert_cls_cosine_mrpc_summary",
      "start_position": 0,
      "end_position": 10
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_LDdvvNPY2TVZSauQANivoPxe`

**Arguments:**
```json
{
  "item_name": "distilbert_cls_cosine_mrpc_summary",
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
      "accuracy": 0.6862745098039216,
      "f1": 0.8134110787172012,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       1.00      0.01      0.02       129\n    paraphrase       0.69      1.00      0.81       279\n\n      accuracy                           0.69       408\n     macro avg       0.84      0.50      0.41       408\n  weighted avg       0.78      0.69      0.56       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 2187 | 102 | 63 | 685 | 2.172s | 0.021s |

---

## Turn 2 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0aa6a9b5a2e2caf30069da4cd410ec8197b45688bebd244d8d`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_LDdvvNPY2TVZSauQANivoPxe",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.6862745098039216, \"f1\": 0.8134110787172012, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       1.00      0.01      0.02       129\\n    paraphrase       0.69      1.00      0.81       279\\n\\n      accuracy                           0.69       408\\n     macro avg       0.84      0.50      0.41       408\\n  weighted avg       0.78      0.69      0.56       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0aa6a9b5a2e2caf30069da4cd410ec8197b45688bebd244d8d`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_V7MM2xL3aeh75XVBFqKlVacU",
    "arguments": {
      "item_name": "distilbert_last4_mean_cosine_mrpc_summary",
      "start_position": 0,
      "end_position": 10
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_V7MM2xL3aeh75XVBFqKlVacU`

**Arguments:**
```json
{
  "item_name": "distilbert_last4_mean_cosine_mrpc_summary",
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
      "accuracy": 0.6838235294117647,
      "f1": 0.8122270742358079,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.00      0.00      0.00       129\n    paraphrase       0.68      1.00      0.81       279\n\n      accuracy                           0.68       408\n     macro avg       0.34      0.50      0.41       408\n  weighted avg       0.47      0.68      0.56       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 2455 | 39 | 0 | 953 | 1.217s | 0.022s |

---

## Turn 3 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0aa6a9b5a2e2caf30069da4cd61f7881979ce1a10f8ca752b5`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_V7MM2xL3aeh75XVBFqKlVacU",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.6838235294117647, \"f1\": 0.8122270742358079, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.00      0.00      0.00       129\\n    paraphrase       0.68      1.00      0.81       279\\n\\n      accuracy                           0.68       408\\n     macro avg       0.34      0.50      0.41       408\\n  weighted avg       0.47      0.68      0.56       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0aa6a9b5a2e2caf30069da4cd61f7881979ce1a10f8ca752b5`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_DkomMY0DjqIlmzgkf6IibGes",
    "arguments": {
      "item_name": "distilbert_max_pool_cosine_mrpc_summary",
      "start_position": 0,
      "end_position": 10
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_DkomMY0DjqIlmzgkf6IibGes`

**Arguments:**
```json
{
  "item_name": "distilbert_max_pool_cosine_mrpc_summary",
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
      "accuracy": 0.6838235294117647,
      "f1": 0.8122270742358079,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.00      0.00      0.00       129\n    paraphrase       0.68      1.00      0.81       279\n\n      accuracy                           0.68       408\n     macro avg       0.34      0.50      0.41       408\n  weighted avg       0.47      0.68      0.56       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 2660 | 38 | 0 | 1158 | 2.242s | 0.008s |

---

## Turn 4 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0aa6a9b5a2e2caf30069da4cd7903c819791db2299f4aed879`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_DkomMY0DjqIlmzgkf6IibGes",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.6838235294117647, \"f1\": 0.8122270742358079, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.00      0.00      0.00       129\\n    paraphrase       0.68      1.00      0.81       279\\n\\n      accuracy                           0.68       408\\n     macro avg       0.34      0.50      0.41       408\\n  weighted avg       0.47      0.68      0.56       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0aa6a9b5a2e2caf30069da4cd7903c819791db2299f4aed879`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_6b5PR2kGYVGBT7gq3ZNd54Zi",
    "arguments": {
      "item_name": "distilbert_mean_cosine_median_threshold_mrpc_summary",
      "start_position": 0,
      "end_position": 10
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_6b5PR2kGYVGBT7gq3ZNd54Zi`

**Arguments:**
```json
{
  "item_name": "distilbert_mean_cosine_median_threshold_mrpc_summary",
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
      "f1": 0.7039337474120083,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.47      0.74      0.57       129\n    paraphrase       0.83      0.61      0.70       279\n\n      accuracy                           0.65       408\n     macro avg       0.65      0.67      0.64       408\n  weighted avg       0.72      0.65      0.66       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 2864 | 40 | 0 | 1362 | 1.302s | 0.014s |

---

## Turn 5 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0aa6a9b5a2e2caf30069da4cd8dc088197bc1f870a8011fe26`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_6b5PR2kGYVGBT7gq3ZNd54Zi",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.6495098039215687, \"f1\": 0.7039337474120083, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.47      0.74      0.57       129\\n    paraphrase       0.83      0.61      0.70       279\\n\\n      accuracy                           0.65       408\\n     macro avg       0.65      0.67      0.64       408\\n  weighted avg       0.72      0.65      0.66       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0aa6a9b5a2e2caf30069da4cd8dc088197bc1f870a8011fe26`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_BJSOLK5BXaLfMobFs62rURQp",
    "arguments": {
      "item_name": "distilbert_no_special_tokens_mean_cosine_mrpc_summary",
      "start_position": 0,
      "end_position": 10
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_BJSOLK5BXaLfMobFs62rURQp`

**Arguments:**
```json
{
  "item_name": "distilbert_no_special_tokens_mean_cosine_mrpc_summary",
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
      "f1": 0.8212703101920237,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.90      0.07      0.13       129\n    paraphrase       0.70      1.00      0.82       279\n\n      accuracy                           0.70       408\n     macro avg       0.80      0.53      0.48       408\n  weighted avg       0.76      0.70      0.60       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 3070 | 40 | 0 | 1568 | 1.268s | 0.007s |

---

## Turn 6 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0aa6a9b5a2e2caf30069da4cda21f48197bd76f7628e416142`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_BJSOLK5BXaLfMobFs62rURQp",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.7034313725490197, \"f1\": 0.8212703101920237, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.90      0.07      0.13       129\\n    paraphrase       0.70      1.00      0.82       279\\n\\n      accuracy                           0.70       408\\n     macro avg       0.80      0.53      0.48       408\\n  weighted avg       0.76      0.70      0.60       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0aa6a9b5a2e2caf30069da4cda21f48197bd76f7628e416142`

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
    "call_id": "call_k9preqQg19ZvDlbPg0G2JOEA",
    "arguments": {
      "item_name": "cosine_mrpc_mean_similarity_prediction",
      "start_position": 0,
      "end_position": 3
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_k9preqQg19ZvDlbPg0G2JOEA`

**Arguments:**
```json
{
  "item_name": "cosine_mrpc_mean_similarity_prediction",
  "start_position": 0,
  "end_position": 3
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    {
      "prediction": 1,
      "similarities": 0.9810966849327087
    },
    {
      "prediction": 1,
      "similarities": 0.9638397097587585
    },
    {
      "prediction": 1,
      "similarities": 0.9804420471191406
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 3276 | 218 | 181 | 1774 | 4.092s | 0.022s |

---

## Turn 7 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0aa6a9b5a2e2caf30069da4cde43448197a717a9ca2a86fe52`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_k9preqQg19ZvDlbPg0G2JOEA",
    "output": "{\"ok\": true, \"result\": [{\"prediction\": 1, \"similarities\": 0.9810966849327087}, {\"prediction\": 1, \"similarities\": 0.9638397097587585}, {\"prediction\": 1, \"similarities\": 0.9804420471191406}]}"
  }
]
```

### Model Output
**response_id:** `resp_0aa6a9b5a2e2caf30069da4cde43448197a717a9ca2a86fe52`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_hTkzM4HeNDPtZ3NzpUQPhDVm",
    "arguments": {
      "item_name": "cosine_mrpc_max_pool_similarity_prediction",
      "start_position": 0,
      "end_position": 3
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_hTkzM4HeNDPtZ3NzpUQPhDVm`

**Arguments:**
```json
{
  "item_name": "cosine_mrpc_max_pool_similarity_prediction",
  "start_position": 0,
  "end_position": 3
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    {
      "prediction": 1,
      "cosine_scores": 0.9697094559669495
    },
    {
      "prediction": 1,
      "cosine_scores": 0.9531527161598206
    },
    {
      "prediction": 1,
      "cosine_scores": 0.9761152267456055
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 3574 | 36 | 0 | 2072 | 2.030s | 0.013s |

---

## Turn 8 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0aa6a9b5a2e2caf30069da4ce0511c81979f7c7f57406f2dd4`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_hTkzM4HeNDPtZ3NzpUQPhDVm",
    "output": "{\"ok\": true, \"result\": [{\"prediction\": 1, \"cosine_scores\": 0.9697094559669495}, {\"prediction\": 1, \"cosine_scores\": 0.9531527161598206}, {\"prediction\": 1, \"cosine_scores\": 0.9761152267456055}]}"
  }
]
```

### Model Output
**response_id:** `resp_0aa6a9b5a2e2caf30069da4ce0511c81979f7c7f57406f2dd4`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_8fo8fWt78jYlRvTlrnRkRvgA",
    "arguments": {
      "item_name": "no_special_cosine_mrpc_similarity_prediction",
      "start_position": 0,
      "end_position": 3
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_8fo8fWt78jYlRvTlrnRkRvgA`

**Arguments:**
```json
{
  "item_name": "no_special_cosine_mrpc_similarity_prediction",
  "start_position": 0,
  "end_position": 3
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    {
      "prediction": 1,
      "cosine_scores": 0.9537599086761475
    },
    {
      "prediction": 1,
      "cosine_scores": 0.895621657371521
    },
    {
      "prediction": 1,
      "cosine_scores": 0.9625198841094971
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 3693 | 36 | 0 | 2191 | 1.621s | 0.020s |

---

## Turn 9 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0aa6a9b5a2e2caf30069da4ce1f210819780b5e6cc067e1b4a`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_8fo8fWt78jYlRvTlrnRkRvgA",
    "output": "{\"ok\": true, \"result\": [{\"prediction\": 1, \"cosine_scores\": 0.9537599086761475}, {\"prediction\": 1, \"cosine_scores\": 0.895621657371521}, {\"prediction\": 1, \"cosine_scores\": 0.9625198841094971}]}"
  }
]
```

### Model Output
**response_id:** `resp_0aa6a9b5a2e2caf30069da4ce1f210819780b5e6cc067e1b4a`

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
    "call_id": "call_OLEnwAmBIgdZCZKB1SRbsWLF",
    "arguments": {
      "item_name": "cosine_mrpc_threshold_score",
      "start_position": 0,
      "end_position": 10
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_OLEnwAmBIgdZCZKB1SRbsWLF`

**Arguments:**
```json
{
  "item_name": "cosine_mrpc_threshold_score",
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
      "prediction": 1,
      "score": 0.937690019607544
    },
    {
      "prediction": 1,
      "score": 0.9651895761489868
    },
    {
      "prediction": 1,
      "score": 0.9854921102523804
    },
    {
      "prediction": 1,
      "score": 0.9670572280883789
    },
    {
      "prediction": 1,
      "score": 0.9688267707824707
    },
    {
      "prediction": 1,
      "score": 0.9290030002593994
    },
    {
      "prediction": 1,
      "score": 0.974102795124054
    },
    {
      "prediction": 1,
      "score": 0.9585970044136047
    },
    {
      "prediction": 1,
      "score": 0.9585968852043152
    },
    {
      "prediction": 1,
      "score": 0.9949901103973389
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 3811 | 69 | 33 | 2309 | 1.822s | 0.019s |

---

## Turn 10 — `get_item_names` [ok]

### Model Input
**previous_response_id:** `resp_0aa6a9b5a2e2caf30069da4ce3c8dc8197ac2e20654505d2cf`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_OLEnwAmBIgdZCZKB1SRbsWLF",
    "output": "{\"ok\": true, \"result\": [{\"prediction\": 1, \"score\": 0.937690019607544}, {\"prediction\": 1, \"score\": 0.9651895761489868}, {\"prediction\": 1, \"score\": 0.9854921102523804}, {\"prediction\": 1, \"score\": 0.9670572280883789}, {\"prediction\": 1, \"score\": 0.9688267707824707}, {\"prediction\": 1, \"score\": 0.9290030002593994}, {\"prediction\": 1, \"score\": 0.974102795124054}, {\"prediction\": 1, \"score\": 0.9585970044136047}, {\"prediction\": 1, \"score\": 0.9585968852043152}, {\"prediction\": 1, \"score\": 0.9949901103973389}]}"
  }
]
```

### Model Output
**response_id:** `resp_0aa6a9b5a2e2caf30069da4ce3c8dc8197ac2e20654505d2cf`

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
    "call_id": "call_kO9vDBvKMroxsJGzx76OOPmv",
    "arguments": {
      "item_type": "document_list"
    }
  }
]
```

### Tool Call
**Tool:** `get_item_names` | **call_id:** `call_kO9vDBvKMroxsJGzx76OOPmv`

**Arguments:**
```json
{
  "item_type": "document_list"
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
| 4088 | 41 | 18 | 2586 | 1.419s | 0.022s |

---

## Turn 11 — `get_item_names` [ok]

### Model Input
**previous_response_id:** `resp_0aa6a9b5a2e2caf30069da4ce539308197bded0c97c241c857`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_kO9vDBvKMroxsJGzx76OOPmv",
    "output": "{\"ok\": true, \"result\": []}"
  }
]
```

### Model Output
**response_id:** `resp_0aa6a9b5a2e2caf30069da4ce539308197bded0c97c241c857`

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
    "call_id": "call_98MH37bXtoMA0y3YcsGYQgQh",
    "arguments": {
      "item_type": "file_list"
    }
  }
]
```

### Tool Call
**Tool:** `get_item_names` | **call_id:** `call_98MH37bXtoMA0y3YcsGYQgQh`

**Arguments:**
```json
{
  "item_type": "file_list"
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
| 4151 | 35 | 12 | 2649 | 1.551s | 0.022s |

---

## Turn 12 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0aa6a9b5a2e2caf30069da4ce6cf0481978ce87ddd7178476d`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_98MH37bXtoMA0y3YcsGYQgQh",
    "output": "{\"ok\": true, \"result\": []}"
  }
]
```

### Model Output
**response_id:** `resp_0aa6a9b5a2e2caf30069da4ce6cf0481978ce87ddd7178476d`

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
    "call_id": "call_ajUxaMSi0hIumeyA4VNMupwi",
    "arguments": {
      "item_name": "glue_mrpc_validation",
      "start_position": 0,
      "end_position": 3
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_ajUxaMSi0hIumeyA4VNMupwi`

**Arguments:**
```json
{
  "item_name": "glue_mrpc_validation",
  "start_position": 0,
  "end_position": 3
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    {
      "sentence1": "He said the foodservice pie business doesn 't fit the company 's long-term growth strategy .",
      "sentence2": "\" The foodservice pie business does not fit our long-term growth strategy .",
      "label": 1,
      "idx": 9
    },
    {
      "sentence1": "Magnarelli said Racicot hated the Iraqi regime and looked forward to using his long years of training in the war .",
      "sentence2": "His wife said he was \" 100 percent behind George Bush \" and looked forward to using his years of training in the war .",
      "label": 0,
      "idx": 18
    },
    {
      "sentence1": "The dollar was at 116.92 yen against the yen , flat on the session , and at 1.2891 against the Swiss franc , also flat .",
      "sentence2": "The dollar was at 116.78 yen JPY = , virtually flat on the session , and at 1.2871 against the Swiss franc CHF = , down 0.1 percent .",
      "label": 0,
      "idx": 25
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 4208 | 1013 | 978 | 2706 | 16.457s | 0.021s |

---

## Turn 13 — `finalize_result` [ok]

### Model Input
**previous_response_id:** `resp_0aa6a9b5a2e2caf30069da4cf748248197bb14c5fd4502c641`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_ajUxaMSi0hIumeyA4VNMupwi",
    "output": "{\"ok\": true, \"result\": [{\"sentence1\": \"He said the foodservice pie business doesn 't fit the company 's long-term growth strategy .\", \"sentence2\": \"\\\" The foodservice pie business does not fit our long-term growth strategy .\", \"label\": 1, \"idx\": 9}, {\"sentence1\": \"Magnarelli said Racicot hated the Iraqi regime and looked forward to using his long years of training in the war .\", \"sentence2\": \"His wife said he was \\\" 100 percent behind George Bush \\\" and looked forward to using his years of training in the war .\", \"label\": 0, \"idx\": 18}, {\"sentence1\": \"The dollar was at 116.92 yen against the yen , flat on the session , and at 1.2891 against the Swiss franc , also flat .\", \"sentence2\": \"The dollar was at 116.78 yen JPY = , virtually flat on the session , and at 1.2871 against the Swiss franc CHF = , down 0.1 percent .\", \"label\": 0, \"idx\": 25}]}"
  }
]
```

### Model Output
**response_id:** `resp_0aa6a9b5a2e2caf30069da4cf748248197bb14c5fd4502c641`

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
    "call_id": "call_mJEYSRwDCwGmmTVCOeSlsMIP",
    "arguments": {
      "summary": "{\"rows\":[{\"source_record\":\"distilbert_no_special_tokens_mean_cosine_mrpc_summary\",\"pooling_strategy\":\"mean pooling\",\"token_scope\":\"exclude special tokens\",\"accuracy\":0.7034,\"f1\":0.8213,\"non_paraphrase_recall\":0.07,\"paraphrase_recall\":1.0,\"interpretation\":\"Best headline accuracy, but still predicts paraphrase for almost everything.\"},{\"source_record\":\"distilbert_cls_cosine_mrpc_summary\",\"pooling_strategy\":\"CLS token representation\",\"token_scope\":\"special classification token only\",\"accuracy\":0.6863,\"f1\":0.8134,\"non_paraphrase_recall\":0.01,\"paraphrase_recall\":1.0,\"interpretation\":\"Slightly above the majority-class baseline; almost no ability to recover non-paraphrases.\"},{\"source_record\":\"distilbert_last4_mean_cosine_mrpc_summary\",\"pooling_strategy\":\"mean pooling over last 4 layers\",\"token_scope\":\"all tokens / last 4 layers\",\"accuracy\":0.6838,\"f1\":0.8122,\"non_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"interpretation\":\"Effectively behaves like an always-paraphrase classifier on MRPC.\"},{\"source_record\":\"distilbert_max_pool_cosine_mrpc_summary\",\"pooling_strategy\":\"max pooling\",\"token_scope\":\"all tokens\",\"accuracy\":0.6838,\"f1\":0.8122,\"non_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"interpretation\":\"Also collapses to majority-class behavior, with no non-paraphrase recall.\"},{\"source_record\":\"distilbert_mean_cosine_median_threshold_mrpc_summary\",\"pooling_strategy\":\"mean pooling\",\"token_scope\":\"all tokens\",\"accuracy\":0.6495,\"f1\":0.7039,\"non_paraphrase_recall\":0.74,\"paraphrase_recall\":0.61,\"interpretation\":\"Lowest overall accuracy, but the only variant with substantial non-paraphrase detection.\"}],\"summary\":\"Across the stored DistilBERT sentence-embedding runs for MRPC, pooling strategy changes overall accuracy only modestly (64.95% to 70.34%) but strongly changes the error profile. The highest accuracy comes from mean pooling after excluding special tokens (70.34%), followed by CLS pooling (68.63%). Mean pooling over the last 4 layers and max pooling both reach 68.38%, which matches the paraphrase-class prevalence implied by the classification reports (279 paraphrases out of 408 examples), indicating these variants behave almost like always predicting the majority paraphrase class. This is consistent with their paraphrase recall of 1.00 and non-paraphrase recall of 0.00. Standard mean pooling over all tokens yields the lowest accuracy (64.95%), but it is the only configuration that meaningfully identifies non-paraphrases (0.74 recall), at the cost of missing many true paraphrases (0.61 recall). Therefore, in this repository, pooling mainly affects the tradeoff between majority-class-biased accuracy and balanced class discrimination rather than producing large absolute gains in headline accuracy. The table should be read as repository evidence from stored cosine-similarity workflows, not as a perfectly controlled ablation, because list names indicate thresholding is not identical across all variants (for example, the all-token mean result uses a median threshold), so the observed differences are not attributable to pooling alone.\"}"
    }
  }
]
```

### Tool Call
**Tool:** `finalize_result` | **call_id:** `call_mJEYSRwDCwGmmTVCOeSlsMIP`

**Arguments:**
```json
{
  "summary": "{\"rows\":[{\"source_record\":\"distilbert_no_special_tokens_mean_cosine_mrpc_summary\",\"pooling_strategy\":\"mean pooling\",\"token_scope\":\"exclude special tokens\",\"accuracy\":0.7034,\"f1\":0.8213,\"non_paraphrase_recall\":0.07,\"paraphrase_recall\":1.0,\"interpretation\":\"Best headline accuracy, but still predicts paraphrase for almost everything.\"},{\"source_record\":\"distilbert_cls_cosine_mrpc_summary\",\"pooling_strategy\":\"CLS token representation\",\"token_scope\":\"special classification token only\",\"accuracy\":0.6863,\"f1\":0.8134,\"non_paraphrase_recall\":0.01,\"paraphrase_recall\":1.0,\"interpretation\":\"Slightly above the majority-class baseline; almost no ability to recover non-paraphrases.\"},{\"source_record\":\"distilbert_last4_mean_cosine_mrpc_summary\",\"pooling_strategy\":\"mean pooling over last 4 layers\",\"token_scope\":\"all tokens / last 4 layers\",\"accuracy\":0.6838,\"f1\":0.8122,\"non_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"interpretation\":\"Effectively behaves like an always-paraphrase classifier on MRPC.\"},{\"source_record\":\"distilbert_max_pool_cosine_mrpc_summary\",\"pooling_strategy\":\"max pooling\",\"token_scope\":\"all tokens\",\"accuracy\":0.6838,\"f1\":0.8122,\"non_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"interpretation\":\"Also collapses to majority-class behavior, with no non-paraphrase recall.\"},{\"source_record\":\"distilbert_mean_cosine_median_threshold_mrpc_summary\",\"pooling_strategy\":\"mean pooling\",\"token_scope\":\"all tokens\",\"accuracy\":0.6495,\"f1\":0.7039,\"non_paraphrase_recall\":0.74,\"paraphrase_recall\":0.61,\"interpretation\":\"Lowest overall accuracy, but the only variant with substantial non-paraphrase detection.\"}],\"summary\":\"Across the stored DistilBERT sentence-embedding runs for MRPC, pooling strategy changes overall accuracy only modestly (64.95% to 70.34%) but strongly changes the error profile. The highest accuracy comes from mean pooling after excluding special tokens (70.34%), followed by CLS pooling (68.63%). Mean pooling over the last 4 layers and max pooling both reach 68.38%, which matches the paraphrase-class prevalence implied by the classification reports (279 paraphrases out of 408 examples), indicating these variants behave almost like always predicting the majority paraphrase class. This is consistent with their paraphrase recall of 1.00 and non-paraphrase recall of 0.00. Standard mean pooling over all tokens yields the lowest accuracy (64.95%), but it is the only configuration that meaningfully identifies non-paraphrases (0.74 recall), at the cost of missing many true paraphrases (0.61 recall). Therefore, in this repository, pooling mainly affects the tradeoff between majority-class-biased accuracy and balanced class discrimination rather than producing large absolute gains in headline accuracy. The table should be read as repository evidence from stored cosine-similarity workflows, not as a perfectly controlled ablation, because list names indicate thresholding is not identical across all variants (for example, the all-token mean result uses a median threshold), so the observed differences are not attributable to pooling alone.\"}"
}
```

### Tool Output
```json
{
  "summary": "{\"rows\":[{\"source_record\":\"distilbert_no_special_tokens_mean_cosine_mrpc_summary\",\"pooling_strategy\":\"mean pooling\",\"token_scope\":\"exclude special tokens\",\"accuracy\":0.7034,\"f1\":0.8213,\"non_paraphrase_recall\":0.07,\"paraphrase_recall\":1.0,\"interpretation\":\"Best headline accuracy, but still predicts paraphrase for almost everything.\"},{\"source_record\":\"distilbert_cls_cosine_mrpc_summary\",\"pooling_strategy\":\"CLS token representation\",\"token_scope\":\"special classification token only\",\"accuracy\":0.6863,\"f1\":0.8134,\"non_paraphrase_recall\":0.01,\"paraphrase_recall\":1.0,\"interpretation\":\"Slightly above the majority-class baseline; almost no ability to recover non-paraphrases.\"},{\"source_record\":\"distilbert_last4_mean_cosine_mrpc_summary\",\"pooling_strategy\":\"mean pooling over last 4 layers\",\"token_scope\":\"all tokens / last 4 layers\",\"accuracy\":0.6838,\"f1\":0.8122,\"non_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"interpretation\":\"Effectively behaves like an always-paraphrase classifier on MRPC.\"},{\"source_record\":\"distilbert_max_pool_cosine_mrpc_summary\",\"pooling_strategy\":\"max pooling\",\"token_scope\":\"all tokens\",\"accuracy\":0.6838,\"f1\":0.8122,\"non_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"interpretation\":\"Also collapses to majority-class behavior, with no non-paraphrase recall.\"},{\"source_record\":\"distilbert_mean_cosine_median_threshold_mrpc_summary\",\"pooling_strategy\":\"mean pooling\",\"token_scope\":\"all tokens\",\"accuracy\":0.6495,\"f1\":0.7039,\"non_paraphrase_recall\":0.74,\"paraphrase_recall\":0.61,\"interpretation\":\"Lowest overall accuracy, but the only variant with substantial non-paraphrase detection.\"}],\"summary\":\"Across the stored DistilBERT sentence-embedding runs for MRPC, pooling strategy changes overall accuracy only modestly (64.95% to 70.34%) but strongly changes the error profile. The highest accuracy comes from mean pooling after excluding special tokens (70.34%), followed by CLS pooling (68.63%). Mean pooling over the last 4 layers and max pooling both reach 68.38%, which matches the paraphrase-class prevalence implied by the classification reports (279 paraphrases out of 408 examples), indicating these variants behave almost like always predicting the majority paraphrase class. This is consistent with their paraphrase recall of 1.00 and non-paraphrase recall of 0.00. Standard mean pooling over all tokens yields the lowest accuracy (64.95%), but it is the only configuration that meaningfully identifies non-paraphrases (0.74 recall), at the cost of missing many true paraphrases (0.61 recall). Therefore, in this repository, pooling mainly affects the tradeoff between majority-class-biased accuracy and balanced class discrimination rather than producing large absolute gains in headline accuracy. The table should be read as repository evidence from stored cosine-similarity workflows, not as a perfectly controlled ablation, because list names indicate thresholding is not identical across all variants (for example, the all-token mean result uses a median threshold), so the observed differences are not attributable to pooling alone.\"}"
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 5470 | 3666 | 2914 | 3968 | 52.271s | 0.000s |

---

# Run Summary

**Final Result:**
```json
{
  "summary": "{\"rows\":[{\"source_record\":\"distilbert_no_special_tokens_mean_cosine_mrpc_summary\",\"pooling_strategy\":\"mean pooling\",\"token_scope\":\"exclude special tokens\",\"accuracy\":0.7034,\"f1\":0.8213,\"non_paraphrase_recall\":0.07,\"paraphrase_recall\":1.0,\"interpretation\":\"Best headline accuracy, but still predicts paraphrase for almost everything.\"},{\"source_record\":\"distilbert_cls_cosine_mrpc_summary\",\"pooling_strategy\":\"CLS token representation\",\"token_scope\":\"special classification token only\",\"accuracy\":0.6863,\"f1\":0.8134,\"non_paraphrase_recall\":0.01,\"paraphrase_recall\":1.0,\"interpretation\":\"Slightly above the majority-class baseline; almost no ability to recover non-paraphrases.\"},{\"source_record\":\"distilbert_last4_mean_cosine_mrpc_summary\",\"pooling_strategy\":\"mean pooling over last 4 layers\",\"token_scope\":\"all tokens / last 4 layers\",\"accuracy\":0.6838,\"f1\":0.8122,\"non_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"interpretation\":\"Effectively behaves like an always-paraphrase classifier on MRPC.\"},{\"source_record\":\"distilbert_max_pool_cosine_mrpc_summary\",\"pooling_strategy\":\"max pooling\",\"token_scope\":\"all tokens\",\"accuracy\":0.6838,\"f1\":0.8122,\"non_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"interpretation\":\"Also collapses to majority-class behavior, with no non-paraphrase recall.\"},{\"source_record\":\"distilbert_mean_cosine_median_threshold_mrpc_summary\",\"pooling_strategy\":\"mean pooling\",\"token_scope\":\"all tokens\",\"accuracy\":0.6495,\"f1\":0.7039,\"non_paraphrase_recall\":0.74,\"paraphrase_recall\":0.61,\"interpretation\":\"Lowest overall accuracy, but the only variant with substantial non-paraphrase detection.\"}],\"summary\":\"Across the stored DistilBERT sentence-embedding runs for MRPC, pooling strategy changes overall accuracy only modestly (64.95% to 70.34%) but strongly changes the error profile. The highest accuracy comes from mean pooling after excluding special tokens (70.34%), followed by CLS pooling (68.63%). Mean pooling over the last 4 layers and max pooling both reach 68.38%, which matches the paraphrase-class prevalence implied by the classification reports (279 paraphrases out of 408 examples), indicating these variants behave almost like always predicting the majority paraphrase class. This is consistent with their paraphrase recall of 1.00 and non-paraphrase recall of 0.00. Standard mean pooling over all tokens yields the lowest accuracy (64.95%), but it is the only configuration that meaningfully identifies non-paraphrases (0.74 recall), at the cost of missing many true paraphrases (0.61 recall). Therefore, in this repository, pooling mainly affects the tradeoff between majority-class-biased accuracy and balanced class discrimination rather than producing large absolute gains in headline accuracy. The table should be read as repository evidence from stored cosine-similarity workflows, not as a perfectly controlled ablation, because list names indicate thresholding is not identical across all variants (for example, the all-token mean result uses a median threshold), so the observed differences are not attributable to pooling alone.\"}"
}
```

**Metrics Summary:**
```json
{
  "tokens": {
    "input": 46939,
    "output": 5422,
    "reasoning": 4225,
    "total": 52361,
    "system_estimate": 1502,
    "conversation": 25981
  },
  "code": {
    "executions": 0,
    "failed_executions": 0,
    "total_lines": 0
  },
  "timing": {
    "api_latency_s": 92.491,
    "exec_latency_s": 0.229,
    "wall_time_s": 92.719
  },
  "api_calls": 14,
  "cost": null
}
```
