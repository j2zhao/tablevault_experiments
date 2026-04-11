# Agent Trace — 20260411T143816Z

**Model:** `gpt-5.4`  
**Timestamp:** 2026-04-11T14:38:16.529746+00:00  
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

## Turn 0 — `code_description_embedding_search` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5cd897c48195b20fe31652be9e79`

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
**response_id:** `resp_096e90c5623324b10069da5cd897c48195b20fe31652be9e79`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_description_embedding_search",
    "call_id": "call_Aw4jTUyCAIBr4bzA4HcbGqUd",
    "arguments": {
      "description_text": "MRPC paraphrase detection symmetry enforcement accuracy NLI-based zero-shot models prediction symmetry strategies experiment"
    }
  }
]
```

### Tool Call
**Tool:** `code_description_embedding_search` | **call_id:** `call_Aw4jTUyCAIBr4bzA4HcbGqUd`

**Arguments:**
```json
{
  "description_text": "MRPC paraphrase detection symmetry enforcement accuracy NLI-based zero-shot models prediction symmetry strategies experiment"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    [
      "BASE",
      "This notebook runs a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the NLI model typeform/distilbert-base-uncased-mnli. Its purpose is to score sentence pairs as paraphrase vs. not paraphrase without task-specific fine-tuning, using a neutral-penalized entailment margin. For each MRPC pair, the notebook evaluates both sentence orders, computes an entailment score minus the larger of the contradiction or neutral scores, averages the two directional margins, and predicts paraphrase when the averaged margin is positive. It then stores per-example predictions and scores in TableVault, links them back to the source validation records, computes evaluation metrics including accuracy, F1, and a classification report, inspects example predictions and errors, and saves dataset-, prediction-, summary-, and process-level metadata and semantic descriptions using OpenAI embeddings.",
      "neutral_penalized_margin_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli natural language inference model. For each sentence pair, it runs inference in both directions (sentence1\u2192sentence2 and sentence2\u2192sentence1), computes an entailment-versus-contradiction margin for each direction, averages the two margins, and predicts paraphrase only when neither direction is classified as contradiction and the average margin is positive. The notebook stores per-example predictions, directional margins, and gate decisions in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, logs error analysis examples, and saves dataset-, prediction-, summary-, and notebook-level metadata and embeddings for later retrieval and documentation.",
      "consensus_then_avg_margin_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using an NLI model. It loads sentence pairs and labels from TableVault, applies the typeform/distilbert-base-uncased-mnli sequence classification model, and treats paraphrase detection as entailment scoring: for each pair, it computes the log-probability difference between entailment and contradiction for both sentence orders (sentence1\u2192sentence2 and sentence2\u2192sentence1), averages the two directional scores, and predicts paraphrase when the averaged score is positive. The notebook stores per-example predictions and directional entailment log-odds in TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves both dataset-level summaries and notebook-level metadata/descriptions with OpenAI embeddings for documentation and retrieval.",
      "entailment_logprob_odds_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This dataset documents a symmetric-order paraphrase evaluation run on the GLUE MRPC validation split using the cross-encoder/quora-distilroberta-base model. It is built from the input dataset glue_mrpc_validation, whose examples contain sentence1, sentence2, and label. For each MRPC pair, the workflow scores both the original order (sentence1, sentence2) and the reversed order (sentence2, sentence1), converts model outputs to positive-class probabilities, averages the two scores, and thresholds the average at 0.5 to produce a final binary prediction.\n\nThe main derived prediction records are stored in distilbert_symmetric_average_prediction with columns y_pred, orig_score, and rev_score, and each record is linked back to the corresponding MRPC validation example. A companion summary record list, quora_cross_encoder_symmetric_average_mrpc_summary, stores aggregate evaluation outputs with columns accuracy, f1, and classification_report across the full validation set.\n\nRole in workflow: this dataset represents the full experiment output for symmetric-average paraphrase detection on MRPC, combining per-example predictions and run-level evaluation metrics for analysis, comparison, and traceability to the original validation inputs.",
      "quora_cross_encoder_symmetric_average_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook runs a zero-shot paraphrase detection experiment on the GLUE MRPC validation set using google/flan-t5-small. It frames each sentence pair as an instruction prompt asking whether the two sentences are paraphrases and scores the first decoder-step logits for the single-token answers yes and no. To reduce prompt bias, it applies contextual calibration by subtracting baseline yes/no logits computed from a null prompt with placeholder inputs (\u201cN/A\u201d, \u201cN/A\u201d), then predicts the label from the higher calibrated logit. The workflow loads MRPC examples from TableVault, generates batch predictions, stores raw and calibrated logits plus final predictions back into TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves summary records and semantic descriptions for the prediction outputs, summary table, and overall notebook process.",
      "flan_t5_contextual_calibrated_yes_no_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using google/flan-t5-small. It frames MRPC as a yes/no text-to-text classification task by prompting the model with two sentences and asking whether they are paraphrases. To reduce order sensitivity, each sentence pair is scored twice\u2014once in the original order and once with the sentences swapped\u2014and the first-token logits for yes and no are averaged across both prompts to produce the final prediction. The notebook loads the validation data from TableVault, runs batched inference with Hugging Face Transformers on MPS or CPU, computes accuracy, F1, and a classification report, inspects example predictions and errors, and stores per-example predictions, logits, summary metrics, and metadata back into TableVault with embedding-based descriptions.",
      "flan_t5_symmetric_prompt_average_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a directional-margin approach to paraphrase detection on the GLUE MRPC validation set. It loads sentence pairs and labels from TableVault, runs the typeform/distilbert-base-uncased-mnli sequence classification model as an NLI-based paraphrase scorer in both directions (sentence1\u2192sentence2 and sentence2\u2192sentence1), computes the entailment-minus-contradiction logit margin for each direction, and uses the minimum of the two margins as the final paraphrase score; pairs with positive minimum margin are predicted as paraphrases. The workflow then stores per-example predictions and margins in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, inspects sample predictions and errors, and saves a summary record and notebook-level metadata back to TableVault.",
      "min_direction_margin_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook runs a lightweight paraphrase detection experiment on the GLUE MRPC validation set and logs the full workflow to TableVault for traceability. It uses the sentence-transformers/all-MiniLM-L6-v2 model with max_seq_length set to 64 to encode each sentence in an MRPC pair into normalized 384-dimensional embeddings. For each example, it computes cosine similarity between the two sentence embeddings, applies a fixed threshold of 0.80 to predict whether the pair is a paraphrase, and evaluates the results with accuracy, F1, and a classification report. The notebook stores the sentence-level embeddings, prediction records, evaluation summary, and metadata descriptions in TableVault, using OpenAI text embeddings to embed the textual descriptions and properties. It also prints sample predictions and error cases to support qualitative inspection of model behavior.",
      "st_all_minilm_l6_max_seq_len_64_cosine_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook runs a paraphrase detection experiment on the GLUE MRPC validation set using the sentence-transformers/all-distilroberta-v1 model. It encodes each sentence in every sentence pair into normalized 768-dimensional embeddings, computes cosine similarity via the dot product, and applies a fixed threshold of 0.72 to predict whether the pair is a paraphrase. The workflow stores sentence embeddings, prediction records, evaluation outputs, and metadata in TableVault, linking all derived artifacts back to the original MRPC validation examples. It then evaluates performance with accuracy, F1, and a classification report, inspects sample predictions and errors, and saves a summary record for the full experiment.",
      "st_all_distilroberta_v1_cosine_threshold_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a simple semantic-similarity baseline for paraphrase detection on the GLUE MRPC validation set. It uses distilbert-base-uncased to encode each sentence, averages the last four hidden layers, applies mean pooling over tokens, and L2-normalizes the resulting sentence embeddings. For each sentence pair, it computes cosine similarity between the two embeddings and converts similarity scores into binary paraphrase predictions using a fixed threshold of 0.85. The workflow loads MRPC examples from TableVault, generates pairwise predictions and similarity scores, computes evaluation metrics including accuracy, F1, and a classification report, inspects example predictions and errors, and stores both per-example outputs and summary results back into TableVault with descriptive metadata.",
      "distilbert_last4_mean_cosine_mrpc",
      "process_list"
    ]
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 1636 | 118 | 78 | 0 | 2.390s | 0.435s |

---

## Turn 1 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5cdb6c48819586731e6eed04123c`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_Aw4jTUyCAIBr4bzA4HcbGqUd",
    "output": "{\"ok\": true, \"result\": [[\"BASE\", \"This notebook runs a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the NLI model typeform/distilbert-base-uncased-mnli. Its purpose is to score sentence pairs as paraphrase vs. not paraphrase without task-specific fine-tuning, using a neutral-penalized entailment margin. For each MRPC pair, the notebook evaluates both sentence orders, computes an entailment score minus the larger of the contradiction or neutral scores, averages the two directional margins, and predicts paraphrase when the averaged margin is positive. It then stores per-example predictions and scores in TableVault, links them back to the source validation records, computes evaluation metrics including accuracy, F1, and a classification report, inspects example predictions and errors, and saves dataset-, prediction-, summary-, and process-level metadata and semantic descriptions using OpenAI embeddings.\", \"neutral_penalized_margin_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli natural language inference model. For each sentence pair, it runs inference in both directions (sentence1\\u2192sentence2 and sentence2\\u2192sentence1), computes an entailment-versus-contradiction margin for each direction, averages the two margins, and predicts paraphrase only when neither direction is classified as contradiction and the average margin is positive. The notebook stores per-example predictions, directional margins, and gate decisions in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, logs error analysis examples, and saves dataset-, prediction-, summary-, and notebook-level metadata and embeddings for later retrieval and documentation.\", \"consensus_then_avg_margin_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using an NLI model. It loads sentence pairs and labels from TableVault, applies the typeform/distilbert-base-uncased-mnli sequence classification model, and treats paraphrase detection as entailment scoring: for each pair, it computes the log-probability difference between entailment and contradiction for both sentence orders (sentence1\\u2192sentence2 and sentence2\\u2192sentence1), averages the two directional scores, and predicts paraphrase when the averaged score is positive. The notebook stores per-example predictions and directional entailment log-odds in TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves both dataset-level summaries and notebook-level metadata/descriptions with OpenAI embeddings for documentation and retrieval.\", \"entailment_logprob_odds_mrpc\", \"process_list\"], [\"BASE\", \"This dataset documents a symmetric-order paraphrase evaluation run on the GLUE MRPC validation split using the cross-encoder/quora-distilroberta-base model. It is built from the input dataset glue_mrpc_validation, whose examples contain sentence1, sentence2, and label. For each MRPC pair, the workflow scores both the original order (sentence1, sentence2) and the reversed order (sentence2, sentence1), converts model outputs to positive-class probabilities, averages the two scores, and thresholds the average at 0.5 to produce a final binary prediction.\\n\\nThe main derived prediction records are stored in distilbert_symmetric_average_prediction with columns y_pred, orig_score, and rev_score, and each record is linked back to the corresponding MRPC validation example. A companion summary record list, quora_cross_encoder_symmetric_average_mrpc_summary, stores aggregate evaluation outputs with columns accuracy, f1, and classification_report across the full validation set.\\n\\nRole in workflow: this dataset represents the full experiment output for symmetric-average paraphrase detection on MRPC, combining per-example predictions and run-level evaluation metrics for analysis, comparison, and traceability to the original validation inputs.\", \"quora_cross_encoder_symmetric_average_mrpc\", \"process_list\"], [\"BASE\", \"This notebook runs a zero-shot paraphrase detection experiment on the GLUE MRPC validation set using google/flan-t5-small. It frames each sentence pair as an instruction prompt asking whether the two sentences are paraphrases and scores the first decoder-step logits for the single-token answers yes and no. To reduce prompt bias, it applies contextual calibration by subtracting baseline yes/no logits computed from a null prompt with placeholder inputs (\\u201cN/A\\u201d, \\u201cN/A\\u201d), then predicts the label from the higher calibrated logit. The workflow loads MRPC examples from TableVault, generates batch predictions, stores raw and calibrated logits plus final predictions back into TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves summary records and semantic descriptions for the prediction outputs, summary table, and overall notebook process.\", \"flan_t5_contextual_calibrated_yes_no_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using google/flan-t5-small. It frames MRPC as a yes/no text-to-text classification task by prompting the model with two sentences and asking whether they are paraphrases. To reduce order sensitivity, each sentence pair is scored twice\\u2014once in the original order and once with the sentences swapped\\u2014and the first-token logits for yes and no are averaged across both prompts to produce the final prediction. The notebook loads the validation data from TableVault, runs batched inference with Hugging Face Transformers on MPS or CPU, computes accuracy, F1, and a classification report, inspects example predictions and errors, and stores per-example predictions, logits, summary metrics, and metadata back into TableVault with embedding-based descriptions.\", \"flan_t5_symmetric_prompt_average_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a directional-margin approach to paraphrase detection on the GLUE MRPC validation set. It loads sentence pairs and labels from TableVault, runs the typeform/distilbert-base-uncased-mnli sequence classification model as an NLI-based paraphrase scorer in both directions (sentence1\\u2192sentence2 and sentence2\\u2192sentence1), computes the entailment-minus-contradiction logit margin for each direction, and uses the minimum of the two margins as the final paraphrase score; pairs with positive minimum margin are predicted as paraphrases. The workflow then stores per-example predictions and margins in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, inspects sample predictions and errors, and saves a summary record and notebook-level metadata back to TableVault.\", \"min_direction_margin_mrpc\", \"process_list\"], [\"BASE\", \"This notebook runs a lightweight paraphrase detection experiment on the GLUE MRPC validation set and logs the full workflow to TableVault for traceability. It uses the sentence-transformers/all-MiniLM-L6-v2 model with max_seq_length set to 64 to encode each sentence in an MRPC pair into normalized 384-dimensional embeddings. For each example, it computes cosine similarity between the two sentence embeddings, applies a fixed threshold of 0.80 to predict whether the pair is a paraphrase, and evaluates the results with accuracy, F1, and a classification report. The notebook stores the sentence-level embeddings, prediction records, evaluation summary, and metadata descriptions in TableVault, using OpenAI text embeddings to embed the textual descriptions and properties. It also prints sample predictions and error cases to support qualitative inspection of model behavior.\", \"st_all_minilm_l6_max_seq_len_64_cosine_mrpc\", \"process_list\"], [\"BASE\", \"This notebook runs a paraphrase detection experiment on the GLUE MRPC validation set using the sentence-transformers/all-distilroberta-v1 model. It encodes each sentence in every sentence pair into normalized 768-dimensional embeddings, computes cosine similarity via the dot product, and applies a fixed threshold of 0.72 to predict whether the pair is a paraphrase. The workflow stores sentence embeddings, prediction records, evaluation outputs, and metadata in TableVault, linking all derived artifacts back to the original MRPC validation examples. It then evaluates performance with accuracy, F1, and a classification report, inspects sample predictions and errors, and saves a summary record for the full experiment.\", \"st_all_distilroberta_v1_cosine_threshold_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a simple semantic-similarity baseline for paraphrase detection on the GLUE MRPC validation set. It uses distilbert-base-uncased to encode each sentence, averages the last four hidden layers, applies mean pooling over tokens, and L2-normalizes the resulting sentence embeddings. For each sentence pair, it computes cosine similarity between the two embeddings and converts similarity scores into binary paraphrase predictions using a fixed threshold of 0.85. The workflow loads MRPC examples from TableVault, generates pairwise predictions and similarity scores, computes evaluation metrics including accuracy, F1, and a classification report, inspects example predictions and errors, and stores both per-example outputs and summary results back into TableVault with descriptive metadata.\", \"distilbert_last4_mean_cosine_mrpc\", \"process_list\"]]}"
  }
]
```

### Model Output
**response_id:** `resp_096e90c5623324b10069da5cdb6c48819586731e6eed04123c`

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
    "call_id": "call_cAkCHcizkzINMWcHe4xubppi",
    "arguments": {
      "name": "entailment_logprob_odds_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_cAkCHcizkzINMWcHe4xubppi`

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
| 3698 | 430 | 402 | 1948 | 6.732s | 0.023s |

---

