# Agent Trace — 20260411T023533Z

**Model:** `gpt-5.4`  
**Timestamp:** 2026-04-11T02:35:33.912585+00:00  
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

- Always act via tool calls — never just describe what you would do.
- On errors, read the error message and retry with corrected arguments.
- **Do not make direct HuggingFace model calls** — all model inference results
  are pre-computed and stored in the TableVault repository. Retrieve them there.

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
**previous_response_id:** `resp_092c4efcdc768a310069d9b3761dd4819b8f74dda57332702b`

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
**response_id:** `resp_092c4efcdc768a310069d9b3761dd4819b8f74dda57332702b`

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
    "call_id": "call_GYWYHmLfJLPpW7f5Ia9pjkNe",
    "arguments": {
      "item_type": "record_list"
    }
  }
]
```

### Tool Call
**Tool:** `get_item_names` | **call_id:** `call_GYWYHmLfJLPpW7f5Ia9pjkNe`

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
| 1475 | 198 | 175 | 0 | 3.361s | 0.022s |

---

## Turn 1 — `get_item_names` [ok]

### Model Input
**previous_response_id:** `resp_092c4efcdc768a310069d9b3795c0c819bb12a6abdf398d154`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_GYWYHmLfJLPpW7f5Ia9pjkNe",
    "output": "{\"ok\": true, \"result\": [\"consensus_then_avg_margin_mrpc_summary\", \"cosine_mrpc_max_pool_similarity_prediction\", \"cosine_mrpc_mean_similarity_prediction\", \"cosine_mrpc_threshold_score\", \"distilbert_cls_cosine_mrpc_summary\", \"distilbert_cross_text_prediction\", \"distilbert_cross_text_prediction_cutoff\", \"distilbert_last4_mean_cosine_mrpc_summary\", \"distilbert_margin_score_prediction_values\", \"distilbert_max_pool_cosine_mrpc_summary\", \"distilbert_mean_cosine_median_threshold_mrpc_summary\", \"distilbert_no_special_tokens_mean_cosine_mrpc_summary\", \"distilbert_quora_softmax_prediction\", \"distilbert_swap_prediction_values\", \"distilbert_symmetric_average_prediction\", \"distilbert-normalized-text-prediction\", \"entailment_logprob_odds_mrpc_summary\", \"flan_prediction_and_logit_prefix\", \"flan_prediction_logit_calibrated\", \"flan_prediction_scored\", \"flan_t5_answer_prefix_yes_no_mrpcc_summary\", \"flan_t5_contextual_calibrated_yes_no_mrpc_summary\", \"flan_t5_full_answer_logprob_mrpc_summary\", \"flan_t5_symmetric_prompt_average_mrpc_summary\", \"flan_t5_true_false_first_step_mrpc_summary\", \"glue_mrpc_validation\", \"google_flan_prediction_and_logits\", \"google_flan_prediction_swapped\", \"hf_pipeline_mrpc_bidirectional_order_average_summary\", \"hf_pipeline_mrpc_margin_rule_summary\", \"hf_pipeline_mrpc_raw_logits_softmax_summary\", \"hf_pipeline_mrpc_short_maxlen_64_summary\", \"hf_pipeline_mrpc_threshold_070_summary\", \"min_direction_margin_mrpc_summary\", \"minilm_cosine_threshold_prediction\", \"mrpc_distilbert_predictions\", \"mrpc_entailment_prediction\", \"mrpc_gate_margin_prediction\", \"mrpc_mean_gap_prediction\", \"mrpc_min_margin_prediction\", \"mrpc_neutral_penalty_prediction\", \"mrpc_paraphrase_inference_distilbert_mistakes\", \"mrpc_paraphrase_inference_distilbert_output\", \"neutral_penalized_margin_mrpc_summary\", \"no_special_cosine_mrpc_similarity_prediction\", \"pipeline_distilbert_shortened\", \"pipeline_distilbert_softmax_probs\", \"pipeline_distilbert_threshold\", \"quora_cross_encoder_max_length_64_mrpc_summary\", \"quora_cross_encoder_prefixed_sentence_tags_mrpc_summary\", \"quora_cross_encoder_softmax_threshold_065_mrpc_summary\", \"quora_cross_encoder_symmetric_average_mrpc_summary\", \"quora_cross_encoder_text_normalized_mrpc_summary\", \"sentence_transformers_mrpc_prediction_distance\", \"sentence_transformers_mrpc_prediction_max64\", \"sentence_transformers_mrpc_prediction_threshold\", \"sentence_transformers_mrpc_prediction_threshold_2\", \"softmax_gap_mean_mrpc_summary\", \"st_all_distilroberta_v1_cosine_threshold_mrpc_summary\", \"st_all_minilm_l6_l2_distance_threshold_mrpc_summary\", \"st_all_minilm_l6_max_seq_len_64_cosine_mrpc_summary\", \"st_paraphrase_minilm_l3_cosine_threshold_mrpc_summary\", \"st_paraphrase_minilm_l6_cosine_threshold_mrpc_summary\", \"threshold_cosine_mrpc_similarity_prediction\"]}"
  }
]
```