## Turn 2 — `code_description_embedding_search` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5ce231148195b9c5b378519c2dfe`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_cAkCHcizkzINMWcHe4xubppi",
    "output": "{\"ok\": true, \"result\": [\"import torch\\nimport numpy as np\\nfrom datasets import Dataset\\nfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\\nfrom tqdm.auto import tqdm\\n\", \"def get_embeddings(text):\\n    return client.embeddings.create(\\n            input=text,\\n            model=\\\"text-embedding-3-large\\\"\\n        ).data[0].embedding\", \"device = torch.device(\\\"mps\\\" if torch.backends.mps.is_available() else \\\"cpu\\\")\\nprint(\\\"device:\\\", device)\\n\", \"model_name = \\\"typeform/distilbert-base-uncased-mnli\\\"\\n\\ntokenizer = AutoTokenizer.from_pretrained(model_name)\\nmodel = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)\\nmodel.eval()\\n\\nid2label = model.config.id2label\\nlabel2id = model.config.label2id\\n\\ndef _normalize_label(x):\\n    return str(x).strip().lower().replace(\\\"-\\\", \\\"_\\\").replace(\\\" \\\", \\\"_\\\")\\n\\nnorm_label2id = {_normalize_label(k): int(v) for k, v in label2id.items()}\\n\\nif \\\"entailment\\\" in norm_label2id:\\n    entailment_id = norm_label2id[\\\"entailment\\\"]\\nelse:\\n    entailment_id = next(i for i, lab in id2label.items() if _normalize_label(lab) == \\\"entailment\\\")\\n\\nif \\\"contradiction\\\" in norm_label2id:\\n    contradiction_id = norm_label2id[\\\"contradiction\\\"]\\nelse:\\n    contradiction_id = next(i for i, lab in id2label.items() if _normalize_label(lab) == \\\"contradiction\\\")\\n\\nprint(model_name)\\nprint(\\\"id2label:\\\", id2label)\\nprint(\\\"entailment_id:\\\", entailment_id, \\\"contradiction_id:\\\", contradiction_id)\\n\", \"ds = vault.query_item_content(\\\"glue_mrpc_validation\\\")\\nds = Dataset.from_list(ds)\\nprint(ds)\\nprint(ds[0])\\n\\nsent1 = ds[\\\"sentence1\\\"]\\nsent2 = ds[\\\"sentence2\\\"]\\ny_true = np.array(ds[\\\"label\\\"])\\n\\nprint(\\\"num_examples:\\\", len(y_true))\\nprint(\\\"positive_rate:\\\", float(y_true.mean()))\\n\", \"batch_size = 64\\ndir12_scores = []\\ndir21_scores = []\\navg_scores = []\\npreds = []\\n\\nwith torch.no_grad():\\n    for i in tqdm(range(0, len(ds), batch_size)):\\n        batch_s1 = sent1[i:i + batch_size]\\n        batch_s2 = sent2[i:i + batch_size]\\n\\n        enc12 = tokenizer(\\n            batch_s1,\\n            batch_s2,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc21 = tokenizer(\\n            batch_s2,\\n            batch_s1,\\n            padding=True,\\n            truncation=True,\\n            max_length=128,\\n            return_tensors=\\\"pt\\\",\\n        )\\n\\n        enc12 = {k: v.to(device) for k, v in enc12.items()}\\n        enc21 = {k: v.to(device) for k, v in enc21.items()}\\n\\n        logits12 = model(**enc12).logits\\n        logits21 = model(**enc21).logits\\n\\n        log_probs12 = torch.log_softmax(logits12, dim=-1)\\n        log_probs21 = torch.log_softmax(logits21, dim=-1)\\n\\n        score12 = (log_probs12[:, entailment_id] - log_probs12[:, contradiction_id]).detach().cpu().numpy()\\n        score21 = (log_probs21[:, entailment_id] - log_probs21[:, contradiction_id]).detach().cpu().numpy()\\n        score_avg = 0.5 * (score12 + score21)\\n        batch_preds = (score_avg > 0).astype(np.int64)\\n\\n        dir12_scores.extend(score12.tolist())\\n        dir21_scores.extend(score21.tolist())\\n        avg_scores.extend(score_avg.tolist())\\n        preds.extend(batch_preds.tolist())\\n\\ndir12_scores = np.array(dir12_scores)\\ndir21_scores = np.array(dir21_scores)\\navg_scores = np.array(avg_scores)\\ny_pred = np.array(preds)\\n\\nprint(\\\"done\\\")\\nprint(\\\"pred_positive_rate:\\\", float(y_pred.mean()))\\n\", \"vault.create_record_list(\\\"mrpc_entailment_prediction\\\", column_names=[\\\"prediction\\\", \\\"dir12\\\", \\\"dir21\\\"])\\n\\nfor i in range(len(y_pred)):\\n    vault.append_record(\\\"mrpc_entailment_prediction\\\", \\n                        {\\n                            \\\"prediction\\\": int(y_pred[i]),\\n                            \\\"dir12\\\": float(dir12_scores[i]),\\n                            \\\"dir21\\\": float(dir21_scores[i]),\\n                        },\\n                       input_items = {\\n                           \\\"glue_mrpc_validation\\\": [i, i + 1],\\n                       }\\n                       )\\n\\ndescription = \\\"mrpc_entailment_prediction contains per-example prediction outputs for the GLUE MRPC validation set generated with the typeform/distilbert-base-uncased-mnli NLI model. Each record corresponds to one validation pair from glue_mrpc_validation and stores three fields: prediction (binary paraphrase decision obtained by thresholding the averaged score at 0), dir12 (entailment-minus-contradiction log-probability score for sentence1 \\\\u2192 sentence2), and dir21 (the same score for sentence2 \\\\u2192 sentence1). The dataset is aligned one-to-one with the source MRPC examples through input item indexing. Its role in this workflow is to capture the model\\\\u2019s directional entailment-based evidence and final paraphrase prediction for downstream evaluation, error analysis, and summary metric computation.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"mrpc_entailment_prediction\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"method\\\": \\\"mnli entailment vs contradiction logprob odds\\\", \\\"dataset_type\\\": \\\"model predictions\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"input_dataset\\\": \\\"glue_mrpc_validation\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"prediction_target\\\": \\\"mrpc label\\\", \\\"labels\\\": \\\"0=not_paraphrase,1=paraphrase\\\", \\\"features\\\": \\\"prediction,dir12,dir21\\\", \\\"pair_ordering\\\": \\\"sentence1->sentence2 and sentence2->sentence1\\\", \\\"text_fields\\\": \\\"sentence1,sentence2\\\", \\\"domain\\\": \\\"news\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"mrpc_entailment_prediction\\\", cat, embedding, prop)\", \"acc = accuracy_score(y_true, y_pred)\\nf1 = f1_score(y_true, y_pred)\\nreport = classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"])\\nprint({\\\"accuracy\\\": acc, \\\"f1\\\": f1})\\nprint(classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"]))\\n\", \"for i in range(5):\\n    print(\\\"=\\\" * 80)\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"dir12_log_odds:\\\", float(dir12_scores[i]))\\n    print(\\\"dir21_log_odds:\\\", float(dir21_scores[i]))\\n    print(\\\"avg_log_odds:\\\", float(avg_scores[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n\", \"mistakes = np.where(y_true != y_pred)[0][:10]\\nprint(\\\"num_errors:\\\", int((y_true != y_pred).sum()))\\n\\nfor i in mistakes:\\n    print(\\\"=\\\" * 80)\\n    print(\\\"idx:\\\", int(i))\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"dir12_log_odds:\\\", float(dir12_scores[i]))\\n    print(\\\"dir21_log_odds:\\\", float(dir21_scores[i]))\\n    print(\\\"avg_log_odds:\\\", float(avg_scores[i]))\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n\", \"vault.create_record_list(\\\"entailment_logprob_odds_mrpc_summary\\\", column_names=[\\\"accuracy\\\", \\\"f1\\\", \\\"classification_report\\\"])\\n\\n\\nsummary = {\\n    \\\"accuracy\\\": float(acc),\\n    \\\"f1\\\": float(f1),\\n    \\\"classification_report\\\": str(report)\\n}\\n\\nvault.append_record(\\\"entailment_logprob_odds_mrpc_summary\\\", summary,\\n                    input_items = {\\n                        \\\"glue_mrpc_validation\\\": [0, len(ds)],\\n                        \\\"mrpc_entailment_prediction\\\": [0, len(ds)]\\n                    })\\n\\nsummary\\n\\ndescription = \\\"Summary dataset for the MRPC entailment-logprob-odds experiment on the GLUE MRPC validation split. It contains evaluation results for paraphrase predictions produced from a zero-shot NLI model (typeform/distilbert-base-uncased-mnli), where each sentence pair is scored using the average entailment-vs-contradiction log-odds across both input orders. Structure: one record with columns accuracy (float), f1 (float), and classification_report (string). Its role in this workflow is to provide a compact experiment-level summary of model performance, derived from the full per-example outputs in mrpc_entailment_prediction and the ground-truth labels in glue_mrpc_validation.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"entailment_logprob_odds_mrpc_summary\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_type\\\": \\\"evaluation summary\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"source_table\\\": \\\"glue_mrpc_validation\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"input_type\\\": \\\"sentence pair\\\", \\\"labels\\\": \\\"not_paraphrase,paraphrase\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"method\\\": \\\"entailment_minus_contradiction_logprob_odds_avg_bidirectional\\\", \\\"metrics\\\": \\\"accuracy,f1,classification_report\\\", \\\"domain\\\": \\\"news\\\", \\\"process\\\": \\\"entailment_logprob_odds_mrpc\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"entailment_logprob_odds_mrpc_summary\\\", cat, embedding, prop)\\n\\n\", \"description = \\\"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using an NLI model. It loads sentence pairs and labels from TableVault, applies the typeform/distilbert-base-uncased-mnli sequence classification model, and treats paraphrase detection as entailment scoring: for each pair, it computes the log-probability difference between entailment and contradiction for both sentence orders (sentence1\\\\u2192sentence2 and sentence2\\\\u2192sentence1), averages the two directional scores, and predicts paraphrase when the averaged score is positive. The notebook stores per-example predictions and directional entailment log-odds in TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves both dataset-level summaries and notebook-level metadata/descriptions with OpenAI embeddings for documentation and retrieval.\\\" # description of whole notebook\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"entailment_logprob_odds_mrpc\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"approach\\\": \\\"NLI entailment-vs-contradiction log-probability odds\\\", \\\"model\\\": \\\"typeform/distilbert-base-uncased-mnli\\\", \\\"model_family\\\": \\\"DistilBERT MNLI sequence classification\\\", \\\"dataset\\\": \\\"glue/mrpc\\\", \\\"dataset_split\\\": \\\"validation\\\", \\\"input_type\\\": \\\"sentence pair\\\", \\\"prediction_rule\\\": \\\"average bidirectional entailment log-odds > 0\\\", \\\"evaluation\\\": \\\"accuracy, f1-score, classification report\\\", \\\"metrics\\\": \\\"accuracy, f1\\\", \\\"artifacts\\\": \\\"per-example predictions, directional scores, summary metrics\\\", \\\"tracking\\\": \\\"TableVault\\\", \\\"embedding_model\\\": \\\"text-embedding-3-large\\\", \\\"frameworks\\\": \\\"transformers, torch, sklearn, datasets\\\", \\\"process_name\\\": \\\"entailment_logprob_odds_mrpc\\\"} #e.g. model: distilbert-base-uncased-MRPC\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"entailment_logprob_odds_mrpc\\\", cat, embedding, prop)\"]}"
  }
]
```

### Model Output
**response_id:** `resp_096e90c5623324b10069da5ce231148195b9c5b378519c2dfe`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_description_embedding_search",
    "call_id": "call_n1gSYpT6D0HMsoJjUD6grLoD",
    "arguments": {
      "description_text": "MRPC zero-shot prompt order symmetry sentence swapped average prompt yes no baseline summary accuracy"
    }
  }
]
```

### Tool Call
**Tool:** `code_description_embedding_search` | **call_id:** `call_n1gSYpT6D0HMsoJjUD6grLoD`

**Arguments:**
```json
{
  "description_text": "MRPC zero-shot prompt order symmetry sentence swapped average prompt yes no baseline summary accuracy"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    [
      "BASE",
      "This dataset documents a symmetric-order paraphrase evaluation run on the GLUE MRPC validation split using the cross-encoder/quora-distilroberta-base model. It is built from the input dataset glue_mrpc_validation, whose examples contain sentence1, sentence2, and label. For each MRPC pair, the workflow scores both the original order (sentence1, sentence2) and the reversed order (sentence2, sentence1), converts model outputs to positive-class probabilities, averages the two scores, and thresholds the average at 0.5 to produce a final binary prediction.\n\nThe main derived prediction records are stored in distilbert_symmetric_average_prediction with columns y_pred, orig_score, and rev_score, and each record is linked back to the corresponding MRPC validation example. A companion summary record list, quora_cross_encoder_symmetric_average_mrpc_summary, stores aggregate evaluation outputs with columns accuracy, f1, and classification_report across the full validation set.\n\nRole in workflow: this dataset represents the full experiment output for symmetric-average paraphrase detection on MRPC, combining per-example predictions and run-level evaluation metrics for analysis, comparison, and traceability to the original validation inputs.",
      "quora_cross_encoder_symmetric_average_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook runs a zero-shot paraphrase detection experiment on the GLUE MRPC validation set using google/flan-t5-small. It frames each sentence pair as an instruction prompt asking whether the two sentences are paraphrases and scores the first decoder-step logits for the single-token answers yes and no. To reduce prompt bias, it applies contextual calibration by subtracting baseline yes/no logits computed from a null prompt with placeholder inputs (\u201cN/A\u201d, \u201cN/A\u201d), then predicts the label from the higher calibrated logit. The workflow loads MRPC examples from TableVault, generates batch predictions, stores raw and calibrated logits plus final predictions back into TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves summary records and semantic descriptions for the prediction outputs, summary table, and overall notebook process.",
      "flan_t5_contextual_calibrated_yes_no_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using google/flan-t5-small. It frames MRPC as a yes/no text-to-text classification task by prompting the model with two sentences and asking whether they are paraphrases. To reduce order sensitivity, each sentence pair is scored twice\u2014once in the original order and once with the sentences swapped\u2014and the first-token logits for yes and no are averaged across both prompts to produce the final prediction. The notebook loads the validation data from TableVault, runs batched inference with Hugging Face Transformers on MPS or CPU, computes accuracy, F1, and a classification report, inspects example predictions and errors, and stores per-example predictions, logits, summary metrics, and metadata back into TableVault with embedding-based descriptions.",
      "flan_t5_symmetric_prompt_average_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook runs a prompt-based paraphrase detection experiment on the GLUE MRPC validation set using google/flan-t5-small. For each sentence pair, it builds an instruction prompt asking whether the two sentences are paraphrases and scores the full decoder log probability of the candidate answers \u201cyes\u201d and \u201cno\u201d (including EOS). The predicted label is chosen by comparing these two sequence log probabilities.\n\nThe workflow loads MRPC validation data from TableVault, tokenizes prompts, performs batched inference with FLAN-T5, records per-example predictions and yes/no scores, and evaluates performance with accuracy, F1, and a classification report. It also prints sample predictions and error cases for qualitative inspection.\n\nResults are written back to TableVault as a scored prediction record list and a summary record list, with dataset lineage links and embedding-based descriptions/metadata for both the outputs and the overall notebook process.",
      "flan_t5_full_answer_logprob_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook runs a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the NLI model typeform/distilbert-base-uncased-mnli. Its purpose is to score sentence pairs as paraphrase vs. not paraphrase without task-specific fine-tuning, using a neutral-penalized entailment margin. For each MRPC pair, the notebook evaluates both sentence orders, computes an entailment score minus the larger of the contradiction or neutral scores, averages the two directional margins, and predicts paraphrase when the averaged margin is positive. It then stores per-example predictions and scores in TableVault, links them back to the source validation records, computes evaluation metrics including accuracy, F1, and a classification report, inspects example predictions and errors, and saves dataset-, prediction-, summary-, and process-level metadata and semantic descriptions using OpenAI embeddings.",
      "neutral_penalized_margin_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates google/flan-t5-small on the GLUE MRPC validation set for binary paraphrase detection. It loads sentence pairs and labels from TableVault, converts each pair into a natural-language prompt asking whether the two sentences have the same meaning, and runs FLAN-T5 as a seq2seq model on MPS or CPU. Using the decoder prefix Answer:, it compares the next-token logits for yes and no to make a classification without full text generation. The workflow saves per-example predictions and yes/no logits to TableVault, computes accuracy, F1, and a classification report, reviews sample predictions and errors, and stores both dataset-level outputs and experiment summary metadata/descriptions back into TableVault for tracking and retrieval.",
      "flan_t5_answer_prefix_yes_no_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates google/flan-t5-small on the GLUE MRPC validation set for binary paraphrase detection using a prompt-based true/false formulation. It loads sentence pairs and labels from the glue_mrpc_validation dataset stored in TableVault, prompts the model with an instruction asking whether the two sentences are paraphrases, and uses the first decoder-step logits for the single-token verbalizers true and false to make predictions. The workflow records per-example predictions and logits in TableVault, computes summary metrics including accuracy, F1, and a classification report, inspects a few examples and errors, and stores dataset, result, and notebook-level descriptions with OpenAI text embeddings for metadata and retrieval.",
      "flan_t5_true_false_first_step_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a Hugging Face paraphrase detection pipeline on the GLUE MRPC validation set using the textattack/distilbert-base-uncased-MRPC sequence classification model. It loads sentence pairs from TableVault, runs inference in both the original and swapped sentence order, extracts the paraphrase-class probabilities, and averages the two scores to reduce sensitivity to input order before generating final binary predictions. The workflow stores per-example prediction outputs and a summary of accuracy, F1, and the full classification report in TableVault, along with notebook, dataset, and result metadata embeddings for later retrieval and documentation.",
      "hf_pipeline_mrpc_bidirectional_order_average",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli natural language inference model. For each sentence pair, it runs inference in both directions (sentence1\u2192sentence2 and sentence2\u2192sentence1), computes an entailment-versus-contradiction margin for each direction, averages the two margins, and predicts paraphrase only when neither direction is classified as contradiction and the average margin is positive. The notebook stores per-example predictions, directional margins, and gate decisions in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, logs error analysis examples, and saves dataset-, prediction-, summary-, and notebook-level metadata and embeddings for later retrieval and documentation.",
      "consensus_then_avg_margin_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using an NLI model. It loads sentence pairs and labels from TableVault, applies the typeform/distilbert-base-uncased-mnli sequence classification model, and treats paraphrase detection as entailment scoring: for each pair, it computes the log-probability difference between entailment and contradiction for both sentence orders (sentence1\u2192sentence2 and sentence2\u2192sentence1), averages the two directional scores, and predicts paraphrase when the averaged score is positive. The notebook stores per-example predictions and directional entailment log-odds in TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves both dataset-level summaries and notebook-level metadata/descriptions with OpenAI embeddings for documentation and retrieval.",
      "entailment_logprob_odds_mrpc",
      "process_list"
    ]
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 7037 | 233 | 195 | 5287 | 4.789s | 0.562s |

---

## Turn 3 — `code_description_embedding_search` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5ce78690819596256b86e82bf28f`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_n1gSYpT6D0HMsoJjUD6grLoD",
    "output": "{\"ok\": true, \"result\": [[\"BASE\", \"This dataset documents a symmetric-order paraphrase evaluation run on the GLUE MRPC validation split using the cross-encoder/quora-distilroberta-base model. It is built from the input dataset glue_mrpc_validation, whose examples contain sentence1, sentence2, and label. For each MRPC pair, the workflow scores both the original order (sentence1, sentence2) and the reversed order (sentence2, sentence1), converts model outputs to positive-class probabilities, averages the two scores, and thresholds the average at 0.5 to produce a final binary prediction.\\n\\nThe main derived prediction records are stored in distilbert_symmetric_average_prediction with columns y_pred, orig_score, and rev_score, and each record is linked back to the corresponding MRPC validation example. A companion summary record list, quora_cross_encoder_symmetric_average_mrpc_summary, stores aggregate evaluation outputs with columns accuracy, f1, and classification_report across the full validation set.\\n\\nRole in workflow: this dataset represents the full experiment output for symmetric-average paraphrase detection on MRPC, combining per-example predictions and run-level evaluation metrics for analysis, comparison, and traceability to the original validation inputs.\", \"quora_cross_encoder_symmetric_average_mrpc\", \"process_list\"], [\"BASE\", \"This notebook runs a zero-shot paraphrase detection experiment on the GLUE MRPC validation set using google/flan-t5-small. It frames each sentence pair as an instruction prompt asking whether the two sentences are paraphrases and scores the first decoder-step logits for the single-token answers yes and no. To reduce prompt bias, it applies contextual calibration by subtracting baseline yes/no logits computed from a null prompt with placeholder inputs (\\u201cN/A\\u201d, \\u201cN/A\\u201d), then predicts the label from the higher calibrated logit. The workflow loads MRPC examples from TableVault, generates batch predictions, stores raw and calibrated logits plus final predictions back into TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves summary records and semantic descriptions for the prediction outputs, summary table, and overall notebook process.\", \"flan_t5_contextual_calibrated_yes_no_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using google/flan-t5-small. It frames MRPC as a yes/no text-to-text classification task by prompting the model with two sentences and asking whether they are paraphrases. To reduce order sensitivity, each sentence pair is scored twice\\u2014once in the original order and once with the sentences swapped\\u2014and the first-token logits for yes and no are averaged across both prompts to produce the final prediction. The notebook loads the validation data from TableVault, runs batched inference with Hugging Face Transformers on MPS or CPU, computes accuracy, F1, and a classification report, inspects example predictions and errors, and stores per-example predictions, logits, summary metrics, and metadata back into TableVault with embedding-based descriptions.\", \"flan_t5_symmetric_prompt_average_mrpc\", \"process_list\"], [\"BASE\", \"This notebook runs a prompt-based paraphrase detection experiment on the GLUE MRPC validation set using google/flan-t5-small. For each sentence pair, it builds an instruction prompt asking whether the two sentences are paraphrases and scores the full decoder log probability of the candidate answers \\u201cyes\\u201d and \\u201cno\\u201d (including EOS). The predicted label is chosen by comparing these two sequence log probabilities.\\n\\nThe workflow loads MRPC validation data from TableVault, tokenizes prompts, performs batched inference with FLAN-T5, records per-example predictions and yes/no scores, and evaluates performance with accuracy, F1, and a classification report. It also prints sample predictions and error cases for qualitative inspection.\\n\\nResults are written back to TableVault as a scored prediction record list and a summary record list, with dataset lineage links and embedding-based descriptions/metadata for both the outputs and the overall notebook process.\", \"flan_t5_full_answer_logprob_mrpc\", \"process_list\"], [\"BASE\", \"This notebook runs a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the NLI model typeform/distilbert-base-uncased-mnli. Its purpose is to score sentence pairs as paraphrase vs. not paraphrase without task-specific fine-tuning, using a neutral-penalized entailment margin. For each MRPC pair, the notebook evaluates both sentence orders, computes an entailment score minus the larger of the contradiction or neutral scores, averages the two directional margins, and predicts paraphrase when the averaged margin is positive. It then stores per-example predictions and scores in TableVault, links them back to the source validation records, computes evaluation metrics including accuracy, F1, and a classification report, inspects example predictions and errors, and saves dataset-, prediction-, summary-, and process-level metadata and semantic descriptions using OpenAI embeddings.\", \"neutral_penalized_margin_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates google/flan-t5-small on the GLUE MRPC validation set for binary paraphrase detection. It loads sentence pairs and labels from TableVault, converts each pair into a natural-language prompt asking whether the two sentences have the same meaning, and runs FLAN-T5 as a seq2seq model on MPS or CPU. Using the decoder prefix Answer:, it compares the next-token logits for yes and no to make a classification without full text generation. The workflow saves per-example predictions and yes/no logits to TableVault, computes accuracy, F1, and a classification report, reviews sample predictions and errors, and stores both dataset-level outputs and experiment summary metadata/descriptions back into TableVault for tracking and retrieval.\", \"flan_t5_answer_prefix_yes_no_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates google/flan-t5-small on the GLUE MRPC validation set for binary paraphrase detection using a prompt-based true/false formulation. It loads sentence pairs and labels from the glue_mrpc_validation dataset stored in TableVault, prompts the model with an instruction asking whether the two sentences are paraphrases, and uses the first decoder-step logits for the single-token verbalizers true and false to make predictions. The workflow records per-example predictions and logits in TableVault, computes summary metrics including accuracy, F1, and a classification report, inspects a few examples and errors, and stores dataset, result, and notebook-level descriptions with OpenAI text embeddings for metadata and retrieval.\", \"flan_t5_true_false_first_step_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a Hugging Face paraphrase detection pipeline on the GLUE MRPC validation set using the textattack/distilbert-base-uncased-MRPC sequence classification model. It loads sentence pairs from TableVault, runs inference in both the original and swapped sentence order, extracts the paraphrase-class probabilities, and averages the two scores to reduce sensitivity to input order before generating final binary predictions. The workflow stores per-example prediction outputs and a summary of accuracy, F1, and the full classification report in TableVault, along with notebook, dataset, and result metadata embeddings for later retrieval and documentation.\", \"hf_pipeline_mrpc_bidirectional_order_average\", \"process_list\"], [\"BASE\", \"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli natural language inference model. For each sentence pair, it runs inference in both directions (sentence1\\u2192sentence2 and sentence2\\u2192sentence1), computes an entailment-versus-contradiction margin for each direction, averages the two margins, and predicts paraphrase only when neither direction is classified as contradiction and the average margin is positive. The notebook stores per-example predictions, directional margins, and gate decisions in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, logs error analysis examples, and saves dataset-, prediction-, summary-, and notebook-level metadata and embeddings for later retrieval and documentation.\", \"consensus_then_avg_margin_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using an NLI model. It loads sentence pairs and labels from TableVault, applies the typeform/distilbert-base-uncased-mnli sequence classification model, and treats paraphrase detection as entailment scoring: for each pair, it computes the log-probability difference between entailment and contradiction for both sentence orders (sentence1\\u2192sentence2 and sentence2\\u2192sentence1), averages the two directional scores, and predicts paraphrase when the averaged score is positive. The notebook stores per-example predictions and directional entailment log-odds in TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves both dataset-level summaries and notebook-level metadata/descriptions with OpenAI embeddings for documentation and retrieval.\", \"entailment_logprob_odds_mrpc\", \"process_list\"]]}"
  }
]
```

### Model Output
**response_id:** `resp_096e90c5623324b10069da5ce78690819596256b86e82bf28f`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_description_embedding_search",
    "call_id": "call_mt8rzaot5t0EQRijjifdVmNJ",
    "arguments": {
      "description_text": "MRPC single direction baseline paraphrase detection typeform distilbert mnli sentence1 sentence2 only accuracy summary"
    }
  }
]
```

### Tool Call
**Tool:** `code_description_embedding_search` | **call_id:** `call_mt8rzaot5t0EQRijjifdVmNJ`

**Arguments:**
```json
{
  "description_text": "MRPC single direction baseline paraphrase detection typeform distilbert mnli sentence1 sentence2 only accuracy summary"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    [
      "BASE",
      "This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli natural language inference model. For each sentence pair, it runs inference in both directions (sentence1\u2192sentence2 and sentence2\u2192sentence1), computes an entailment-versus-contradiction margin for each direction, averages the two margins, and predicts paraphrase only when neither direction is classified as contradiction and the average margin is positive. The notebook stores per-example predictions, directional margins, and gate decisions in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, logs error analysis examples, and saves dataset-, prediction-, summary-, and notebook-level metadata and embeddings for later retrieval and documentation.",
      "consensus_then_avg_margin_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a simple paraphrase detection baseline on the GLUE MRPC validation set using DistilBERT sentence embeddings. It loads the distilbert-base-uncased model, encodes each sentence in a pair, mean-pools token embeddings while excluding special tokens such as [CLS] and [SEP], L2-normalizes the pooled vectors, and computes cosine similarity between the two sentence embeddings. A fixed similarity threshold of 0.85 is used to predict whether each pair is a paraphrase. The notebook then measures accuracy, F1, and a full classification report, inspects example predictions and errors, and stores per-example predictions, cosine scores, summary metrics, and notebook/process metadata in TableVault with embedding-based descriptions for later retrieval and documentation.",
      "distilbert_no_special_tokens_mean_cosine_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook runs a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the NLI model typeform/distilbert-base-uncased-mnli. Its purpose is to score sentence pairs as paraphrase vs. not paraphrase without task-specific fine-tuning, using a neutral-penalized entailment margin. For each MRPC pair, the notebook evaluates both sentence orders, computes an entailment score minus the larger of the contradiction or neutral scores, averages the two directional margins, and predicts paraphrase when the averaged margin is positive. It then stores per-example predictions and scores in TableVault, links them back to the source validation records, computes evaluation metrics including accuracy, F1, and a classification report, inspects example predictions and errors, and saves dataset-, prediction-, summary-, and process-level metadata and semantic descriptions using OpenAI embeddings.",
      "neutral_penalized_margin_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a directional-margin approach to paraphrase detection on the GLUE MRPC validation set. It loads sentence pairs and labels from TableVault, runs the typeform/distilbert-base-uncased-mnli sequence classification model as an NLI-based paraphrase scorer in both directions (sentence1\u2192sentence2 and sentence2\u2192sentence1), computes the entailment-minus-contradiction logit margin for each direction, and uses the minimum of the two margins as the final paraphrase score; pairs with positive minimum margin are predicted as paraphrases. The workflow then stores per-example predictions and margins in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, inspects sample predictions and errors, and saves a summary record and notebook-level metadata back to TableVault.",
      "min_direction_margin_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a simple paraphrase detection pipeline on the GLUE MRPC validation set using DistilBERT sentence embeddings. It loads sentence pairs and labels from TableVault, encodes each sentence with distilbert-base-uncased, applies masked max pooling over token embeddings, L2-normalizes the pooled vectors, and computes cosine similarity between the two sentence embeddings. A fixed cosine threshold is used to convert similarity scores into binary paraphrase predictions, and the notebook reports accuracy, F1, a full classification report, and example errors. It also records per-example predictions, summary metrics, and workflow metadata back into TableVault, with OpenAI-generated description embeddings for searchable experiment documentation.",
      "distilbert_max_pool_cosine_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a simple semantic-similarity baseline for paraphrase detection on the GLUE MRPC validation set. It uses distilbert-base-uncased to encode each sentence, averages the last four hidden layers, applies mean pooling over tokens, and L2-normalizes the resulting sentence embeddings. For each sentence pair, it computes cosine similarity between the two embeddings and converts similarity scores into binary paraphrase predictions using a fixed threshold of 0.85. The workflow loads MRPC examples from TableVault, generates pairwise predictions and similarity scores, computes evaluation metrics including accuracy, F1, and a classification report, inspects example predictions and errors, and stores both per-example outputs and summary results back into TableVault with descriptive metadata.",
      "distilbert_last4_mean_cosine_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a sentence-transformer baseline for paraphrase detection on the GLUE MRPC validation set and documents the full workflow in TableVault. It uses the sentence-transformers/paraphrase-MiniLM-L3-v2 model to encode each sentence pair into 384-dimensional normalized embeddings, computes cosine similarity via the embedding dot product, and applies a fixed threshold of 0.74 to predict whether the two sentences are paraphrases. The notebook loads sentence1, sentence2, and gold labels from glue_mrpc_validation, generates embeddings for both sentence columns in batches, and stores those embeddings in TableVault with lineage links back to the source records. It then creates a prediction record list, evaluates performance with accuracy, F1, and a full classification report, and prints example predictions plus a small set of misclassified cases for qualitative inspection. In addition, it saves an experiment summary record and attaches natural-language descriptions and metadata properties to the process outputs using OpenAI text embeddings, so the dataset, intermediate artifacts, predictions, and overall experiment can be discovered and understood later.",
      "st_paraphrase_minilm_l3_cosine_threshold_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook runs a paraphrase detection experiment on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli sequence classification model in an NLI-style formulation. For each sentence pair, it scores both input orders (sentence1, sentence2) and (sentence2, sentence1), computes the softmax probability gap between entailment and contradiction for each order, averages the two gaps, and predicts paraphrase when the mean gap is greater than zero. The workflow loads the MRPC validation examples from TableVault, performs batched inference with Hugging Face Transformers and PyTorch, and stores per-example predictions and gap scores back into TableVault with lineage to the source records. It then evaluates the method with accuracy, F1, and a classification report, inspects sample predictions and errors, and saves an experiment summary plus descriptive metadata and embeddings for the prediction table, summary table, and overall notebook process.",
      "softmax_gap_mean_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using an NLI model. It loads sentence pairs and labels from TableVault, applies the typeform/distilbert-base-uncased-mnli sequence classification model, and treats paraphrase detection as entailment scoring: for each pair, it computes the log-probability difference between entailment and contradiction for both sentence orders (sentence1\u2192sentence2 and sentence2\u2192sentence1), averages the two directional scores, and predicts paraphrase when the averaged score is positive. The notebook stores per-example predictions and directional entailment log-odds in TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves both dataset-level summaries and notebook-level metadata/descriptions with OpenAI embeddings for documentation and retrieval.",
      "entailment_logprob_odds_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a Hugging Face paraphrase detection pipeline on the GLUE MRPC validation set using the textattack/distilbert-base-uncased-MRPC sequence classification model. It loads sentence pairs from TableVault, runs inference in both the original and swapped sentence order, extracts the paraphrase-class probabilities, and averages the two scores to reduce sensitivity to input order before generating final binary predictions. The workflow stores per-example prediction outputs and a summary of accuracy, F1, and the full classification report in TableVault, along with notebook, dataset, and result metadata embeddings for later retrieval and documentation.",
      "hf_pipeline_mrpc_bidirectional_order_average",
      "process_list"
    ]
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 9187 | 228 | 184 | 7437 | 3.836s | 0.597s |

---

## Turn 4 — `code_description_embedding_search` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5cebfb8881959a32de1cf8f8a753`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_mt8rzaot5t0EQRijjifdVmNJ",
    "output": "{\"ok\": true, \"result\": [[\"BASE\", \"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli natural language inference model. For each sentence pair, it runs inference in both directions (sentence1\\u2192sentence2 and sentence2\\u2192sentence1), computes an entailment-versus-contradiction margin for each direction, averages the two margins, and predicts paraphrase only when neither direction is classified as contradiction and the average margin is positive. The notebook stores per-example predictions, directional margins, and gate decisions in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, logs error analysis examples, and saves dataset-, prediction-, summary-, and notebook-level metadata and embeddings for later retrieval and documentation.\", \"consensus_then_avg_margin_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a simple paraphrase detection baseline on the GLUE MRPC validation set using DistilBERT sentence embeddings. It loads the distilbert-base-uncased model, encodes each sentence in a pair, mean-pools token embeddings while excluding special tokens such as [CLS] and [SEP], L2-normalizes the pooled vectors, and computes cosine similarity between the two sentence embeddings. A fixed similarity threshold of 0.85 is used to predict whether each pair is a paraphrase. The notebook then measures accuracy, F1, and a full classification report, inspects example predictions and errors, and stores per-example predictions, cosine scores, summary metrics, and notebook/process metadata in TableVault with embedding-based descriptions for later retrieval and documentation.\", \"distilbert_no_special_tokens_mean_cosine_mrpc\", \"process_list\"], [\"BASE\", \"This notebook runs a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the NLI model typeform/distilbert-base-uncased-mnli. Its purpose is to score sentence pairs as paraphrase vs. not paraphrase without task-specific fine-tuning, using a neutral-penalized entailment margin. For each MRPC pair, the notebook evaluates both sentence orders, computes an entailment score minus the larger of the contradiction or neutral scores, averages the two directional margins, and predicts paraphrase when the averaged margin is positive. It then stores per-example predictions and scores in TableVault, links them back to the source validation records, computes evaluation metrics including accuracy, F1, and a classification report, inspects example predictions and errors, and saves dataset-, prediction-, summary-, and process-level metadata and semantic descriptions using OpenAI embeddings.\", \"neutral_penalized_margin_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a directional-margin approach to paraphrase detection on the GLUE MRPC validation set. It loads sentence pairs and labels from TableVault, runs the typeform/distilbert-base-uncased-mnli sequence classification model as an NLI-based paraphrase scorer in both directions (sentence1\\u2192sentence2 and sentence2\\u2192sentence1), computes the entailment-minus-contradiction logit margin for each direction, and uses the minimum of the two margins as the final paraphrase score; pairs with positive minimum margin are predicted as paraphrases. The workflow then stores per-example predictions and margins in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, inspects sample predictions and errors, and saves a summary record and notebook-level metadata back to TableVault.\", \"min_direction_margin_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a simple paraphrase detection pipeline on the GLUE MRPC validation set using DistilBERT sentence embeddings. It loads sentence pairs and labels from TableVault, encodes each sentence with distilbert-base-uncased, applies masked max pooling over token embeddings, L2-normalizes the pooled vectors, and computes cosine similarity between the two sentence embeddings. A fixed cosine threshold is used to convert similarity scores into binary paraphrase predictions, and the notebook reports accuracy, F1, a full classification report, and example errors. It also records per-example predictions, summary metrics, and workflow metadata back into TableVault, with OpenAI-generated description embeddings for searchable experiment documentation.\", \"distilbert_max_pool_cosine_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a simple semantic-similarity baseline for paraphrase detection on the GLUE MRPC validation set. It uses distilbert-base-uncased to encode each sentence, averages the last four hidden layers, applies mean pooling over tokens, and L2-normalizes the resulting sentence embeddings. For each sentence pair, it computes cosine similarity between the two embeddings and converts similarity scores into binary paraphrase predictions using a fixed threshold of 0.85. The workflow loads MRPC examples from TableVault, generates pairwise predictions and similarity scores, computes evaluation metrics including accuracy, F1, and a classification report, inspects example predictions and errors, and stores both per-example outputs and summary results back into TableVault with descriptive metadata.\", \"distilbert_last4_mean_cosine_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a sentence-transformer baseline for paraphrase detection on the GLUE MRPC validation set and documents the full workflow in TableVault. It uses the sentence-transformers/paraphrase-MiniLM-L3-v2 model to encode each sentence pair into 384-dimensional normalized embeddings, computes cosine similarity via the embedding dot product, and applies a fixed threshold of 0.74 to predict whether the two sentences are paraphrases. The notebook loads sentence1, sentence2, and gold labels from glue_mrpc_validation, generates embeddings for both sentence columns in batches, and stores those embeddings in TableVault with lineage links back to the source records. It then creates a prediction record list, evaluates performance with accuracy, F1, and a full classification report, and prints example predictions plus a small set of misclassified cases for qualitative inspection. In addition, it saves an experiment summary record and attaches natural-language descriptions and metadata properties to the process outputs using OpenAI text embeddings, so the dataset, intermediate artifacts, predictions, and overall experiment can be discovered and understood later.\", \"st_paraphrase_minilm_l3_cosine_threshold_mrpc\", \"process_list\"], [\"BASE\", \"This notebook runs a paraphrase detection experiment on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli sequence classification model in an NLI-style formulation. For each sentence pair, it scores both input orders (sentence1, sentence2) and (sentence2, sentence1), computes the softmax probability gap between entailment and contradiction for each order, averages the two gaps, and predicts paraphrase when the mean gap is greater than zero. The workflow loads the MRPC validation examples from TableVault, performs batched inference with Hugging Face Transformers and PyTorch, and stores per-example predictions and gap scores back into TableVault with lineage to the source records. It then evaluates the method with accuracy, F1, and a classification report, inspects sample predictions and errors, and saves an experiment summary plus descriptive metadata and embeddings for the prediction table, summary table, and overall notebook process.\", \"softmax_gap_mean_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using an NLI model. It loads sentence pairs and labels from TableVault, applies the typeform/distilbert-base-uncased-mnli sequence classification model, and treats paraphrase detection as entailment scoring: for each pair, it computes the log-probability difference between entailment and contradiction for both sentence orders (sentence1\\u2192sentence2 and sentence2\\u2192sentence1), averages the two directional scores, and predicts paraphrase when the averaged score is positive. The notebook stores per-example predictions and directional entailment log-odds in TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves both dataset-level summaries and notebook-level metadata/descriptions with OpenAI embeddings for documentation and retrieval.\", \"entailment_logprob_odds_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a Hugging Face paraphrase detection pipeline on the GLUE MRPC validation set using the textattack/distilbert-base-uncased-MRPC sequence classification model. It loads sentence pairs from TableVault, runs inference in both the original and swapped sentence order, extracts the paraphrase-class probabilities, and averages the two scores to reduce sensitivity to input order before generating final binary predictions. The workflow stores per-example prediction outputs and a summary of accuracy, F1, and the full classification report in TableVault, along with notebook, dataset, and result metadata embeddings for later retrieval and documentation.\", \"hf_pipeline_mrpc_bidirectional_order_average\", \"process_list\"]]}"
  }
]
```

### Model Output
**response_id:** `resp_096e90c5623324b10069da5cebfb8881959a32de1cf8f8a753`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_description_embedding_search",
    "call_id": "call_K1DoSUKxvP7cRELCgKmAFzGL",
    "arguments": {
      "description_text": "MRPC original order only zero-shot flan t5 single prompt no swap summary accuracy"
    }
  }
]
```

### Tool Call
**Tool:** `code_description_embedding_search` | **call_id:** `call_K1DoSUKxvP7cRELCgKmAFzGL`