### Model Output
**response_id:** `resp_092c4efcdc768a310069d9b3795c0c819bb12a6abdf398d154`

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
    "call_id": "call_6p2jUfl5BNSmu9CDBUxX1n3x",
    "arguments": {
      "item_type": "document_list"
    }
  }
]
```

### Tool Call
**Tool:** `get_item_names` | **call_id:** `call_6p2jUfl5BNSmu9CDBUxX1n3x`

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
| 2379 | 37 | 14 | 832 | 1.830s | 0.020s |

---

## Turn 2 — `get_item_names` [ok]

### Model Input
**previous_response_id:** `resp_092c4efcdc768a310069d9b37b39e4819b8ac8eef279356749`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_6p2jUfl5BNSmu9CDBUxX1n3x",
    "output": "{\"ok\": true, \"result\": []}"
  }
]
```

### Model Output
**response_id:** `resp_092c4efcdc768a310069d9b37b39e4819b8ac8eef279356749`

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
    "call_id": "call_cYi8lfDbM80hU6HO4fdZalUJ",
    "arguments": {
      "item_type": "file_list"
    }
  }
]
```

### Tool Call
**Tool:** `get_item_names` | **call_id:** `call_cYi8lfDbM80hU6HO4fdZalUJ`

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
| 2438 | 32 | 9 | 891 | 1.171s | 0.022s |

---

## Turn 3 — `get_item_names` [ok]

### Model Input
**previous_response_id:** `resp_092c4efcdc768a310069d9b37c66c4819ba47682cc98882bd3`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_cYi8lfDbM80hU6HO4fdZalUJ",
    "output": "{\"ok\": true, \"result\": []}"
  }
]
```

### Model Output
**response_id:** `resp_092c4efcdc768a310069d9b37c66c4819ba47682cc98882bd3`

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
    "call_id": "call_4ZpafkPlvp2HYjDJx3NLCN1B",
    "arguments": {
      "item_type": "embedding_list"
    }
  }
]
```

### Tool Call
**Tool:** `get_item_names` | **call_id:** `call_4ZpafkPlvp2HYjDJx3NLCN1B`

**Arguments:**
```json
{
  "item_type": "embedding_list"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "sentence-transformers-sentence-1-distance_threshold",
    "sentence-transformers-sentence-1-max64",
    "sentence-transformers-sentence-1-threshold",
    "sentence-transformers-sentence-1-threshold_2",
    "sentence-transformers-sentence-2-distance_threshold",
    "sentence-transformers-sentence-2-max64",
    "sentence-transformers-sentence-2-threshold",
    "sentence-transformers-sentence-2-threshold_2"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 2492 | 36 | 13 | 945 | 1.554s | 0.024s |

---

## Turn 4 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_092c4efcdc768a310069d9b37dfae0819ba07058c325495182`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_4ZpafkPlvp2HYjDJx3NLCN1B",
    "output": "{\"ok\": true, \"result\": [\"sentence-transformers-sentence-1-distance_threshold\", \"sentence-transformers-sentence-1-max64\", \"sentence-transformers-sentence-1-threshold\", \"sentence-transformers-sentence-1-threshold_2\", \"sentence-transformers-sentence-2-distance_threshold\", \"sentence-transformers-sentence-2-max64\", \"sentence-transformers-sentence-2-threshold\", \"sentence-transformers-sentence-2-threshold_2\"]}"
  }
]
```

### Model Output
**response_id:** `resp_092c4efcdc768a310069d9b37dfae0819ba07058c325495182`

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
    "call_id": "call_Q1oywdLC1Q0FvywEm0vOlxjN",
    "arguments": {
      "item_name": "distilbert_cls_cosine_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_Q1oywdLC1Q0FvywEm0vOlxjN`