**Arguments:**
```json
{
  "description_text": "MRPC original order only zero-shot flan t5 single prompt no swap summary accuracy"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    [
      "BASE",
      "This notebook runs a zero-shot paraphrase detection experiment on the GLUE MRPC validation set using google/flan-t5-small. It frames each sentence pair as an instruction prompt asking whether the two sentences are paraphrases and scores the first decoder-step logits for the single-token answers yes and no. To reduce prompt bias, it applies contextual calibration by subtracting baseline yes/no logits computed from a null prompt with placeholder inputs (\u201cN/A\u201d, \u201cN/A\u201d), then predicts the label from the higher calibrated logit. The workflow loads MRPC examples from TableVault, generates batch predictions, stores raw and calibrated logits plus final predictions back into TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves summary records and semantic descriptions for the prediction outputs, summary table, and overall notebook process.",
      "flan_t5_contextual_calibrated_yes_no_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates google/flan-t5-small on the GLUE MRPC validation set for binary paraphrase detection. It loads sentence pairs and labels from TableVault, converts each pair into a natural-language prompt asking whether the two sentences have the same meaning, and runs FLAN-T5 as a seq2seq model on MPS or CPU. Using the decoder prefix Answer:, it compares the next-token logits for yes and no to make a classification without full text generation. The workflow saves per-example predictions and yes/no logits to TableVault, computes accuracy, F1, and a classification report, reviews sample predictions and errors, and stores both dataset-level outputs and experiment summary metadata/descriptions back into TableVault for tracking and retrieval.",
      "flan_t5_answer_prefix_yes_no_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using google/flan-t5-small. It frames MRPC as a yes/no text-to-text classification task by prompting the model with two sentences and asking whether they are paraphrases. To reduce order sensitivity, each sentence pair is scored twice\u2014once in the original order and once with the sentences swapped\u2014and the first-token logits for yes and no are averaged across both prompts to produce the final prediction. The notebook loads the validation data from TableVault, runs batched inference with Hugging Face Transformers on MPS or CPU, computes accuracy, F1, and a classification report, inspects example predictions and errors, and stores per-example predictions, logits, summary metrics, and metadata back into TableVault with embedding-based descriptions.",
      "flan_t5_symmetric_prompt_average_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook runs a prompt-based paraphrase detection experiment on the GLUE MRPC validation set using google/flan-t5-small. For each sentence pair, it builds an instruction prompt asking whether the two sentences are paraphrases and scores the full decoder log probability of the candidate answers \u201cyes\u201d and \u201cno\u201d (including EOS). The predicted label is chosen by comparing these two sequence log probabilities.\n\nThe workflow loads MRPC validation data from TableVault, tokenizes prompts, performs batched inference with FLAN-T5, records per-example predictions and yes/no scores, and evaluates performance with accuracy, F1, and a classification report. It also prints sample predictions and error cases for qualitative inspection.\n\nResults are written back to TableVault as a scored prediction record list and a summary record list, with dataset lineage links and embedding-based descriptions/metadata for both the outputs and the overall notebook process.",
      "flan_t5_full_answer_logprob_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates google/flan-t5-small on the GLUE MRPC validation set for binary paraphrase detection using a prompt-based true/false formulation. It loads sentence pairs and labels from the glue_mrpc_validation dataset stored in TableVault, prompts the model with an instruction asking whether the two sentences are paraphrases, and uses the first decoder-step logits for the single-token verbalizers true and false to make predictions. The workflow records per-example predictions and logits in TableVault, computes summary metrics including accuracy, F1, and a classification report, inspects a few examples and errors, and stores dataset, result, and notebook-level descriptions with OpenAI text embeddings for metadata and retrieval.",
      "flan_t5_true_false_first_step_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook runs a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the NLI model typeform/distilbert-base-uncased-mnli. Its purpose is to score sentence pairs as paraphrase vs. not paraphrase without task-specific fine-tuning, using a neutral-penalized entailment margin. For each MRPC pair, the notebook evaluates both sentence orders, computes an entailment score minus the larger of the contradiction or neutral scores, averages the two directional margins, and predicts paraphrase when the averaged margin is positive. It then stores per-example predictions and scores in TableVault, links them back to the source validation records, computes evaluation metrics including accuracy, F1, and a classification report, inspects example predictions and errors, and saves dataset-, prediction-, summary-, and process-level metadata and semantic descriptions using OpenAI embeddings.",
      "neutral_penalized_margin_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a Hugging Face paraphrase detection pipeline on the GLUE MRPC validation set using the textattack/distilbert-base-uncased-MRPC sequence classification model. It loads sentence pairs from TableVault, runs inference in both the original and swapped sentence order, extracts the paraphrase-class probabilities, and averages the two scores to reduce sensitivity to input order before generating final binary predictions. The workflow stores per-example prediction outputs and a summary of accuracy, F1, and the full classification report in TableVault, along with notebook, dataset, and result metadata embeddings for later retrieval and documentation.",
      "hf_pipeline_mrpc_bidirectional_order_average",
      "process_list"
    ],
    [
      "BASE",
      "This dataset documents a symmetric-order paraphrase evaluation run on the GLUE MRPC validation split using the cross-encoder/quora-distilroberta-base model. It is built from the input dataset glue_mrpc_validation, whose examples contain sentence1, sentence2, and label. For each MRPC pair, the workflow scores both the original order (sentence1, sentence2) and the reversed order (sentence2, sentence1), converts model outputs to positive-class probabilities, averages the two scores, and thresholds the average at 0.5 to produce a final binary prediction.\n\nThe main derived prediction records are stored in distilbert_symmetric_average_prediction with columns y_pred, orig_score, and rev_score, and each record is linked back to the corresponding MRPC validation example. A companion summary record list, quora_cross_encoder_symmetric_average_mrpc_summary, stores aggregate evaluation outputs with columns accuracy, f1, and classification_report across the full validation set.\n\nRole in workflow: this dataset represents the full experiment output for symmetric-average paraphrase detection on MRPC, combining per-example predictions and run-level evaluation metrics for analysis, comparison, and traceability to the original validation inputs.",
      "quora_cross_encoder_symmetric_average_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli natural language inference model. For each sentence pair, it runs inference in both directions (sentence1\u2192sentence2 and sentence2\u2192sentence1), computes an entailment-versus-contradiction margin for each direction, averages the two margins, and predicts paraphrase only when neither direction is classified as contradiction and the average margin is positive. The notebook stores per-example predictions, directional margins, and gate decisions in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, logs error analysis examples, and saves dataset-, prediction-, summary-, and notebook-level metadata and embeddings for later retrieval and documentation.",
      "consensus_then_avg_margin_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using an NLI model. It loads sentence pairs and labels from TableVault, applies the typeform/distilbert-base-uncased-mnli sequence classification model, and treats paraphrase detection as entailment scoring: for each pair, it computes the log-probability difference between entailment and contradiction for both sentence orders (sentence1\u2192sentence2 and sentence2\u2192sentence1), averages the two directional scores, and predicts paraphrase when the averaged score is positive. The notebook stores per-example predictions and directional entailment log-odds in TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves both dataset-level summaries and notebook-level metadata/descriptions with OpenAI embeddings for documentation and retrieval.",
      "entailment_logprob_odds_mrpc",
      "process_list"
    ]
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 11263 | 61 | 22 | 9513 | 1.863s | 0.455s |

---

## Turn 5 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5cee4a0481959c1ff16f1cae095b`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_K1DoSUKxvP7cRELCgKmAFzGL",
    "output": "{\"ok\": true, \"result\": [[\"BASE\", \"This notebook runs a zero-shot paraphrase detection experiment on the GLUE MRPC validation set using google/flan-t5-small. It frames each sentence pair as an instruction prompt asking whether the two sentences are paraphrases and scores the first decoder-step logits for the single-token answers yes and no. To reduce prompt bias, it applies contextual calibration by subtracting baseline yes/no logits computed from a null prompt with placeholder inputs (\\u201cN/A\\u201d, \\u201cN/A\\u201d), then predicts the label from the higher calibrated logit. The workflow loads MRPC examples from TableVault, generates batch predictions, stores raw and calibrated logits plus final predictions back into TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves summary records and semantic descriptions for the prediction outputs, summary table, and overall notebook process.\", \"flan_t5_contextual_calibrated_yes_no_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates google/flan-t5-small on the GLUE MRPC validation set for binary paraphrase detection. It loads sentence pairs and labels from TableVault, converts each pair into a natural-language prompt asking whether the two sentences have the same meaning, and runs FLAN-T5 as a seq2seq model on MPS or CPU. Using the decoder prefix Answer:, it compares the next-token logits for yes and no to make a classification without full text generation. The workflow saves per-example predictions and yes/no logits to TableVault, computes accuracy, F1, and a classification report, reviews sample predictions and errors, and stores both dataset-level outputs and experiment summary metadata/descriptions back into TableVault for tracking and retrieval.\", \"flan_t5_answer_prefix_yes_no_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using google/flan-t5-small. It frames MRPC as a yes/no text-to-text classification task by prompting the model with two sentences and asking whether they are paraphrases. To reduce order sensitivity, each sentence pair is scored twice\\u2014once in the original order and once with the sentences swapped\\u2014and the first-token logits for yes and no are averaged across both prompts to produce the final prediction. The notebook loads the validation data from TableVault, runs batched inference with Hugging Face Transformers on MPS or CPU, computes accuracy, F1, and a classification report, inspects example predictions and errors, and stores per-example predictions, logits, summary metrics, and metadata back into TableVault with embedding-based descriptions.\", \"flan_t5_symmetric_prompt_average_mrpc\", \"process_list\"], [\"BASE\", \"This notebook runs a prompt-based paraphrase detection experiment on the GLUE MRPC validation set using google/flan-t5-small. For each sentence pair, it builds an instruction prompt asking whether the two sentences are paraphrases and scores the full decoder log probability of the candidate answers \\u201cyes\\u201d and \\u201cno\\u201d (including EOS). The predicted label is chosen by comparing these two sequence log probabilities.\\n\\nThe workflow loads MRPC validation data from TableVault, tokenizes prompts, performs batched inference with FLAN-T5, records per-example predictions and yes/no scores, and evaluates performance with accuracy, F1, and a classification report. It also prints sample predictions and error cases for qualitative inspection.\\n\\nResults are written back to TableVault as a scored prediction record list and a summary record list, with dataset lineage links and embedding-based descriptions/metadata for both the outputs and the overall notebook process.\", \"flan_t5_full_answer_logprob_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates google/flan-t5-small on the GLUE MRPC validation set for binary paraphrase detection using a prompt-based true/false formulation. It loads sentence pairs and labels from the glue_mrpc_validation dataset stored in TableVault, prompts the model with an instruction asking whether the two sentences are paraphrases, and uses the first decoder-step logits for the single-token verbalizers true and false to make predictions. The workflow records per-example predictions and logits in TableVault, computes summary metrics including accuracy, F1, and a classification report, inspects a few examples and errors, and stores dataset, result, and notebook-level descriptions with OpenAI text embeddings for metadata and retrieval.\", \"flan_t5_true_false_first_step_mrpc\", \"process_list\"], [\"BASE\", \"This notebook runs a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the NLI model typeform/distilbert-base-uncased-mnli. Its purpose is to score sentence pairs as paraphrase vs. not paraphrase without task-specific fine-tuning, using a neutral-penalized entailment margin. For each MRPC pair, the notebook evaluates both sentence orders, computes an entailment score minus the larger of the contradiction or neutral scores, averages the two directional margins, and predicts paraphrase when the averaged margin is positive. It then stores per-example predictions and scores in TableVault, links them back to the source validation records, computes evaluation metrics including accuracy, F1, and a classification report, inspects example predictions and errors, and saves dataset-, prediction-, summary-, and process-level metadata and semantic descriptions using OpenAI embeddings.\", \"neutral_penalized_margin_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a Hugging Face paraphrase detection pipeline on the GLUE MRPC validation set using the textattack/distilbert-base-uncased-MRPC sequence classification model. It loads sentence pairs from TableVault, runs inference in both the original and swapped sentence order, extracts the paraphrase-class probabilities, and averages the two scores to reduce sensitivity to input order before generating final binary predictions. The workflow stores per-example prediction outputs and a summary of accuracy, F1, and the full classification report in TableVault, along with notebook, dataset, and result metadata embeddings for later retrieval and documentation.\", \"hf_pipeline_mrpc_bidirectional_order_average\", \"process_list\"], [\"BASE\", \"This dataset documents a symmetric-order paraphrase evaluation run on the GLUE MRPC validation split using the cross-encoder/quora-distilroberta-base model. It is built from the input dataset glue_mrpc_validation, whose examples contain sentence1, sentence2, and label. For each MRPC pair, the workflow scores both the original order (sentence1, sentence2) and the reversed order (sentence2, sentence1), converts model outputs to positive-class probabilities, averages the two scores, and thresholds the average at 0.5 to produce a final binary prediction.\\n\\nThe main derived prediction records are stored in distilbert_symmetric_average_prediction with columns y_pred, orig_score, and rev_score, and each record is linked back to the corresponding MRPC validation example. A companion summary record list, quora_cross_encoder_symmetric_average_mrpc_summary, stores aggregate evaluation outputs with columns accuracy, f1, and classification_report across the full validation set.\\n\\nRole in workflow: this dataset represents the full experiment output for symmetric-average paraphrase detection on MRPC, combining per-example predictions and run-level evaluation metrics for analysis, comparison, and traceability to the original validation inputs.\", \"quora_cross_encoder_symmetric_average_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli natural language inference model. For each sentence pair, it runs inference in both directions (sentence1\\u2192sentence2 and sentence2\\u2192sentence1), computes an entailment-versus-contradiction margin for each direction, averages the two margins, and predicts paraphrase only when neither direction is classified as contradiction and the average margin is positive. The notebook stores per-example predictions, directional margins, and gate decisions in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, logs error analysis examples, and saves dataset-, prediction-, summary-, and notebook-level metadata and embeddings for later retrieval and documentation.\", \"consensus_then_avg_margin_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using an NLI model. It loads sentence pairs and labels from TableVault, applies the typeform/distilbert-base-uncased-mnli sequence classification model, and treats paraphrase detection as entailment scoring: for each pair, it computes the log-probability difference between entailment and contradiction for both sentence orders (sentence1\\u2192sentence2 and sentence2\\u2192sentence1), averages the two directional scores, and predicts paraphrase when the averaged score is positive. The notebook stores per-example predictions and directional entailment log-odds in TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves both dataset-level summaries and notebook-level metadata/descriptions with OpenAI embeddings for documentation and retrieval.\", \"entailment_logprob_odds_mrpc\", \"process_list\"]]}"
  }
]
```

### Model Output
**response_id:** `resp_096e90c5623324b10069da5cee4a0481959c1ff16f1cae095b`

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
    "call_id": "call_NCbyHVZQqFBaEWEXGpK6UaAR",
    "arguments": {
      "item_name": "entailment_logprob_odds_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_NCbyHVZQqFBaEWEXGpK6UaAR`

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
| 13241 | 635 | 595 | 11491 | 9.070s | 0.022s |

---

## Turn 6 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5cf7600c8195aa1ad95f141d35ec`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_NCbyHVZQqFBaEWEXGpK6UaAR",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.7034313725490197, \"f1\": 0.7729831144465291, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.53      0.63      0.57       129\\n    paraphrase       0.81      0.74      0.77       279\\n\\n      accuracy                           0.70       408\\n     macro avg       0.67      0.68      0.67       408\\n  weighted avg       0.72      0.70      0.71       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_096e90c5623324b10069da5cf7600c8195aa1ad95f141d35ec`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_aX3Or2dY4QenOuEgjPqt5o6w",
    "arguments": {
      "item_name": "min_direction_margin_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_aX3Or2dY4QenOuEgjPqt5o6w`

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
| 14042 | 34 | 0 | 12292 | 1.616s | 0.020s |

---

## Turn 7 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5cf902b08195bfa9f9e7fc66ab78`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_aX3Or2dY4QenOuEgjPqt5o6w",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.5857843137254902, \"f1\": 0.5888077858880778, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.43      0.91      0.58       129\\n    paraphrase       0.92      0.43      0.59       279\\n\\n      accuracy                           0.59       408\\n     macro avg       0.67      0.67      0.59       408\\n  weighted avg       0.76      0.59      0.59       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_096e90c5623324b10069da5cf902b08195bfa9f9e7fc66ab78`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_FrnnWYbqrJHiICZB02qfRpjS",
    "arguments": {
      "item_name": "consensus_then_avg_margin_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_FrnnWYbqrJHiICZB02qfRpjS`

**Arguments:**
```json
{
  "item_name": "consensus_then_avg_margin_mrpc_summary",
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
| 14242 | 36 | 0 | 12492 | 1.413s | 0.015s |

---

## Turn 8 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5cfa71d08195a5cdea7ad93345e8`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_FrnnWYbqrJHiICZB02qfRpjS",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.7009803921568627, \"f1\": 0.769811320754717, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.52      0.64      0.57       129\\n    paraphrase       0.81      0.73      0.77       279\\n\\n      accuracy                           0.70       408\\n     macro avg       0.67      0.68      0.67       408\\n  weighted avg       0.72      0.70      0.71       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_096e90c5623324b10069da5cfa71d08195a5cdea7ad93345e8`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_AlCeSPYPBEGknX0MocbpVsok",
    "arguments": {
      "item_name": "neutral_penalized_margin_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_AlCeSPYPBEGknX0MocbpVsok`

**Arguments:**
```json
{
  "item_name": "neutral_penalized_margin_mrpc_summary",
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
| 14443 | 36 | 0 | 12693 | 1.521s | 0.019s |

---

## Turn 9 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5cfbfb3c81958d0e73446e68eca1`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_AlCeSPYPBEGknX0MocbpVsok",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.5563725490196079, \"f1\": 0.5322997416020672, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.41      0.96      0.58       129\\n    paraphrase       0.95      0.37      0.53       279\\n\\n      accuracy                           0.56       408\\n     macro avg       0.68      0.67      0.56       408\\n  weighted avg       0.78      0.56      0.55       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_096e90c5623324b10069da5cfbfb3c81958d0e73446e68eca1`

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
    "call_id": "call_TAfFua7f2PXijrcRIdxnrZdr",
    "arguments": {
      "item_name": "softmax_gap_mean_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_TAfFua7f2PXijrcRIdxnrZdr`

**Arguments:**
```json
{
  "item_name": "softmax_gap_mean_mrpc_summary",
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
| 14645 | 48 | 11 | 12895 | 1.721s | 0.019s |

---

## Turn 10 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5cfdb72881959a71cd735b9ffde9`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_TAfFua7f2PXijrcRIdxnrZdr",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.7181372549019608, \"f1\": 0.7905282331511839, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.55      0.59      0.57       129\\n    paraphrase       0.80      0.78      0.79       279\\n\\n      accuracy                           0.72       408\\n     macro avg       0.68      0.68      0.68       408\\n  weighted avg       0.72      0.72      0.72       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_096e90c5623324b10069da5cfdb72881959a71cd735b9ffde9`

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
    "call_id": "call_VHbCST3RrF172Fw5q535QIih",
    "arguments": {
      "name": "flan_t5_symmetric_prompt_average_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_VHbCST3RrF172Fw5q535QIih`

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
| 14859 | 204 | 175 | 13109 | 6.228s | 0.019s |

---

## Turn 11 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5d03fbb481959350b27ffdce4855`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_VHbCST3RrF172Fw5q535QIih",
    "output": "{\"ok\": true, \"result\": [\"def get_embeddings(text):\\n    return client.embeddings.create(\\n            input=text,\\n            model=\\\"text-embedding-3-large\\\"\\n        ).data[0].embedding\", \"import torch\\nimport numpy as np\\nfrom datasets import Dataset\\nfrom transformers import AutoTokenizer, AutoModelForSeq2SeqLM\\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\\nfrom tqdm.auto import tqdm\\n\\ndevice = torch.device(\\\"mps\\\" if torch.backends.mps.is_available() else \\\"cpu\\\")\\nprint(\\\"device:\\\", device)\\n\", \"model_name = \\\"google/flan-t5-small\\\"\\n\\ntokenizer = AutoTokenizer.from_pretrained(model_name)\\nmodel = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)\\nmodel.eval()\\n\\nlabel_names = {0: \\\"not_paraphrase\\\", 1: \\\"paraphrase\\\"}\\nprint(model_name)\\nprint(\\\"vocab_size:\\\", model.config.vocab_size)\\n\", \"def get_single_token_id(text):\\n    candidates = [text, text.lower(), f\\\" {text}\\\", f\\\" {text.lower()}\\\"]\\n    for cand in candidates:\\n        ids = tokenizer.encode(cand, add_special_tokens=False)\\n        if len(ids) == 1:\\n            token = tokenizer.convert_ids_to_tokens(ids)[0]\\n            print({\\\"requested\\\": text, \\\"matched_text\\\": cand, \\\"token_id\\\": ids[0], \\\"token\\\": token})\\n            return ids[0]\\n    raise ValueError(f\\\"Could not find a single-token form for {text!r}\\\")\\n\\nyes_token_id = get_single_token_id(\\\"yes\\\")\\nno_token_id = get_single_token_id(\\\"no\\\")\\n\\ndecoder_start_token_id = model.config.decoder_start_token_id\\nif decoder_start_token_id is None:\\n    decoder_start_token_id = tokenizer.pad_token_id\\n\\nprint(\\\"decoder_start_token_id:\\\", decoder_start_token_id)\\nprint(\\\"pad_token_id:\\\", tokenizer.pad_token_id)\\n\", \"ds = vault.query_item_content(\\\"glue_mrpc_validation\\\")\\nds = Dataset.from_list(ds)\\nprint(ds)\\nprint(ds[0])\\n\\nsent1 = ds[\\\"sentence1\\\"]\\nsent2 = ds[\\\"sentence2\\\"]\\ny_true = np.array(ds[\\\"label\\\"])\\n\\nprint(\\\"num_examples:\\\", len(y_true))\\nprint(\\\"positive_rate:\\\", y_true.mean())\\n\", \"def build_prompt(sentence_a, sentence_b):\\n    return (\\n        \\\"Are the following two sentences paraphrases? Answer yes or no.\\\\n\\\"\\n        f\\\"Sentence 1: {sentence_a}\\\\n\\\"\\n        f\\\"Sentence 2: {sentence_b}\\\"\\n    )\\n\\nbatch_size = 32\\npreds = []\\nforward_yes_logits = []\\nforward_no_logits = []\\nswapped_yes_logits = []\\nswapped_no_logits = []\\n\\nwith torch.no_grad():\\n    for i in tqdm(range(0, len(ds), batch_size)):\\n        batch_s1 = sent1[i:i + batch_size]\\n        batch_s2 = sent2[i:i + batch_size]\\n\\n        prompts_forward = [build_prompt(a, b) for a, b in zip(batch_s1, batch_s2)]\\n        prompts_swapped = [build_prompt(b, a) for a, b in zip(batch_s1, batch_s2)]\\n\\n        enc_forward = tokenizer(\\n            prompts_forward,\\n            padding=True,\\n            truncation=True,\\n            max_length=256,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc_swapped = tokenizer(\\n            prompts_swapped,\\n            padding=True,\\n            truncation=True,\\n            max_length=256,\\n            return_tensors=\\\"pt\\\",\\n        )\\n\\n        enc_forward = {k: v.to(device) for k, v in enc_forward.items()}\\n        enc_swapped = {k: v.to(device) for k, v in enc_swapped.items()}\\n\\n        decoder_input_ids = torch.full(\\n            (len(batch_s1), 1),\\n            decoder_start_token_id,\\n            dtype=torch.long,\\n            device=device,\\n        )\\n\\n        logits_forward = model(**enc_forward, decoder_input_ids=decoder_input_ids).logits[:, 0, :]\\n        logits_swapped = model(**enc_swapped, decoder_input_ids=decoder_input_ids).logits[:, 0, :]\\n\\n        yes_forward = logits_forward[:, yes_token_id]\\n        no_forward = logits_forward[:, no_token_id]\\n        yes_swapped = logits_swapped[:, yes_token_id]\\n        no_swapped = logits_swapped[:, no_token_id]\\n\\n        avg_yes_batch = (yes_forward + yes_swapped) / 2.0\\n        avg_no_batch = (no_forward + no_swapped) / 2.0\\n        batch_preds = (avg_yes_batch > avg_no_batch).long().cpu().numpy()\\n\\n        preds.extend(batch_preds.tolist())\\n        forward_yes_logits.extend(yes_forward.cpu().numpy().tolist())\\n        forward_no_logits.extend(no_forward.cpu().numpy().tolist())\\n        swapped_yes_logits.extend(yes_swapped.cpu().numpy().tolist())\\n        swapped_no_logits.extend(no_swapped.cpu().numpy().tolist())\\n\\ny_pred = np.array(preds)\\nforward_yes_logits = np.array(forward_yes_logits)\\nforward_no_logits = np.array(forward_no_logits)\\nswapped_yes_logits = np.array(swapped_yes_logits)\\nswapped_no_logits = np.array(swapped_no_logits)\\navg_yes_logits = (forward_yes_logits + swapped_yes_logits) / 2.0\\navg_no_logits = (forward_no_logits + swapped_no_logits) / 2.0\\n\\nprint(\\\"done\\\")\\n\", \"\\nvault.create_record_list(\\\"google_flan_prediction_swapped\\\", column_names=[\\\"prediction\\\", \\\"yes_logits\\\", \\\"no_logits\\\", \\\"swapped_yes_logits\\\", \\\"swapped_no_logits\\\"])\\n\\nfor i in range(len(y_pred)):\\n    vault.append_record(\\\"google_flan_prediction_swapped\\\", \\n                        {\\n                            \\\"prediction\\\": int(y_pred[i]),\\n                            \\\"yes_logits\\\": float(forward_yes_logits[i]),\\n                            \\\"no_logits\\\": float(forward_no_logits[i]),\\n                            \\\"swapped_yes_logits\\\": float(swapped_yes_logits[i]),\\n                            \\\"swapped_no_logits\\\": float(swapped_no_logits[i]),\\n                        },\\n                       input_items = {\\n                           \\\"glue_mrpc_validation\\\": [i, i + 1],\\n                       }\\n                       )\\n\\ndescription = \\\"Per-example prediction outputs from google/flan-t5-small on the GLUE MRPC validation set using a yes/no paraphrase prompt evaluated in both original and swapped sentence order. Each record is aligned to one input example from glue_mrpc_validation and contains: prediction (binary paraphrase decision after averaging forward and swapped logits), yes_logits (forward-order logit for \\\\u201cyes\\\\u201d), no_logits (forward-order logit for \\\\u201cno\\\\u201d), swapped_yes_logits (swapped-order logit for \\\\u201cyes\\\\u201d), and swapped_no_logits (swapped-order logit for \\\\u201cno\\\\u201d). This dataset is used as the intermediate model-output table in the workflow, supporting order-symmetric paraphrase prediction, error analysis, and computation of final evaluation metrics in the summary dataset.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"google_flan_prediction_swapped\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_role\\\": \\\"model predictions\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"google/flan-t5-small\\\", \\\"prompting\\\": \\\"yes/no question\\\", \\\"inference_method\\\": \\\"symmetric swapped-prompt average\\\", \\\"prediction_type\\\": \\\"binary classification\\\", \\\"output_columns\\\": \\\"prediction, yes_logits, no_logits, swapped_yes_logits, swapped_no_logits\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"google_flan_prediction_swapped\\\", cat, embedding, prop)\", \"acc = accuracy_score(y_true, y_pred)\\nf1 = f1_score(y_true, y_pred)\\nreport = classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"], zero_division=0)\\nprint({\\\"accuracy\\\": acc, \\\"f1\\\": f1})\\nprint(classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"], zero_division=0))\\n\", \"for i in range(5):\\n    print(\\\"=\\\" * 80)\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]), \\\"label:\\\", label_names[int(y_pred[i])])\\n    print(\\n        {\\n            \\\"forward_yes_logit\\\": float(forward_yes_logits[i]),\\n            \\\"forward_no_logit\\\": float(forward_no_logits[i]),\\n            \\\"swapped_yes_logit\\\": float(swapped_yes_logits[i]),\\n            \\\"swapped_no_logit\\\": float(swapped_no_logits[i]),\\n            \\\"avg_yes_logit\\\": float(avg_yes_logits[i]),\\n            \\\"avg_no_logit\\\": float(avg_no_logits[i]),\\n        }\\n    )\\n\", \"mistakes = np.where(y_true != y_pred)[0][:10]\\nprint(\\\"num_errors:\\\", int((y_true != y_pred).sum()))\\n\\nfor i in mistakes:\\n    print(\\\"=\\\" * 80)\\n    print(\\\"idx:\\\", int(i))\\n    print(\\\"sentence1:\\\", sent1[i])\\n    print(\\\"sentence2:\\\", sent2[i])\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n    print(\\n        {\\n            \\\"forward_yes_logit\\\": float(forward_yes_logits[i]),\\n            \\\"forward_no_logit\\\": float(forward_no_logits[i]),\\n            \\\"swapped_yes_logit\\\": float(swapped_yes_logits[i]),\\n            \\\"swapped_no_logit\\\": float(swapped_no_logits[i]),\\n            \\\"avg_yes_logit\\\": float(avg_yes_logits[i]),\\n            \\\"avg_no_logit\\\": float(avg_no_logits[i]),\\n        }\\n    )\\n\", \"\\nvault.create_record_list(\\\"flan_t5_symmetric_prompt_average_mrpc_summary\\\", column_names=[\\\"accuracy\\\", \\\"f1\\\", \\\"classification_report\\\"])\\n\\n\\nsummary = {\\n    \\\"accuracy\\\": float(acc),\\n    \\\"f1\\\": float(f1),\\n    \\\"classification_report\\\": str(report)\\n}\\n\\nvault.append_record(\\\"flan_t5_symmetric_prompt_average_mrpc_summary\\\", summary,\\n                    input_items = {\\n                        \\\"glue_mrpc_validation\\\": [0, len(ds)],\\n                        \\\"google_flan_prediction_swapped\\\": [0, len(ds)]\\n                    })\\n\\nsummary\\n\\ndescription = \\\"Summary dataset for the FLAN-T5 symmetric-prompt MRPC evaluation run. It contains a single aggregate record describing model performance on the full glue_mrpc_validation split, computed from predictions stored in google_flan_prediction_swapped. The fields are: accuracy (float, overall classification accuracy), f1 (float, binary F1 score for paraphrase detection), and classification_report (string, the full scikit-learn classification report with precision, recall, F1, and support for both not_paraphrase and paraphrase classes). Its role in this workflow is to provide a compact experiment-level evaluation artifact that links the source validation examples and prediction outputs to final metrics for the notebook/process flan_t5_symmetric_prompt_average_mrpc.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"flan_t5_symmetric_prompt_average_mrpc_summary\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_type\\\": \\\"evaluation summary\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"google/flan-t5-small\\\", \\\"prompting_method\\\": \\\"symmetric prompt averaging\\\", \\\"prediction_target\\\": \\\"binary yes/no\\\", \\\"metrics\\\": \\\"accuracy,f1,classification_report\\\", \\\"input_items\\\": \\\"glue_mrpc_validation,google_flan_prediction_swapped\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"flan_t5_symmetric_prompt_average_mrpc_summary\\\", cat, embedding, prop)\\n\\n\", \"description = \\\"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using google/flan-t5-small. It frames MRPC as a yes/no text-to-text classification task by prompting the model with two sentences and asking whether they are paraphrases. To reduce order sensitivity, each sentence pair is scored twice\\\\u2014once in the original order and once with the sentences swapped\\\\u2014and the first-token logits for yes and no are averaged across both prompts to produce the final prediction. The notebook loads the validation data from TableVault, runs batched inference with Hugging Face Transformers on MPS or CPU, computes accuracy, F1, and a classification report, inspects example predictions and errors, and stores per-example predictions, logits, summary metrics, and metadata back into TableVault with embedding-based descriptions.\\\" # description of whole notebook\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"flan_t5_symmetric_prompt_average_mrpc\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset\\\": \\\"glue/mrpc\\\", \\\"dataset_split\\\": \\\"validation\\\", \\\"model\\\": \\\"google/flan-t5-small\\\", \\\"model_family\\\": \\\"flan-t5\\\", \\\"inference_method\\\": \\\"zero-shot seq2seq first-token logit comparison\\\", \\\"prompt_strategy\\\": \\\"symmetric prompt averaging with sentence order swap\\\", \\\"labels\\\": \\\"yes/no mapped to paraphrase/not_paraphrase\\\", \\\"evaluation\\\": \\\"accuracy, f1-score, classification_report\\\", \\\"frameworks\\\": \\\"transformers, pytorch, datasets, sklearn\\\", \\\"storage\\\": \\\"tablevault\\\", \\\"database\\\": \\\"arangodb\\\", \\\"embedding_model\\\": \\\"text-embedding-3-large\\\", \\\"process_name\\\": \\\"flan_t5_symmetric_prompt_average_mrpc\\\"} #e.g. model: distilbert-base-uncased-MRPC\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"flan_t5_symmetric_prompt_average_mrpc\\\", cat, embedding, prop)\"]}"
  }
]
```

### Model Output
**response_id:** `resp_096e90c5623324b10069da5d03fbb481959350b27ffdce4855`

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
    "call_id": "call_grwXqfMUX3UJsy5qlBxgJjqO",
    "arguments": {
      "name": "flan_t5_answer_prefix_yes_no_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_grwXqfMUX3UJsy5qlBxgJjqO`

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
| 18325 | 64 | 35 | 16575 | 3.561s | 0.009s |

---

## Turn 12 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5d0790d4819590a94e15bb0ad3d7`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_grwXqfMUX3UJsy5qlBxgJjqO",
    "output": "{\"ok\": true, \"result\": [\"model_name = \\\"google/flan-t5-small\\\"\\n\\ntokenizer = AutoTokenizer.from_pretrained(model_name)\\nmodel = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)\\nmodel.eval()\\n\\ndef get_single_token_id(text):\\n    ids = tokenizer(text, add_special_tokens=False).input_ids\\n    if len(ids) != 1:\\n        raise ValueError(f\\\"{text!r} is not a single token: {ids} -> {tokenizer.convert_ids_to_tokens(ids)}\\\")\\n    return ids[0]\\n\\nyes_token_id = get_single_token_id(\\\"yes\\\")\\nno_token_id = get_single_token_id(\\\"no\\\")\\n\\nanswer_prefix = \\\"Answer:\\\"\\nanswer_prefix_ids = tokenizer(answer_prefix, add_special_tokens=False).input_ids\\ndecoder_start_token_id = model.config.decoder_start_token_id\\n\\nprint(\\\"model:\\\", model_name)\\nprint(\\\"decoder_start_token_id:\\\", decoder_start_token_id)\\nprint(\\\"yes_token_id:\\\", yes_token_id, \\\"token:\\\", tokenizer.convert_ids_to_tokens([yes_token_id]))\\nprint(\\\"no_token_id:\\\", no_token_id, \\\"token:\\\", tokenizer.convert_ids_to_tokens([no_token_id]))\\nprint(\\\"answer_prefix_ids:\\\", answer_prefix_ids, \\\"tokens:\\\", tokenizer.convert_ids_to_tokens(answer_prefix_ids))\\n\", \"ds = vault.query_item_content(\\\"glue_mrpc_validation\\\")\\nds = Dataset.from_list(ds)\\nprint(ds)\\nprint(ds[0])\\n\\nsent1 = ds[\\\"sentence1\\\"]\\nsent2 = ds[\\\"sentence2\\\"]\\ny_true = np.array(ds[\\\"label\\\"])\\n\\nprompts = [\\n    f\\\"Do these two sentences have the same meaning? Sentence 1: {s1} Sentence 2: {s2}\\\"\\n    for s1, s2 in zip(sent1, sent2)\\n]\\n\\nprint(\\\"num_examples:\\\", len(ds))\\nprint(\\\"positive_rate:\\\", float(y_true.mean()))\\nprint(\\\"sample_prompt:\\\", prompts[0])\\n\", \"batch_size = 16\\npreds = []\\nyes_logits_all = []\\nno_logits_all = []\\n\\ndecoder_prefix_ids = [decoder_start_token_id] + answer_prefix_ids\\ndecoder_prefix = torch.tensor(decoder_prefix_ids, dtype=torch.long, device=device)\\n\\nwith torch.no_grad():\\n    for i in tqdm(range(0, len(prompts), batch_size)):\\n        batch_prompts = prompts[i:i + batch_size]\\n\\n        enc = tokenizer(\\n            batch_prompts,\\n            padding=True,\\n            truncation=True,\\n            max_length=256,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc = {k: v.to(device) for k, v in enc.items()}\\n\\n        batch_decoder_input_ids = decoder_prefix.unsqueeze(0).repeat(len(batch_prompts), 1)\\n\\n        logits = model(**enc, decoder_input_ids=batch_decoder_input_ids).logits\\n        step_logits = logits[:, -1, :]\\n\\n        batch_yes_logits = step_logits[:, yes_token_id]\\n        batch_no_logits = step_logits[:, no_token_id]\\n        batch_preds = (batch_yes_logits > batch_no_logits).long().cpu().numpy()\\n\\n        preds.extend(batch_preds.tolist())\\n        yes_logits_all.extend(batch_yes_logits.detach().cpu().numpy().tolist())\\n        no_logits_all.extend(batch_no_logits.detach().cpu().numpy().tolist())\\n\\ny_pred = np.array(preds)\\nyes_logits_all = np.array(yes_logits_all)\\nno_logits_all = np.array(no_logits_all)\\n\\nprint(\\\"done\\\")\\nprint(\\\"num_predicted_positive:\\\", int(y_pred.sum()))\\n\", \"\\nvault.create_record_list(\\\"flan_prediction_and_logit_prefix\\\", column_names=[\\\"prediction\\\",\\\"yes_logits\\\", \\\"no_logits\\\"])\\n\\nfor i in range(len(y_pred)):\\n    vault.append_record(\\\"flan_prediction_and_logit_prefix\\\", \\n                        {\\n                            \\\"prediction\\\": int(y_pred[i]),\\n                            \\\"yes_logits\\\": float(yes_logits_all[i]),\\n                            \\\"no_logits\\\": float(no_logits_all[i]),\\n                        },\\n                       input_items = {\\n                           \\\"glue_mrpc_validation\\\": [i, i + 1],\\n                       }\\n                       )\\n\\ndescription = \\\"This dataset stores per-example inference outputs from google/flan-t5-small on the GLUE MRPC validation set using a prompted yes/no paraphrase detection setup. Each record corresponds to one input pair from glue_mrpc_validation and contains three fields: prediction (binary label, where 1 indicates the model preferred \\\\u201cyes\\\\u201d and 0 indicates it preferred \\\\u201cno\\\\u201d), yes_logits (the decoder logit for the token \\\\u201cyes\\\\u201d at the answer position), and no_logits (the decoder logit for the token \\\\u201cno\\\\u201d at the answer position). Predictions are produced by prompting the model with the two sentences, forcing the decoder prefix \\\\u201cAnswer:\\\\u201d, and selecting the higher of the yes/no logits. In this workflow, the dataset serves as the main model output table for downstream evaluation, error analysis, and summary metric generation, while preserving a row-level link back to the original MRPC validation examples.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"flan_prediction_and_logit_prefix\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_type\\\": \\\"model predictions and logits\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"google/flan-t5-small\\\", \\\"prompt_type\\\": \\\"yes/no question answering\\\", \\\"decoder_prefix\\\": \\\"Answer:\\\", \\\"label_space\\\": \\\"binary\\\", \\\"output_columns\\\": \\\"prediction, yes_logits, no_logits\\\", \\\"input_fields\\\": \\\"sentence1, sentence2\\\", \\\"prediction_target\\\": \\\"paraphrase label\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"flan_prediction_and_logit_prefix\\\", cat, embedding, prop)\", \"acc = accuracy_score(y_true, y_pred)\\nf1 = f1_score(y_true, y_pred)\\nreport = classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"], zero_division=0)\\nprint({\\\"accuracy\\\": acc, \\\"f1\\\": f1})\\nprint(classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"], zero_division=0))\\n\", \"for i in range(5):\\n    print(\\\"=\\\" * 100)\\n    print(\\\"idx:\\\", i)\\n    print(\\\"prompt:\\\", prompts[i])\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n    print(\\\"yes_logit:\\\", float(yes_logits_all[i]), \\\"no_logit:\\\", float(no_logits_all[i]))\\n\\nmistakes = np.where(y_true != y_pred)[0][:10]\\nprint(\\\"num_errors:\\\", int((y_true != y_pred).sum()))\\n\\nfor i in mistakes:\\n    print(\\\"=\\\" * 100)\\n    print(\\\"idx:\\\", int(i))\\n    print(\\\"prompt:\\\", prompts[i])\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n    print(\\\"yes_logit:\\\", float(yes_logits_all[i]), \\\"no_logit:\\\", float(no_logits_all[i]))\\n\", \"vault.create_record_list(\\\"flan_t5_answer_prefix_yes_no_mrpcc_summary\\\", column_names=[\\\"accuracy\\\", \\\"f1\\\", \\\"classification_report\\\"])\\n\\n\\nsummary = {\\n    \\\"accuracy\\\": float(acc),\\n    \\\"f1\\\": float(f1),\\n    \\\"classification_report\\\": str(report)\\n}\\n\\nvault.append_record(\\\"flan_t5_answer_prefix_yes_no_mrpcc_summary\\\", summary,\\n                    input_items = {\\n                        \\\"glue_mrpc_validation\\\": [0, len(ds)],\\n                        \\\"flan_prediction_and_logit_prefix\\\": [0, len(ds)]\\n                    })\\n\\nsummary\\n\\ndescription = \\\"Summary dataset for the FLAN-T5-small MRPC validation run using answer-prefix yes/no scoring. It contains aggregate evaluation results computed from predictions on the glue_mrpc_validation dataset, based on comparing the model\\\\u2019s logits for the tokens \\\\u201cyes\\\\u201d and \\\\u201cno\\\\u201d after the decoder prefix \\\\u201cAnswer:\\\\u201d. The dataset structure has three fields: accuracy (float), f1 (float), and classification_report (string with per-class precision/recall/F1/support). In this workflow, it serves as the experiment-level summary record for the notebook, linking the full validation input set and the per-example prediction/logit dataset flan_prediction_and_logit_prefix into a single compact performance summary.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"flan_t5_answer_prefix_yes_no_mrpcc_summary\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"benchmark\\\": \\\"GLUE\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"google/flan-t5-small\\\", \\\"model_family\\\": \\\"flan-t5\\\", \\\"input_type\\\": \\\"sentence pair\\\", \\\"prompt_type\\\": \\\"yes/no question with answer prefix\\\", \\\"evaluation_method\\\": \\\"decoder next-token yes/no logits\\\", \\\"output_type\\\": \\\"evaluation summary metrics\\\", \\\"metrics\\\": \\\"accuracy,f1,classification_report\\\", \\\"label_space\\\": \\\"not_paraphrase,paraphrase\\\", \\\"prediction_source\\\": \\\"flan_prediction_and_logit_prefix\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"flan_t5_answer_prefix_yes_no_mrpcc_summary\\\", cat, embedding, prop)\\n\\n\\n\", \"description = \\\"This notebook evaluates google/flan-t5-small on the GLUE MRPC validation set for binary paraphrase detection. It loads sentence pairs and labels from TableVault, converts each pair into a natural-language prompt asking whether the two sentences have the same meaning, and runs FLAN-T5 as a seq2seq model on MPS or CPU. Using the decoder prefix Answer:, it compares the next-token logits for yes and no to make a classification without full text generation. The workflow saves per-example predictions and yes/no logits to TableVault, computes accuracy, F1, and a classification report, reviews sample predictions and errors, and stores both dataset-level outputs and experiment summary metadata/descriptions back into TableVault for tracking and retrieval.\\\" # description of whole notebook\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"flan_t5_answer_prefix_yes_no_mrpc\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"problem_type\\\": \\\"binary text classification\\\", \\\"dataset\\\": \\\"glue/mrpc\\\", \\\"dataset_split\\\": \\\"validation\\\", \\\"model\\\": \\\"google/flan-t5-small\\\", \\\"model_family\\\": \\\"FLAN-T5\\\", \\\"framework\\\": \\\"transformers, pytorch\\\", \\\"inference_method\\\": \\\"generative seq2seq yes/no logit comparison\\\", \\\"prompt_format\\\": \\\"instruction prompt with answer prefix 'Answer:'\\\", \\\"label_space\\\": \\\"yes/no\\\", \\\"evaluation\\\": \\\"accuracy, f1-score, classification_report\\\", \\\"artifacts\\\": \\\"predictions, yes_logits, no_logits, summary metrics\\\", \\\"storage\\\": \\\"TableVault\\\", \\\"device\\\": \\\"mps_or_cpu\\\"} #e.g. model: distilbert-base-uncased-MRPC\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"flan_t5_answer_prefix_yes_no_mrpc\\\", cat, embedding, prop)\"]}"
  }
]
```

### Model Output
**response_id:** `resp_096e90c5623324b10069da5d0790d4819590a94e15bb0ad3d7`

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
    "call_id": "call_WVMH39QIPpj1SV1B5baKwleF",
    "arguments": {
      "item_name": "flan_t5_symmetric_prompt_average_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_WVMH39QIPpj1SV1B5baKwleF`