**Arguments:**
```json
{
  "item_name": "distilbert_cls_cosine_mrpc_summary",
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
| 2641 | 263 | 224 | 1094 | 4.378s | 0.019s |

---

## Turn 5 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_092c4efcdc768a310069d9b3825d6c819baed997c081fa9b3a`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_Q1oywdLC1Q0FvywEm0vOlxjN",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.6862745098039216, \"f1\": 0.8134110787172012, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       1.00      0.01      0.02       129\\n    paraphrase       0.69      1.00      0.81       279\\n\\n      accuracy                           0.69       408\\n     macro avg       0.84      0.50      0.41       408\\n  weighted avg       0.78      0.69      0.56       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_092c4efcdc768a310069d9b3825d6c819baed997c081fa9b3a`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_q3kWvRsobZZUzjKkaD5mbZNL",
    "arguments": {
      "item_name": "distilbert_mean_cosine_median_threshold_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_q3kWvRsobZZUzjKkaD5mbZNL`

**Arguments:**
```json
{
  "item_name": "distilbert_mean_cosine_median_threshold_mrpc_summary",
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
| 3070 | 40 | 0 | 1523 | 1.363s | 0.023s |

---

## Turn 6 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_092c4efcdc768a310069d9b383c5d8819b93d744d93401a8e6`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_q3kWvRsobZZUzjKkaD5mbZNL",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.6495098039215687, \"f1\": 0.7039337474120083, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.47      0.74      0.57       129\\n    paraphrase       0.83      0.61      0.70       279\\n\\n      accuracy                           0.65       408\\n     macro avg       0.65      0.67      0.64       408\\n  weighted avg       0.72      0.65      0.66       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_092c4efcdc768a310069d9b383c5d8819b93d744d93401a8e6`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_JZr5ah1S4O8nbYDE7PYPWcz3",
    "arguments": {
      "item_name": "distilbert_max_pool_cosine_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_JZr5ah1S4O8nbYDE7PYPWcz3`

**Arguments:**
```json
{
  "item_name": "distilbert_max_pool_cosine_mrpc_summary",
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
| 3276 | 38 | 0 | 1729 | 1.307s | 0.019s |

---

## Turn 7 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_092c4efcdc768a310069d9b385138c819bb94ba0a5bb29e285`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_JZr5ah1S4O8nbYDE7PYPWcz3",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.6838235294117647, \"f1\": 0.8122270742358079, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.00      0.00      0.00       129\\n    paraphrase       0.68      1.00      0.81       279\\n\\n      accuracy                           0.68       408\\n     macro avg       0.34      0.50      0.41       408\\n  weighted avg       0.47      0.68      0.56       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_092c4efcdc768a310069d9b385138c819bb94ba0a5bb29e285`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_4yQtplU7iTfla1O1CFuguqqC",
    "arguments": {
      "item_name": "distilbert_last4_mean_cosine_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_4yQtplU7iTfla1O1CFuguqqC`

**Arguments:**
```json
{
  "item_name": "distilbert_last4_mean_cosine_mrpc_summary",
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
| 3480 | 39 | 0 | 1933 | 2.289s | 0.018s |

---

## Turn 8 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_092c4efcdc768a310069d9b387641c819bb7eb88b814bf9cc5`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_4yQtplU7iTfla1O1CFuguqqC",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.6838235294117647, \"f1\": 0.8122270742358079, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.00      0.00      0.00       129\\n    paraphrase       0.68      1.00      0.81       279\\n\\n      accuracy                           0.68       408\\n     macro avg       0.34      0.50      0.41       408\\n  weighted avg       0.47      0.68      0.56       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_092c4efcdc768a310069d9b387641c819bb7eb88b814bf9cc5`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_8Gz7Q814BWxWgAxZLS32tt2u",
    "arguments": {
      "item_name": "distilbert_no_special_tokens_mean_cosine_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_8Gz7Q814BWxWgAxZLS32tt2u`

**Arguments:**
```json
{
  "item_name": "distilbert_no_special_tokens_mean_cosine_mrpc_summary",
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
      "f1": 0.8212703101920237,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.90      0.07      0.13       129\n    paraphrase       0.70      1.00      0.82       279\n\n      accuracy                           0.70       408\n     macro avg       0.80      0.53      0.48       408\n  weighted avg       0.76      0.70      0.60       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 3685 | 40 | 0 | 2138 | 1.605s | 0.023s |

---

## Turn 9 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_092c4efcdc768a310069d9b3890610819ba9bbfb2594fc4e9e`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_8Gz7Q814BWxWgAxZLS32tt2u",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.7034313725490197, \"f1\": 0.8212703101920237, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.90      0.07      0.13       129\\n    paraphrase       0.70      1.00      0.82       279\\n\\n      accuracy                           0.70       408\\n     macro avg       0.80      0.53      0.48       408\\n  weighted avg       0.76      0.70      0.60       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_092c4efcdc768a310069d9b3890610819ba9bbfb2594fc4e9e`

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
    "call_id": "call_RLyiXRnaFBTmNC8qCo0YykRX",
    "arguments": {
      "item_name": "cosine_mrpc_mean_similarity_prediction",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_RLyiXRnaFBTmNC8qCo0YykRX`

**Arguments:**
```json
{
  "item_name": "cosine_mrpc_mean_similarity_prediction",
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
      "similarities": 0.9810966849327087
    },
    {
      "prediction": 1,
      "similarities": 0.9638397097587585
    },
    {
      "prediction": 1,
      "similarities": 0.9804420471191406
    },
    {
      "prediction": 1,
      "similarities": 0.9758433699607849
    },
    {
      "prediction": 1,
      "similarities": 0.9712404608726501
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 3891 | 80 | 43 | 2344 | 1.739s | 0.017s |

---

## Turn 10 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_092c4efcdc768a310069d9b38ad5bc819b9c50dc605540201c`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_RLyiXRnaFBTmNC8qCo0YykRX",
    "output": "{\"ok\": true, \"result\": [{\"prediction\": 1, \"similarities\": 0.9810966849327087}, {\"prediction\": 1, \"similarities\": 0.9638397097587585}, {\"prediction\": 1, \"similarities\": 0.9804420471191406}, {\"prediction\": 1, \"similarities\": 0.9758433699607849}, {\"prediction\": 1, \"similarities\": 0.9712404608726501}]}"
  }
]
```

### Model Output
**response_id:** `resp_092c4efcdc768a310069d9b38ad5bc819b9c50dc605540201c`

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
    "call_id": "call_a5LwoVgdjzOdK40DxkVa76Yk",
    "arguments": {
      "item_name": "cosine_mrpc_threshold_score",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_a5LwoVgdjzOdK40DxkVa76Yk`

**Arguments:**
```json
{
  "item_name": "cosine_mrpc_threshold_score",
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
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 4091 | 50 | 14 | 2544 | 1.715s | 0.021s |

---

## Turn 11 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_092c4efcdc768a310069d9b38c850c819b81d49abb3df06725`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_a5LwoVgdjzOdK40DxkVa76Yk",
    "output": "{\"ok\": true, \"result\": [{\"prediction\": 1, \"score\": 0.937690019607544}, {\"prediction\": 1, \"score\": 0.9651895761489868}, {\"prediction\": 1, \"score\": 0.9854921102523804}, {\"prediction\": 1, \"score\": 0.9670572280883789}, {\"prediction\": 1, \"score\": 0.9688267707824707}]}"
  }
]
```

### Model Output
**response_id:** `resp_092c4efcdc768a310069d9b38c850c819b81d49abb3df06725`

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
    "call_id": "call_eRyvP0YhcbRHM2MnZW8YmXEL",
    "arguments": {
      "item_name": "glue_mrpc_validation",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_eRyvP0YhcbRHM2MnZW8YmXEL`

**Arguments:**
```json
{
  "item_name": "glue_mrpc_validation",
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
    },
    {
      "sentence1": "The AFL-CIO is waiting until October to decide if it will endorse a candidate .",
      "sentence2": "The AFL-CIO announced Wednesday that it will decide in October whether to endorse a candidate before the primaries .",
      "label": 1,
      "idx": 32
    },
    {
      "sentence1": "No dates have been set for the civil or the criminal trial .",
      "sentence2": "No dates have been set for the criminal or civil cases , but Shanley has pleaded not guilty .",
      "label": 0,
      "idx": 33
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 4255 | 434 | 399 | 2708 | 6.163s | 0.022s |

---

## Turn 12 — `finalize_result` [ok]

### Model Input
**previous_response_id:** `resp_092c4efcdc768a310069d9b392b65c819b8ddf5fbaf2ff2285`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_eRyvP0YhcbRHM2MnZW8YmXEL",
    "output": "{\"ok\": true, \"result\": [{\"sentence1\": \"He said the foodservice pie business doesn 't fit the company 's long-term growth strategy .\", \"sentence2\": \"\\\" The foodservice pie business does not fit our long-term growth strategy .\", \"label\": 1, \"idx\": 9}, {\"sentence1\": \"Magnarelli said Racicot hated the Iraqi regime and looked forward to using his long years of training in the war .\", \"sentence2\": \"His wife said he was \\\" 100 percent behind George Bush \\\" and looked forward to using his years of training in the war .\", \"label\": 0, \"idx\": 18}, {\"sentence1\": \"The dollar was at 116.92 yen against the yen , flat on the session , and at 1.2891 against the Swiss franc , also flat .\", \"sentence2\": \"The dollar was at 116.78 yen JPY = , virtually flat on the session , and at 1.2871 against the Swiss franc CHF = , down 0.1 percent .\", \"label\": 0, \"idx\": 25}, {\"sentence1\": \"The AFL-CIO is waiting until October to decide if it will endorse a candidate .\", \"sentence2\": \"The AFL-CIO announced Wednesday that it will decide in October whether to endorse a candidate before the primaries .\", \"label\": 1, \"idx\": 32}, {\"sentence1\": \"No dates have been set for the civil or the criminal trial .\", \"sentence2\": \"No dates have been set for the criminal or civil cases , but Shanley has pleaded not guilty .\", \"label\": 0, \"idx\": 33}]}"
  }
]
```

### Model Output
**response_id:** `resp_092c4efcdc768a310069d9b392b65c819b8ddf5fbaf2ff2285`

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
    "call_id": "call_PXTGSqsXtTtYOP88Naexc36E",
    "arguments": {
      "summary": "{\"rows\":[{\"source_item\":\"distilbert_no_special_tokens_mean_cosine_mrpc_summary\",\"pooling_strategy\":\"Mean pooling over token embeddings, excluding special tokens\",\"accuracy\":0.7034,\"paraphrase_f1\":0.8213,\"non_paraphrase_recall\":0.07,\"paraphrase_recall\":1.0,\"balanced_recall\":0.535,\"observed_behavior\":\"Best headline accuracy, but still predicts paraphrase for almost all pairs.\"},{\"source_item\":\"distilbert_cls_cosine_mrpc_summary\",\"pooling_strategy\":\"CLS-token representation\",\"accuracy\":0.6863,\"paraphrase_f1\":0.8134,\"non_paraphrase_recall\":0.01,\"paraphrase_recall\":1.0,\"balanced_recall\":0.505,\"observed_behavior\":\"Near-majority-class behavior; almost never detects non-paraphrases.\"},{\"source_item\":\"distilbert_max_pool_cosine_mrpc_summary\",\"pooling_strategy\":\"Max pooling over token embeddings\",\"accuracy\":0.6838,\"paraphrase_f1\":0.8122,\"non_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"balanced_recall\":0.5,\"observed_behavior\":\"Matches the paraphrase-majority baseline; effectively labels every pair as paraphrase.\"},{\"source_item\":\"distilbert_last4_mean_cosine_mrpc_summary\",\"pooling_strategy\":\"Mean pooling with last-4-layer aggregation\",\"accuracy\":0.6838,\"paraphrase_f1\":0.8122,\"non_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"balanced_recall\":0.5,\"observed_behavior\":\"No improvement over max pooling at the evaluation level; also collapses to paraphrase predictions.\"},{\"source_item\":\"distilbert_mean_cosine_median_threshold_mrpc_summary\",\"pooling_strategy\":\"Standard mean pooling over token embeddings\",\"accuracy\":0.6495,\"paraphrase_f1\":0.7039,\"non_paraphrase_recall\":0.74,\"paraphrase_recall\":0.61,\"balanced_recall\":0.675,\"observed_behavior\":\"Lowest accuracy, but the only variant with substantial sensitivity to both classes instead of mostly predicting paraphrase.\"}],\"summary\":\"The repository contains five DistilBERT sentence-representation evaluations for MRPC based on cosine-style paraphrase decisions. Headline accuracy changes only modestly across pooling strategies, spanning 0.6495 to 0.7034. The highest stored accuracy comes from mean pooling without special tokens, followed by CLS pooling; max pooling and last-4-layer mean tie slightly lower, while standard mean pooling is worst on raw accuracy. However, the class-wise evidence shows that accuracy alone is misleading here. MRPC validation is paraphrase-heavy in these summaries (279 paraphrases vs 129 non-paraphrases), and three strategies\u2014max pooling, last-4 mean, and nearly CLS/no-special mean\u2014show extremely low non-paraphrase recall while maintaining perfect paraphrase recall. In practice, these behave like an almost-always-paraphrase classifier, so their higher accuracy is largely driven by class imbalance rather than true discrimination. Standard mean pooling reverses that pattern: it lowers headline accuracy and positive-class F1, but it is the only method with strong non-paraphrase recall and the best balanced recall across the two classes. Interpreted scientifically, pooling strategy affects MRPC performance mostly by shifting the precision-recall tradeoff and susceptibility to majority-class collapse, not by producing a large absolute gain in accuracy. Excluding special tokens gives the best top-line accuracy in the stored runs, but standard mean pooling appears less degenerate if the goal is to distinguish both paraphrases and non-paraphrases. A limitation is that the repository naming suggests similar but not perfectly identical thresholding procedures (one run explicitly uses a median threshold), so small differences may reflect both pooling and decision-threshold choices.\"}"
    }
  }
]
```

### Tool Call
**Tool:** `finalize_result` | **call_id:** `call_PXTGSqsXtTtYOP88Naexc36E`

**Arguments:**
```json
{
  "summary": "{\"rows\":[{\"source_item\":\"distilbert_no_special_tokens_mean_cosine_mrpc_summary\",\"pooling_strategy\":\"Mean pooling over token embeddings, excluding special tokens\",\"accuracy\":0.7034,\"paraphrase_f1\":0.8213,\"non_paraphrase_recall\":0.07,\"paraphrase_recall\":1.0,\"balanced_recall\":0.535,\"observed_behavior\":\"Best headline accuracy, but still predicts paraphrase for almost all pairs.\"},{\"source_item\":\"distilbert_cls_cosine_mrpc_summary\",\"pooling_strategy\":\"CLS-token representation\",\"accuracy\":0.6863,\"paraphrase_f1\":0.8134,\"non_paraphrase_recall\":0.01,\"paraphrase_recall\":1.0,\"balanced_recall\":0.505,\"observed_behavior\":\"Near-majority-class behavior; almost never detects non-paraphrases.\"},{\"source_item\":\"distilbert_max_pool_cosine_mrpc_summary\",\"pooling_strategy\":\"Max pooling over token embeddings\",\"accuracy\":0.6838,\"paraphrase_f1\":0.8122,\"non_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"balanced_recall\":0.5,\"observed_behavior\":\"Matches the paraphrase-majority baseline; effectively labels every pair as paraphrase.\"},{\"source_item\":\"distilbert_last4_mean_cosine_mrpc_summary\",\"pooling_strategy\":\"Mean pooling with last-4-layer aggregation\",\"accuracy\":0.6838,\"paraphrase_f1\":0.8122,\"non_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"balanced_recall\":0.5,\"observed_behavior\":\"No improvement over max pooling at the evaluation level; also collapses to paraphrase predictions.\"},{\"source_item\":\"distilbert_mean_cosine_median_threshold_mrpc_summary\",\"pooling_strategy\":\"Standard mean pooling over token embeddings\",\"accuracy\":0.6495,\"paraphrase_f1\":0.7039,\"non_paraphrase_recall\":0.74,\"paraphrase_recall\":0.61,\"balanced_recall\":0.675,\"observed_behavior\":\"Lowest accuracy, but the only variant with substantial sensitivity to both classes instead of mostly predicting paraphrase.\"}],\"summary\":\"The repository contains five DistilBERT sentence-representation evaluations for MRPC based on cosine-style paraphrase decisions. Headline accuracy changes only modestly across pooling strategies, spanning 0.6495 to 0.7034. The highest stored accuracy comes from mean pooling without special tokens, followed by CLS pooling; max pooling and last-4-layer mean tie slightly lower, while standard mean pooling is worst on raw accuracy. However, the class-wise evidence shows that accuracy alone is misleading here. MRPC validation is paraphrase-heavy in these summaries (279 paraphrases vs 129 non-paraphrases), and three strategies\u2014max pooling, last-4 mean, and nearly CLS/no-special mean\u2014show extremely low non-paraphrase recall while maintaining perfect paraphrase recall. In practice, these behave like an almost-always-paraphrase classifier, so their higher accuracy is largely driven by class imbalance rather than true discrimination. Standard mean pooling reverses that pattern: it lowers headline accuracy and positive-class F1, but it is the only method with strong non-paraphrase recall and the best balanced recall across the two classes. Interpreted scientifically, pooling strategy affects MRPC performance mostly by shifting the precision-recall tradeoff and susceptibility to majority-class collapse, not by producing a large absolute gain in accuracy. Excluding special tokens gives the best top-line accuracy in the stored runs, but standard mean pooling appears less degenerate if the goal is to distinguish both paraphrases and non-paraphrases. A limitation is that the repository naming suggests similar but not perfectly identical thresholding procedures (one run explicitly uses a median threshold), so small differences may reflect both pooling and decision-threshold choices.\"}"
}
```

### Tool Output
```json
{
  "summary": "{\"rows\":[{\"source_item\":\"distilbert_no_special_tokens_mean_cosine_mrpc_summary\",\"pooling_strategy\":\"Mean pooling over token embeddings, excluding special tokens\",\"accuracy\":0.7034,\"paraphrase_f1\":0.8213,\"non_paraphrase_recall\":0.07,\"paraphrase_recall\":1.0,\"balanced_recall\":0.535,\"observed_behavior\":\"Best headline accuracy, but still predicts paraphrase for almost all pairs.\"},{\"source_item\":\"distilbert_cls_cosine_mrpc_summary\",\"pooling_strategy\":\"CLS-token representation\",\"accuracy\":0.6863,\"paraphrase_f1\":0.8134,\"non_paraphrase_recall\":0.01,\"paraphrase_recall\":1.0,\"balanced_recall\":0.505,\"observed_behavior\":\"Near-majority-class behavior; almost never detects non-paraphrases.\"},{\"source_item\":\"distilbert_max_pool_cosine_mrpc_summary\",\"pooling_strategy\":\"Max pooling over token embeddings\",\"accuracy\":0.6838,\"paraphrase_f1\":0.8122,\"non_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"balanced_recall\":0.5,\"observed_behavior\":\"Matches the paraphrase-majority baseline; effectively labels every pair as paraphrase.\"},{\"source_item\":\"distilbert_last4_mean_cosine_mrpc_summary\",\"pooling_strategy\":\"Mean pooling with last-4-layer aggregation\",\"accuracy\":0.6838,\"paraphrase_f1\":0.8122,\"non_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"balanced_recall\":0.5,\"observed_behavior\":\"No improvement over max pooling at the evaluation level; also collapses to paraphrase predictions.\"},{\"source_item\":\"distilbert_mean_cosine_median_threshold_mrpc_summary\",\"pooling_strategy\":\"Standard mean pooling over token embeddings\",\"accuracy\":0.6495,\"paraphrase_f1\":0.7039,\"non_paraphrase_recall\":0.74,\"paraphrase_recall\":0.61,\"balanced_recall\":0.675,\"observed_behavior\":\"Lowest accuracy, but the only variant with substantial sensitivity to both classes instead of mostly predicting paraphrase.\"}],\"summary\":\"The repository contains five DistilBERT sentence-representation evaluations for MRPC based on cosine-style paraphrase decisions. Headline accuracy changes only modestly across pooling strategies, spanning 0.6495 to 0.7034. The highest stored accuracy comes from mean pooling without special tokens, followed by CLS pooling; max pooling and last-4-layer mean tie slightly lower, while standard mean pooling is worst on raw accuracy. However, the class-wise evidence shows that accuracy alone is misleading here. MRPC validation is paraphrase-heavy in these summaries (279 paraphrases vs 129 non-paraphrases), and three strategies\u2014max pooling, last-4 mean, and nearly CLS/no-special mean\u2014show extremely low non-paraphrase recall while maintaining perfect paraphrase recall. In practice, these behave like an almost-always-paraphrase classifier, so their higher accuracy is largely driven by class imbalance rather than true discrimination. Standard mean pooling reverses that pattern: it lowers headline accuracy and positive-class F1, but it is the only method with strong non-paraphrase recall and the best balanced recall across the two classes. Interpreted scientifically, pooling strategy affects MRPC performance mostly by shifting the precision-recall tradeoff and susceptibility to majority-class collapse, not by producing a large absolute gain in accuracy. Excluding special tokens gives the best top-line accuracy in the stored runs, but standard mean pooling appears less degenerate if the goal is to distinguish both paraphrases and non-paraphrases. A limitation is that the repository naming suggests similar but not perfectly identical thresholding procedures (one run explicitly uses a median threshold), so small differences may reflect both pooling and decision-threshold choices.\"}"
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 5058 | 4972 | 4127 | 3511 | 65.063s | 0.000s |

---

# Run Summary

**Final Result:**
```json
{
  "summary": "{\"rows\":[{\"source_item\":\"distilbert_no_special_tokens_mean_cosine_mrpc_summary\",\"pooling_strategy\":\"Mean pooling over token embeddings, excluding special tokens\",\"accuracy\":0.7034,\"paraphrase_f1\":0.8213,\"non_paraphrase_recall\":0.07,\"paraphrase_recall\":1.0,\"balanced_recall\":0.535,\"observed_behavior\":\"Best headline accuracy, but still predicts paraphrase for almost all pairs.\"},{\"source_item\":\"distilbert_cls_cosine_mrpc_summary\",\"pooling_strategy\":\"CLS-token representation\",\"accuracy\":0.6863,\"paraphrase_f1\":0.8134,\"non_paraphrase_recall\":0.01,\"paraphrase_recall\":1.0,\"balanced_recall\":0.505,\"observed_behavior\":\"Near-majority-class behavior; almost never detects non-paraphrases.\"},{\"source_item\":\"distilbert_max_pool_cosine_mrpc_summary\",\"pooling_strategy\":\"Max pooling over token embeddings\",\"accuracy\":0.6838,\"paraphrase_f1\":0.8122,\"non_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"balanced_recall\":0.5,\"observed_behavior\":\"Matches the paraphrase-majority baseline; effectively labels every pair as paraphrase.\"},{\"source_item\":\"distilbert_last4_mean_cosine_mrpc_summary\",\"pooling_strategy\":\"Mean pooling with last-4-layer aggregation\",\"accuracy\":0.6838,\"paraphrase_f1\":0.8122,\"non_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"balanced_recall\":0.5,\"observed_behavior\":\"No improvement over max pooling at the evaluation level; also collapses to paraphrase predictions.\"},{\"source_item\":\"distilbert_mean_cosine_median_threshold_mrpc_summary\",\"pooling_strategy\":\"Standard mean pooling over token embeddings\",\"accuracy\":0.6495,\"paraphrase_f1\":0.7039,\"non_paraphrase_recall\":0.74,\"paraphrase_recall\":0.61,\"balanced_recall\":0.675,\"observed_behavior\":\"Lowest accuracy, but the only variant with substantial sensitivity to both classes instead of mostly predicting paraphrase.\"}],\"summary\":\"The repository contains five DistilBERT sentence-representation evaluations for MRPC based on cosine-style paraphrase decisions. Headline accuracy changes only modestly across pooling strategies, spanning 0.6495 to 0.7034. The highest stored accuracy comes from mean pooling without special tokens, followed by CLS pooling; max pooling and last-4-layer mean tie slightly lower, while standard mean pooling is worst on raw accuracy. However, the class-wise evidence shows that accuracy alone is misleading here. MRPC validation is paraphrase-heavy in these summaries (279 paraphrases vs 129 non-paraphrases), and three strategies\u2014max pooling, last-4 mean, and nearly CLS/no-special mean\u2014show extremely low non-paraphrase recall while maintaining perfect paraphrase recall. In practice, these behave like an almost-always-paraphrase classifier, so their higher accuracy is largely driven by class imbalance rather than true discrimination. Standard mean pooling reverses that pattern: it lowers headline accuracy and positive-class F1, but it is the only method with strong non-paraphrase recall and the best balanced recall across the two classes. Interpreted scientifically, pooling strategy affects MRPC performance mostly by shifting the precision-recall tradeoff and susceptibility to majority-class collapse, not by producing a large absolute gain in accuracy. Excluding special tokens gives the best top-line accuracy in the stored runs, but standard mean pooling appears less degenerate if the goal is to distinguish both paraphrases and non-paraphrases. A limitation is that the repository naming suggests similar but not perfectly identical thresholding procedures (one run explicitly uses a median threshold), so small differences may reflect both pooling and decision-threshold choices.\"}"
}
```

**Metrics Summary:**
```json
{
  "tokens": {
    "input": 42231,
    "output": 6259,
    "reasoning": 5018,
    "total": 48490,
    "system_estimate": 1547,
    "conversation": 22192
  },
  "code": {
    "executions": 0,
    "failed_executions": 0,
    "total_lines": 0
  },
  "timing": {
    "api_latency_s": 93.538,
    "exec_latency_s": 0.249,
    "wall_time_s": 93.787
  },
  "api_calls": 13,
  "cost": null
}
```