**Arguments:**
```json
{
  "item_name": "flan_t5_symmetric_prompt_average_mrpc_summary",
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
| 21024 | 262 | 221 | 19274 | 4.807s | 0.013s |

---

## Turn 13 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5d0c59708195972ba443176b8db4`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_WVMH39QIPpj1SV1B5baKwleF",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.7377450980392157, \"f1\": 0.8065099457504521, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.58      0.60      0.59       129\\n    paraphrase       0.81      0.80      0.81       279\\n\\n      accuracy                           0.74       408\\n     macro avg       0.70      0.70      0.70       408\\n  weighted avg       0.74      0.74      0.74       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_096e90c5623324b10069da5d0c59708195972ba443176b8db4`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_vhqMJVUk9hDCGX5C5fFLMAix",
    "arguments": {
      "item_name": "flan_t5_answer_prefix_yes_no_mrpcc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_vhqMJVUk9hDCGX5C5fFLMAix`

**Arguments:**
```json
{
  "item_name": "flan_t5_answer_prefix_yes_no_mrpcc_summary",
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
| 21451 | 40 | 0 | 19701 | 3.162s | 0.013s |

---

## Turn 14 — `get_code` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5d0f895c81959966268f7a6d648b`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_vhqMJVUk9hDCGX5C5fFLMAix",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.6372549019607843, \"f1\": 0.6877637130801688, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.46      0.75      0.57       129\\n    paraphrase       0.84      0.58      0.69       279\\n\\n      accuracy                           0.64       408\\n     macro avg       0.65      0.67      0.63       408\\n  weighted avg       0.72      0.64      0.65       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_096e90c5623324b10069da5d0f895c81959966268f7a6d648b`

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
    "call_id": "call_HSHluAgvBOD7quNTH5YawkPi",
    "arguments": {
      "name": "flan_t5_contextual_calibrated_yes_no_mrpc"
    }
  }
]
```

### Tool Call
**Tool:** `get_code` | **call_id:** `call_HSHluAgvBOD7quNTH5YawkPi`

**Arguments:**
```json
{
  "name": "flan_t5_contextual_calibrated_yes_no_mrpc"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    "def get_embeddings(text):\n    return client.embeddings.create(\n            input=text,\n            model=\"text-embedding-3-large\"\n        ).data[0].embedding",
    "import torch\nimport numpy as np\nfrom datasets import Dataset\nfrom transformers import AutoTokenizer, AutoModelForSeq2SeqLM\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\nfrom tqdm.auto import tqdm\n\ndevice = torch.device(\"mps\" if torch.backends.mps.is_available() else \"cpu\")\nprint(\"device:\", device)\n",
    "model_name = \"google/flan-t5-small\"\n\ntokenizer = AutoTokenizer.from_pretrained(model_name)\nmodel = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)\nmodel.eval()\n\ndecoder_start_token_id = model.config.decoder_start_token_id\nif decoder_start_token_id is None:\n    decoder_start_token_id = tokenizer.pad_token_id\n\nyes_ids = tokenizer.encode(\"yes\", add_special_tokens=False)\nno_ids = tokenizer.encode(\"no\", add_special_tokens=False)\n\nprint(\"model_name:\", model_name)\nprint(\"decoder_start_token_id:\", decoder_start_token_id)\nprint(\"yes_ids:\", yes_ids, \"tokens:\", tokenizer.convert_ids_to_tokens(yes_ids))\nprint(\"no_ids:\", no_ids, \"tokens:\", tokenizer.convert_ids_to_tokens(no_ids))\n\nassert len(yes_ids) == 1, f\"'yes' must be a single token, got {yes_ids}\"\nassert len(no_ids) == 1, f\"'no' must be a single token, got {no_ids}\"\n\nyes_id = yes_ids[0]\nno_id = no_ids[0]\n",
    "prompt_template = (\n    \"Determine whether the following two sentences are paraphrases. \"\n    \"Answer yes or no.\\n\"\n    \"Sentence 1: {sentence1}\\n\"\n    \"Sentence 2: {sentence2}\\n\"\n    \"Answer:\"\n)\n\ndef build_prompt(sentence1, sentence2):\n    return prompt_template.format(sentence1=sentence1, sentence2=sentence2)\n\ncalibration_prompt = build_prompt(\"N/A\", \"N/A\")\nprint(calibration_prompt)\n",
    "cal_enc = tokenizer(\n    [calibration_prompt],\n    padding=True,\n    truncation=True,\n    max_length=256,\n    return_tensors=\"pt\",\n)\ncal_enc = {k: v.to(device) for k, v in cal_enc.items()}\ncal_decoder_input_ids = torch.full(\n    (1, 1),\n    decoder_start_token_id,\n    dtype=torch.long,\n    device=device,\n)\n\nwith torch.no_grad():\n    cal_logits = model(**cal_enc, decoder_input_ids=cal_decoder_input_ids).logits\n\nbaseline_yes_logit = float(cal_logits[0, 0, yes_id].detach().cpu())\nbaseline_no_logit = float(cal_logits[0, 0, no_id].detach().cpu())\n\nprint({\"baseline_yes_logit\": baseline_yes_logit, \"baseline_no_logit\": baseline_no_logit})\n",
    "ds = vault.query_item_content(\"glue_mrpc_validation\")\nds = Dataset.from_list(ds)\nprint(ds)\nprint(ds[0])\n\nsent1 = ds[\"sentence1\"]\nsent2 = ds[\"sentence2\"]\ny_true = np.array(ds[\"label\"])\nprompts = [build_prompt(s1, s2) for s1, s2 in zip(sent1, sent2)]\n\nprint(\"num_examples:\", len(ds))\nprint(\"positive_rate:\", y_true.mean())\nprint(\"first_prompt:\\n\", prompts[0])\n",
    "batch_size = 32\nraw_yes_logits = []\nraw_no_logits = []\ncal_yes_logits = []\ncal_no_logits = []\npreds = []\n\nwith torch.no_grad():\n    for i in tqdm(range(0, len(prompts), batch_size)):\n        batch_prompts = prompts[i:i + batch_size]\n\n        enc = tokenizer(\n            batch_prompts,\n            padding=True,\n            truncation=True,\n            max_length=256,\n            return_tensors=\"pt\",\n        )\n        enc = {k: v.to(device) for k, v in enc.items()}\n\n        batch_decoder_input_ids = torch.full(\n            (len(batch_prompts), 1),\n            decoder_start_token_id,\n            dtype=torch.long,\n            device=device,\n        )\n\n        logits = model(**enc, decoder_input_ids=batch_decoder_input_ids).logits[:, 0, :]\n\n        batch_yes = logits[:, yes_id].detach().cpu().numpy()\n        batch_no = logits[:, no_id].detach().cpu().numpy()\n\n        batch_cal_yes = batch_yes - baseline_yes_logit\n        batch_cal_no = batch_no - baseline_no_logit\n        batch_preds = (batch_cal_yes > batch_cal_no).astype(np.int64)\n\n        raw_yes_logits.extend(batch_yes.tolist())\n        raw_no_logits.extend(batch_no.tolist())\n        cal_yes_logits.extend(batch_cal_yes.tolist())\n        cal_no_logits.extend(batch_cal_no.tolist())\n        preds.extend(batch_preds.tolist())\n\ny_pred = np.array(preds)\nraw_yes_logits = np.array(raw_yes_logits)\nraw_no_logits = np.array(raw_no_logits)\ncal_yes_logits = np.array(cal_yes_logits)\ncal_no_logits = np.array(cal_no_logits)\n\nprint(\"done\")\n",
    "\nvault.create_record_list(\"flan_prediction_logit_calibrated\", column_names=[\"prediction\",\"raw_yes_logits\", \"raw_no_logits\", \"cal_yes_logits\", \"cal_no_logits\"])\n\nfor i in range(len(y_pred)):\n    vault.append_record(\"flan_prediction_logit_calibrated\", \n                        {\n                            \"prediction\": int(y_pred[i]),\n                            \"raw_yes_logits\": float(raw_yes_logits[i]),\n                            \"raw_no_logits\": float(raw_no_logits[i]),\n                            \"cal_yes_logits\": float(cal_yes_logits[i]),\n                            \"cal_no_logits\": float(cal_no_logits[i]),\n                        },\n                       input_items = {\n                           \"glue_mrpc_validation\": [i, i + 1],\n                       }\n                       )\n\ndescription = \"Per-example prediction dataset for the GLUE MRPC validation set produced by prompting google/flan-t5-small with a yes/no paraphrase question and applying contextual calibration. Each record corresponds to one input sentence pair from glue_mrpc_validation and stores the model\\u2019s binary prediction (1 = paraphrase/yes, 0 = not paraphrase/no), the raw first-step logits for the yes and no tokens (raw_yes_logits, raw_no_logits), and the calibrated logits after subtracting baseline logits from a null calibration prompt (cal_yes_logits, cal_no_logits). This record list is the main intermediate output of the workflow: it preserves calibrated model scores for each example, supports error analysis and inspection, and is used to compute the downstream summary metrics in flan_t5_contextual_calibrated_yes_no_mrpc_summary.\"\nembedding = get_embeddings(description)\nvault.create_description(\"flan_prediction_logit_calibrated\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"dataset_role\": \"model prediction logits\", \"source\": \"glue/mrpc\", \"source_split\": \"validation\", \"size\": \"408\", \"model\": \"google/flan-t5-small\", \"prompt_type\": \"yes/no instruction prompt\", \"calibration\": \"contextual logit calibration\", \"label_space\": \"yes/no\", \"prediction_target\": \"paraphrase label\", \"input_fields\": \"sentence1,sentence2\", \"output_fields\": \"prediction,raw_yes_logits,raw_no_logits,cal_yes_logits,cal_no_logits\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"flan_prediction_logit_calibrated\", cat, embedding, prop)",
    "acc = accuracy_score(y_true, y_pred)\nf1 = f1_score(y_true, y_pred)\nreport = classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"])\nprint({\"accuracy\": acc, \"f1\": f1})\nprint(classification_report(y_true, y_pred, target_names=[\"not_paraphrase\", \"paraphrase\"]))\n",
    "for i in range(5):\n    print(\"=\" * 80)\n    print(\"idx:\", i)\n    print(prompts[i])\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]))\n    print(\"raw_yes_logit:\", float(raw_yes_logits[i]))\n    print(\"raw_no_logit:\", float(raw_no_logits[i]))\n    print(\"calibrated_yes_logit:\", float(cal_yes_logits[i]))\n    print(\"calibrated_no_logit:\", float(cal_no_logits[i]))\n",
    "mistakes = np.where(y_true != y_pred)[0][:10]\nprint(\"num_errors:\", int((y_true != y_pred).sum()))\n\nfor i in mistakes:\n    print(\"=\" * 80)\n    print(\"idx:\", int(i))\n    print(prompts[i])\n    print(\"true:\", int(y_true[i]), \"pred:\", int(y_pred[i]))\n    print(\"raw_yes_logit:\", float(raw_yes_logits[i]))\n    print(\"raw_no_logit:\", float(raw_no_logits[i]))\n    print(\"calibrated_yes_logit:\", float(cal_yes_logits[i]))\n    print(\"calibrated_no_logit:\", float(cal_no_logits[i]))\n\n\nvault.create_record_list(\"flan_t5_contextual_calibrated_yes_no_mrpc_summary\", column_names=[\"accuracy\", \"f1\", \"classification_report\"])\n\n\nsummary = {\n    \"accuracy\": float(acc),\n    \"f1\": float(f1),\n    \"classification_report\": str(report)\n}\n\nvault.append_record(\"flan_t5_contextual_calibrated_yes_no_mrpc_summary\", summary,\n                    input_items = {\n                        \"glue_mrpc_validation\": [0, len(ds)],\n                        \"flan_prediction_logit_calibrated\": [0, len(ds)]\n                    })\n\nsummary\n\ndescription = \"Aggregate evaluation summary for the flan-t5-small contextual yes/no paraphrase classifier on the GLUE MRPC validation set after logit calibration. This dataset is a record list with one summary record containing the fields: accuracy (float), f1 (float), and classification_report (string with per-class precision/recall/F1 and support for not_paraphrase and paraphrase). It is produced after generating calibrated predictions in flan_prediction_logit_calibrated and compares those predictions against the ground-truth labels in glue_mrpc_validation. Its role in this workflow is to store run-level performance metrics for the full validation set, providing a compact summary of model quality for this notebook execution.\"\nembedding = get_embeddings(description)\nvault.create_description(\"flan_t5_contextual_calibrated_yes_no_mrpc_summary\", description, embedding)\n\nproperties = {\"artifact_type\": \"evaluation summary\", \"task\": \"paraphrase detection\", \"benchmark\": \"GLUE\", \"source\": \"glue/mrpc\", \"input_dataset\": \"glue_mrpc_validation\", \"split\": \"validation\", \"size\": \"408\", \"model\": \"google/flan-t5-small\", \"prompt_format\": \"yes/no seq2seq\", \"calibration\": \"contextual logit calibration\", \"label_space\": \"binary\", \"metrics\": \"accuracy,f1,classification_report\"} #e.g. task: paraphrase detection\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"flan_t5_contextual_calibrated_yes_no_mrpc_summary\", cat, embedding, prop)\n\n\n",
    "description = \"This notebook runs a zero-shot paraphrase detection experiment on the GLUE MRPC validation set using google/flan-t5-small. It frames each sentence pair as an instruction prompt asking whether the two sentences are paraphrases and scores the first decoder-step logits for the single-token answers yes and no. To reduce prompt bias, it applies contextual calibration by subtracting baseline yes/no logits computed from a null prompt with placeholder inputs (\\u201cN/A\\u201d, \\u201cN/A\\u201d), then predicts the label from the higher calibrated logit. The workflow loads MRPC examples from TableVault, generates batch predictions, stores raw and calibrated logits plus final predictions back into TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves summary records and semantic descriptions for the prediction outputs, summary table, and overall notebook process.\" # description of whole notebook\nembedding = get_embeddings(description)\nvault.create_description(\"flan_t5_contextual_calibrated_yes_no_mrpc\", description, embedding)\n\nproperties = {\"task\": \"paraphrase detection\", \"problem_type\": \"binary text classification\", \"method\": \"zero-shot seq2seq yes/no prompting with contextual calibration\", \"calibration\": \"contextual calibration using baseline logits from N/A prompt\", \"model\": \"google/flan-t5-small\", \"model_family\": \"FLAN-T5\", \"dataset\": \"glue/mrpc\", \"dataset_split\": \"validation\", \"input_format\": \"sentence pair prompt\", \"label_space\": \"yes/no\", \"prediction_signal\": \"first-decoder-step logits for yes and no tokens\", \"evaluation\": \"accuracy, f1-score, classification report\", \"frameworks\": \"PyTorch, Hugging Face Transformers, Datasets, scikit-learn\", \"tracking\": \"TableVault\", \"embedding_model\": \"text-embedding-3-large\", \"artifacts\": \"per-example calibrated logits and summary metrics\", \"process_name\": \"flan_t5_contextual_calibrated_yes_no_mrpc\"} #e.g. model: distilbert-base-uncased-MRPC\n\nfor prop, cat in properties.items():\n    embedding = get_embeddings(prop)\n    vault.create_description(\"flan_t5_contextual_calibrated_yes_no_mrpc\", cat, embedding, prop)"
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 21657 | 54 | 22 | 19907 | 1.929s | 0.010s |

---

## Turn 15 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5d117adc8195b171e6f7e8b73394`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_HSHluAgvBOD7quNTH5YawkPi",
    "output": "{\"ok\": true, \"result\": [\"def get_embeddings(text):\\n    return client.embeddings.create(\\n            input=text,\\n            model=\\\"text-embedding-3-large\\\"\\n        ).data[0].embedding\", \"import torch\\nimport numpy as np\\nfrom datasets import Dataset\\nfrom transformers import AutoTokenizer, AutoModelForSeq2SeqLM\\nfrom sklearn.metrics import accuracy_score, f1_score, classification_report\\nfrom tqdm.auto import tqdm\\n\\ndevice = torch.device(\\\"mps\\\" if torch.backends.mps.is_available() else \\\"cpu\\\")\\nprint(\\\"device:\\\", device)\\n\", \"model_name = \\\"google/flan-t5-small\\\"\\n\\ntokenizer = AutoTokenizer.from_pretrained(model_name)\\nmodel = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)\\nmodel.eval()\\n\\ndecoder_start_token_id = model.config.decoder_start_token_id\\nif decoder_start_token_id is None:\\n    decoder_start_token_id = tokenizer.pad_token_id\\n\\nyes_ids = tokenizer.encode(\\\"yes\\\", add_special_tokens=False)\\nno_ids = tokenizer.encode(\\\"no\\\", add_special_tokens=False)\\n\\nprint(\\\"model_name:\\\", model_name)\\nprint(\\\"decoder_start_token_id:\\\", decoder_start_token_id)\\nprint(\\\"yes_ids:\\\", yes_ids, \\\"tokens:\\\", tokenizer.convert_ids_to_tokens(yes_ids))\\nprint(\\\"no_ids:\\\", no_ids, \\\"tokens:\\\", tokenizer.convert_ids_to_tokens(no_ids))\\n\\nassert len(yes_ids) == 1, f\\\"'yes' must be a single token, got {yes_ids}\\\"\\nassert len(no_ids) == 1, f\\\"'no' must be a single token, got {no_ids}\\\"\\n\\nyes_id = yes_ids[0]\\nno_id = no_ids[0]\\n\", \"prompt_template = (\\n    \\\"Determine whether the following two sentences are paraphrases. \\\"\\n    \\\"Answer yes or no.\\\\n\\\"\\n    \\\"Sentence 1: {sentence1}\\\\n\\\"\\n    \\\"Sentence 2: {sentence2}\\\\n\\\"\\n    \\\"Answer:\\\"\\n)\\n\\ndef build_prompt(sentence1, sentence2):\\n    return prompt_template.format(sentence1=sentence1, sentence2=sentence2)\\n\\ncalibration_prompt = build_prompt(\\\"N/A\\\", \\\"N/A\\\")\\nprint(calibration_prompt)\\n\", \"cal_enc = tokenizer(\\n    [calibration_prompt],\\n    padding=True,\\n    truncation=True,\\n    max_length=256,\\n    return_tensors=\\\"pt\\\",\\n)\\ncal_enc = {k: v.to(device) for k, v in cal_enc.items()}\\ncal_decoder_input_ids = torch.full(\\n    (1, 1),\\n    decoder_start_token_id,\\n    dtype=torch.long,\\n    device=device,\\n)\\n\\nwith torch.no_grad():\\n    cal_logits = model(**cal_enc, decoder_input_ids=cal_decoder_input_ids).logits\\n\\nbaseline_yes_logit = float(cal_logits[0, 0, yes_id].detach().cpu())\\nbaseline_no_logit = float(cal_logits[0, 0, no_id].detach().cpu())\\n\\nprint({\\\"baseline_yes_logit\\\": baseline_yes_logit, \\\"baseline_no_logit\\\": baseline_no_logit})\\n\", \"ds = vault.query_item_content(\\\"glue_mrpc_validation\\\")\\nds = Dataset.from_list(ds)\\nprint(ds)\\nprint(ds[0])\\n\\nsent1 = ds[\\\"sentence1\\\"]\\nsent2 = ds[\\\"sentence2\\\"]\\ny_true = np.array(ds[\\\"label\\\"])\\nprompts = [build_prompt(s1, s2) for s1, s2 in zip(sent1, sent2)]\\n\\nprint(\\\"num_examples:\\\", len(ds))\\nprint(\\\"positive_rate:\\\", y_true.mean())\\nprint(\\\"first_prompt:\\\\n\\\", prompts[0])\\n\", \"batch_size = 32\\nraw_yes_logits = []\\nraw_no_logits = []\\ncal_yes_logits = []\\ncal_no_logits = []\\npreds = []\\n\\nwith torch.no_grad():\\n    for i in tqdm(range(0, len(prompts), batch_size)):\\n        batch_prompts = prompts[i:i + batch_size]\\n\\n        enc = tokenizer(\\n            batch_prompts,\\n            padding=True,\\n            truncation=True,\\n            max_length=256,\\n            return_tensors=\\\"pt\\\",\\n        )\\n        enc = {k: v.to(device) for k, v in enc.items()}\\n\\n        batch_decoder_input_ids = torch.full(\\n            (len(batch_prompts), 1),\\n            decoder_start_token_id,\\n            dtype=torch.long,\\n            device=device,\\n        )\\n\\n        logits = model(**enc, decoder_input_ids=batch_decoder_input_ids).logits[:, 0, :]\\n\\n        batch_yes = logits[:, yes_id].detach().cpu().numpy()\\n        batch_no = logits[:, no_id].detach().cpu().numpy()\\n\\n        batch_cal_yes = batch_yes - baseline_yes_logit\\n        batch_cal_no = batch_no - baseline_no_logit\\n        batch_preds = (batch_cal_yes > batch_cal_no).astype(np.int64)\\n\\n        raw_yes_logits.extend(batch_yes.tolist())\\n        raw_no_logits.extend(batch_no.tolist())\\n        cal_yes_logits.extend(batch_cal_yes.tolist())\\n        cal_no_logits.extend(batch_cal_no.tolist())\\n        preds.extend(batch_preds.tolist())\\n\\ny_pred = np.array(preds)\\nraw_yes_logits = np.array(raw_yes_logits)\\nraw_no_logits = np.array(raw_no_logits)\\ncal_yes_logits = np.array(cal_yes_logits)\\ncal_no_logits = np.array(cal_no_logits)\\n\\nprint(\\\"done\\\")\\n\", \"\\nvault.create_record_list(\\\"flan_prediction_logit_calibrated\\\", column_names=[\\\"prediction\\\",\\\"raw_yes_logits\\\", \\\"raw_no_logits\\\", \\\"cal_yes_logits\\\", \\\"cal_no_logits\\\"])\\n\\nfor i in range(len(y_pred)):\\n    vault.append_record(\\\"flan_prediction_logit_calibrated\\\", \\n                        {\\n                            \\\"prediction\\\": int(y_pred[i]),\\n                            \\\"raw_yes_logits\\\": float(raw_yes_logits[i]),\\n                            \\\"raw_no_logits\\\": float(raw_no_logits[i]),\\n                            \\\"cal_yes_logits\\\": float(cal_yes_logits[i]),\\n                            \\\"cal_no_logits\\\": float(cal_no_logits[i]),\\n                        },\\n                       input_items = {\\n                           \\\"glue_mrpc_validation\\\": [i, i + 1],\\n                       }\\n                       )\\n\\ndescription = \\\"Per-example prediction dataset for the GLUE MRPC validation set produced by prompting google/flan-t5-small with a yes/no paraphrase question and applying contextual calibration. Each record corresponds to one input sentence pair from glue_mrpc_validation and stores the model\\\\u2019s binary prediction (1 = paraphrase/yes, 0 = not paraphrase/no), the raw first-step logits for the yes and no tokens (raw_yes_logits, raw_no_logits), and the calibrated logits after subtracting baseline logits from a null calibration prompt (cal_yes_logits, cal_no_logits). This record list is the main intermediate output of the workflow: it preserves calibrated model scores for each example, supports error analysis and inspection, and is used to compute the downstream summary metrics in flan_t5_contextual_calibrated_yes_no_mrpc_summary.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"flan_prediction_logit_calibrated\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"dataset_role\\\": \\\"model prediction logits\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"source_split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"google/flan-t5-small\\\", \\\"prompt_type\\\": \\\"yes/no instruction prompt\\\", \\\"calibration\\\": \\\"contextual logit calibration\\\", \\\"label_space\\\": \\\"yes/no\\\", \\\"prediction_target\\\": \\\"paraphrase label\\\", \\\"input_fields\\\": \\\"sentence1,sentence2\\\", \\\"output_fields\\\": \\\"prediction,raw_yes_logits,raw_no_logits,cal_yes_logits,cal_no_logits\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"flan_prediction_logit_calibrated\\\", cat, embedding, prop)\", \"acc = accuracy_score(y_true, y_pred)\\nf1 = f1_score(y_true, y_pred)\\nreport = classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"])\\nprint({\\\"accuracy\\\": acc, \\\"f1\\\": f1})\\nprint(classification_report(y_true, y_pred, target_names=[\\\"not_paraphrase\\\", \\\"paraphrase\\\"]))\\n\", \"for i in range(5):\\n    print(\\\"=\\\" * 80)\\n    print(\\\"idx:\\\", i)\\n    print(prompts[i])\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n    print(\\\"raw_yes_logit:\\\", float(raw_yes_logits[i]))\\n    print(\\\"raw_no_logit:\\\", float(raw_no_logits[i]))\\n    print(\\\"calibrated_yes_logit:\\\", float(cal_yes_logits[i]))\\n    print(\\\"calibrated_no_logit:\\\", float(cal_no_logits[i]))\\n\", \"mistakes = np.where(y_true != y_pred)[0][:10]\\nprint(\\\"num_errors:\\\", int((y_true != y_pred).sum()))\\n\\nfor i in mistakes:\\n    print(\\\"=\\\" * 80)\\n    print(\\\"idx:\\\", int(i))\\n    print(prompts[i])\\n    print(\\\"true:\\\", int(y_true[i]), \\\"pred:\\\", int(y_pred[i]))\\n    print(\\\"raw_yes_logit:\\\", float(raw_yes_logits[i]))\\n    print(\\\"raw_no_logit:\\\", float(raw_no_logits[i]))\\n    print(\\\"calibrated_yes_logit:\\\", float(cal_yes_logits[i]))\\n    print(\\\"calibrated_no_logit:\\\", float(cal_no_logits[i]))\\n\\n\\nvault.create_record_list(\\\"flan_t5_contextual_calibrated_yes_no_mrpc_summary\\\", column_names=[\\\"accuracy\\\", \\\"f1\\\", \\\"classification_report\\\"])\\n\\n\\nsummary = {\\n    \\\"accuracy\\\": float(acc),\\n    \\\"f1\\\": float(f1),\\n    \\\"classification_report\\\": str(report)\\n}\\n\\nvault.append_record(\\\"flan_t5_contextual_calibrated_yes_no_mrpc_summary\\\", summary,\\n                    input_items = {\\n                        \\\"glue_mrpc_validation\\\": [0, len(ds)],\\n                        \\\"flan_prediction_logit_calibrated\\\": [0, len(ds)]\\n                    })\\n\\nsummary\\n\\ndescription = \\\"Aggregate evaluation summary for the flan-t5-small contextual yes/no paraphrase classifier on the GLUE MRPC validation set after logit calibration. This dataset is a record list with one summary record containing the fields: accuracy (float), f1 (float), and classification_report (string with per-class precision/recall/F1 and support for not_paraphrase and paraphrase). It is produced after generating calibrated predictions in flan_prediction_logit_calibrated and compares those predictions against the ground-truth labels in glue_mrpc_validation. Its role in this workflow is to store run-level performance metrics for the full validation set, providing a compact summary of model quality for this notebook execution.\\\"\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"flan_t5_contextual_calibrated_yes_no_mrpc_summary\\\", description, embedding)\\n\\nproperties = {\\\"artifact_type\\\": \\\"evaluation summary\\\", \\\"task\\\": \\\"paraphrase detection\\\", \\\"benchmark\\\": \\\"GLUE\\\", \\\"source\\\": \\\"glue/mrpc\\\", \\\"input_dataset\\\": \\\"glue_mrpc_validation\\\", \\\"split\\\": \\\"validation\\\", \\\"size\\\": \\\"408\\\", \\\"model\\\": \\\"google/flan-t5-small\\\", \\\"prompt_format\\\": \\\"yes/no seq2seq\\\", \\\"calibration\\\": \\\"contextual logit calibration\\\", \\\"label_space\\\": \\\"binary\\\", \\\"metrics\\\": \\\"accuracy,f1,classification_report\\\"} #e.g. task: paraphrase detection\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"flan_t5_contextual_calibrated_yes_no_mrpc_summary\\\", cat, embedding, prop)\\n\\n\\n\", \"description = \\\"This notebook runs a zero-shot paraphrase detection experiment on the GLUE MRPC validation set using google/flan-t5-small. It frames each sentence pair as an instruction prompt asking whether the two sentences are paraphrases and scores the first decoder-step logits for the single-token answers yes and no. To reduce prompt bias, it applies contextual calibration by subtracting baseline yes/no logits computed from a null prompt with placeholder inputs (\\\\u201cN/A\\\\u201d, \\\\u201cN/A\\\\u201d), then predicts the label from the higher calibrated logit. The workflow loads MRPC examples from TableVault, generates batch predictions, stores raw and calibrated logits plus final predictions back into TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves summary records and semantic descriptions for the prediction outputs, summary table, and overall notebook process.\\\" # description of whole notebook\\nembedding = get_embeddings(description)\\nvault.create_description(\\\"flan_t5_contextual_calibrated_yes_no_mrpc\\\", description, embedding)\\n\\nproperties = {\\\"task\\\": \\\"paraphrase detection\\\", \\\"problem_type\\\": \\\"binary text classification\\\", \\\"method\\\": \\\"zero-shot seq2seq yes/no prompting with contextual calibration\\\", \\\"calibration\\\": \\\"contextual calibration using baseline logits from N/A prompt\\\", \\\"model\\\": \\\"google/flan-t5-small\\\", \\\"model_family\\\": \\\"FLAN-T5\\\", \\\"dataset\\\": \\\"glue/mrpc\\\", \\\"dataset_split\\\": \\\"validation\\\", \\\"input_format\\\": \\\"sentence pair prompt\\\", \\\"label_space\\\": \\\"yes/no\\\", \\\"prediction_signal\\\": \\\"first-decoder-step logits for yes and no tokens\\\", \\\"evaluation\\\": \\\"accuracy, f1-score, classification report\\\", \\\"frameworks\\\": \\\"PyTorch, Hugging Face Transformers, Datasets, scikit-learn\\\", \\\"tracking\\\": \\\"TableVault\\\", \\\"embedding_model\\\": \\\"text-embedding-3-large\\\", \\\"artifacts\\\": \\\"per-example calibrated logits and summary metrics\\\", \\\"process_name\\\": \\\"flan_t5_contextual_calibrated_yes_no_mrpc\\\"} #e.g. model: distilbert-base-uncased-MRPC\\n\\nfor prop, cat in properties.items():\\n    embedding = get_embeddings(prop)\\n    vault.create_description(\\\"flan_t5_contextual_calibrated_yes_no_mrpc\\\", cat, embedding, prop)\"]}"
  }
]
```

### Model Output
**response_id:** `resp_096e90c5623324b10069da5d117adc8195b171e6f7e8b73394`

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
    "call_id": "call_xpsnflwFUaNfNhP1GfuGxZq5",
    "arguments": {
      "item_name": "flan_t5_contextual_calibrated_yes_no_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_xpsnflwFUaNfNhP1GfuGxZq5`

**Arguments:**
```json
{
  "item_name": "flan_t5_contextual_calibrated_yes_no_mrpc_summary",
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
      "accuracy": 0.40441176470588236,
      "f1": 0.24299065420560748,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.34      0.98      0.51       129\n    paraphrase       0.93      0.14      0.24       279\n\n      accuracy                           0.40       408\n     macro avg       0.64      0.56      0.38       408\n  weighted avg       0.74      0.40      0.33       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 24918 | 52 | 8 | 23168 | 2.043s | 0.024s |

---

## Turn 16 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5d1387548195a2a3e143362cb4da`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_xpsnflwFUaNfNhP1GfuGxZq5",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.40441176470588236, \"f1\": 0.24299065420560748, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.34      0.98      0.51       129\\n    paraphrase       0.93      0.14      0.24       279\\n\\n      accuracy                           0.40       408\\n     macro avg       0.64      0.56      0.38       408\\n  weighted avg       0.74      0.40      0.33       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_096e90c5623324b10069da5d1387548195a2a3e143362cb4da`

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
    "call_id": "call_TLRn7DW58dDbb5iCYZ4KmpQb",
    "arguments": {
      "item_name": "flan_t5_full_answer_logprob_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_TLRn7DW58dDbb5iCYZ4KmpQb`

**Arguments:**
```json
{
  "item_name": "flan_t5_full_answer_logprob_mrpc_summary",
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
      "f1": 0.6911447084233261,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.47      0.81      0.59       129\n    paraphrase       0.87      0.57      0.69       279\n\n      accuracy                           0.65       408\n     macro avg       0.67      0.69      0.64       408\n  weighted avg       0.74      0.65      0.66       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 25136 | 753 | 712 | 23386 | 16.665s | 0.021s |

---

## Turn 17 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5d2439e481959c6635db629e9f71`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_TLRn7DW58dDbb5iCYZ4KmpQb",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.6495098039215687, \"f1\": 0.6911447084233261, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.47      0.81      0.59       129\\n    paraphrase       0.87      0.57      0.69       279\\n\\n      accuracy                           0.65       408\\n     macro avg       0.67      0.69      0.64       408\\n  weighted avg       0.74      0.65      0.66       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_096e90c5623324b10069da5d2439e481959c6635db629e9f71`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_IPkRJYdD2TMxFRFow3X3bqsC",
    "arguments": {
      "item_name": "flan_t5_true_false_first_step_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_IPkRJYdD2TMxFRFow3X3bqsC`

**Arguments:**
```json
{
  "item_name": "flan_t5_true_false_first_step_mrpc_summary",
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
      "accuracy": 0.5833333333333334,
      "f1": 0.6443514644351465,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.40      0.65      0.50       129\n    paraphrase       0.77      0.55      0.64       279\n\n      accuracy                           0.58       408\n     macro avg       0.59      0.60      0.57       408\n  weighted avg       0.66      0.58      0.60       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 26055 | 39 | 0 | 24305 | 4.585s | 0.022s |

---

## Turn 18 — `code_description_embedding_search` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5d28d59881958698c71618757eea`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_IPkRJYdD2TMxFRFow3X3bqsC",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.5833333333333334, \"f1\": 0.6443514644351465, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.40      0.65      0.50       129\\n    paraphrase       0.77      0.55      0.64       279\\n\\n      accuracy                           0.58       408\\n     macro avg       0.59      0.60      0.57       408\\n  weighted avg       0.66      0.58      0.60       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_096e90c5623324b10069da5d28d59881958698c71618757eea`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "code_description_embedding_search",
    "call_id": "call_7cKILugVogJF9mhw6IBNQbYC",
    "arguments": {
      "description_text": "same prompt no swap flan t5 are the following two sentences paraphrases answer yes or no MRPC"
    }
  }
]
```

### Tool Call
**Tool:** `code_description_embedding_search` | **call_id:** `call_7cKILugVogJF9mhw6IBNQbYC`

**Arguments:**
```json
{
  "description_text": "same prompt no swap flan t5 are the following two sentences paraphrases answer yes or no MRPC"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    [
      "BASE",
      "This notebook runs a prompt-based paraphrase detection experiment on the GLUE MRPC validation set using google/flan-t5-small. For each sentence pair, it builds an instruction prompt asking whether the two sentences are paraphrases and scores the full decoder log probability of the candidate answers \u201cyes\u201d and \u201cno\u201d (including EOS). The predicted label is chosen by comparing these two sequence log probabilities.\n\nThe workflow loads MRPC validation data from TableVault, tokenizes prompts, performs batched inference with FLAN-T5, records per-example predictions and yes/no scores, and evaluates performance with accuracy, F1, and a classification report. It also prints sample predictions and error cases for qualitative inspection.\n\nResults are written back to TableVault as a scored prediction record list and a summary record list, with dataset lineage links and embedding-based descriptions/metadata for both the outputs and the overall notebook process.",
      "flan_t5_full_answer_logprob_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates google/flan-t5-small on the GLUE MRPC validation set for binary paraphrase detection. It loads sentence pairs and labels from TableVault, converts each pair into a natural-language prompt asking whether the two sentences have the same meaning, and runs FLAN-T5 as a seq2seq model on MPS or CPU. Using the decoder prefix Answer:, it compares the next-token logits for yes and no to make a classification without full text generation. The workflow saves per-example predictions and yes/no logits to TableVault, computes accuracy, F1, and a classification report, reviews sample predictions and errors, and stores both dataset-level outputs and experiment summary metadata/descriptions back into TableVault for tracking and retrieval.",
      "flan_t5_answer_prefix_yes_no_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook runs a zero-shot paraphrase detection experiment on the GLUE MRPC validation set using google/flan-t5-small. It frames each sentence pair as an instruction prompt asking whether the two sentences are paraphrases and scores the first decoder-step logits for the single-token answers yes and no. To reduce prompt bias, it applies contextual calibration by subtracting baseline yes/no logits computed from a null prompt with placeholder inputs (\u201cN/A\u201d, \u201cN/A\u201d), then predicts the label from the higher calibrated logit. The workflow loads MRPC examples from TableVault, generates batch predictions, stores raw and calibrated logits plus final predictions back into TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves summary records and semantic descriptions for the prediction outputs, summary table, and overall notebook process.",
      "flan_t5_contextual_calibrated_yes_no_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates google/flan-t5-small on the GLUE MRPC validation set for binary paraphrase detection using a prompt-based true/false formulation. It loads sentence pairs and labels from the glue_mrpc_validation dataset stored in TableVault, prompts the model with an instruction asking whether the two sentences are paraphrases, and uses the first decoder-step logits for the single-token verbalizers true and false to make predictions. The workflow records per-example predictions and logits in TableVault, computes summary metrics including accuracy, F1, and a classification report, inspects a few examples and errors, and stores dataset, result, and notebook-level descriptions with OpenAI text embeddings for metadata and retrieval.",
      "flan_t5_true_false_first_step_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using google/flan-t5-small. It frames MRPC as a yes/no text-to-text classification task by prompting the model with two sentences and asking whether they are paraphrases. To reduce order sensitivity, each sentence pair is scored twice\u2014once in the original order and once with the sentences swapped\u2014and the first-token logits for yes and no are averaged across both prompts to produce the final prediction. The notebook loads the validation data from TableVault, runs batched inference with Hugging Face Transformers on MPS or CPU, computes accuracy, F1, and a classification report, inspects example predictions and errors, and stores per-example predictions, logits, summary metrics, and metadata back into TableVault with embedding-based descriptions.",
      "flan_t5_symmetric_prompt_average_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a Hugging Face paraphrase detection pipeline on the GLUE MRPC validation set using the textattack/distilbert-base-uncased-MRPC sequence classification model. It loads sentence pairs from TableVault, runs inference in both the original and swapped sentence order, extracts the paraphrase-class probabilities, and averages the two scores to reduce sensitivity to input order before generating final binary predictions. The workflow stores per-example prediction outputs and a summary of accuracy, F1, and the full classification report in TableVault, along with notebook, dataset, and result metadata embeddings for later retrieval and documentation.",
      "hf_pipeline_mrpc_bidirectional_order_average",
      "process_list"
    ],
    [
      "BASE",
      "This notebook runs a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the NLI model typeform/distilbert-base-uncased-mnli. Its purpose is to score sentence pairs as paraphrase vs. not paraphrase without task-specific fine-tuning, using a neutral-penalized entailment margin. For each MRPC pair, the notebook evaluates both sentence orders, computes an entailment score minus the larger of the contradiction or neutral scores, averages the two directional margins, and predicts paraphrase when the averaged margin is positive. It then stores per-example predictions and scores in TableVault, links them back to the source validation records, computes evaluation metrics including accuracy, F1, and a classification report, inspects example predictions and errors, and saves dataset-, prediction-, summary-, and process-level metadata and semantic descriptions using OpenAI embeddings.",
      "neutral_penalized_margin_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook runs a lightweight paraphrase detection experiment on the GLUE MRPC validation set and logs the full workflow to TableVault for traceability. It uses the sentence-transformers/all-MiniLM-L6-v2 model with max_seq_length set to 64 to encode each sentence in an MRPC pair into normalized 384-dimensional embeddings. For each example, it computes cosine similarity between the two sentence embeddings, applies a fixed threshold of 0.80 to predict whether the pair is a paraphrase, and evaluates the results with accuracy, F1, and a classification report. The notebook stores the sentence-level embeddings, prediction records, evaluation summary, and metadata descriptions in TableVault, using OpenAI text embeddings to embed the textual descriptions and properties. It also prints sample predictions and error cases to support qualitative inspection of model behavior.",
      "st_all_minilm_l6_max_seq_len_64_cosine_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli natural language inference model. For each sentence pair, it runs inference in both directions (sentence1\u2192sentence2 and sentence2\u2192sentence1), computes an entailment-versus-contradiction margin for each direction, averages the two margins, and predicts paraphrase only when neither direction is classified as contradiction and the average margin is positive. The notebook stores per-example predictions, directional margins, and gate decisions in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, logs error analysis examples, and saves dataset-, prediction-, summary-, and notebook-level metadata and embeddings for later retrieval and documentation.",
      "consensus_then_avg_margin_mrpc",
      "process_list"
    ],
    [
      "BASE",
      "This notebook runs a paraphrase detection experiment on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli sequence classification model in an NLI-style formulation. For each sentence pair, it scores both input orders (sentence1, sentence2) and (sentence2, sentence1), computes the softmax probability gap between entailment and contradiction for each order, averages the two gaps, and predicts paraphrase when the mean gap is greater than zero. The workflow loads the MRPC validation examples from TableVault, performs batched inference with Hugging Face Transformers and PyTorch, and stores per-example predictions and gap scores back into TableVault with lineage to the source records. It then evaluates the method with accuracy, F1, and a classification report, inspects sample predictions and errors, and saves an experiment summary plus descriptive metadata and embeddings for the prediction table, summary table, and overall notebook process.",
      "softmax_gap_mean_mrpc",
      "process_list"
    ]
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 26260 | 635 | 592 | 24510 | 10.935s | 0.561s |

---

## Turn 19 — `finalize_result` [ok]

### Model Input
**previous_response_id:** `resp_096e90c5623324b10069da5d345a2481959ea7075911fc6b18`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_7cKILugVogJF9mhw6IBNQbYC",
    "output": "{\"ok\": true, \"result\": [[\"BASE\", \"This notebook runs a prompt-based paraphrase detection experiment on the GLUE MRPC validation set using google/flan-t5-small. For each sentence pair, it builds an instruction prompt asking whether the two sentences are paraphrases and scores the full decoder log probability of the candidate answers \\u201cyes\\u201d and \\u201cno\\u201d (including EOS). The predicted label is chosen by comparing these two sequence log probabilities.\\n\\nThe workflow loads MRPC validation data from TableVault, tokenizes prompts, performs batched inference with FLAN-T5, records per-example predictions and yes/no scores, and evaluates performance with accuracy, F1, and a classification report. It also prints sample predictions and error cases for qualitative inspection.\\n\\nResults are written back to TableVault as a scored prediction record list and a summary record list, with dataset lineage links and embedding-based descriptions/metadata for both the outputs and the overall notebook process.\", \"flan_t5_full_answer_logprob_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates google/flan-t5-small on the GLUE MRPC validation set for binary paraphrase detection. It loads sentence pairs and labels from TableVault, converts each pair into a natural-language prompt asking whether the two sentences have the same meaning, and runs FLAN-T5 as a seq2seq model on MPS or CPU. Using the decoder prefix Answer:, it compares the next-token logits for yes and no to make a classification without full text generation. The workflow saves per-example predictions and yes/no logits to TableVault, computes accuracy, F1, and a classification report, reviews sample predictions and errors, and stores both dataset-level outputs and experiment summary metadata/descriptions back into TableVault for tracking and retrieval.\", \"flan_t5_answer_prefix_yes_no_mrpc\", \"process_list\"], [\"BASE\", \"This notebook runs a zero-shot paraphrase detection experiment on the GLUE MRPC validation set using google/flan-t5-small. It frames each sentence pair as an instruction prompt asking whether the two sentences are paraphrases and scores the first decoder-step logits for the single-token answers yes and no. To reduce prompt bias, it applies contextual calibration by subtracting baseline yes/no logits computed from a null prompt with placeholder inputs (\\u201cN/A\\u201d, \\u201cN/A\\u201d), then predicts the label from the higher calibrated logit. The workflow loads MRPC examples from TableVault, generates batch predictions, stores raw and calibrated logits plus final predictions back into TableVault, computes evaluation metrics including accuracy, F1, and a classification report, inspects sample predictions and errors, and saves summary records and semantic descriptions for the prediction outputs, summary table, and overall notebook process.\", \"flan_t5_contextual_calibrated_yes_no_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates google/flan-t5-small on the GLUE MRPC validation set for binary paraphrase detection using a prompt-based true/false formulation. It loads sentence pairs and labels from the glue_mrpc_validation dataset stored in TableVault, prompts the model with an instruction asking whether the two sentences are paraphrases, and uses the first decoder-step logits for the single-token verbalizers true and false to make predictions. The workflow records per-example predictions and logits in TableVault, computes summary metrics including accuracy, F1, and a classification report, inspects a few examples and errors, and stores dataset, result, and notebook-level descriptions with OpenAI text embeddings for metadata and retrieval.\", \"flan_t5_true_false_first_step_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using google/flan-t5-small. It frames MRPC as a yes/no text-to-text classification task by prompting the model with two sentences and asking whether they are paraphrases. To reduce order sensitivity, each sentence pair is scored twice\\u2014once in the original order and once with the sentences swapped\\u2014and the first-token logits for yes and no are averaged across both prompts to produce the final prediction. The notebook loads the validation data from TableVault, runs batched inference with Hugging Face Transformers on MPS or CPU, computes accuracy, F1, and a classification report, inspects example predictions and errors, and stores per-example predictions, logits, summary metrics, and metadata back into TableVault with embedding-based descriptions.\", \"flan_t5_symmetric_prompt_average_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a Hugging Face paraphrase detection pipeline on the GLUE MRPC validation set using the textattack/distilbert-base-uncased-MRPC sequence classification model. It loads sentence pairs from TableVault, runs inference in both the original and swapped sentence order, extracts the paraphrase-class probabilities, and averages the two scores to reduce sensitivity to input order before generating final binary predictions. The workflow stores per-example prediction outputs and a summary of accuracy, F1, and the full classification report in TableVault, along with notebook, dataset, and result metadata embeddings for later retrieval and documentation.\", \"hf_pipeline_mrpc_bidirectional_order_average\", \"process_list\"], [\"BASE\", \"This notebook runs a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the NLI model typeform/distilbert-base-uncased-mnli. Its purpose is to score sentence pairs as paraphrase vs. not paraphrase without task-specific fine-tuning, using a neutral-penalized entailment margin. For each MRPC pair, the notebook evaluates both sentence orders, computes an entailment score minus the larger of the contradiction or neutral scores, averages the two directional margins, and predicts paraphrase when the averaged margin is positive. It then stores per-example predictions and scores in TableVault, links them back to the source validation records, computes evaluation metrics including accuracy, F1, and a classification report, inspects example predictions and errors, and saves dataset-, prediction-, summary-, and process-level metadata and semantic descriptions using OpenAI embeddings.\", \"neutral_penalized_margin_mrpc\", \"process_list\"], [\"BASE\", \"This notebook runs a lightweight paraphrase detection experiment on the GLUE MRPC validation set and logs the full workflow to TableVault for traceability. It uses the sentence-transformers/all-MiniLM-L6-v2 model with max_seq_length set to 64 to encode each sentence in an MRPC pair into normalized 384-dimensional embeddings. For each example, it computes cosine similarity between the two sentence embeddings, applies a fixed threshold of 0.80 to predict whether the pair is a paraphrase, and evaluates the results with accuracy, F1, and a classification report. The notebook stores the sentence-level embeddings, prediction records, evaluation summary, and metadata descriptions in TableVault, using OpenAI text embeddings to embed the textual descriptions and properties. It also prints sample predictions and error cases to support qualitative inspection of model behavior.\", \"st_all_minilm_l6_max_seq_len_64_cosine_mrpc\", \"process_list\"], [\"BASE\", \"This notebook evaluates a zero-shot paraphrase detection workflow on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli natural language inference model. For each sentence pair, it runs inference in both directions (sentence1\\u2192sentence2 and sentence2\\u2192sentence1), computes an entailment-versus-contradiction margin for each direction, averages the two margins, and predicts paraphrase only when neither direction is classified as contradiction and the average margin is positive. The notebook stores per-example predictions, directional margins, and gate decisions in TableVault, computes accuracy, F1, and a classification report against the MRPC labels, logs error analysis examples, and saves dataset-, prediction-, summary-, and notebook-level metadata and embeddings for later retrieval and documentation.\", \"consensus_then_avg_margin_mrpc\", \"process_list\"], [\"BASE\", \"This notebook runs a paraphrase detection experiment on the GLUE MRPC validation set using the typeform/distilbert-base-uncased-mnli sequence classification model in an NLI-style formulation. For each sentence pair, it scores both input orders (sentence1, sentence2) and (sentence2, sentence1), computes the softmax probability gap between entailment and contradiction for each order, averages the two gaps, and predicts paraphrase when the mean gap is greater than zero. The workflow loads the MRPC validation examples from TableVault, performs batched inference with Hugging Face Transformers and PyTorch, and stores per-example predictions and gap scores back into TableVault with lineage to the source records. It then evaluates the method with accuracy, F1, and a classification report, inspects sample predictions and errors, and saves an experiment summary plus descriptive metadata and embeddings for the prediction table, summary table, and overall notebook process.\", \"softmax_gap_mean_mrpc\", \"process_list\"]]}"
  }
]
```

### Model Output
**response_id:** `resp_096e90c5623324b10069da5d345a2481959ea7075911fc6b18`

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
    "call_id": "call_v7OYC5zWWbNOfTUUyWsMYKX8",
    "arguments": {
      "summary": "{\"rows\":[{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"softmax gap mean\",\"symmetry_rule\":\"average entailment-minus-contradiction probability gap over both sentence orders\",\"accuracy\":0.718,\"f1\":0.791,\"paraphrase_recall\":0.78},{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"entailment log-probability odds\",\"symmetry_rule\":\"average entailment-minus-contradiction log-probability odds over both sentence orders\",\"accuracy\":0.703,\"f1\":0.773,\"paraphrase_recall\":0.74},{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"consensus then average margin\",\"symmetry_rule\":\"average bidirectional entailment-vs-contradiction margins, but require neither direction to be contradiction\",\"accuracy\":0.701,\"f1\":0.770,\"paraphrase_recall\":0.73},{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"min-direction margin\",\"symmetry_rule\":\"use the minimum bidirectional entailment-minus-contradiction margin as final score\",\"accuracy\":0.586,\"f1\":0.589,\"paraphrase_recall\":0.43},{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"neutral-penalized average margin\",\"symmetry_rule\":\"average bidirectional entailment margin after subtracting max(contradiction, neutral)\",\"accuracy\":0.556,\"f1\":0.532,\"paraphrase_recall\":0.37},{\"model_group\":\"Prompt-based zero-shot paraphrase scoring\",\"model\":\"google/flan-t5-small\",\"strategy\":\"symmetric prompt average\",\"symmetry_rule\":\"average yes/no first-token logits across original and swapped prompts\",\"accuracy\":0.738,\"f1\":0.807,\"paraphrase_recall\":0.8},{\"model_group\":\"Prompt-based zero-shot paraphrase scoring\",\"model\":\"google/flan-t5-small\",\"strategy\":\"answer-prefix yes/no baseline\",\"symmetry_rule\":\"none; single prompt order\",\"accuracy\":0.637,\"f1\":0.688,\"paraphrase_recall\":0.58},{\"model_group\":\"Prompt-based zero-shot paraphrase scoring\",\"model\":\"google/flan-t5-small\",\"strategy\":\"full-answer log-probability baseline\",\"symmetry_rule\":\"none; single prompt order\",\"accuracy\":0.65,\"f1\":0.691,\"paraphrase_recall\":0.57}],\"summary\":\"Repository evidence from MRPC validation experiments shows that prediction symmetry is most helpful when enforced with soft bidirectional averaging, not with hard conservative constraints. For the NLI-based MNLI model (typeform/distilbert-base-uncased-mnli), the best symmetric rule was averaging bidirectional entailment-vs-contradiction evidence: softmax-gap mean reached 0.718 accuracy, while averaged log-probability odds reached 0.703 and a contradiction-gated average reached 0.701. In contrast, stricter symmetry enforcement substantially reduced accuracy: taking the minimum directional margin dropped accuracy to 0.586, and neutral-penalized averaging fell further to 0.556. The class reports indicate why: these stricter rules sharply reduced paraphrase recall (0.43 and 0.37 respectively), implying an over-conservative bias toward predicting non-paraphrase. This is particularly damaging on MRPC validation, which is paraphrase-heavy (279 positive vs. 129 negative examples). For the prompt-based zero-shot model (google/flan-t5-small), explicit symmetry via swap-and-average prompt scoring gave the strongest result, with 0.738 accuracy and 0.807 F1, outperforming single-order baselines such as answer-prefix yes/no (0.637) and full-answer log-probability scoring (0.650). Thus, for both model families, symmetry enforcement helps when it smooths order effects by averaging evidence across both directions, but hurts when it imposes a hard agreement bottleneck or heavy penalty that suppresses positive predictions. The main limitation is that the zero-shot FLAN comparisons are not perfectly controlled: prompt wording and decoding/scoring choices differ across runs, so not all of the gain can be attributed solely to symmetry. By contrast, the NLI runs are a more controlled comparison because they share the same underlying model and differ mainly in how bidirectional evidence is combined. The table should therefore be read as comparative repository evidence on MRPC validation, not as a formal causal ablation with confidence intervals.\"}"
    }
  }
]
```

### Tool Call
**Tool:** `finalize_result` | **call_id:** `call_v7OYC5zWWbNOfTUUyWsMYKX8`

**Arguments:**
```json
{
  "summary": "{\"rows\":[{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"softmax gap mean\",\"symmetry_rule\":\"average entailment-minus-contradiction probability gap over both sentence orders\",\"accuracy\":0.718,\"f1\":0.791,\"paraphrase_recall\":0.78},{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"entailment log-probability odds\",\"symmetry_rule\":\"average entailment-minus-contradiction log-probability odds over both sentence orders\",\"accuracy\":0.703,\"f1\":0.773,\"paraphrase_recall\":0.74},{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"consensus then average margin\",\"symmetry_rule\":\"average bidirectional entailment-vs-contradiction margins, but require neither direction to be contradiction\",\"accuracy\":0.701,\"f1\":0.770,\"paraphrase_recall\":0.73},{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"min-direction margin\",\"symmetry_rule\":\"use the minimum bidirectional entailment-minus-contradiction margin as final score\",\"accuracy\":0.586,\"f1\":0.589,\"paraphrase_recall\":0.43},{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"neutral-penalized average margin\",\"symmetry_rule\":\"average bidirectional entailment margin after subtracting max(contradiction, neutral)\",\"accuracy\":0.556,\"f1\":0.532,\"paraphrase_recall\":0.37},{\"model_group\":\"Prompt-based zero-shot paraphrase scoring\",\"model\":\"google/flan-t5-small\",\"strategy\":\"symmetric prompt average\",\"symmetry_rule\":\"average yes/no first-token logits across original and swapped prompts\",\"accuracy\":0.738,\"f1\":0.807,\"paraphrase_recall\":0.8},{\"model_group\":\"Prompt-based zero-shot paraphrase scoring\",\"model\":\"google/flan-t5-small\",\"strategy\":\"answer-prefix yes/no baseline\",\"symmetry_rule\":\"none; single prompt order\",\"accuracy\":0.637,\"f1\":0.688,\"paraphrase_recall\":0.58},{\"model_group\":\"Prompt-based zero-shot paraphrase scoring\",\"model\":\"google/flan-t5-small\",\"strategy\":\"full-answer log-probability baseline\",\"symmetry_rule\":\"none; single prompt order\",\"accuracy\":0.65,\"f1\":0.691,\"paraphrase_recall\":0.57}],\"summary\":\"Repository evidence from MRPC validation experiments shows that prediction symmetry is most helpful when enforced with soft bidirectional averaging, not with hard conservative constraints. For the NLI-based MNLI model (typeform/distilbert-base-uncased-mnli), the best symmetric rule was averaging bidirectional entailment-vs-contradiction evidence: softmax-gap mean reached 0.718 accuracy, while averaged log-probability odds reached 0.703 and a contradiction-gated average reached 0.701. In contrast, stricter symmetry enforcement substantially reduced accuracy: taking the minimum directional margin dropped accuracy to 0.586, and neutral-penalized averaging fell further to 0.556. The class reports indicate why: these stricter rules sharply reduced paraphrase recall (0.43 and 0.37 respectively), implying an over-conservative bias toward predicting non-paraphrase. This is particularly damaging on MRPC validation, which is paraphrase-heavy (279 positive vs. 129 negative examples). For the prompt-based zero-shot model (google/flan-t5-small), explicit symmetry via swap-and-average prompt scoring gave the strongest result, with 0.738 accuracy and 0.807 F1, outperforming single-order baselines such as answer-prefix yes/no (0.637) and full-answer log-probability scoring (0.650). Thus, for both model families, symmetry enforcement helps when it smooths order effects by averaging evidence across both directions, but hurts when it imposes a hard agreement bottleneck or heavy penalty that suppresses positive predictions. The main limitation is that the zero-shot FLAN comparisons are not perfectly controlled: prompt wording and decoding/scoring choices differ across runs, so not all of the gain can be attributed solely to symmetry. By contrast, the NLI runs are a more controlled comparison because they share the same underlying model and differ mainly in how bidirectional evidence is combined. The table should therefore be read as comparative repository evidence on MRPC validation, not as a formal causal ablation with confidence intervals.\"}"
}
```

### Tool Output
```json
{
  "summary": "{\"rows\":[{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"softmax gap mean\",\"symmetry_rule\":\"average entailment-minus-contradiction probability gap over both sentence orders\",\"accuracy\":0.718,\"f1\":0.791,\"paraphrase_recall\":0.78},{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"entailment log-probability odds\",\"symmetry_rule\":\"average entailment-minus-contradiction log-probability odds over both sentence orders\",\"accuracy\":0.703,\"f1\":0.773,\"paraphrase_recall\":0.74},{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"consensus then average margin\",\"symmetry_rule\":\"average bidirectional entailment-vs-contradiction margins, but require neither direction to be contradiction\",\"accuracy\":0.701,\"f1\":0.770,\"paraphrase_recall\":0.73},{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"min-direction margin\",\"symmetry_rule\":\"use the minimum bidirectional entailment-minus-contradiction margin as final score\",\"accuracy\":0.586,\"f1\":0.589,\"paraphrase_recall\":0.43},{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"neutral-penalized average margin\",\"symmetry_rule\":\"average bidirectional entailment margin after subtracting max(contradiction, neutral)\",\"accuracy\":0.556,\"f1\":0.532,\"paraphrase_recall\":0.37},{\"model_group\":\"Prompt-based zero-shot paraphrase scoring\",\"model\":\"google/flan-t5-small\",\"strategy\":\"symmetric prompt average\",\"symmetry_rule\":\"average yes/no first-token logits across original and swapped prompts\",\"accuracy\":0.738,\"f1\":0.807,\"paraphrase_recall\":0.8},{\"model_group\":\"Prompt-based zero-shot paraphrase scoring\",\"model\":\"google/flan-t5-small\",\"strategy\":\"answer-prefix yes/no baseline\",\"symmetry_rule\":\"none; single prompt order\",\"accuracy\":0.637,\"f1\":0.688,\"paraphrase_recall\":0.58},{\"model_group\":\"Prompt-based zero-shot paraphrase scoring\",\"model\":\"google/flan-t5-small\",\"strategy\":\"full-answer log-probability baseline\",\"symmetry_rule\":\"none; single prompt order\",\"accuracy\":0.65,\"f1\":0.691,\"paraphrase_recall\":0.57}],\"summary\":\"Repository evidence from MRPC validation experiments shows that prediction symmetry is most helpful when enforced with soft bidirectional averaging, not with hard conservative constraints. For the NLI-based MNLI model (typeform/distilbert-base-uncased-mnli), the best symmetric rule was averaging bidirectional entailment-vs-contradiction evidence: softmax-gap mean reached 0.718 accuracy, while averaged log-probability odds reached 0.703 and a contradiction-gated average reached 0.701. In contrast, stricter symmetry enforcement substantially reduced accuracy: taking the minimum directional margin dropped accuracy to 0.586, and neutral-penalized averaging fell further to 0.556. The class reports indicate why: these stricter rules sharply reduced paraphrase recall (0.43 and 0.37 respectively), implying an over-conservative bias toward predicting non-paraphrase. This is particularly damaging on MRPC validation, which is paraphrase-heavy (279 positive vs. 129 negative examples). For the prompt-based zero-shot model (google/flan-t5-small), explicit symmetry via swap-and-average prompt scoring gave the strongest result, with 0.738 accuracy and 0.807 F1, outperforming single-order baselines such as answer-prefix yes/no (0.637) and full-answer log-probability scoring (0.650). Thus, for both model families, symmetry enforcement helps when it smooths order effects by averaging evidence across both directions, but hurts when it imposes a hard agreement bottleneck or heavy penalty that suppresses positive predictions. The main limitation is that the zero-shot FLAN comparisons are not perfectly controlled: prompt wording and decoding/scoring choices differ across runs, so not all of the gain can be attributed solely to symmetry. By contrast, the NLI runs are a more controlled comparison because they share the same underlying model and differ mainly in how bidirectional evidence is combined. The table should therefore be read as comparative repository evidence on MRPC validation, not as a formal causal ablation with confidence intervals.\"}"
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 28750 | 4140 | 3106 | 27000 | 68.455s | 0.000s |

---

# Run Summary

**Final Result:**
```json
{
  "summary": "{\"rows\":[{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"softmax gap mean\",\"symmetry_rule\":\"average entailment-minus-contradiction probability gap over both sentence orders\",\"accuracy\":0.718,\"f1\":0.791,\"paraphrase_recall\":0.78},{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"entailment log-probability odds\",\"symmetry_rule\":\"average entailment-minus-contradiction log-probability odds over both sentence orders\",\"accuracy\":0.703,\"f1\":0.773,\"paraphrase_recall\":0.74},{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"consensus then average margin\",\"symmetry_rule\":\"average bidirectional entailment-vs-contradiction margins, but require neither direction to be contradiction\",\"accuracy\":0.701,\"f1\":0.770,\"paraphrase_recall\":0.73},{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"min-direction margin\",\"symmetry_rule\":\"use the minimum bidirectional entailment-minus-contradiction margin as final score\",\"accuracy\":0.586,\"f1\":0.589,\"paraphrase_recall\":0.43},{\"model_group\":\"NLI-based paraphrase scoring\",\"model\":\"typeform/distilbert-base-uncased-mnli\",\"strategy\":\"neutral-penalized average margin\",\"symmetry_rule\":\"average bidirectional entailment margin after subtracting max(contradiction, neutral)\",\"accuracy\":0.556,\"f1\":0.532,\"paraphrase_recall\":0.37},{\"model_group\":\"Prompt-based zero-shot paraphrase scoring\",\"model\":\"google/flan-t5-small\",\"strategy\":\"symmetric prompt average\",\"symmetry_rule\":\"average yes/no first-token logits across original and swapped prompts\",\"accuracy\":0.738,\"f1\":0.807,\"paraphrase_recall\":0.8},{\"model_group\":\"Prompt-based zero-shot paraphrase scoring\",\"model\":\"google/flan-t5-small\",\"strategy\":\"answer-prefix yes/no baseline\",\"symmetry_rule\":\"none; single prompt order\",\"accuracy\":0.637,\"f1\":0.688,\"paraphrase_recall\":0.58},{\"model_group\":\"Prompt-based zero-shot paraphrase scoring\",\"model\":\"google/flan-t5-small\",\"strategy\":\"full-answer log-probability baseline\",\"symmetry_rule\":\"none; single prompt order\",\"accuracy\":0.65,\"f1\":0.691,\"paraphrase_recall\":0.57}],\"summary\":\"Repository evidence from MRPC validation experiments shows that prediction symmetry is most helpful when enforced with soft bidirectional averaging, not with hard conservative constraints. For the NLI-based MNLI model (typeform/distilbert-base-uncased-mnli), the best symmetric rule was averaging bidirectional entailment-vs-contradiction evidence: softmax-gap mean reached 0.718 accuracy, while averaged log-probability odds reached 0.703 and a contradiction-gated average reached 0.701. In contrast, stricter symmetry enforcement substantially reduced accuracy: taking the minimum directional margin dropped accuracy to 0.586, and neutral-penalized averaging fell further to 0.556. The class reports indicate why: these stricter rules sharply reduced paraphrase recall (0.43 and 0.37 respectively), implying an over-conservative bias toward predicting non-paraphrase. This is particularly damaging on MRPC validation, which is paraphrase-heavy (279 positive vs. 129 negative examples). For the prompt-based zero-shot model (google/flan-t5-small), explicit symmetry via swap-and-average prompt scoring gave the strongest result, with 0.738 accuracy and 0.807 F1, outperforming single-order baselines such as answer-prefix yes/no (0.637) and full-answer log-probability scoring (0.650). Thus, for both model families, symmetry enforcement helps when it smooths order effects by averaging evidence across both directions, but hurts when it imposes a hard agreement bottleneck or heavy penalty that suppresses positive predictions. The main limitation is that the zero-shot FLAN comparisons are not perfectly controlled: prompt wording and decoding/scoring choices differ across runs, so not all of the gain can be attributed solely to symmetry. By contrast, the NLI runs are a more controlled comparison because they share the same underlying model and differ mainly in how bidirectional evidence is combined. The table should therefore be read as comparative repository evidence on MRPC validation, not as a formal causal ablation with confidence intervals.\"}"
}
```

**Metrics Summary:**
```json
{
  "tokens": {
    "input": 331869,
    "output": 8102,
    "reasoning": 6358,
    "total": 339971,
    "system_estimate": 1750,
    "conversation": 296983
  },
  "code": {
    "executions": 0,
    "failed_executions": 0,
    "total_lines": 0
  },
  "timing": {
    "api_latency_s": 157.323,
    "exec_latency_s": 2.858,
    "wall_time_s": 160.181
  },
  "api_calls": 20,
  "cost": null
}
```
