# Agent Trace — 20260411T135617Z

**Model:** `gpt-5.4`  
**Timestamp:** 2026-04-11T13:56:17.350310+00:00  
**Task:** How sensitive are similarity-based paraphrase classifiers to the choice of decision threshold, and does this vary across model families?

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

## Turn 0 — `description_search` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da53017290819b92077960d61e07e5`

**Pending messages:**
```json
[
  {
    "role": "user",
    "content": "How sensitive are similarity-based paraphrase classifiers to the choice of decision threshold, and does this vary across model families?"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da53017290819b92077960d61e07e5`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "description_search",
    "call_id": "call_wZL9hwUCA9HQIgFznYOTzYSC",
    "arguments": {
      "description_text": "paraphrase similarity threshold classifier model family decision threshold evaluation"
    }
  }
]
```

### Tool Call
**Tool:** `description_search` | **call_id:** `call_wZL9hwUCA9HQIgFznYOTzYSC`

**Arguments:**
```json
{
  "description_text": "paraphrase similarity threshold classifier model family decision threshold evaluation"
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
| 1701 | 92 | 61 | 0 | 2.111s | 0.050s |

---

## Turn 1 — `description_search` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da53039530819bb51252c2aaab6b58`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_wZL9hwUCA9HQIgFznYOTzYSC",
    "output": "{\"ok\": true, \"result\": []}"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da53039530819bb51252c2aaab6b58`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "description_search",
    "call_id": "call_xOvxpF9pQ5b1QhxmMn0YV10N",
    "arguments": {
      "description_text": "paraphrase"
    }
  }
]
```

### Tool Call
**Tool:** `description_search` | **call_id:** `call_xOvxpF9pQ5b1QhxmMn0YV10N`

**Arguments:**
```json
{
  "description_text": "paraphrase"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    [
      "BASE",
      "sentence-transformers-sentence-1-distance_threshold is an embedding dataset containing one 384-dimensional sentence embedding for the sentence1 field of each example in the GLUE MRPC validation set. Each item is a normalized dense vector generated with the sentence-transformers/all-MiniLM-L6-v2 model, and each embedding is linked back to the corresponding source row in glue_mrpc_validation through the input_items index mapping. This dataset does not store raw text columns itself; its primary field is the embedding vector for sentence1. In this workflow, it serves as the sentence1 representation used with the matching sentence-transformers-sentence-2-distance_threshold embeddings to compute L2 distances, apply a fixed distance threshold, and produce paraphrase predictions.",
      "sentence-transformers-sentence-1-distance_threshold",
      "embedding_list"
    ],
    [
      "BASE",
      "Embedding list containing one 384-dimensional normalized sentence embedding per row for the sentence1 field of the GLUE MRPC validation dataset. Each embedding is generated with the sentence-transformers/all-MiniLM-L6-v2 model using max_seq_length=64, so inputs may be truncated beyond 64 tokens. Structure: this dataset stores a single embedding vector for each original example and is linked back to the corresponding row in glue_mrpc_validation via input item indices. In this workflow, it provides the vector representation of the first sentence in each pair, which is later compared with the matching sentence-transformers-sentence-2-max64 embedding using cosine similarity to produce paraphrase predictions.",
      "sentence-transformers-sentence-1-max64",
      "embedding_list"
    ],
    [
      "BASE",
      "This dataset stores the normalized SentenceTransformer embeddings for the sentence1 field of each example in the GLUE MRPC validation set. Each item is a single 384-dimensional float vector produced by the model sentence-transformers/paraphrase-MiniLM-L3-v2, with one embedding per input row and lineage linked back to the corresponding glue_mrpc_validation record.\n\nStructure: an embedding list with ndim=384. There are no tabular feature columns; each entry consists of the embedding vector plus metadata links to the source row in glue_mrpc_validation.\n\nRole in the workflow: this dataset represents the first sentence in each MRPC pair in embedding space. These vectors are used with the corresponding sentence-2 embeddings to compute cosine similarity scores, which are then thresholded (0.74) to generate paraphrase predictions.",
      "sentence-transformers-sentence-1-threshold",
      "embedding_list"
    ],
    [
      "BASE",
      "This dataset stores the sentence embeddings for the sentence1 field of the GLUE MRPC validation set. Each item is a 768-dimensional float vector produced by the sentence-transformers/all-distilroberta-v1 model with normalized embeddings enabled, so dot products correspond to cosine similarity. The dataset is structured as an embedding list: one embedding per MRPC validation example, with each embedding linked to the corresponding row in glue_mrpc_validation through input item provenance. In this workflow, it provides the first-sentence representation used with the matching sentence-transformers-sentence-2-threshold_2 embeddings to compute similarity scores and apply a 0.72 threshold for paraphrase prediction.",
      "sentence-transformers-sentence-1-threshold_2",
      "embedding_list"
    ],
    [
      "BASE",
      "This dataset stores one normalized sentence embedding per example for the sentence2 field in the GLUE MRPC validation split. Each item is a 384-dimensional float vector generated by the sentence-transformers/all-MiniLM-L6-v2 model, with each embedding linked back to the corresponding source row in glue_mrpc_validation via input item lineage. Structure: an embedding list where each entry contains a single 384-length embedding vector and its association to the matching MRPC example index. In this workflow, these sentence2 embeddings are paired with the corresponding sentence1 embeddings from sentence-transformers-sentence-1-distance_threshold, and the L2 distance between the two vectors is used with a fixed threshold to predict whether the sentence pair is a paraphrase.",
      "sentence-transformers-sentence-2-distance_threshold",
      "embedding_list"
    ],
    [
      "BASE",
      "Embedding dataset containing one 384-dimensional normalized sentence embedding per row for the sentence2 field of each example in the GLUE MRPC validation set. Each vector was produced with the sentence-transformers/all-MiniLM-L6-v2 model using a maximum sequence length of 64, so it represents the truncated second sentence in a paraphrase pair. The dataset structure is an embedding list: each item stores a single 384-float embedding and is linked back to the corresponding row in glue_mrpc_validation. In this workflow, these sentence2 embeddings are paired with the matching sentence-transformers-sentence-1-max64 embeddings to compute cosine similarity scores and generate paraphrase predictions.",
      "sentence-transformers-sentence-2-max64",
      "embedding_list"
    ],
    [
      "BASE",
      "sentence-transformers-sentence-2-threshold is an embedding dataset containing one normalized 384-dimensional sentence embedding for the sentence2 field of each example in the GLUE MRPC validation set. Each entry corresponds 1-to-1 with a row in glue_mrpc_validation and is linked back to the source record through input_items, so the dataset structure is an ordered list of embedding vectors plus provenance to the original example index range. The embeddings are produced with the sentence-transformers/paraphrase-MiniLM-L3-v2 model and are intended to represent the second sentence in each MRPC pair. In this workflow, this dataset is used together with the matching sentence-transformers-sentence-1-threshold embeddings to compute cosine similarity scores and generate threshold-based paraphrase predictions.",
      "sentence-transformers-sentence-2-threshold",
      "embedding_list"
    ],
    [
      "BASE",
      "This dataset stores the sentence embedding for the second sentence (sentence2) of each example in the GLUE MRPC validation set. It is an embedding list with one row per MRPC record, where each item contains a 768-dimensional, L2-normalized vector produced by the sentence-transformers/all-distilroberta-v1 model, and each embedding is linked back to the corresponding source row in glue_mrpc_validation through the input_items index range [i, i+1]. In this workflow, these sentence2 embeddings are paired with the corresponding sentence1 embeddings from sentence-transformers-sentence-1-threshold_2, and their dot product is used as cosine similarity to make threshold-based paraphrase predictions.",
      "sentence-transformers-sentence-2-threshold_2",
      "embedding_list"
    ],
    [
      "BASE",
      "Summary dataset for the MRPC validation evaluation of the consensus-then-average-margin inference method. It contains aggregate performance results computed by comparing the generated paraphrase predictions against the true labels from glue_mrpc_validation, using prediction records stored in mrpc_gate_margin_prediction. The dataset is structured as a record list with columns: accuracy (float), f1 (float), and classification_report (string containing the full per-class sklearn classification report for not_paraphrase and paraphrase). In this workflow, it serves as the final evaluation artifact for the notebook, linking the full MRPC validation set and the per-example prediction dataset to a compact summary of model performance.",
      "consensus_then_avg_margin_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "This dataset stores per-example paraphrase predictions for the GLUE MRPC validation set produced by a DistilBERT-based cosine similarity pipeline. For each sentence pair from glue_mrpc_validation, the notebook encodes sentence1 and sentence2 with distilbert-base-uncased, applies masked max pooling to the token embeddings, computes the cosine similarity between the two normalized sentence embeddings, and converts that score to a binary prediction using a threshold of 0.85.\n\nStructure:\n- prediction: integer binary label predicted by the similarity rule (1 = paraphrase, 0 = not paraphrase)\n- cosine_scores: float cosine similarity between the max-pooled embeddings of the two sentences\n\nEach record corresponds to one input sentence pair and is linked back to the source validation examples through input_items. In this workflow, the dataset serves as the main model-output table for downstream evaluation, inspection of correct and incorrect predictions, and creation of the final summary metrics dataset.",
      "cosine_mrpc_max_pool_similarity_prediction",
      "record_list"
    ],
    [
      "BASE",
      "This dataset stores per-example paraphrase predictions for the GLUE MRPC validation set produced by this notebook\u2019s embedding-similarity baseline. Each record corresponds to one sentence pair from glue_mrpc_validation and contains two fields: prediction, a binary label (1 if the pair is predicted to be a paraphrase, 0 otherwise), and similarities, the cosine similarity score between the L2-normalized sentence embeddings of sentence1 and sentence2. The embeddings are generated with distilbert-base-uncased by averaging the last 4 hidden layers at the token level and then mean-pooling across tokens. Predictions are created by applying a fixed threshold of 0.85 to the similarity score. In this workflow, this dataset is the intermediate model output used to inspect individual examples, analyze errors, and compute the final evaluation summary in distilbert_last4_mean_cosine_mrpc_summary.",
      "cosine_mrpc_mean_similarity_prediction",
      "record_list"
    ],
    [
      "BASE",
      "Per-example prediction dataset for the GLUE MRPC validation split. Each record corresponds to one sentence pair from glue_mrpc_validation and stores the output of a simple paraphrase classifier built from DistilBERT sentence embeddings. The dataset has two fields: prediction, a binary label where 1 means paraphrase and 0 means not paraphrase, produced by thresholding the cosine similarity at 0.85; and score, the raw cosine similarity between the L2-normalized first-token embeddings of sentence1 and sentence2 from distilbert-base-uncased. In this workflow, this dataset is the main record of model inference results, used for error analysis, inspection of individual examples, and as input to the downstream summary dataset distilbert_cls_cosine_mrpc_summary.",
      "cosine_mrpc_threshold_score",
      "record_list"
    ],
    [
      "BASE",
      "distilbert_cross_text_prediction stores per-example model outputs generated by applying the cross-encoder/quora-distilroberta-base cross-encoder to the GLUE MRPC validation dataset, using prefixed inputs of the form \u201cSentence 1: \u2026\u201d and \u201cSentence 2: \u2026\u201d. Each record corresponds to one source sentence pair from glue_mrpc_validation and contains two fields: prediction, the predicted binary paraphrase label (0 = not paraphrase, 1 = paraphrase), and score, the model\u2019s positive-class score used to derive the prediction. In this workflow, this dataset serves as the prediction table for the validation run and is later joined with the original MRPC labels to compute accuracy, F1, error analysis, and the experiment summary.",
      "distilbert_cross_text_prediction",
      "record_list"
    ],
    [
      "BASE",
      "Per-example prediction outputs from the cross-encoder paraphrase model evaluated on the GLUE MRPC validation set. Each row corresponds to one sentence pair from glue_mrpc_validation and stores two fields: prediction (binary predicted label, where 1 indicates paraphrase and 0 indicates not_paraphrase) and score (the model\u2019s positive-class score for the pair; in this notebook, the softmax probability of the paraphrase class when logits are returned). This dataset is an intermediate inference artifact used to persist row-level model outputs, trace them back to the source MRPC examples, inspect correct and incorrect predictions, and support downstream summary evaluation such as accuracy, F1, and the classification report.",
      "distilbert_cross_text_prediction_cutoff",
      "record_list"
    ],
    [
      "BASE",
      "Summary dataset for the DistilBERT cosine-similarity MRPC validation experiment. It contains an aggregate evaluation record for paraphrase detection on the GLUE MRPC validation split, where sentence1 and sentence2 are encoded with distilbert-base-uncased, the last 4 hidden layers are averaged, mean pooled into sentence embeddings, and classified by cosine similarity using a threshold of 0.85. The dataset structure has 3 fields: accuracy (float), f1 (float), and classification_report (string with per-class precision/recall/F1 and support). In this workflow, it serves as the final experiment-level metrics table summarizing model performance over the full validation set, with provenance linked to both the source dataset glue_mrpc_validation and the per-example prediction dataset cosine_mrpc_mean_similarity_prediction.",
      "distilbert_last4_mean_cosine_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "Row-level prediction outputs for the GLUE MRPC validation set produced by the Hugging Face model textattack/distilbert-base-uncased-MRPC. Each record corresponds to one input sentence pair from glue_mrpc_validation and stores: prediction (final binary class after applying a margin rule), score_pos (softmax score for the paraphrase class), and score_neg (softmax score for the not_paraphrase class). In this workflow, the dataset serves as the persisted model-output table used to trace predictions back to the original validation examples and to support downstream metric computation, error analysis, and experiment summaries.",
      "distilbert_margin_score_prediction_values",
      "record_list"
    ],
    [
      "BASE",
      "This dataset stores the experiment-level evaluation summary for the DistilBERT max-pooling cosine-similarity approach on the GLUE MRPC validation set. It contains a single summary record with three fields: accuracy (float), f1 (float), and classification_report (string). The values are computed by comparing binary paraphrase predictions\u2014generated by thresholding cosine similarity between max-pooled DistilBERT embeddings of sentence pairs\u2014against the ground-truth MRPC labels. In this workflow, the dataset serves as the final aggregated results table for the notebook, capturing overall model performance in a compact form for later inspection, comparison, and lineage tracking back to the validation data and prediction outputs.",
      "distilbert_max_pool_cosine_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "distilbert_mean_cosine_median_threshold_mrpc_summary is a summary dataset containing the evaluation results for the DistilBERT mean-pooled cosine-similarity baseline on the GLUE MRPC validation set. It stores aggregate metrics computed after encoding each sentence pair with distilbert-base-uncased, measuring cosine similarity between the two sentence embeddings, and converting scores to binary paraphrase predictions using the median similarity as the decision threshold. The dataset has three fields: accuracy (float), f1 (float), and classification_report (string with per-class precision/recall/F1 and support). In this workflow, it serves as the final experiment-level output that summarizes model performance over the full validation split, with provenance linked to both the source dataset glue_mrpc_validation and the per-example prediction dataset threshold_cosine_mrpc_similarity_prediction.",
      "distilbert_mean_cosine_median_threshold_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "Summary dataset for the MRPC validation run using distilbert-base-uncased sentence embeddings. It contains aggregate evaluation results for paraphrase prediction on glue_mrpc_validation, where sentence1 and sentence2 are encoded separately, token embeddings are mean-pooled while excluding special tokens ([CLS], [SEP]), cosine similarity is computed between the two sentence embeddings, and a fixed threshold of 0.85 is used to produce binary paraphrase predictions.\n\nStructure: one record with fields accuracy (float), f1 (float), and classification_report (string). The record is linked to the full glue_mrpc_validation input range and to the no_special_cosine_mrpc_similarity_prediction dataset that stores per-example predictions and cosine scores.\n\nRole in workflow: this dataset is the experiment-level evaluation summary, used to capture the overall performance of the no-special-token mean-pooled cosine-similarity baseline on MRPC validation.",
      "distilbert_no_special_tokens_mean_cosine_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "Per-example prediction dataset produced by running the cross-encoder model cross-encoder/quora-distilroberta-base on the glue_mrpc_validation sentence-pair dataset. Each record corresponds to one MRPC validation example and stores two fields: y_pred, the final binary paraphrase prediction after applying a 0.65 threshold, and pos_scores, the model\u2019s positive-class score/probability for the paraphrase label derived from the model output. The records are linked back to the matching source example in glue_mrpc_validation, enabling row-level inspection of predictions, error analysis, and downstream aggregation. In this workflow, this dataset is the main prediction output used to compare model decisions against ground-truth labels and to build the evaluation summary dataset.",
      "distilbert_quora_softmax_prediction",
      "record_list"
    ],
    [
      "BASE",
      "Per-example prediction outputs for the GLUE MRPC validation set generated with the textattack/distilbert-base-uncased-MRPC classifier under two sentence orders. Each record corresponds to one validation example and contains three fields: prediction (final binary label after averaging both orders and thresholding at 0.5), pos_probs (paraphrase probability for the original input order: sentence1, sentence2), and swap_pos_probs (paraphrase probability for the swapped order: sentence2, sentence1). This dataset is the intermediate prediction table used to capture order-sensitive model scores, produce the bidirectional averaged decision, and feed the final evaluation summary.",
      "distilbert_swap_prediction_values",
      "record_list"
    ],
    [
      "BASE",
      "Per-example prediction dataset for the GLUE MRPC validation split generated with the cross-encoder/quora-distilroberta-base model using symmetric inference over sentence order. Each record corresponds to one input sentence pair from glue_mrpc_validation and stores: y_pred (final binary paraphrase prediction after averaging forward and reverse scores and thresholding at 0.5), orig_score (positive-class probability for the original order: sentence1, sentence2), and rev_score (positive-class probability for the reversed order: sentence2, sentence1). This dataset is used as the main prediction artifact in the workflow: it captures model outputs for every validation example, supports error analysis and inspection of order sensitivity, and serves as an input to the downstream summary dataset that reports overall accuracy, F1, and the classification report.",
      "distilbert_symmetric_average_prediction",
      "record_list"
    ],
    [
      "BASE",
      "Summary dataset for the MRPC entailment-logprob-odds experiment on the GLUE MRPC validation split. It contains evaluation results for paraphrase predictions produced from a zero-shot NLI model (typeform/distilbert-base-uncased-mnli), where each sentence pair is scored using the average entailment-vs-contradiction log-odds across both input orders. Structure: one record with columns accuracy (float), f1 (float), and classification_report (string). Its role in this workflow is to provide a compact experiment-level summary of model performance, derived from the full per-example outputs in mrpc_entailment_prediction and the ground-truth labels in glue_mrpc_validation.",
      "entailment_logprob_odds_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "This dataset stores per-example inference outputs from google/flan-t5-small on the GLUE MRPC validation set using a prompted yes/no paraphrase detection setup. Each record corresponds to one input pair from glue_mrpc_validation and contains three fields: prediction (binary label, where 1 indicates the model preferred \u201cyes\u201d and 0 indicates it preferred \u201cno\u201d), yes_logits (the decoder logit for the token \u201cyes\u201d at the answer position), and no_logits (the decoder logit for the token \u201cno\u201d at the answer position). Predictions are produced by prompting the model with the two sentences, forcing the decoder prefix \u201cAnswer:\u201d, and selecting the higher of the yes/no logits. In this workflow, the dataset serves as the main model output table for downstream evaluation, error analysis, and summary metric generation, while preserving a row-level link back to the original MRPC validation examples.",
      "flan_prediction_and_logit_prefix",
      "record_list"
    ],
    [
      "BASE",
      "Per-example prediction dataset for the GLUE MRPC validation set produced by prompting google/flan-t5-small with a yes/no paraphrase question and applying contextual calibration. Each record corresponds to one input sentence pair from glue_mrpc_validation and stores the model\u2019s binary prediction (1 = paraphrase/yes, 0 = not paraphrase/no), the raw first-step logits for the yes and no tokens (raw_yes_logits, raw_no_logits), and the calibrated logits after subtracting baseline logits from a null calibration prompt (cal_yes_logits, cal_no_logits). This record list is the main intermediate output of the workflow: it preserves calibrated model scores for each example, supports error analysis and inspection, and is used to compute the downstream summary metrics in flan_t5_contextual_calibrated_yes_no_mrpc_summary.",
      "flan_prediction_logit_calibrated",
      "record_list"
    ],
    [
      "BASE",
      "flan_prediction_scored is a per-example prediction dataset generated by running google/flan-t5-small on the GLUE MRPC validation set with a yes/no paraphrase prompt. Each record corresponds to one input pair from glue_mrpc_validation and stores the model\u2019s binary prediction and the sequence log-probability scores for the two candidate answers. The fields are: prediction (integer label, where 1 indicates yes/paraphrase and 0 indicates no/not paraphrase), yes_scores (float log-probability of the full answer token sequence for \u201cyes\u201d), and no_scores (float log-probability of the full answer token sequence for \u201cno\u201d). In this workflow, this dataset serves as the scored inference output used to inspect example-level model behavior and to compute downstream summary metrics such as accuracy, F1, and the classification report.",
      "flan_prediction_scored",
      "record_list"
    ],
    [
      "BASE",
      "Aggregate evaluation summary for the flan-t5-small contextual yes/no paraphrase classifier on the GLUE MRPC validation set after logit calibration. This dataset is a record list with one summary record containing the fields: accuracy (float), f1 (float), and classification_report (string with per-class precision/recall/F1 and support for not_paraphrase and paraphrase). It is produced after generating calibrated predictions in flan_prediction_logit_calibrated and compares those predictions against the ground-truth labels in glue_mrpc_validation. Its role in this workflow is to store run-level performance metrics for the full validation set, providing a compact summary of model quality for this notebook execution.",
      "flan_t5_contextual_calibrated_yes_no_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "flan_t5_full_answer_logprob_mrpc_summary is an experiment-level summary dataset for evaluating google/flan-t5-small on the GLUE MRPC validation split using prompt-based yes/no paraphrase prediction with full-answer log-probability scoring. It contains a single record with three fields: accuracy (float), f1 (float), and classification_report (string from sklearn with per-class precision, recall, f1, and support for not_paraphrase and paraphrase). This dataset is produced after generating example-level predictions in flan_prediction_scored and comparing them against the ground-truth MRPC labels. Its role in the workflow is to store the aggregate evaluation results for the entire validation run, linking the underlying input dataset (glue_mrpc_validation) and the per-example prediction dataset (flan_prediction_scored).",
      "flan_t5_full_answer_logprob_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "Summary dataset for the FLAN-T5 symmetric-prompt MRPC evaluation run. It contains a single aggregate record describing model performance on the full glue_mrpc_validation split, computed from predictions stored in google_flan_prediction_swapped. The fields are: accuracy (float, overall classification accuracy), f1 (float, binary F1 score for paraphrase detection), and classification_report (string, the full scikit-learn classification report with precision, recall, F1, and support for both not_paraphrase and paraphrase classes). Its role in this workflow is to provide a compact experiment-level evaluation artifact that links the source validation examples and prediction outputs to final metrics for the notebook/process flan_t5_symmetric_prompt_average_mrpc.",
      "flan_t5_symmetric_prompt_average_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "Summary dataset for the FLAN-T5 MRPC evaluation run using first-step true/false token scoring. It contains aggregate performance results for google/flan-t5-small on the glue_mrpc_validation split, where each example is prompted as a paraphrase detection task and predicted by comparing the first decoder-step logits for the tokens true and false. The record list has three fields: accuracy (float), f1 (float, for the positive/paraphrase class), and classification_report (string containing the full per-class precision/recall/F1 summary). In this workflow, this dataset serves as the experiment-level evaluation artifact that summarizes model performance over the full validation set and links the source validation data with the per-example prediction/logit dataset google_flan_prediction_and_logits.",
      "flan_t5_true_false_first_step_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "glue_mrpc_validation is the validation split of the GLUE MRPC (Microsoft Research Paraphrase Corpus) dataset stored in TableVault for this notebook. Each record contains sentence1, sentence2, label, and idx, where sentence1 and sentence2 are a pair of sentences, label is a binary paraphrase target (1 = paraphrase, 0 = not paraphrase), and idx is the example identifier from the original dataset. This dataset is the ground-truth evaluation input for the workflow: the sentence pairs are tokenized and passed to the pretrained textattack/distilbert-base-uncased-MRPC model, and the labels are used to compute accuracy, F1, error cases, and the final classification report. It serves as the source dataset linked to downstream prediction, mistake-analysis, and summary output records.",
      "glue_mrpc_validation",
      "record_list"
    ],
    [
      "BASE",
      "Per-example inference outputs from google/flan-t5-small on the GLUE MRPC validation set using a prompted true/false paraphrase decision. Each record corresponds to one validation example and is linked to the matching source row in glue_mrpc_validation. The dataset has three fields: prediction (binary model decision, where 1 means the logit for \u201ctrue\u201d is greater than the logit for \u201cfalse\u201d), true_logits (the first-decoder-step logit for the token \u201ctrue\u201d), and false_logits (the first-decoder-step logit for the token \u201cfalse\u201d). In this workflow, this dataset is the stored prediction artifact used to inspect model behavior on individual examples and to support the downstream summary evaluation dataset with accuracy, F1, and classification report.",
      "google_flan_prediction_and_logits",
      "record_list"
    ],
    [
      "BASE",
      "Per-example prediction outputs from google/flan-t5-small on the GLUE MRPC validation set using a yes/no paraphrase prompt evaluated in both original and swapped sentence order. Each record is aligned to one input example from glue_mrpc_validation and contains: prediction (binary paraphrase decision after averaging forward and swapped logits), yes_logits (forward-order logit for \u201cyes\u201d), no_logits (forward-order logit for \u201cno\u201d), swapped_yes_logits (swapped-order logit for \u201cyes\u201d), and swapped_no_logits (swapped-order logit for \u201cno\u201d). This dataset is used as the intermediate model-output table in the workflow, supporting order-symmetric paraphrase prediction, error analysis, and computation of final evaluation metrics in the summary dataset.",
      "google_flan_prediction_swapped",
      "record_list"
    ],
    [
      "BASE",
      "Summary dataset for the bidirectional MRPC evaluation run. It contains aggregate evaluation results for the TextAttack DistilBERT MRPC classifier on the GLUE MRPC validation set, where paraphrase probabilities are computed for both the original sentence order and the swapped sentence order, then averaged before thresholding to make the final prediction.\n\nStructure:\n- accuracy: float overall classification accuracy on the validation set\n- f1: float F1 score for the paraphrase class\n- classification_report: string version of the sklearn classification report, including per-class precision, recall, F1, and support\n\nRole in this workflow:\nThis dataset serves as the experiment-level evaluation summary for the notebook. It records the final performance metrics derived from comparing the averaged bidirectional predictions against the true labels, and links those metrics back to both the source dataset (glue_mrpc_validation) and the per-example prediction dataset (distilbert_swap_prediction_values).",
      "hf_pipeline_mrpc_bidirectional_order_average_summary",
      "record_list"
    ],
    [
      "BASE",
      "This dataset stores the aggregate evaluation results for the notebook\u2019s MRPC margin-rule experiment. It contains a summary record with three fields: accuracy (float), f1 (float), and classification_report (string containing the full sklearn classification report, including per-class precision, recall, f1-score, and support for not_paraphrase and paraphrase). The values are computed by comparing the true labels from glue_mrpc_validation against binary predictions produced from the TextAttack DistilBERT MRPC model, where prediction = 1 when score_pos - score_neg exceeds the configured margin threshold. Its role in the workflow is to provide a compact, final performance summary for the full validation set, linked to both the source validation data and the per-example prediction dataset distilbert_margin_score_prediction_values.",
      "hf_pipeline_mrpc_margin_rule_summary",
      "record_list"
    ],
    [
      "BASE",
      "This dataset stores the aggregate evaluation summary for the DistilBERT MRPC inference run on the GLUE MRPC validation set after converting pipeline raw logits to softmax probabilities. It contains one summary record with three fields: accuracy (overall prediction accuracy), f1 (binary F1 score for paraphrase detection), and classification_report (the full sklearn text report with per-class precision, recall, F1, support, and overall averages). In this workflow, it serves as the experiment-level performance snapshot, linking the source validation examples and the per-example prediction dataset pipeline_distilbert_softmax_probs so that users can quickly inspect overall model quality without recomputing metrics.",
      "hf_pipeline_mrpc_raw_logits_softmax_summary",
      "record_list"
    ],
    [
      "BASE",
      "Summary dataset for the hf_pipeline_mrpc_threshold_070 experiment. It contains a single evaluation record aggregating model performance on the full glue_mrpc_validation split after running the Hugging Face text-classification pipeline with textattack/distilbert-base-uncased-MRPC and converting paraphrase probabilities to binary predictions using a 0.70 threshold. The dataset has three fields: accuracy (float), f1 (float, for the positive paraphrase class), and classification_report (string produced by sklearn, containing per-class precision, recall, f1-score, support, and overall averages). Its role in the workflow is to provide a compact experiment-level summary derived from the validation labels and the per-example predictions stored in pipeline_distilbert_threshold, so the notebook can track and compare final thresholded evaluation results.",
      "hf_pipeline_mrpc_threshold_070_summary",
      "record_list"
    ],
    [
      "BASE",
      "Summary dataset for the min_direction_margin_mrpc workflow. It contains experiment-level evaluation results for paraphrase detection on the GLUE MRPC validation set, where predictions are made by scoring each sentence pair in both directions with an MNLI model and using the minimum entailment-minus-contradiction margin as the decision signal. The dataset has one record with three fields: accuracy (float), f1 (float), and classification_report (string). Its role is to store the final aggregated performance summary derived from the source validation examples and the per-example prediction dataset mrpc_min_margin_prediction, so future users can quickly inspect the overall outcome of this notebook without recomputing metrics.",
      "min_direction_margin_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "Row-level prediction dataset for the GLUE MRPC validation set produced by the sentence-transformers/paraphrase-MiniLM-L6-v2 model. Each record corresponds to one sentence pair from glue_mrpc_validation and stores two fields: prediction (binary label, where 0 = not_paraphrase and 1 = paraphrase) and score (cosine similarity between the normalized embeddings of sentence1 and sentence2). Predictions are generated by applying a fixed threshold of 0.78 to the cosine similarity score. In this workflow, this dataset serves as the per-example model output used for downstream evaluation, error analysis, and creation of the summary metrics dataset.",
      "minilm_cosine_threshold_prediction",
      "record_list"
    ],
    [
      "BASE",
      "Model prediction outputs for the GLUE MRPC validation set generated by the textattack/distilbert-base-uncased-MRPC sequence classification model. Each record corresponds to one sentence-pair example in glue_mrpc_validation and stores the model\u2019s predicted class label for paraphrase detection. The dataset has a single field, prediction, which is an integer class ID (0 = not paraphrase, 1 = paraphrase). In this workflow, it serves as the inference output table linked back to the source validation examples and is used to compute evaluation metrics, compare predictions with ground-truth labels, and identify error cases.",
      "mrpc_distilbert_predictions",
      "record_list"
    ],
    [
      "BASE",
      "mrpc_entailment_prediction contains per-example prediction outputs for the GLUE MRPC validation set generated with the typeform/distilbert-base-uncased-mnli NLI model. Each record corresponds to one validation pair from glue_mrpc_validation and stores three fields: prediction (binary paraphrase decision obtained by thresholding the averaged score at 0), dir12 (entailment-minus-contradiction log-probability score for sentence1 \u2192 sentence2), and dir21 (the same score for sentence2 \u2192 sentence1). The dataset is aligned one-to-one with the source MRPC examples through input item indexing. Its role in this workflow is to capture the model\u2019s directional entailment-based evidence and final paraphrase prediction for downstream evaluation, error analysis, and summary metric computation.",
      "mrpc_entailment_prediction",
      "record_list"
    ],
    [
      "BASE",
      "mrpc_gate_margin_prediction is a per-example prediction dataset derived from the GLUE MRPC validation split. For each validation pair (sentence1, sentence2), the notebook runs the NLI model typeform/distilbert-base-uncased-mnli in both input orders, sentence1\u2192sentence2 and sentence2\u2192sentence1, and stores the resulting decision signals used for paraphrase classification. The dataset has four fields: prediction (final binary paraphrase prediction, 1 for paraphrase and 0 for not paraphrase), margin_12 (entailment logit minus contradiction logit for sentence1 paired with sentence2), margin_21 (the same margin for the reversed order), and gate (boolean flag that is true only when neither direction\u2019s argmax label is contradiction). The final prediction is produced by requiring gate = true and the average of margin_12 and margin_21 to be greater than 0. This dataset serves as the main intermediate output of the workflow: it preserves the model\u2019s directional margin scores and final gated prediction for each MRPC example, and it is then used to compute the summary accuracy, F1, and classification report.",
      "mrpc_gate_margin_prediction",
      "record_list"
    ],
    [
      "BASE",
      "Per-example prediction dataset for the GLUE MRPC validation split, generated by running the sentence pairs through the typeform/distilbert-base-uncased-mnli model in both input orders. Each record corresponds to one MRPC validation example and is linked to the matching row in glue_mrpc_validation. The dataset has three fields: prediction (binary paraphrase decision, where 1 indicates paraphrase and 0 indicates not paraphrase), gap_12 (entailment probability minus contradiction probability for sentence1\u2192sentence2), and gap_21 (the same probability gap for sentence2\u2192sentence1). In this workflow, it serves as the stored per-instance model output used to inspect directional confidence, compare predictions with ground-truth MRPC labels, and build the downstream summary metrics in softmax_gap_mean_mrpc_summary.",
      "mrpc_mean_gap_prediction",
      "record_list"
    ],
    [
      "BASE",
      "mrpc_min_margin_prediction is an example-level prediction dataset derived from the GLUE MRPC validation split. For each sentence pair in glue_mrpc_validation, it stores the binary paraphrase prediction produced by a zero-shot NLI model (typeform/distilbert-base-uncased-mnli) and the confidence score used to make that prediction.\n\nEach record corresponds to one MRPC validation example and has two fields: prediction, an integer label where 1 indicates paraphrase and 0 indicates not_paraphrase; and min_margin, a float equal to the minimum of the entailment-versus-contradiction logit margins computed in both input directions, sentence1\u2192sentence2 and sentence2\u2192sentence1. The prediction is defined as 1 when min_margin > 0, otherwise 0.\n\nIn this workflow, this dataset serves as the per-example output of the min-direction-margin inference step. It is used as the input to downstream evaluation and summarization, including accuracy, F1, classification report generation, and error analysis.",
      "mrpc_min_margin_prediction",
      "record_list"
    ],
    [
      "BASE",
      "Per-example prediction dataset for the GLUE MRPC validation split, produced by applying the typeform/distilbert-base-uncased-mnli model as a zero-shot paraphrase detector. Each record corresponds to one sentence pair from glue_mrpc_validation and stores: prediction (binary paraphrase decision, where 1 indicates paraphrase and 0 indicates not_paraphrase), score_12 (entailment logit minus max(contradiction, neutral) for sentence1 -> sentence2), and score_21 (the same score for sentence2 -> sentence1). The final prediction is derived from the average of the two directional scores. In this workflow, this dataset captures the model\u2019s per-example outputs for downstream evaluation, inspection of mistakes, and construction of the overall summary metrics.",
      "mrpc_neutral_penalty_prediction",
      "record_list"
    ],
    [
      "BASE",
      "Subset of error cases from the GLUE MRPC validation run using the textattack/distilbert-base-uncased-MRPC model. Each record captures one misclassified sentence pair and includes the fields: idx (validation-set position), sentence1, sentence2, true (ground-truth binary label), and pred (model-predicted binary label). This dataset is created by selecting the first 10 examples where the model prediction differs from the true label, and each record is linked back to the corresponding source example in glue_mrpc_validation and its entry in mrpc_distilbert_predictions. Its role in the workflow is error analysis: it provides a compact, inspectable sample of model failures for diagnosing paraphrase detection mistakes.",
      "mrpc_paraphrase_inference_distilbert_mistakes",
      "record_list"
    ],
    [
      "BASE",
      "This dataset contains the final evaluation summary for the textattack/distilbert-base-uncased-MRPC model on the GLUE MRPC validation split. It is a small output table with one record summarizing model performance over the full validation dataset.\n\nFields:\n- accuracy: overall classification accuracy on the validation set\n- f1: F1 score for the paraphrase classification task\n- classification_report: full text report from sklearn including precision, recall, F1, and support for the not_paraphrase and paraphrase classes\n\nIn this workflow, this dataset serves as the final results artifact. It is created after running batched inference on sentence pairs, comparing predictions against ground-truth labels, and aggregating the metrics. The record is linked to the full validation input dataset and the prediction dataset so a user can trace the reported metrics back to the underlying examples and model outputs.",
      "mrpc_paraphrase_inference_distilbert_output",
      "record_list"
    ],
    [
      "BASE",
      "Aggregate evaluation summary for the neutral-penalized margin MRPC experiment. This dataset contains a single summary record computed from the GLUE MRPC validation set and the derived mrpc_neutral_penalty_prediction records. Its fields are: accuracy (float, overall prediction accuracy), f1 (float, F1 score for the paraphrase class), and classification_report (string, full sklearn classification report with per-class precision, recall, F1, and support). In this workflow, it serves as the compact experiment-level output used to record and retrieve overall model performance after scoring sentence pairs with the MNLI model and converting the bidirectional entailment-vs.-non-entailment margin into paraphrase predictions.",
      "neutral_penalized_margin_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "Per-example prediction dataset for the GLUE MRPC validation split. Each record corresponds to one sentence pair from glue_mrpc_validation and stores the model output from this notebook\u2019s similarity-based paraphrase detection pipeline using distilbert-base-uncased embeddings. The fields are: prediction (binary label, 1 if the cosine similarity between the two sentence embeddings is at least 0.85, otherwise 0) and cosine_scores (the raw cosine similarity score as a float). The embeddings are produced by mean-pooling DistilBERT token representations while excluding special tokens such as [CLS] and [SEP], followed by L2 normalization. In this workflow, this dataset serves as the detailed per-row inference output that links back to the original MRPC validation examples and is then used to compute and document overall evaluation metrics in the summary dataset.",
      "no_special_cosine_mrpc_similarity_prediction",
      "record_list"
    ],
    [
      "BASE",
      "Per-example inference outputs for the GLUE MRPC validation set produced by the Hugging Face text-classification pipeline using textattack/distilbert-base-uncased-MRPC. Each record corresponds to one input sentence pair from glue_mrpc_validation and stores the model\u2019s predicted class and the softmax probability of the positive/paraphrase class. The dataset is structured as one row per validation example with fields for prediction (integer class label from argmax) and the positive-class probability (intended as positive_probs; in the appended records this is written as paraphrase_probs). In this workflow, this dataset serves as the main prediction artifact linking model outputs back to the source validation examples and is used downstream to compute accuracy, F1, and the classification report summary.",
      "pipeline_distilbert_softmax_probs",
      "record_list"
    ],
    [
      "BASE",
      "Per-example inference results from the Hugging Face model textattack/distilbert-base-uncased-MRPC run on the glue_mrpc_validation dataset. Each record corresponds to one sentence pair from the MRPC validation split and stores two fields: prediction, a binary label produced by thresholding the model\u2019s paraphrase probability at 0.70; and paraphrase_probs, the softmax probability assigned to the positive paraphrase class. Records are linked back to the matching input example in glue_mrpc_validation. This dataset serves as the main prediction output of the workflow and is used for downstream evaluation, error analysis, and creation of the run-level summary dataset.",
      "pipeline_distilbert_threshold",
      "record_list"
    ],
    [
      "BASE",
      "This dataset stores the evaluation summary for the notebook run quora_cross_encoder_prefixed_sentence_tags_mrpc on the GLUE MRPC validation set. It contains a summary record of the cross-encoder paraphrase detection results produced from the prediction dataset distilbert_cross_text_prediction. Its fields are: accuracy (float, overall classification accuracy), f1 (float, binary F1 score for paraphrase detection), and classification_report (string, the full sklearn classification report with precision, recall, F1, and support for the not_paraphrase and paraphrase classes). In this workflow, it serves as the experiment-level metrics dataset that aggregates model performance over the full validation set and links the source inputs from glue_mrpc_validation and the generated predictions.",
      "quora_cross_encoder_prefixed_sentence_tags_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "Experiment-level evaluation summary for the notebook run using the cross-encoder/quora-distilroberta-base model on the GLUE MRPC validation split with a paraphrase decision threshold of 0.65 applied to the positive softmax score. This dataset contains a single summary record with the fields: accuracy (float), f1 (float), and classification_report (string produced by sklearn, summarizing precision, recall, f1-score, and support for the not_paraphrase and paraphrase classes). It is derived from the full glue_mrpc_validation dataset and the corresponding per-example predictions stored in distilbert_quora_softmax_prediction, and its role is to capture the overall performance of this experiment in a compact, queryable form for comparison, tracking, and documentation.",
      "quora_cross_encoder_softmax_threshold_065_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "Summary dataset for the notebook\u2019s evaluation run of the cross-encoder/quora-distilroberta-base model on the GLUE MRPC validation set using symmetric scoring. It contains aggregate performance results computed after predicting each sentence pair in both original and reversed order, averaging the two positive-class scores, and thresholding at 0.5.\n\nStructure: a record list with columns accuracy, f1, and classification_report. accuracy is the overall validation accuracy, f1 is the binary F1 score for paraphrase detection, and classification_report is the full sklearn text report summarizing class-wise precision, recall, F1, and support for the labels not_paraphrase and paraphrase.\n\nRole in the workflow: this dataset stores the run-level evaluation summary for the prediction dataset distilbert_symmetric_average_prediction, linked to both the source input dataset glue_mrpc_validation and the generated prediction records. It is intended as the compact experiment result table for comparing or auditing this notebook run.",
      "quora_cross_encoder_symmetric_average_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "This dataset stores the evaluation summary for the notebook run that applies the cross-encoder/quora-distilroberta-base model to the GLUE MRPC validation set after text normalization. It contains a single aggregated record rather than per-example predictions. The fields are: accuracy (float), f1 (float), and classification_report (string with the full sklearn classification report for the not_paraphrase/paraphrase labels). Its role in the workflow is to capture experiment-level performance metrics derived from comparing the normalized-text predictions in distilbert-normalized-text-prediction against the ground-truth labels in glue_mrpc_validation, providing a compact summary of model performance for this run.",
      "quora_cross_encoder_text_normalized_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "Per-example prediction dataset for the GLUE MRPC validation set, generated by comparing sentence embeddings from sentence-transformers/all-MiniLM-L6-v2. Each record contains a single field, prediction, which is a binary label: 1 when the L2 distance between the normalized embeddings of sentence1 and sentence2 is less than or equal to the fixed threshold (0.63), and 0 otherwise. The dataset has one record per validation example and is linked back to the original glue_mrpc_validation row as well as the corresponding sentence 1 and sentence 2 embedding entries. Its role in this workflow is to store the model\u2019s threshold-based paraphrase decisions so they can be inspected, traced to source inputs, and used to compute evaluation metrics such as accuracy, F1, and the classification report.",
      "sentence_transformers_mrpc_prediction_distance",
      "record_list"
    ],
    [
      "BASE",
      "Binary paraphrase predictions for the GLUE MRPC validation set, generated by encoding each sentence pair with sentence-transformers/all-MiniLM-L6-v2 using max_seq_length=64, computing the cosine similarity between the normalized sentence1 and sentence2 embeddings, and applying a threshold of 0.80. This record list contains one row per validation example with a single field, prediction, where 1 indicates predicted paraphrase and 0 indicates predicted non-paraphrase. Each record is linked back to the corresponding source example in glue_mrpc_validation and to the two embedding lists sentence-transformers-sentence-1-max64 and sentence-transformers-sentence-2-max64. In this workflow, the dataset serves as the stored model output used for downstream evaluation, error analysis, and experiment summary reporting.",
      "sentence_transformers_mrpc_prediction_max64",
      "record_list"
    ],
    [
      "BASE",
      "sentence_transformers_mrpc_prediction_threshold is a record list containing the per-example binary predictions produced on the GLUE MRPC validation set by a SentenceTransformer paraphrase model. Each record has a single field, prediction, where 1 indicates the sentence pair is predicted to be a paraphrase and 0 indicates not_paraphrase. Predictions are generated by encoding sentence1 and sentence2 with sentence-transformers/paraphrase-MiniLM-L3-v2, computing their cosine similarity via normalized embedding dot product, and applying a fixed threshold of 0.74. The dataset is aligned one-to-one with glue_mrpc_validation and is linked to the corresponding sentence-pair embeddings, making it the main stored output used for error analysis, metric computation, and creation of the workflow summary dataset.",
      "sentence_transformers_mrpc_prediction_threshold",
      "record_list"
    ],
    [
      "BASE",
      "Binary prediction table for the GLUE MRPC validation set produced by the sentence-transformers/all-distilroberta-v1 model. Each record corresponds to one validation example and stores a single field, prediction, where 1 indicates the sentence pair is predicted to be a paraphrase and 0 indicates not_paraphrase. Predictions are generated by computing the cosine similarity between the normalized embeddings of sentence1 and sentence2 and applying a fixed threshold of 0.72. This dataset serves as the model output layer in the workflow, linking each prediction back to the original MRPC example and the two sentence embedding datasets, and it is used downstream to compute accuracy, F1, error analysis, and the experiment summary.",
      "sentence_transformers_mrpc_prediction_threshold_2",
      "record_list"
    ],
    [
      "BASE",
      "Summary record list for the MRPC validation evaluation of a threshold-based paraphrase detection workflow using sentence-transformers/all-distilroberta-v1. This dataset contains experiment-level metrics computed by comparing predicted paraphrase labels from cosine similarity scores between sentence1 and sentence2 embeddings against the ground-truth labels in glue_mrpc_validation. Its structure is a record list with three fields: accuracy (float), f1 (float), and classification_report (string containing the full per-class evaluation report). In this notebook, it serves as the final aggregated result of the process, linking the full GLUE MRPC validation set and the generated prediction record list into a compact summary of model performance for the chosen cosine threshold.",
      "st_all_distilroberta_v1_cosine_threshold_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "Summary dataset for the MRPC validation run using sentence-transformers/all-MiniLM-L6-v2 sentence embeddings and an L2 distance threshold classifier. It contains a single record that aggregates evaluation results over the full glue_mrpc_validation dataset after predicting whether each sentence pair is a paraphrase based on whether the embedding distance is less than or equal to the chosen threshold (0.63).\n\nFields:\naccuracy: overall classification accuracy on the validation set\nf1: F1 score for the paraphrase class\nclassification_report: full text report from sklearn with precision, recall, F1, and support for both not_paraphrase and paraphrase classes\n\nRole in the workflow:\nThis dataset stores the experiment-level evaluation summary for the notebook. It provides a compact record of model performance derived from the per-example prediction dataset sentence_transformers_mrpc_prediction_distance and linked to the full glue_mrpc_validation input range.",
      "st_all_minilm_l6_l2_distance_threshold_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "Summary dataset for the MRPC validation experiment using sentence-transformers/all-MiniLM-L6-v2 with max_seq_length=64 and cosine-similarity thresholding. It contains aggregate evaluation results for the prediction run, not per-example data. The record list has three fields: accuracy (float), f1 (float), and classification_report (string with the full class-wise sklearn report for not_paraphrase vs paraphrase). In this workflow, it stores the final performance summary of the predicted paraphrase labels generated from cosine scores between sentence1 and sentence2 embeddings on glue_mrpc_validation, providing a compact experiment-level result linked back to the source validation set and prediction outputs.",
      "st_all_minilm_l6_max_seq_len_64_cosine_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "This dataset stores the run-level evaluation summary for the SentenceTransformer bi-encoder cosine-similarity paraphrase detection experiment on the GLUE MRPC validation set. It contains a single summary record rather than per-example predictions. The fields are: accuracy (float), f1 (float), and classification_report (string with class-wise precision, recall, and F1 statistics). In this workflow, it serves as the compact results table that aggregates model performance after generating sentence embeddings, scoring sentence pairs with cosine similarity, applying a fixed decision threshold, and comparing predictions against the MRPC ground-truth labels.",
      "st_paraphrase_minilm_l3_cosine_threshold_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "This dataset stores the evaluation summary for the paraphrase detection workflow using sentence-transformers/paraphrase-MiniLM-L6-v2 on the GLUE MRPC validation set with cosine-similarity thresholding at 0.78. It contains a single summary record with three fields: accuracy (float), f1 (float), and classification_report (string). The metrics are computed by comparing thresholded cosine-similarity predictions from the minilm_cosine_threshold_prediction dataset against the ground-truth labels in glue_mrpc_validation. Its role in this workflow is to provide a compact, experiment-level performance summary for the notebook, linking the full validation set and per-example predictions to aggregate evaluation results.",
      "st_paraphrase_minilm_l6_cosine_threshold_mrpc_summary",
      "record_list"
    ]
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 1814 | 33 | 10 | 0 | 1.168s | 0.018s |

---

## Turn 2 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da5304d654819ba6d52333f0c92800`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_xOvxpF9pQ5b1QhxmMn0YV10N",
    "output": "{\"ok\": true, \"result\": [[\"BASE\", \"sentence-transformers-sentence-1-distance_threshold is an embedding dataset containing one 384-dimensional sentence embedding for the sentence1 field of each example in the GLUE MRPC validation set. Each item is a normalized dense vector generated with the sentence-transformers/all-MiniLM-L6-v2 model, and each embedding is linked back to the corresponding source row in glue_mrpc_validation through the input_items index mapping. This dataset does not store raw text columns itself; its primary field is the embedding vector for sentence1. In this workflow, it serves as the sentence1 representation used with the matching sentence-transformers-sentence-2-distance_threshold embeddings to compute L2 distances, apply a fixed distance threshold, and produce paraphrase predictions.\", \"sentence-transformers-sentence-1-distance_threshold\", \"embedding_list\"], [\"BASE\", \"Embedding list containing one 384-dimensional normalized sentence embedding per row for the sentence1 field of the GLUE MRPC validation dataset. Each embedding is generated with the sentence-transformers/all-MiniLM-L6-v2 model using max_seq_length=64, so inputs may be truncated beyond 64 tokens. Structure: this dataset stores a single embedding vector for each original example and is linked back to the corresponding row in glue_mrpc_validation via input item indices. In this workflow, it provides the vector representation of the first sentence in each pair, which is later compared with the matching sentence-transformers-sentence-2-max64 embedding using cosine similarity to produce paraphrase predictions.\", \"sentence-transformers-sentence-1-max64\", \"embedding_list\"], [\"BASE\", \"This dataset stores the normalized SentenceTransformer embeddings for the sentence1 field of each example in the GLUE MRPC validation set. Each item is a single 384-dimensional float vector produced by the model sentence-transformers/paraphrase-MiniLM-L3-v2, with one embedding per input row and lineage linked back to the corresponding glue_mrpc_validation record.\\n\\nStructure: an embedding list with ndim=384. There are no tabular feature columns; each entry consists of the embedding vector plus metadata links to the source row in glue_mrpc_validation.\\n\\nRole in the workflow: this dataset represents the first sentence in each MRPC pair in embedding space. These vectors are used with the corresponding sentence-2 embeddings to compute cosine similarity scores, which are then thresholded (0.74) to generate paraphrase predictions.\", \"sentence-transformers-sentence-1-threshold\", \"embedding_list\"], [\"BASE\", \"This dataset stores the sentence embeddings for the sentence1 field of the GLUE MRPC validation set. Each item is a 768-dimensional float vector produced by the sentence-transformers/all-distilroberta-v1 model with normalized embeddings enabled, so dot products correspond to cosine similarity. The dataset is structured as an embedding list: one embedding per MRPC validation example, with each embedding linked to the corresponding row in glue_mrpc_validation through input item provenance. In this workflow, it provides the first-sentence representation used with the matching sentence-transformers-sentence-2-threshold_2 embeddings to compute similarity scores and apply a 0.72 threshold for paraphrase prediction.\", \"sentence-transformers-sentence-1-threshold_2\", \"embedding_list\"], [\"BASE\", \"This dataset stores one normalized sentence embedding per example for the sentence2 field in the GLUE MRPC validation split. Each item is a 384-dimensional float vector generated by the sentence-transformers/all-MiniLM-L6-v2 model, with each embedding linked back to the corresponding source row in glue_mrpc_validation via input item lineage. Structure: an embedding list where each entry contains a single 384-length embedding vector and its association to the matching MRPC example index. In this workflow, these sentence2 embeddings are paired with the corresponding sentence1 embeddings from sentence-transformers-sentence-1-distance_threshold, and the L2 distance between the two vectors is used with a fixed threshold to predict whether the sentence pair is a paraphrase.\", \"sentence-transformers-sentence-2-distance_threshold\", \"embedding_list\"], [\"BASE\", \"Embedding dataset containing one 384-dimensional normalized sentence embedding per row for the sentence2 field of each example in the GLUE MRPC validation set. Each vector was produced with the sentence-transformers/all-MiniLM-L6-v2 model using a maximum sequence length of 64, so it represents the truncated second sentence in a paraphrase pair. The dataset structure is an embedding list: each item stores a single 384-float embedding and is linked back to the corresponding row in glue_mrpc_validation. In this workflow, these sentence2 embeddings are paired with the matching sentence-transformers-sentence-1-max64 embeddings to compute cosine similarity scores and generate paraphrase predictions.\", \"sentence-transformers-sentence-2-max64\", \"embedding_list\"], [\"BASE\", \"sentence-transformers-sentence-2-threshold is an embedding dataset containing one normalized 384-dimensional sentence embedding for the sentence2 field of each example in the GLUE MRPC validation set. Each entry corresponds 1-to-1 with a row in glue_mrpc_validation and is linked back to the source record through input_items, so the dataset structure is an ordered list of embedding vectors plus provenance to the original example index range. The embeddings are produced with the sentence-transformers/paraphrase-MiniLM-L3-v2 model and are intended to represent the second sentence in each MRPC pair. In this workflow, this dataset is used together with the matching sentence-transformers-sentence-1-threshold embeddings to compute cosine similarity scores and generate threshold-based paraphrase predictions.\", \"sentence-transformers-sentence-2-threshold\", \"embedding_list\"], [\"BASE\", \"This dataset stores the sentence embedding for the second sentence (sentence2) of each example in the GLUE MRPC validation set. It is an embedding list with one row per MRPC record, where each item contains a 768-dimensional, L2-normalized vector produced by the sentence-transformers/all-distilroberta-v1 model, and each embedding is linked back to the corresponding source row in glue_mrpc_validation through the input_items index range [i, i+1]. In this workflow, these sentence2 embeddings are paired with the corresponding sentence1 embeddings from sentence-transformers-sentence-1-threshold_2, and their dot product is used as cosine similarity to make threshold-based paraphrase predictions.\", \"sentence-transformers-sentence-2-threshold_2\", \"embedding_list\"], [\"BASE\", \"Summary dataset for the MRPC validation evaluation of the consensus-then-average-margin inference method. It contains aggregate performance results computed by comparing the generated paraphrase predictions against the true labels from glue_mrpc_validation, using prediction records stored in mrpc_gate_margin_prediction. The dataset is structured as a record list with columns: accuracy (float), f1 (float), and classification_report (string containing the full per-class sklearn classification report for not_paraphrase and paraphrase). In this workflow, it serves as the final evaluation artifact for the notebook, linking the full MRPC validation set and the per-example prediction dataset to a compact summary of model performance.\", \"consensus_then_avg_margin_mrpc_summary\", \"record_list\"], [\"BASE\", \"This dataset stores per-example paraphrase predictions for the GLUE MRPC validation set produced by a DistilBERT-based cosine similarity pipeline. For each sentence pair from glue_mrpc_validation, the notebook encodes sentence1 and sentence2 with distilbert-base-uncased, applies masked max pooling to the token embeddings, computes the cosine similarity between the two normalized sentence embeddings, and converts that score to a binary prediction using a threshold of 0.85.\\n\\nStructure:\\n- prediction: integer binary label predicted by the similarity rule (1 = paraphrase, 0 = not paraphrase)\\n- cosine_scores: float cosine similarity between the max-pooled embeddings of the two sentences\\n\\nEach record corresponds to one input sentence pair and is linked back to the source validation examples through input_items. In this workflow, the dataset serves as the main model-output table for downstream evaluation, inspection of correct and incorrect predictions, and creation of the final summary metrics dataset.\", \"cosine_mrpc_max_pool_similarity_prediction\", \"record_list\"], [\"BASE\", \"This dataset stores per-example paraphrase predictions for the GLUE MRPC validation set produced by this notebook\\u2019s embedding-similarity baseline. Each record corresponds to one sentence pair from glue_mrpc_validation and contains two fields: prediction, a binary label (1 if the pair is predicted to be a paraphrase, 0 otherwise), and similarities, the cosine similarity score between the L2-normalized sentence embeddings of sentence1 and sentence2. The embeddings are generated with distilbert-base-uncased by averaging the last 4 hidden layers at the token level and then mean-pooling across tokens. Predictions are created by applying a fixed threshold of 0.85 to the similarity score. In this workflow, this dataset is the intermediate model output used to inspect individual examples, analyze errors, and compute the final evaluation summary in distilbert_last4_mean_cosine_mrpc_summary.\", \"cosine_mrpc_mean_similarity_prediction\", \"record_list\"], [\"BASE\", \"Per-example prediction dataset for the GLUE MRPC validation split. Each record corresponds to one sentence pair from glue_mrpc_validation and stores the output of a simple paraphrase classifier built from DistilBERT sentence embeddings. The dataset has two fields: prediction, a binary label where 1 means paraphrase and 0 means not paraphrase, produced by thresholding the cosine similarity at 0.85; and score, the raw cosine similarity between the L2-normalized first-token embeddings of sentence1 and sentence2 from distilbert-base-uncased. In this workflow, this dataset is the main record of model inference results, used for error analysis, inspection of individual examples, and as input to the downstream summary dataset distilbert_cls_cosine_mrpc_summary.\", \"cosine_mrpc_threshold_score\", \"record_list\"], [\"BASE\", \"distilbert_cross_text_prediction stores per-example model outputs generated by applying the cross-encoder/quora-distilroberta-base cross-encoder to the GLUE MRPC validation dataset, using prefixed inputs of the form \\u201cSentence 1: \\u2026\\u201d and \\u201cSentence 2: \\u2026\\u201d. Each record corresponds to one source sentence pair from glue_mrpc_validation and contains two fields: prediction, the predicted binary paraphrase label (0 = not paraphrase, 1 = paraphrase), and score, the model\\u2019s positive-class score used to derive the prediction. In this workflow, this dataset serves as the prediction table for the validation run and is later joined with the original MRPC labels to compute accuracy, F1, error analysis, and the experiment summary.\", \"distilbert_cross_text_prediction\", \"record_list\"], [\"BASE\", \"Per-example prediction outputs from the cross-encoder paraphrase model evaluated on the GLUE MRPC validation set. Each row corresponds to one sentence pair from glue_mrpc_validation and stores two fields: prediction (binary predicted label, where 1 indicates paraphrase and 0 indicates not_paraphrase) and score (the model\\u2019s positive-class score for the pair; in this notebook, the softmax probability of the paraphrase class when logits are returned). This dataset is an intermediate inference artifact used to persist row-level model outputs, trace them back to the source MRPC examples, inspect correct and incorrect predictions, and support downstream summary evaluation such as accuracy, F1, and the classification report.\", \"distilbert_cross_text_prediction_cutoff\", \"record_list\"], [\"BASE\", \"Summary dataset for the DistilBERT cosine-similarity MRPC validation experiment. It contains an aggregate evaluation record for paraphrase detection on the GLUE MRPC validation split, where sentence1 and sentence2 are encoded with distilbert-base-uncased, the last 4 hidden layers are averaged, mean pooled into sentence embeddings, and classified by cosine similarity using a threshold of 0.85. The dataset structure has 3 fields: accuracy (float), f1 (float), and classification_report (string with per-class precision/recall/F1 and support). In this workflow, it serves as the final experiment-level metrics table summarizing model performance over the full validation set, with provenance linked to both the source dataset glue_mrpc_validation and the per-example prediction dataset cosine_mrpc_mean_similarity_prediction.\", \"distilbert_last4_mean_cosine_mrpc_summary\", \"record_list\"], [\"BASE\", \"Row-level prediction outputs for the GLUE MRPC validation set produced by the Hugging Face model textattack/distilbert-base-uncased-MRPC. Each record corresponds to one input sentence pair from glue_mrpc_validation and stores: prediction (final binary class after applying a margin rule), score_pos (softmax score for the paraphrase class), and score_neg (softmax score for the not_paraphrase class). In this workflow, the dataset serves as the persisted model-output table used to trace predictions back to the original validation examples and to support downstream metric computation, error analysis, and experiment summaries.\", \"distilbert_margin_score_prediction_values\", \"record_list\"], [\"BASE\", \"This dataset stores the experiment-level evaluation summary for the DistilBERT max-pooling cosine-similarity approach on the GLUE MRPC validation set. It contains a single summary record with three fields: accuracy (float), f1 (float), and classification_report (string). The values are computed by comparing binary paraphrase predictions\\u2014generated by thresholding cosine similarity between max-pooled DistilBERT embeddings of sentence pairs\\u2014against the ground-truth MRPC labels. In this workflow, the dataset serves as the final aggregated results table for the notebook, capturing overall model performance in a compact form for later inspection, comparison, and lineage tracking back to the validation data and prediction outputs.\", \"distilbert_max_pool_cosine_mrpc_summary\", \"record_list\"], [\"BASE\", \"distilbert_mean_cosine_median_threshold_mrpc_summary is a summary dataset containing the evaluation results for the DistilBERT mean-pooled cosine-similarity baseline on the GLUE MRPC validation set. It stores aggregate metrics computed after encoding each sentence pair with distilbert-base-uncased, measuring cosine similarity between the two sentence embeddings, and converting scores to binary paraphrase predictions using the median similarity as the decision threshold. The dataset has three fields: accuracy (float), f1 (float), and classification_report (string with per-class precision/recall/F1 and support). In this workflow, it serves as the final experiment-level output that summarizes model performance over the full validation split, with provenance linked to both the source dataset glue_mrpc_validation and the per-example prediction dataset threshold_cosine_mrpc_similarity_prediction.\", \"distilbert_mean_cosine_median_threshold_mrpc_summary\", \"record_list\"], [\"BASE\", \"Summary dataset for the MRPC validation run using distilbert-base-uncased sentence embeddings. It contains aggregate evaluation results for paraphrase prediction on glue_mrpc_validation, where sentence1 and sentence2 are encoded separately, token embeddings are mean-pooled while excluding special tokens ([CLS], [SEP]), cosine similarity is computed between the two sentence embeddings, and a fixed threshold of 0.85 is used to produce binary paraphrase predictions.\\n\\nStructure: one record with fields accuracy (float), f1 (float), and classification_report (string). The record is linked to the full glue_mrpc_validation input range and to the no_special_cosine_mrpc_similarity_prediction dataset that stores per-example predictions and cosine scores.\\n\\nRole in workflow: this dataset is the experiment-level evaluation summary, used to capture the overall performance of the no-special-token mean-pooled cosine-similarity baseline on MRPC validation.\", \"distilbert_no_special_tokens_mean_cosine_mrpc_summary\", \"record_list\"], [\"BASE\", \"Per-example prediction dataset produced by running the cross-encoder model cross-encoder/quora-distilroberta-base on the glue_mrpc_validation sentence-pair dataset. Each record corresponds to one MRPC validation example and stores two fields: y_pred, the final binary paraphrase prediction after applying a 0.65 threshold, and pos_scores, the model\\u2019s positive-class score/probability for the paraphrase label derived from the model output. The records are linked back to the matching source example in glue_mrpc_validation, enabling row-level inspection of predictions, error analysis, and downstream aggregation. In this workflow, this dataset is the main prediction output used to compare model decisions against ground-truth labels and to build the evaluation summary dataset.\", \"distilbert_quora_softmax_prediction\", \"record_list\"], [\"BASE\", \"Per-example prediction outputs for the GLUE MRPC validation set generated with the textattack/distilbert-base-uncased-MRPC classifier under two sentence orders. Each record corresponds to one validation example and contains three fields: prediction (final binary label after averaging both orders and thresholding at 0.5), pos_probs (paraphrase probability for the original input order: sentence1, sentence2), and swap_pos_probs (paraphrase probability for the swapped order: sentence2, sentence1). This dataset is the intermediate prediction table used to capture order-sensitive model scores, produce the bidirectional averaged decision, and feed the final evaluation summary.\", \"distilbert_swap_prediction_values\", \"record_list\"], [\"BASE\", \"Per-example prediction dataset for the GLUE MRPC validation split generated with the cross-encoder/quora-distilroberta-base model using symmetric inference over sentence order. Each record corresponds to one input sentence pair from glue_mrpc_validation and stores: y_pred (final binary paraphrase prediction after averaging forward and reverse scores and thresholding at 0.5), orig_score (positive-class probability for the original order: sentence1, sentence2), and rev_score (positive-class probability for the reversed order: sentence2, sentence1). This dataset is used as the main prediction artifact in the workflow: it captures model outputs for every validation example, supports error analysis and inspection of order sensitivity, and serves as an input to the downstream summary dataset that reports overall accuracy, F1, and the classification report.\", \"distilbert_symmetric_average_prediction\", \"record_list\"], [\"BASE\", \"Summary dataset for the MRPC entailment-logprob-odds experiment on the GLUE MRPC validation split. It contains evaluation results for paraphrase predictions produced from a zero-shot NLI model (typeform/distilbert-base-uncased-mnli), where each sentence pair is scored using the average entailment-vs-contradiction log-odds across both input orders. Structure: one record with columns accuracy (float), f1 (float), and classification_report (string). Its role in this workflow is to provide a compact experiment-level summary of model performance, derived from the full per-example outputs in mrpc_entailment_prediction and the ground-truth labels in glue_mrpc_validation.\", \"entailment_logprob_odds_mrpc_summary\", \"record_list\"], [\"BASE\", \"This dataset stores per-example inference outputs from google/flan-t5-small on the GLUE MRPC validation set using a prompted yes/no paraphrase detection setup. Each record corresponds to one input pair from glue_mrpc_validation and contains three fields: prediction (binary label, where 1 indicates the model preferred \\u201cyes\\u201d and 0 indicates it preferred \\u201cno\\u201d), yes_logits (the decoder logit for the token \\u201cyes\\u201d at the answer position), and no_logits (the decoder logit for the token \\u201cno\\u201d at the answer position). Predictions are produced by prompting the model with the two sentences, forcing the decoder prefix \\u201cAnswer:\\u201d, and selecting the higher of the yes/no logits. In this workflow, the dataset serves as the main model output table for downstream evaluation, error analysis, and summary metric generation, while preserving a row-level link back to the original MRPC validation examples.\", \"flan_prediction_and_logit_prefix\", \"record_list\"], [\"BASE\", \"Per-example prediction dataset for the GLUE MRPC validation set produced by prompting google/flan-t5-small with a yes/no paraphrase question and applying contextual calibration. Each record corresponds to one input sentence pair from glue_mrpc_validation and stores the model\\u2019s binary prediction (1 = paraphrase/yes, 0 = not paraphrase/no), the raw first-step logits for the yes and no tokens (raw_yes_logits, raw_no_logits), and the calibrated logits after subtracting baseline logits from a null calibration prompt (cal_yes_logits, cal_no_logits). This record list is the main intermediate output of the workflow: it preserves calibrated model scores for each example, supports error analysis and inspection, and is used to compute the downstream summary metrics in flan_t5_contextual_calibrated_yes_no_mrpc_summary.\", \"flan_prediction_logit_calibrated\", \"record_list\"], [\"BASE\", \"flan_prediction_scored is a per-example prediction dataset generated by running google/flan-t5-small on the GLUE MRPC validation set with a yes/no paraphrase prompt. Each record corresponds to one input pair from glue_mrpc_validation and stores the model\\u2019s binary prediction and the sequence log-probability scores for the two candidate answers. The fields are: prediction (integer label, where 1 indicates yes/paraphrase and 0 indicates no/not paraphrase), yes_scores (float log-probability of the full answer token sequence for \\u201cyes\\u201d), and no_scores (float log-probability of the full answer token sequence for \\u201cno\\u201d). In this workflow, this dataset serves as the scored inference output used to inspect example-level model behavior and to compute downstream summary metrics such as accuracy, F1, and the classification report.\", \"flan_prediction_scored\", \"record_list\"], [\"BASE\", \"Aggregate evaluation summary for the flan-t5-small contextual yes/no paraphrase classifier on the GLUE MRPC validation set after logit calibration. This dataset is a record list with one summary record containing the fields: accuracy (float), f1 (float), and classification_report (string with per-class precision/recall/F1 and support for not_paraphrase and paraphrase). It is produced after generating calibrated predictions in flan_prediction_logit_calibrated and compares those predictions against the ground-truth labels in glue_mrpc_validation. Its role in this workflow is to store run-level performance metrics for the full validation set, providing a compact summary of model quality for this notebook execution.\", \"flan_t5_contextual_calibrated_yes_no_mrpc_summary\", \"record_list\"], [\"BASE\", \"flan_t5_full_answer_logprob_mrpc_summary is an experiment-level summary dataset for evaluating google/flan-t5-small on the GLUE MRPC validation split using prompt-based yes/no paraphrase prediction with full-answer log-probability scoring. It contains a single record with three fields: accuracy (float), f1 (float), and classification_report (string from sklearn with per-class precision, recall, f1, and support for not_paraphrase and paraphrase). This dataset is produced after generating example-level predictions in flan_prediction_scored and comparing them against the ground-truth MRPC labels. Its role in the workflow is to store the aggregate evaluation results for the entire validation run, linking the underlying input dataset (glue_mrpc_validation) and the per-example prediction dataset (flan_prediction_scored).\", \"flan_t5_full_answer_logprob_mrpc_summary\", \"record_list\"], [\"BASE\", \"Summary dataset for the FLAN-T5 symmetric-prompt MRPC evaluation run. It contains a single aggregate record describing model performance on the full glue_mrpc_validation split, computed from predictions stored in google_flan_prediction_swapped. The fields are: accuracy (float, overall classification accuracy), f1 (float, binary F1 score for paraphrase detection), and classification_report (string, the full scikit-learn classification report with precision, recall, F1, and support for both not_paraphrase and paraphrase classes). Its role in this workflow is to provide a compact experiment-level evaluation artifact that links the source validation examples and prediction outputs to final metrics for the notebook/process flan_t5_symmetric_prompt_average_mrpc.\", \"flan_t5_symmetric_prompt_average_mrpc_summary\", \"record_list\"], [\"BASE\", \"Summary dataset for the FLAN-T5 MRPC evaluation run using first-step true/false token scoring. It contains aggregate performance results for google/flan-t5-small on the glue_mrpc_validation split, where each example is prompted as a paraphrase detection task and predicted by comparing the first decoder-step logits for the tokens true and false. The record list has three fields: accuracy (float), f1 (float, for the positive/paraphrase class), and classification_report (string containing the full per-class precision/recall/F1 summary). In this workflow, this dataset serves as the experiment-level evaluation artifact that summarizes model performance over the full validation set and links the source validation data with the per-example prediction/logit dataset google_flan_prediction_and_logits.\", \"flan_t5_true_false_first_step_mrpc_summary\", \"record_list\"], [\"BASE\", \"glue_mrpc_validation is the validation split of the GLUE MRPC (Microsoft Research Paraphrase Corpus) dataset stored in TableVault for this notebook. Each record contains sentence1, sentence2, label, and idx, where sentence1 and sentence2 are a pair of sentences, label is a binary paraphrase target (1 = paraphrase, 0 = not paraphrase), and idx is the example identifier from the original dataset. This dataset is the ground-truth evaluation input for the workflow: the sentence pairs are tokenized and passed to the pretrained textattack/distilbert-base-uncased-MRPC model, and the labels are used to compute accuracy, F1, error cases, and the final classification report. It serves as the source dataset linked to downstream prediction, mistake-analysis, and summary output records.\", \"glue_mrpc_validation\", \"record_list\"], [\"BASE\", \"Per-example inference outputs from google/flan-t5-small on the GLUE MRPC validation set using a prompted true/false paraphrase decision. Each record corresponds to one validation example and is linked to the matching source row in glue_mrpc_validation. The dataset has three fields: prediction (binary model decision, where 1 means the logit for \\u201ctrue\\u201d is greater than the logit for \\u201cfalse\\u201d), true_logits (the first-decoder-step logit for the token \\u201ctrue\\u201d), and false_logits (the first-decoder-step logit for the token \\u201cfalse\\u201d). In this workflow, this dataset is the stored prediction artifact used to inspect model behavior on individual examples and to support the downstream summary evaluation dataset with accuracy, F1, and classification report.\", \"google_flan_prediction_and_logits\", \"record_list\"], [\"BASE\", \"Per-example prediction outputs from google/flan-t5-small on the GLUE MRPC validation set using a yes/no paraphrase prompt evaluated in both original and swapped sentence order. Each record is aligned to one input example from glue_mrpc_validation and contains: prediction (binary paraphrase decision after averaging forward and swapped logits), yes_logits (forward-order logit for \\u201cyes\\u201d), no_logits (forward-order logit for \\u201cno\\u201d), swapped_yes_logits (swapped-order logit for \\u201cyes\\u201d), and swapped_no_logits (swapped-order logit for \\u201cno\\u201d). This dataset is used as the intermediate model-output table in the workflow, supporting order-symmetric paraphrase prediction, error analysis, and computation of final evaluation metrics in the summary dataset.\", \"google_flan_prediction_swapped\", \"record_list\"], [\"BASE\", \"Summary dataset for the bidirectional MRPC evaluation run. It contains aggregate evaluation results for the TextAttack DistilBERT MRPC classifier on the GLUE MRPC validation set, where paraphrase probabilities are computed for both the original sentence order and the swapped sentence order, then averaged before thresholding to make the final prediction.\\n\\nStructure:\\n- accuracy: float overall classification accuracy on the validation set\\n- f1: float F1 score for the paraphrase class\\n- classification_report: string version of the sklearn classification report, including per-class precision, recall, F1, and support\\n\\nRole in this workflow:\\nThis dataset serves as the experiment-level evaluation summary for the notebook. It records the final performance metrics derived from comparing the averaged bidirectional predictions against the true labels, and links those metrics back to both the source dataset (glue_mrpc_validation) and the per-example prediction dataset (distilbert_swap_prediction_values).\", \"hf_pipeline_mrpc_bidirectional_order_average_summary\", \"record_list\"], [\"BASE\", \"This dataset stores the aggregate evaluation results for the notebook\\u2019s MRPC margin-rule experiment. It contains a summary record with three fields: accuracy (float), f1 (float), and classification_report (string containing the full sklearn classification report, including per-class precision, recall, f1-score, and support for not_paraphrase and paraphrase). The values are computed by comparing the true labels from glue_mrpc_validation against binary predictions produced from the TextAttack DistilBERT MRPC model, where prediction = 1 when score_pos - score_neg exceeds the configured margin threshold. Its role in the workflow is to provide a compact, final performance summary for the full validation set, linked to both the source validation data and the per-example prediction dataset distilbert_margin_score_prediction_values.\", \"hf_pipeline_mrpc_margin_rule_summary\", \"record_list\"], [\"BASE\", \"This dataset stores the aggregate evaluation summary for the DistilBERT MRPC inference run on the GLUE MRPC validation set after converting pipeline raw logits to softmax probabilities. It contains one summary record with three fields: accuracy (overall prediction accuracy), f1 (binary F1 score for paraphrase detection), and classification_report (the full sklearn text report with per-class precision, recall, F1, support, and overall averages). In this workflow, it serves as the experiment-level performance snapshot, linking the source validation examples and the per-example prediction dataset pipeline_distilbert_softmax_probs so that users can quickly inspect overall model quality without recomputing metrics.\", \"hf_pipeline_mrpc_raw_logits_softmax_summary\", \"record_list\"], [\"BASE\", \"Summary dataset for the hf_pipeline_mrpc_threshold_070 experiment. It contains a single evaluation record aggregating model performance on the full glue_mrpc_validation split after running the Hugging Face text-classification pipeline with textattack/distilbert-base-uncased-MRPC and converting paraphrase probabilities to binary predictions using a 0.70 threshold. The dataset has three fields: accuracy (float), f1 (float, for the positive paraphrase class), and classification_report (string produced by sklearn, containing per-class precision, recall, f1-score, support, and overall averages). Its role in the workflow is to provide a compact experiment-level summary derived from the validation labels and the per-example predictions stored in pipeline_distilbert_threshold, so the notebook can track and compare final thresholded evaluation results.\", \"hf_pipeline_mrpc_threshold_070_summary\", \"record_list\"], [\"BASE\", \"Summary dataset for the min_direction_margin_mrpc workflow. It contains experiment-level evaluation results for paraphrase detection on the GLUE MRPC validation set, where predictions are made by scoring each sentence pair in both directions with an MNLI model and using the minimum entailment-minus-contradiction margin as the decision signal. The dataset has one record with three fields: accuracy (float), f1 (float), and classification_report (string). Its role is to store the final aggregated performance summary derived from the source validation examples and the per-example prediction dataset mrpc_min_margin_prediction, so future users can quickly inspect the overall outcome of this notebook without recomputing metrics.\", \"min_direction_margin_mrpc_summary\", \"record_list\"], [\"BASE\", \"Row-level prediction dataset for the GLUE MRPC validation set produced by the sentence-transformers/paraphrase-MiniLM-L6-v2 model. Each record corresponds to one sentence pair from glue_mrpc_validation and stores two fields: prediction (binary label, where 0 = not_paraphrase and 1 = paraphrase) and score (cosine similarity between the normalized embeddings of sentence1 and sentence2). Predictions are generated by applying a fixed threshold of 0.78 to the cosine similarity score. In this workflow, this dataset serves as the per-example model output used for downstream evaluation, error analysis, and creation of the summary metrics dataset.\", \"minilm_cosine_threshold_prediction\", \"record_list\"], [\"BASE\", \"Model prediction outputs for the GLUE MRPC validation set generated by the textattack/distilbert-base-uncased-MRPC sequence classification model. Each record corresponds to one sentence-pair example in glue_mrpc_validation and stores the model\\u2019s predicted class label for paraphrase detection. The dataset has a single field, prediction, which is an integer class ID (0 = not paraphrase, 1 = paraphrase). In this workflow, it serves as the inference output table linked back to the source validation examples and is used to compute evaluation metrics, compare predictions with ground-truth labels, and identify error cases.\", \"mrpc_distilbert_predictions\", \"record_list\"], [\"BASE\", \"mrpc_entailment_prediction contains per-example prediction outputs for the GLUE MRPC validation set generated with the typeform/distilbert-base-uncased-mnli NLI model. Each record corresponds to one validation pair from glue_mrpc_validation and stores three fields: prediction (binary paraphrase decision obtained by thresholding the averaged score at 0), dir12 (entailment-minus-contradiction log-probability score for sentence1 \\u2192 sentence2), and dir21 (the same score for sentence2 \\u2192 sentence1). The dataset is aligned one-to-one with the source MRPC examples through input item indexing. Its role in this workflow is to capture the model\\u2019s directional entailment-based evidence and final paraphrase prediction for downstream evaluation, error analysis, and summary metric computation.\", \"mrpc_entailment_prediction\", \"record_list\"], [\"BASE\", \"mrpc_gate_margin_prediction is a per-example prediction dataset derived from the GLUE MRPC validation split. For each validation pair (sentence1, sentence2), the notebook runs the NLI model typeform/distilbert-base-uncased-mnli in both input orders, sentence1\\u2192sentence2 and sentence2\\u2192sentence1, and stores the resulting decision signals used for paraphrase classification. The dataset has four fields: prediction (final binary paraphrase prediction, 1 for paraphrase and 0 for not paraphrase), margin_12 (entailment logit minus contradiction logit for sentence1 paired with sentence2), margin_21 (the same margin for the reversed order), and gate (boolean flag that is true only when neither direction\\u2019s argmax label is contradiction). The final prediction is produced by requiring gate = true and the average of margin_12 and margin_21 to be greater than 0. This dataset serves as the main intermediate output of the workflow: it preserves the model\\u2019s directional margin scores and final gated prediction for each MRPC example, and it is then used to compute the summary accuracy, F1, and classification report.\", \"mrpc_gate_margin_prediction\", \"record_list\"], [\"BASE\", \"Per-example prediction dataset for the GLUE MRPC validation split, generated by running the sentence pairs through the typeform/distilbert-base-uncased-mnli model in both input orders. Each record corresponds to one MRPC validation example and is linked to the matching row in glue_mrpc_validation. The dataset has three fields: prediction (binary paraphrase decision, where 1 indicates paraphrase and 0 indicates not paraphrase), gap_12 (entailment probability minus contradiction probability for sentence1\\u2192sentence2), and gap_21 (the same probability gap for sentence2\\u2192sentence1). In this workflow, it serves as the stored per-instance model output used to inspect directional confidence, compare predictions with ground-truth MRPC labels, and build the downstream summary metrics in softmax_gap_mean_mrpc_summary.\", \"mrpc_mean_gap_prediction\", \"record_list\"], [\"BASE\", \"mrpc_min_margin_prediction is an example-level prediction dataset derived from the GLUE MRPC validation split. For each sentence pair in glue_mrpc_validation, it stores the binary paraphrase prediction produced by a zero-shot NLI model (typeform/distilbert-base-uncased-mnli) and the confidence score used to make that prediction.\\n\\nEach record corresponds to one MRPC validation example and has two fields: prediction, an integer label where 1 indicates paraphrase and 0 indicates not_paraphrase; and min_margin, a float equal to the minimum of the entailment-versus-contradiction logit margins computed in both input directions, sentence1\\u2192sentence2 and sentence2\\u2192sentence1. The prediction is defined as 1 when min_margin > 0, otherwise 0.\\n\\nIn this workflow, this dataset serves as the per-example output of the min-direction-margin inference step. It is used as the input to downstream evaluation and summarization, including accuracy, F1, classification report generation, and error analysis.\", \"mrpc_min_margin_prediction\", \"record_list\"], [\"BASE\", \"Per-example prediction dataset for the GLUE MRPC validation split, produced by applying the typeform/distilbert-base-uncased-mnli model as a zero-shot paraphrase detector. Each record corresponds to one sentence pair from glue_mrpc_validation and stores: prediction (binary paraphrase decision, where 1 indicates paraphrase and 0 indicates not_paraphrase), score_12 (entailment logit minus max(contradiction, neutral) for sentence1 -> sentence2), and score_21 (the same score for sentence2 -> sentence1). The final prediction is derived from the average of the two directional scores. In this workflow, this dataset captures the model\\u2019s per-example outputs for downstream evaluation, inspection of mistakes, and construction of the overall summary metrics.\", \"mrpc_neutral_penalty_prediction\", \"record_list\"], [\"BASE\", \"Subset of error cases from the GLUE MRPC validation run using the textattack/distilbert-base-uncased-MRPC model. Each record captures one misclassified sentence pair and includes the fields: idx (validation-set position), sentence1, sentence2, true (ground-truth binary label), and pred (model-predicted binary label). This dataset is created by selecting the first 10 examples where the model prediction differs from the true label, and each record is linked back to the corresponding source example in glue_mrpc_validation and its entry in mrpc_distilbert_predictions. Its role in the workflow is error analysis: it provides a compact, inspectable sample of model failures for diagnosing paraphrase detection mistakes.\", \"mrpc_paraphrase_inference_distilbert_mistakes\", \"record_list\"], [\"BASE\", \"This dataset contains the final evaluation summary for the textattack/distilbert-base-uncased-MRPC model on the GLUE MRPC validation split. It is a small output table with one record summarizing model performance over the full validation dataset.\\n\\nFields:\\n- accuracy: overall classification accuracy on the validation set\\n- f1: F1 score for the paraphrase classification task\\n- classification_report: full text report from sklearn including precision, recall, F1, and support for the not_paraphrase and paraphrase classes\\n\\nIn this workflow, this dataset serves as the final results artifact. It is created after running batched inference on sentence pairs, comparing predictions against ground-truth labels, and aggregating the metrics. The record is linked to the full validation input dataset and the prediction dataset so a user can trace the reported metrics back to the underlying examples and model outputs.\", \"mrpc_paraphrase_inference_distilbert_output\", \"record_list\"], [\"BASE\", \"Aggregate evaluation summary for the neutral-penalized margin MRPC experiment. This dataset contains a single summary record computed from the GLUE MRPC validation set and the derived mrpc_neutral_penalty_prediction records. Its fields are: accuracy (float, overall prediction accuracy), f1 (float, F1 score for the paraphrase class), and classification_report (string, full sklearn classification report with per-class precision, recall, F1, and support). In this workflow, it serves as the compact experiment-level output used to record and retrieve overall model performance after scoring sentence pairs with the MNLI model and converting the bidirectional entailment-vs.-non-entailment margin into paraphrase predictions.\", \"neutral_penalized_margin_mrpc_summary\", \"record_list\"], [\"BASE\", \"Per-example prediction dataset for the GLUE MRPC validation split. Each record corresponds to one sentence pair from glue_mrpc_validation and stores the model output from this notebook\\u2019s similarity-based paraphrase detection pipeline using distilbert-base-uncased embeddings. The fields are: prediction (binary label, 1 if the cosine similarity between the two sentence embeddings is at least 0.85, otherwise 0) and cosine_scores (the raw cosine similarity score as a float). The embeddings are produced by mean-pooling DistilBERT token representations while excluding special tokens such as [CLS] and [SEP], followed by L2 normalization. In this workflow, this dataset serves as the detailed per-row inference output that links back to the original MRPC validation examples and is then used to compute and document overall evaluation metrics in the summary dataset.\", \"no_special_cosine_mrpc_similarity_prediction\", \"record_list\"], [\"BASE\", \"Per-example inference outputs for the GLUE MRPC validation set produced by the Hugging Face text-classification pipeline using textattack/distilbert-base-uncased-MRPC. Each record corresponds to one input sentence pair from glue_mrpc_validation and stores the model\\u2019s predicted class and the softmax probability of the positive/paraphrase class. The dataset is structured as one row per validation example with fields for prediction (integer class label from argmax) and the positive-class probability (intended as positive_probs; in the appended records this is written as paraphrase_probs). In this workflow, this dataset serves as the main prediction artifact linking model outputs back to the source validation examples and is used downstream to compute accuracy, F1, and the classification report summary.\", \"pipeline_distilbert_softmax_probs\", \"record_list\"], [\"BASE\", \"Per-example inference results from the Hugging Face model textattack/distilbert-base-uncased-MRPC run on the glue_mrpc_validation dataset. Each record corresponds to one sentence pair from the MRPC validation split and stores two fields: prediction, a binary label produced by thresholding the model\\u2019s paraphrase probability at 0.70; and paraphrase_probs, the softmax probability assigned to the positive paraphrase class. Records are linked back to the matching input example in glue_mrpc_validation. This dataset serves as the main prediction output of the workflow and is used for downstream evaluation, error analysis, and creation of the run-level summary dataset.\", \"pipeline_distilbert_threshold\", \"record_list\"], [\"BASE\", \"This dataset stores the evaluation summary for the notebook run quora_cross_encoder_prefixed_sentence_tags_mrpc on the GLUE MRPC validation set. It contains a summary record of the cross-encoder paraphrase detection results produced from the prediction dataset distilbert_cross_text_prediction. Its fields are: accuracy (float, overall classification accuracy), f1 (float, binary F1 score for paraphrase detection), and classification_report (string, the full sklearn classification report with precision, recall, F1, and support for the not_paraphrase and paraphrase classes). In this workflow, it serves as the experiment-level metrics dataset that aggregates model performance over the full validation set and links the source inputs from glue_mrpc_validation and the generated predictions.\", \"quora_cross_encoder_prefixed_sentence_tags_mrpc_summary\", \"record_list\"], [\"BASE\", \"Experiment-level evaluation summary for the notebook run using the cross-encoder/quora-distilroberta-base model on the GLUE MRPC validation split with a paraphrase decision threshold of 0.65 applied to the positive softmax score. This dataset contains a single summary record with the fields: accuracy (float), f1 (float), and classification_report (string produced by sklearn, summarizing precision, recall, f1-score, and support for the not_paraphrase and paraphrase classes). It is derived from the full glue_mrpc_validation dataset and the corresponding per-example predictions stored in distilbert_quora_softmax_prediction, and its role is to capture the overall performance of this experiment in a compact, queryable form for comparison, tracking, and documentation.\", \"quora_cross_encoder_softmax_threshold_065_mrpc_summary\", \"record_list\"], [\"BASE\", \"Summary dataset for the notebook\\u2019s evaluation run of the cross-encoder/quora-distilroberta-base model on the GLUE MRPC validation set using symmetric scoring. It contains aggregate performance results computed after predicting each sentence pair in both original and reversed order, averaging the two positive-class scores, and thresholding at 0.5.\\n\\nStructure: a record list with columns accuracy, f1, and classification_report. accuracy is the overall validation accuracy, f1 is the binary F1 score for paraphrase detection, and classification_report is the full sklearn text report summarizing class-wise precision, recall, F1, and support for the labels not_paraphrase and paraphrase.\\n\\nRole in the workflow: this dataset stores the run-level evaluation summary for the prediction dataset distilbert_symmetric_average_prediction, linked to both the source input dataset glue_mrpc_validation and the generated prediction records. It is intended as the compact experiment result table for comparing or auditing this notebook run.\", \"quora_cross_encoder_symmetric_average_mrpc_summary\", \"record_list\"], [\"BASE\", \"This dataset stores the evaluation summary for the notebook run that applies the cross-encoder/quora-distilroberta-base model to the GLUE MRPC validation set after text normalization. It contains a single aggregated record rather than per-example predictions. The fields are: accuracy (float), f1 (float), and classification_report (string with the full sklearn classification report for the not_paraphrase/paraphrase labels). Its role in the workflow is to capture experiment-level performance metrics derived from comparing the normalized-text predictions in distilbert-normalized-text-prediction against the ground-truth labels in glue_mrpc_validation, providing a compact summary of model performance for this run.\", \"quora_cross_encoder_text_normalized_mrpc_summary\", \"record_list\"], [\"BASE\", \"Per-example prediction dataset for the GLUE MRPC validation set, generated by comparing sentence embeddings from sentence-transformers/all-MiniLM-L6-v2. Each record contains a single field, prediction, which is a binary label: 1 when the L2 distance between the normalized embeddings of sentence1 and sentence2 is less than or equal to the fixed threshold (0.63), and 0 otherwise. The dataset has one record per validation example and is linked back to the original glue_mrpc_validation row as well as the corresponding sentence 1 and sentence 2 embedding entries. Its role in this workflow is to store the model\\u2019s threshold-based paraphrase decisions so they can be inspected, traced to source inputs, and used to compute evaluation metrics such as accuracy, F1, and the classification report.\", \"sentence_transformers_mrpc_prediction_distance\", \"record_list\"], [\"BASE\", \"Binary paraphrase predictions for the GLUE MRPC validation set, generated by encoding each sentence pair with sentence-transformers/all-MiniLM-L6-v2 using max_seq_length=64, computing the cosine similarity between the normalized sentence1 and sentence2 embeddings, and applying a threshold of 0.80. This record list contains one row per validation example with a single field, prediction, where 1 indicates predicted paraphrase and 0 indicates predicted non-paraphrase. Each record is linked back to the corresponding source example in glue_mrpc_validation and to the two embedding lists sentence-transformers-sentence-1-max64 and sentence-transformers-sentence-2-max64. In this workflow, the dataset serves as the stored model output used for downstream evaluation, error analysis, and experiment summary reporting.\", \"sentence_transformers_mrpc_prediction_max64\", \"record_list\"], [\"BASE\", \"sentence_transformers_mrpc_prediction_threshold is a record list containing the per-example binary predictions produced on the GLUE MRPC validation set by a SentenceTransformer paraphrase model. Each record has a single field, prediction, where 1 indicates the sentence pair is predicted to be a paraphrase and 0 indicates not_paraphrase. Predictions are generated by encoding sentence1 and sentence2 with sentence-transformers/paraphrase-MiniLM-L3-v2, computing their cosine similarity via normalized embedding dot product, and applying a fixed threshold of 0.74. The dataset is aligned one-to-one with glue_mrpc_validation and is linked to the corresponding sentence-pair embeddings, making it the main stored output used for error analysis, metric computation, and creation of the workflow summary dataset.\", \"sentence_transformers_mrpc_prediction_threshold\", \"record_list\"], [\"BASE\", \"Binary prediction table for the GLUE MRPC validation set produced by the sentence-transformers/all-distilroberta-v1 model. Each record corresponds to one validation example and stores a single field, prediction, where 1 indicates the sentence pair is predicted to be a paraphrase and 0 indicates not_paraphrase. Predictions are generated by computing the cosine similarity between the normalized embeddings of sentence1 and sentence2 and applying a fixed threshold of 0.72. This dataset serves as the model output layer in the workflow, linking each prediction back to the original MRPC example and the two sentence embedding datasets, and it is used downstream to compute accuracy, F1, error analysis, and the experiment summary.\", \"sentence_transformers_mrpc_prediction_threshold_2\", \"record_list\"], [\"BASE\", \"Summary record list for the MRPC validation evaluation of a threshold-based paraphrase detection workflow using sentence-transformers/all-distilroberta-v1. This dataset contains experiment-level metrics computed by comparing predicted paraphrase labels from cosine similarity scores between sentence1 and sentence2 embeddings against the ground-truth labels in glue_mrpc_validation. Its structure is a record list with three fields: accuracy (float), f1 (float), and classification_report (string containing the full per-class evaluation report). In this notebook, it serves as the final aggregated result of the process, linking the full GLUE MRPC validation set and the generated prediction record list into a compact summary of model performance for the chosen cosine threshold.\", \"st_all_distilroberta_v1_cosine_threshold_mrpc_summary\", \"record_list\"], [\"BASE\", \"Summary dataset for the MRPC validation run using sentence-transformers/all-MiniLM-L6-v2 sentence embeddings and an L2 distance threshold classifier. It contains a single record that aggregates evaluation results over the full glue_mrpc_validation dataset after predicting whether each sentence pair is a paraphrase based on whether the embedding distance is less than or equal to the chosen threshold (0.63).\\n\\nFields:\\naccuracy: overall classification accuracy on the validation set\\nf1: F1 score for the paraphrase class\\nclassification_report: full text report from sklearn with precision, recall, F1, and support for both not_paraphrase and paraphrase classes\\n\\nRole in the workflow:\\nThis dataset stores the experiment-level evaluation summary for the notebook. It provides a compact record of model performance derived from the per-example prediction dataset sentence_transformers_mrpc_prediction_distance and linked to the full glue_mrpc_validation input range.\", \"st_all_minilm_l6_l2_distance_threshold_mrpc_summary\", \"record_list\"], [\"BASE\", \"Summary dataset for the MRPC validation experiment using sentence-transformers/all-MiniLM-L6-v2 with max_seq_length=64 and cosine-similarity thresholding. It contains aggregate evaluation results for the prediction run, not per-example data. The record list has three fields: accuracy (float), f1 (float), and classification_report (string with the full class-wise sklearn report for not_paraphrase vs paraphrase). In this workflow, it stores the final performance summary of the predicted paraphrase labels generated from cosine scores between sentence1 and sentence2 embeddings on glue_mrpc_validation, providing a compact experiment-level result linked back to the source validation set and prediction outputs.\", \"st_all_minilm_l6_max_seq_len_64_cosine_mrpc_summary\", \"record_list\"], [\"BASE\", \"This dataset stores the run-level evaluation summary for the SentenceTransformer bi-encoder cosine-similarity paraphrase detection experiment on the GLUE MRPC validation set. It contains a single summary record rather than per-example predictions. The fields are: accuracy (float), f1 (float), and classification_report (string with class-wise precision, recall, and F1 statistics). In this workflow, it serves as the compact results table that aggregates model performance after generating sentence embeddings, scoring sentence pairs with cosine similarity, applying a fixed decision threshold, and comparing predictions against the MRPC ground-truth labels.\", \"st_paraphrase_minilm_l3_cosine_threshold_mrpc_summary\", \"record_list\"], [\"BASE\", \"This dataset stores the evaluation summary for the paraphrase detection workflow using sentence-transformers/paraphrase-MiniLM-L6-v2 on the GLUE MRPC validation set with cosine-similarity thresholding at 0.78. It contains a single summary record with three fields: accuracy (float), f1 (float), and classification_report (string). The metrics are computed by comparing thresholded cosine-similarity predictions from the minilm_cosine_threshold_prediction dataset against the ground-truth labels in glue_mrpc_validation. Its role in this workflow is to provide a compact, experiment-level performance summary for the notebook, linking the full validation set and per-example predictions to aggregate evaluation results.\", \"st_paraphrase_minilm_l6_cosine_threshold_mrpc_summary\", \"record_list\"]]}"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da5304d654819ba6d52333f0c92800`

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
    "call_id": "call_SyYtzmvtSEGNhQQyn4wxDRug",
    "arguments": {
      "item_name": "distilbert_last4_mean_cosine_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_SyYtzmvtSEGNhQQyn4wxDRug`

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
| 13169 | 1042 | 1001 | 11342 | 16.186s | 0.019s |

---

## Turn 3 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da5314f618819b9e79f0686338676b`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_SyYtzmvtSEGNhQQyn4wxDRug",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.6838235294117647, \"f1\": 0.8122270742358079, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.00      0.00      0.00       129\\n    paraphrase       0.68      1.00      0.81       279\\n\\n      accuracy                           0.68       408\\n     macro avg       0.34      0.50      0.41       408\\n  weighted avg       0.47      0.68      0.56       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da5314f618819b9e79f0686338676b`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_TWRnOK6JIiRlWydxRalCsrxa",
    "arguments": {
      "item_name": "distilbert_mean_cosine_median_threshold_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_TWRnOK6JIiRlWydxRalCsrxa`

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
| 14377 | 40 | 0 | 12550 | 2.824s | 0.019s |

---

## Turn 4 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da5317cfec819b8eae3e857a562b00`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_TWRnOK6JIiRlWydxRalCsrxa",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.6495098039215687, \"f1\": 0.7039337474120083, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.47      0.74      0.57       129\\n    paraphrase       0.83      0.61      0.70       279\\n\\n      accuracy                           0.65       408\\n     macro avg       0.65      0.67      0.64       408\\n  weighted avg       0.72      0.65      0.66       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da5317cfec819b8eae3e857a562b00`

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
    "call_id": "call_Goo2LWxFktBAYIEArqbji8O0",
    "arguments": {
      "item_name": "distilbert_no_special_tokens_mean_cosine_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_Goo2LWxFktBAYIEArqbji8O0`

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
| 14583 | 87 | 45 | 12756 | 2.337s | 0.021s |

---

## Turn 5 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da531a2adc819b8db96029e799e47b`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_Goo2LWxFktBAYIEArqbji8O0",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.7034313725490197, \"f1\": 0.8212703101920237, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.90      0.07      0.13       129\\n    paraphrase       0.70      1.00      0.82       279\\n\\n      accuracy                           0.70       408\\n     macro avg       0.80      0.53      0.48       408\\n  weighted avg       0.76      0.70      0.60       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da531a2adc819b8db96029e799e47b`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_GlWcYPLcrm2OC8yuIDNO5msF",
    "arguments": {
      "item_name": "distilbert_max_pool_cosine_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_GlWcYPLcrm2OC8yuIDNO5msF`

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
| 14836 | 38 | 0 | 13009 | 1.714s | 0.005s |

---

## Turn 6 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da531be284819ba9c11994c018058b`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_GlWcYPLcrm2OC8yuIDNO5msF",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.6838235294117647, \"f1\": 0.8122270742358079, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.00      0.00      0.00       129\\n    paraphrase       0.68      1.00      0.81       279\\n\\n      accuracy                           0.68       408\\n     macro avg       0.34      0.50      0.41       408\\n  weighted avg       0.47      0.68      0.56       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da531be284819ba9c11994c018058b`

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
    "call_id": "call_QgpPzNP5uqjWNaEZoYkvK9Rq",
    "arguments": {
      "item_name": "st_paraphrase_minilm_l3_cosine_threshold_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_QgpPzNP5uqjWNaEZoYkvK9Rq`

**Arguments:**
```json
{
  "item_name": "st_paraphrase_minilm_l3_cosine_threshold_mrpc_summary",
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
      "accuracy": 0.7132352941176471,
      "f1": 0.7929203539823009,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.55      0.52      0.53       129\n    paraphrase       0.78      0.80      0.79       279\n\n      accuracy                           0.71       408\n     macro avg       0.67      0.66      0.66       408\n  weighted avg       0.71      0.71      0.71       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 15040 | 70 | 26 | 13213 | 1.944s | 0.015s |

---

## Turn 7 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da531dd894819bba3f3ab54a52f7bb`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_QgpPzNP5uqjWNaEZoYkvK9Rq",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.7132352941176471, \"f1\": 0.7929203539823009, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.55      0.52      0.53       129\\n    paraphrase       0.78      0.80      0.79       279\\n\\n      accuracy                           0.71       408\\n     macro avg       0.67      0.66      0.66       408\\n  weighted avg       0.71      0.71      0.71       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da531dd894819bba3f3ab54a52f7bb`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_KR1SVEMz0r5p2uhVh9GkR9v8",
    "arguments": {
      "item_name": "st_paraphrase_minilm_l6_cosine_threshold_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_KR1SVEMz0r5p2uhVh9GkR9v8`

**Arguments:**
```json
{
  "item_name": "st_paraphrase_minilm_l6_cosine_threshold_mrpc_summary",
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
      "f1": 0.7706766917293233,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.52      0.63      0.57       129\n    paraphrase       0.81      0.73      0.77       279\n\n      accuracy                           0.70       408\n     macro avg       0.67      0.68      0.67       408\n  weighted avg       0.72      0.70      0.71       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 15276 | 42 | 0 | 13449 | 2.796s | 0.021s |

---

## Turn 8 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da5320ac64819ba31bb7399e22bca8`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_KR1SVEMz0r5p2uhVh9GkR9v8",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.7009803921568627, \"f1\": 0.7706766917293233, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.52      0.63      0.57       129\\n    paraphrase       0.81      0.73      0.77       279\\n\\n      accuracy                           0.70       408\\n     macro avg       0.67      0.68      0.67       408\\n  weighted avg       0.72      0.70      0.71       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da5320ac64819ba31bb7399e22bca8`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_mt8I8rF3hKRKK2NX8FBKQttL",
    "arguments": {
      "item_name": "st_all_minilm_l6_max_seq_len_64_cosine_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_mt8I8rF3hKRKK2NX8FBKQttL`

**Arguments:**
```json
{
  "item_name": "st_all_minilm_l6_max_seq_len_64_cosine_mrpc_summary",
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
      "accuracy": 0.6764705882352942,
      "f1": 0.7441860465116279,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.49      0.65      0.56       129\n    paraphrase       0.81      0.69      0.74       279\n\n      accuracy                           0.68       408\n     macro avg       0.65      0.67      0.65       408\n  weighted avg       0.71      0.68      0.69       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 15484 | 44 | 0 | 13657 | 2.900s | 0.018s |

---

## Turn 9 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da532395e8819ba4c20bbd6c0c2b67`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_mt8I8rF3hKRKK2NX8FBKQttL",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.6764705882352942, \"f1\": 0.7441860465116279, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.49      0.65      0.56       129\\n    paraphrase       0.81      0.69      0.74       279\\n\\n      accuracy                           0.68       408\\n     macro avg       0.65      0.67      0.65       408\\n  weighted avg       0.71      0.68      0.69       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da532395e8819ba4c20bbd6c0c2b67`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_HXB8C3jMcE6ply4ffbEwfWTF",
    "arguments": {
      "item_name": "st_all_minilm_l6_l2_distance_threshold_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_HXB8C3jMcE6ply4ffbEwfWTF`

**Arguments:**
```json
{
  "item_name": "st_all_minilm_l6_l2_distance_threshold_mrpc_summary",
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
      "accuracy": 0.678921568627451,
      "f1": 0.7456310679611651,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.49      0.66      0.56       129\n    paraphrase       0.81      0.69      0.75       279\n\n      accuracy                           0.68       408\n     macro avg       0.65      0.67      0.66       408\n  weighted avg       0.71      0.68      0.69       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 15694 | 41 | 0 | 13867 | 1.839s | 0.006s |

---

## Turn 10 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da53256f90819bbc1aaeba9d906bb3`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_HXB8C3jMcE6ply4ffbEwfWTF",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.678921568627451, \"f1\": 0.7456310679611651, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.49      0.66      0.56       129\\n    paraphrase       0.81      0.69      0.75       279\\n\\n      accuracy                           0.68       408\\n     macro avg       0.65      0.67      0.66       408\\n  weighted avg       0.71      0.68      0.69       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da53256f90819bbc1aaeba9d906bb3`

**Output items:**
```json
[
  {
    "type": "function_call",
    "name": "get_item",
    "call_id": "call_miW8QRB8D6F8Ocisu6Ka01Sl",
    "arguments": {
      "item_name": "st_all_distilroberta_v1_cosine_threshold_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_miW8QRB8D6F8Ocisu6Ka01Sl`

**Arguments:**
```json
{
  "item_name": "st_all_distilroberta_v1_cosine_threshold_mrpc_summary",
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
      "accuracy": 0.7230392156862745,
      "f1": 0.8055077452667814,
      "classification_report": "                precision    recall  f1-score   support\n\nnot_paraphrase       0.58      0.47      0.52       129\n    paraphrase       0.77      0.84      0.81       279\n\n      accuracy                           0.72       408\n     macro avg       0.68      0.66      0.66       408\n  weighted avg       0.71      0.72      0.71       408\n"
    }
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 15900 | 42 | 0 | 14073 | 1.416s | 0.019s |

---

## Turn 11 — `description_search` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da5326dc8c819b894c3c2ac3cb5dea`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_miW8QRB8D6F8Ocisu6Ka01Sl",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.7230392156862745, \"f1\": 0.8055077452667814, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       0.58      0.47      0.52       129\\n    paraphrase       0.77      0.84      0.81       279\\n\\n      accuracy                           0.72       408\\n     macro avg       0.68      0.66      0.66       408\\n  weighted avg       0.71      0.72      0.71       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da5326dc8c819b894c3c2ac3cb5dea`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "description_search",
    "call_id": "call_gkz7Bw3dJTSj9ECBT10opH7a",
    "arguments": {
      "description_text": "cosine median threshold similarity summary"
    }
  }
]
```

### Tool Call
**Tool:** `description_search` | **call_id:** `call_gkz7Bw3dJTSj9ECBT10opH7a`

**Arguments:**
```json
{
  "description_text": "cosine median threshold similarity summary"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    [
      "BASE",
      "distilbert_mean_cosine_median_threshold_mrpc_summary is a summary dataset containing the evaluation results for the DistilBERT mean-pooled cosine-similarity baseline on the GLUE MRPC validation set. It stores aggregate metrics computed after encoding each sentence pair with distilbert-base-uncased, measuring cosine similarity between the two sentence embeddings, and converting scores to binary paraphrase predictions using the median similarity as the decision threshold. The dataset has three fields: accuracy (float), f1 (float), and classification_report (string with per-class precision/recall/F1 and support). In this workflow, it serves as the final experiment-level output that summarizes model performance over the full validation split, with provenance linked to both the source dataset glue_mrpc_validation and the per-example prediction dataset threshold_cosine_mrpc_similarity_prediction.",
      "distilbert_mean_cosine_median_threshold_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "Per-example prediction dataset for the GLUE MRPC validation split generated by a DistilBERT sentence-similarity baseline. Each record corresponds to one sentence pair from glue_mrpc_validation and stores two fields: prediction, a binary label produced by thresholding cosine similarity between the mean-pooled DistilBERT embeddings of sentence1 and sentence2; and cosine_scores, the raw cosine similarity value for that pair. The threshold is the median cosine similarity over the full validation set. In this workflow, this dataset is the intermediate output used to inspect pairwise similarity predictions and to support downstream evaluation and summary metrics.",
      "threshold_cosine_mrpc_similarity_prediction",
      "record_list"
    ]
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 16108 | 417 | 391 | 14281 | 11.175s | 0.047s |

---

## Turn 12 — `description_search` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da53321658819b8f4bb0e51ca5bb60`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_gkz7Bw3dJTSj9ECBT10opH7a",
    "output": "{\"ok\": true, \"result\": [[\"BASE\", \"distilbert_mean_cosine_median_threshold_mrpc_summary is a summary dataset containing the evaluation results for the DistilBERT mean-pooled cosine-similarity baseline on the GLUE MRPC validation set. It stores aggregate metrics computed after encoding each sentence pair with distilbert-base-uncased, measuring cosine similarity between the two sentence embeddings, and converting scores to binary paraphrase predictions using the median similarity as the decision threshold. The dataset has three fields: accuracy (float), f1 (float), and classification_report (string with per-class precision/recall/F1 and support). In this workflow, it serves as the final experiment-level output that summarizes model performance over the full validation split, with provenance linked to both the source dataset glue_mrpc_validation and the per-example prediction dataset threshold_cosine_mrpc_similarity_prediction.\", \"distilbert_mean_cosine_median_threshold_mrpc_summary\", \"record_list\"], [\"BASE\", \"Per-example prediction dataset for the GLUE MRPC validation split generated by a DistilBERT sentence-similarity baseline. Each record corresponds to one sentence pair from glue_mrpc_validation and stores two fields: prediction, a binary label produced by thresholding cosine similarity between the mean-pooled DistilBERT embeddings of sentence1 and sentence2; and cosine_scores, the raw cosine similarity value for that pair. The threshold is the median cosine similarity over the full validation set. In this workflow, this dataset is the intermediate output used to inspect pairwise similarity predictions and to support downstream evaluation and summary metrics.\", \"threshold_cosine_mrpc_similarity_prediction\", \"record_list\"]]}"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da53321658819b8f4bb0e51ca5bb60`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "description_search",
    "call_id": "call_oSnzm5sxHGTfdps8Ux3oJkQw",
    "arguments": {
      "description_text": "cosine-similarity threshold paraphrase summary MRPC"
    }
  }
]
```

### Tool Call
**Tool:** `description_search` | **call_id:** `call_oSnzm5sxHGTfdps8Ux3oJkQw`

**Arguments:**
```json
{
  "description_text": "cosine-similarity threshold paraphrase summary MRPC"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    [
      "BASE",
      "This dataset stores per-example paraphrase predictions for the GLUE MRPC validation set produced by a DistilBERT-based cosine similarity pipeline. For each sentence pair from glue_mrpc_validation, the notebook encodes sentence1 and sentence2 with distilbert-base-uncased, applies masked max pooling to the token embeddings, computes the cosine similarity between the two normalized sentence embeddings, and converts that score to a binary prediction using a threshold of 0.85.\n\nStructure:\n- prediction: integer binary label predicted by the similarity rule (1 = paraphrase, 0 = not paraphrase)\n- cosine_scores: float cosine similarity between the max-pooled embeddings of the two sentences\n\nEach record corresponds to one input sentence pair and is linked back to the source validation examples through input_items. In this workflow, the dataset serves as the main model-output table for downstream evaluation, inspection of correct and incorrect predictions, and creation of the final summary metrics dataset.",
      "cosine_mrpc_max_pool_similarity_prediction",
      "record_list"
    ],
    [
      "BASE",
      "This dataset stores per-example paraphrase predictions for the GLUE MRPC validation set produced by this notebook\u2019s embedding-similarity baseline. Each record corresponds to one sentence pair from glue_mrpc_validation and contains two fields: prediction, a binary label (1 if the pair is predicted to be a paraphrase, 0 otherwise), and similarities, the cosine similarity score between the L2-normalized sentence embeddings of sentence1 and sentence2. The embeddings are generated with distilbert-base-uncased by averaging the last 4 hidden layers at the token level and then mean-pooling across tokens. Predictions are created by applying a fixed threshold of 0.85 to the similarity score. In this workflow, this dataset is the intermediate model output used to inspect individual examples, analyze errors, and compute the final evaluation summary in distilbert_last4_mean_cosine_mrpc_summary.",
      "cosine_mrpc_mean_similarity_prediction",
      "record_list"
    ],
    [
      "BASE",
      "Per-example prediction dataset for the GLUE MRPC validation split. Each record corresponds to one sentence pair from glue_mrpc_validation and stores the output of a simple paraphrase classifier built from DistilBERT sentence embeddings. The dataset has two fields: prediction, a binary label where 1 means paraphrase and 0 means not paraphrase, produced by thresholding the cosine similarity at 0.85; and score, the raw cosine similarity between the L2-normalized first-token embeddings of sentence1 and sentence2 from distilbert-base-uncased. In this workflow, this dataset is the main record of model inference results, used for error analysis, inspection of individual examples, and as input to the downstream summary dataset distilbert_cls_cosine_mrpc_summary.",
      "cosine_mrpc_threshold_score",
      "record_list"
    ],
    [
      "BASE",
      "Summary dataset for the DistilBERT cosine-similarity MRPC validation experiment. It contains an aggregate evaluation record for paraphrase detection on the GLUE MRPC validation split, where sentence1 and sentence2 are encoded with distilbert-base-uncased, the last 4 hidden layers are averaged, mean pooled into sentence embeddings, and classified by cosine similarity using a threshold of 0.85. The dataset structure has 3 fields: accuracy (float), f1 (float), and classification_report (string with per-class precision/recall/F1 and support). In this workflow, it serves as the final experiment-level metrics table summarizing model performance over the full validation set, with provenance linked to both the source dataset glue_mrpc_validation and the per-example prediction dataset cosine_mrpc_mean_similarity_prediction.",
      "distilbert_last4_mean_cosine_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "This dataset stores the experiment-level evaluation summary for the DistilBERT max-pooling cosine-similarity approach on the GLUE MRPC validation set. It contains a single summary record with three fields: accuracy (float), f1 (float), and classification_report (string). The values are computed by comparing binary paraphrase predictions\u2014generated by thresholding cosine similarity between max-pooled DistilBERT embeddings of sentence pairs\u2014against the ground-truth MRPC labels. In this workflow, the dataset serves as the final aggregated results table for the notebook, capturing overall model performance in a compact form for later inspection, comparison, and lineage tracking back to the validation data and prediction outputs.",
      "distilbert_max_pool_cosine_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "distilbert_mean_cosine_median_threshold_mrpc_summary is a summary dataset containing the evaluation results for the DistilBERT mean-pooled cosine-similarity baseline on the GLUE MRPC validation set. It stores aggregate metrics computed after encoding each sentence pair with distilbert-base-uncased, measuring cosine similarity between the two sentence embeddings, and converting scores to binary paraphrase predictions using the median similarity as the decision threshold. The dataset has three fields: accuracy (float), f1 (float), and classification_report (string with per-class precision/recall/F1 and support). In this workflow, it serves as the final experiment-level output that summarizes model performance over the full validation split, with provenance linked to both the source dataset glue_mrpc_validation and the per-example prediction dataset threshold_cosine_mrpc_similarity_prediction.",
      "distilbert_mean_cosine_median_threshold_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "Summary dataset for the MRPC validation run using distilbert-base-uncased sentence embeddings. It contains aggregate evaluation results for paraphrase prediction on glue_mrpc_validation, where sentence1 and sentence2 are encoded separately, token embeddings are mean-pooled while excluding special tokens ([CLS], [SEP]), cosine similarity is computed between the two sentence embeddings, and a fixed threshold of 0.85 is used to produce binary paraphrase predictions.\n\nStructure: one record with fields accuracy (float), f1 (float), and classification_report (string). The record is linked to the full glue_mrpc_validation input range and to the no_special_cosine_mrpc_similarity_prediction dataset that stores per-example predictions and cosine scores.\n\nRole in workflow: this dataset is the experiment-level evaluation summary, used to capture the overall performance of the no-special-token mean-pooled cosine-similarity baseline on MRPC validation.",
      "distilbert_no_special_tokens_mean_cosine_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "Row-level prediction dataset for the GLUE MRPC validation set produced by the sentence-transformers/paraphrase-MiniLM-L6-v2 model. Each record corresponds to one sentence pair from glue_mrpc_validation and stores two fields: prediction (binary label, where 0 = not_paraphrase and 1 = paraphrase) and score (cosine similarity between the normalized embeddings of sentence1 and sentence2). Predictions are generated by applying a fixed threshold of 0.78 to the cosine similarity score. In this workflow, this dataset serves as the per-example model output used for downstream evaluation, error analysis, and creation of the summary metrics dataset.",
      "minilm_cosine_threshold_prediction",
      "record_list"
    ],
    [
      "BASE",
      "Binary paraphrase predictions for the GLUE MRPC validation set, generated by encoding each sentence pair with sentence-transformers/all-MiniLM-L6-v2 using max_seq_length=64, computing the cosine similarity between the normalized sentence1 and sentence2 embeddings, and applying a threshold of 0.80. This record list contains one row per validation example with a single field, prediction, where 1 indicates predicted paraphrase and 0 indicates predicted non-paraphrase. Each record is linked back to the corresponding source example in glue_mrpc_validation and to the two embedding lists sentence-transformers-sentence-1-max64 and sentence-transformers-sentence-2-max64. In this workflow, the dataset serves as the stored model output used for downstream evaluation, error analysis, and experiment summary reporting.",
      "sentence_transformers_mrpc_prediction_max64",
      "record_list"
    ],
    [
      "BASE",
      "sentence_transformers_mrpc_prediction_threshold is a record list containing the per-example binary predictions produced on the GLUE MRPC validation set by a SentenceTransformer paraphrase model. Each record has a single field, prediction, where 1 indicates the sentence pair is predicted to be a paraphrase and 0 indicates not_paraphrase. Predictions are generated by encoding sentence1 and sentence2 with sentence-transformers/paraphrase-MiniLM-L3-v2, computing their cosine similarity via normalized embedding dot product, and applying a fixed threshold of 0.74. The dataset is aligned one-to-one with glue_mrpc_validation and is linked to the corresponding sentence-pair embeddings, making it the main stored output used for error analysis, metric computation, and creation of the workflow summary dataset.",
      "sentence_transformers_mrpc_prediction_threshold",
      "record_list"
    ],
    [
      "BASE",
      "Binary prediction table for the GLUE MRPC validation set produced by the sentence-transformers/all-distilroberta-v1 model. Each record corresponds to one validation example and stores a single field, prediction, where 1 indicates the sentence pair is predicted to be a paraphrase and 0 indicates not_paraphrase. Predictions are generated by computing the cosine similarity between the normalized embeddings of sentence1 and sentence2 and applying a fixed threshold of 0.72. This dataset serves as the model output layer in the workflow, linking each prediction back to the original MRPC example and the two sentence embedding datasets, and it is used downstream to compute accuracy, F1, error analysis, and the experiment summary.",
      "sentence_transformers_mrpc_prediction_threshold_2",
      "record_list"
    ],
    [
      "BASE",
      "Summary record list for the MRPC validation evaluation of a threshold-based paraphrase detection workflow using sentence-transformers/all-distilroberta-v1. This dataset contains experiment-level metrics computed by comparing predicted paraphrase labels from cosine similarity scores between sentence1 and sentence2 embeddings against the ground-truth labels in glue_mrpc_validation. Its structure is a record list with three fields: accuracy (float), f1 (float), and classification_report (string containing the full per-class evaluation report). In this notebook, it serves as the final aggregated result of the process, linking the full GLUE MRPC validation set and the generated prediction record list into a compact summary of model performance for the chosen cosine threshold.",
      "st_all_distilroberta_v1_cosine_threshold_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "Summary dataset for the MRPC validation experiment using sentence-transformers/all-MiniLM-L6-v2 with max_seq_length=64 and cosine-similarity thresholding. It contains aggregate evaluation results for the prediction run, not per-example data. The record list has three fields: accuracy (float), f1 (float), and classification_report (string with the full class-wise sklearn report for not_paraphrase vs paraphrase). In this workflow, it stores the final performance summary of the predicted paraphrase labels generated from cosine scores between sentence1 and sentence2 embeddings on glue_mrpc_validation, providing a compact experiment-level result linked back to the source validation set and prediction outputs.",
      "st_all_minilm_l6_max_seq_len_64_cosine_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "This dataset stores the run-level evaluation summary for the SentenceTransformer bi-encoder cosine-similarity paraphrase detection experiment on the GLUE MRPC validation set. It contains a single summary record rather than per-example predictions. The fields are: accuracy (float), f1 (float), and classification_report (string with class-wise precision, recall, and F1 statistics). In this workflow, it serves as the compact results table that aggregates model performance after generating sentence embeddings, scoring sentence pairs with cosine similarity, applying a fixed decision threshold, and comparing predictions against the MRPC ground-truth labels.",
      "st_paraphrase_minilm_l3_cosine_threshold_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "This dataset stores the evaluation summary for the paraphrase detection workflow using sentence-transformers/paraphrase-MiniLM-L6-v2 on the GLUE MRPC validation set with cosine-similarity thresholding at 0.78. It contains a single summary record with three fields: accuracy (float), f1 (float), and classification_report (string). The metrics are computed by comparing thresholded cosine-similarity predictions from the minilm_cosine_threshold_prediction dataset against the ground-truth labels in glue_mrpc_validation. Its role in this workflow is to provide a compact, experiment-level performance summary for the notebook, linking the full validation set and per-example predictions to aggregate evaluation results.",
      "st_paraphrase_minilm_l6_cosine_threshold_mrpc_summary",
      "record_list"
    ]
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 16874 | 151 | 120 | 15047 | 3.708s | 0.051s |

---

## Turn 13 — `description_search` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da5335dca0819b8ec45b970ad89a1f`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_oSnzm5sxHGTfdps8Ux3oJkQw",
    "output": "{\"ok\": true, \"result\": [[\"BASE\", \"This dataset stores per-example paraphrase predictions for the GLUE MRPC validation set produced by a DistilBERT-based cosine similarity pipeline. For each sentence pair from glue_mrpc_validation, the notebook encodes sentence1 and sentence2 with distilbert-base-uncased, applies masked max pooling to the token embeddings, computes the cosine similarity between the two normalized sentence embeddings, and converts that score to a binary prediction using a threshold of 0.85.\\n\\nStructure:\\n- prediction: integer binary label predicted by the similarity rule (1 = paraphrase, 0 = not paraphrase)\\n- cosine_scores: float cosine similarity between the max-pooled embeddings of the two sentences\\n\\nEach record corresponds to one input sentence pair and is linked back to the source validation examples through input_items. In this workflow, the dataset serves as the main model-output table for downstream evaluation, inspection of correct and incorrect predictions, and creation of the final summary metrics dataset.\", \"cosine_mrpc_max_pool_similarity_prediction\", \"record_list\"], [\"BASE\", \"This dataset stores per-example paraphrase predictions for the GLUE MRPC validation set produced by this notebook\\u2019s embedding-similarity baseline. Each record corresponds to one sentence pair from glue_mrpc_validation and contains two fields: prediction, a binary label (1 if the pair is predicted to be a paraphrase, 0 otherwise), and similarities, the cosine similarity score between the L2-normalized sentence embeddings of sentence1 and sentence2. The embeddings are generated with distilbert-base-uncased by averaging the last 4 hidden layers at the token level and then mean-pooling across tokens. Predictions are created by applying a fixed threshold of 0.85 to the similarity score. In this workflow, this dataset is the intermediate model output used to inspect individual examples, analyze errors, and compute the final evaluation summary in distilbert_last4_mean_cosine_mrpc_summary.\", \"cosine_mrpc_mean_similarity_prediction\", \"record_list\"], [\"BASE\", \"Per-example prediction dataset for the GLUE MRPC validation split. Each record corresponds to one sentence pair from glue_mrpc_validation and stores the output of a simple paraphrase classifier built from DistilBERT sentence embeddings. The dataset has two fields: prediction, a binary label where 1 means paraphrase and 0 means not paraphrase, produced by thresholding the cosine similarity at 0.85; and score, the raw cosine similarity between the L2-normalized first-token embeddings of sentence1 and sentence2 from distilbert-base-uncased. In this workflow, this dataset is the main record of model inference results, used for error analysis, inspection of individual examples, and as input to the downstream summary dataset distilbert_cls_cosine_mrpc_summary.\", \"cosine_mrpc_threshold_score\", \"record_list\"], [\"BASE\", \"Summary dataset for the DistilBERT cosine-similarity MRPC validation experiment. It contains an aggregate evaluation record for paraphrase detection on the GLUE MRPC validation split, where sentence1 and sentence2 are encoded with distilbert-base-uncased, the last 4 hidden layers are averaged, mean pooled into sentence embeddings, and classified by cosine similarity using a threshold of 0.85. The dataset structure has 3 fields: accuracy (float), f1 (float), and classification_report (string with per-class precision/recall/F1 and support). In this workflow, it serves as the final experiment-level metrics table summarizing model performance over the full validation set, with provenance linked to both the source dataset glue_mrpc_validation and the per-example prediction dataset cosine_mrpc_mean_similarity_prediction.\", \"distilbert_last4_mean_cosine_mrpc_summary\", \"record_list\"], [\"BASE\", \"This dataset stores the experiment-level evaluation summary for the DistilBERT max-pooling cosine-similarity approach on the GLUE MRPC validation set. It contains a single summary record with three fields: accuracy (float), f1 (float), and classification_report (string). The values are computed by comparing binary paraphrase predictions\\u2014generated by thresholding cosine similarity between max-pooled DistilBERT embeddings of sentence pairs\\u2014against the ground-truth MRPC labels. In this workflow, the dataset serves as the final aggregated results table for the notebook, capturing overall model performance in a compact form for later inspection, comparison, and lineage tracking back to the validation data and prediction outputs.\", \"distilbert_max_pool_cosine_mrpc_summary\", \"record_list\"], [\"BASE\", \"distilbert_mean_cosine_median_threshold_mrpc_summary is a summary dataset containing the evaluation results for the DistilBERT mean-pooled cosine-similarity baseline on the GLUE MRPC validation set. It stores aggregate metrics computed after encoding each sentence pair with distilbert-base-uncased, measuring cosine similarity between the two sentence embeddings, and converting scores to binary paraphrase predictions using the median similarity as the decision threshold. The dataset has three fields: accuracy (float), f1 (float), and classification_report (string with per-class precision/recall/F1 and support). In this workflow, it serves as the final experiment-level output that summarizes model performance over the full validation split, with provenance linked to both the source dataset glue_mrpc_validation and the per-example prediction dataset threshold_cosine_mrpc_similarity_prediction.\", \"distilbert_mean_cosine_median_threshold_mrpc_summary\", \"record_list\"], [\"BASE\", \"Summary dataset for the MRPC validation run using distilbert-base-uncased sentence embeddings. It contains aggregate evaluation results for paraphrase prediction on glue_mrpc_validation, where sentence1 and sentence2 are encoded separately, token embeddings are mean-pooled while excluding special tokens ([CLS], [SEP]), cosine similarity is computed between the two sentence embeddings, and a fixed threshold of 0.85 is used to produce binary paraphrase predictions.\\n\\nStructure: one record with fields accuracy (float), f1 (float), and classification_report (string). The record is linked to the full glue_mrpc_validation input range and to the no_special_cosine_mrpc_similarity_prediction dataset that stores per-example predictions and cosine scores.\\n\\nRole in workflow: this dataset is the experiment-level evaluation summary, used to capture the overall performance of the no-special-token mean-pooled cosine-similarity baseline on MRPC validation.\", \"distilbert_no_special_tokens_mean_cosine_mrpc_summary\", \"record_list\"], [\"BASE\", \"Row-level prediction dataset for the GLUE MRPC validation set produced by the sentence-transformers/paraphrase-MiniLM-L6-v2 model. Each record corresponds to one sentence pair from glue_mrpc_validation and stores two fields: prediction (binary label, where 0 = not_paraphrase and 1 = paraphrase) and score (cosine similarity between the normalized embeddings of sentence1 and sentence2). Predictions are generated by applying a fixed threshold of 0.78 to the cosine similarity score. In this workflow, this dataset serves as the per-example model output used for downstream evaluation, error analysis, and creation of the summary metrics dataset.\", \"minilm_cosine_threshold_prediction\", \"record_list\"], [\"BASE\", \"Binary paraphrase predictions for the GLUE MRPC validation set, generated by encoding each sentence pair with sentence-transformers/all-MiniLM-L6-v2 using max_seq_length=64, computing the cosine similarity between the normalized sentence1 and sentence2 embeddings, and applying a threshold of 0.80. This record list contains one row per validation example with a single field, prediction, where 1 indicates predicted paraphrase and 0 indicates predicted non-paraphrase. Each record is linked back to the corresponding source example in glue_mrpc_validation and to the two embedding lists sentence-transformers-sentence-1-max64 and sentence-transformers-sentence-2-max64. In this workflow, the dataset serves as the stored model output used for downstream evaluation, error analysis, and experiment summary reporting.\", \"sentence_transformers_mrpc_prediction_max64\", \"record_list\"], [\"BASE\", \"sentence_transformers_mrpc_prediction_threshold is a record list containing the per-example binary predictions produced on the GLUE MRPC validation set by a SentenceTransformer paraphrase model. Each record has a single field, prediction, where 1 indicates the sentence pair is predicted to be a paraphrase and 0 indicates not_paraphrase. Predictions are generated by encoding sentence1 and sentence2 with sentence-transformers/paraphrase-MiniLM-L3-v2, computing their cosine similarity via normalized embedding dot product, and applying a fixed threshold of 0.74. The dataset is aligned one-to-one with glue_mrpc_validation and is linked to the corresponding sentence-pair embeddings, making it the main stored output used for error analysis, metric computation, and creation of the workflow summary dataset.\", \"sentence_transformers_mrpc_prediction_threshold\", \"record_list\"], [\"BASE\", \"Binary prediction table for the GLUE MRPC validation set produced by the sentence-transformers/all-distilroberta-v1 model. Each record corresponds to one validation example and stores a single field, prediction, where 1 indicates the sentence pair is predicted to be a paraphrase and 0 indicates not_paraphrase. Predictions are generated by computing the cosine similarity between the normalized embeddings of sentence1 and sentence2 and applying a fixed threshold of 0.72. This dataset serves as the model output layer in the workflow, linking each prediction back to the original MRPC example and the two sentence embedding datasets, and it is used downstream to compute accuracy, F1, error analysis, and the experiment summary.\", \"sentence_transformers_mrpc_prediction_threshold_2\", \"record_list\"], [\"BASE\", \"Summary record list for the MRPC validation evaluation of a threshold-based paraphrase detection workflow using sentence-transformers/all-distilroberta-v1. This dataset contains experiment-level metrics computed by comparing predicted paraphrase labels from cosine similarity scores between sentence1 and sentence2 embeddings against the ground-truth labels in glue_mrpc_validation. Its structure is a record list with three fields: accuracy (float), f1 (float), and classification_report (string containing the full per-class evaluation report). In this notebook, it serves as the final aggregated result of the process, linking the full GLUE MRPC validation set and the generated prediction record list into a compact summary of model performance for the chosen cosine threshold.\", \"st_all_distilroberta_v1_cosine_threshold_mrpc_summary\", \"record_list\"], [\"BASE\", \"Summary dataset for the MRPC validation experiment using sentence-transformers/all-MiniLM-L6-v2 with max_seq_length=64 and cosine-similarity thresholding. It contains aggregate evaluation results for the prediction run, not per-example data. The record list has three fields: accuracy (float), f1 (float), and classification_report (string with the full class-wise sklearn report for not_paraphrase vs paraphrase). In this workflow, it stores the final performance summary of the predicted paraphrase labels generated from cosine scores between sentence1 and sentence2 embeddings on glue_mrpc_validation, providing a compact experiment-level result linked back to the source validation set and prediction outputs.\", \"st_all_minilm_l6_max_seq_len_64_cosine_mrpc_summary\", \"record_list\"], [\"BASE\", \"This dataset stores the run-level evaluation summary for the SentenceTransformer bi-encoder cosine-similarity paraphrase detection experiment on the GLUE MRPC validation set. It contains a single summary record rather than per-example predictions. The fields are: accuracy (float), f1 (float), and classification_report (string with class-wise precision, recall, and F1 statistics). In this workflow, it serves as the compact results table that aggregates model performance after generating sentence embeddings, scoring sentence pairs with cosine similarity, applying a fixed decision threshold, and comparing predictions against the MRPC ground-truth labels.\", \"st_paraphrase_minilm_l3_cosine_threshold_mrpc_summary\", \"record_list\"], [\"BASE\", \"This dataset stores the evaluation summary for the paraphrase detection workflow using sentence-transformers/paraphrase-MiniLM-L6-v2 on the GLUE MRPC validation set with cosine-similarity thresholding at 0.78. It contains a single summary record with three fields: accuracy (float), f1 (float), and classification_report (string). The metrics are computed by comparing thresholded cosine-similarity predictions from the minilm_cosine_threshold_prediction dataset against the ground-truth labels in glue_mrpc_validation. Its role in this workflow is to provide a compact, experiment-level performance summary for the notebook, linking the full validation set and per-example predictions to aggregate evaluation results.\", \"st_paraphrase_minilm_l6_cosine_threshold_mrpc_summary\", \"record_list\"]]}"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da5335dca0819b8ec45b970ad89a1f`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "description_search",
    "call_id": "call_yXZKGzu9XKEb9ybwgCInWYhm",
    "arguments": {
      "description_text": "distilbert cls cosine mrpc summary"
    }
  }
]
```

### Tool Call
**Tool:** `description_search` | **call_id:** `call_yXZKGzu9XKEb9ybwgCInWYhm`

**Arguments:**
```json
{
  "description_text": "distilbert cls cosine mrpc summary"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    [
      "BASE",
      "Summary dataset for the DistilBERT CLS cosine-similarity evaluation on the GLUE MRPC validation split. It contains aggregate evaluation results computed by comparing thresholded cosine-similarity predictions from sentence-pair embeddings against the ground-truth MRPC labels. The record list has three fields: accuracy (float), f1 (float), and classification_report (string with per-class precision/recall/F1 and support). In this workflow, it serves as the experiment-level evaluation artifact: a compact summary of model performance derived from the glue_mrpc_validation inputs and the per-example predictions stored in cosine_mrpc_threshold_score.",
      "distilbert_cls_cosine_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "Summary dataset for the MRPC validation run using distilbert-base-uncased sentence embeddings. It contains aggregate evaluation results for paraphrase prediction on glue_mrpc_validation, where sentence1 and sentence2 are encoded separately, token embeddings are mean-pooled while excluding special tokens ([CLS], [SEP]), cosine similarity is computed between the two sentence embeddings, and a fixed threshold of 0.85 is used to produce binary paraphrase predictions.\n\nStructure: one record with fields accuracy (float), f1 (float), and classification_report (string). The record is linked to the full glue_mrpc_validation input range and to the no_special_cosine_mrpc_similarity_prediction dataset that stores per-example predictions and cosine scores.\n\nRole in workflow: this dataset is the experiment-level evaluation summary, used to capture the overall performance of the no-special-token mean-pooled cosine-similarity baseline on MRPC validation.",
      "distilbert_no_special_tokens_mean_cosine_mrpc_summary",
      "record_list"
    ],
    [
      "BASE",
      "Per-example prediction dataset for the GLUE MRPC validation split. Each record corresponds to one sentence pair from glue_mrpc_validation and stores the model output from this notebook\u2019s similarity-based paraphrase detection pipeline using distilbert-base-uncased embeddings. The fields are: prediction (binary label, 1 if the cosine similarity between the two sentence embeddings is at least 0.85, otherwise 0) and cosine_scores (the raw cosine similarity score as a float). The embeddings are produced by mean-pooling DistilBERT token representations while excluding special tokens such as [CLS] and [SEP], followed by L2 normalization. In this workflow, this dataset serves as the detailed per-row inference output that links back to the original MRPC validation examples and is then used to compute and document overall evaluation metrics in the summary dataset.",
      "no_special_cosine_mrpc_similarity_prediction",
      "record_list"
    ]
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 19665 | 53 | 25 | 17838 | 1.612s | 0.034s |

---

## Turn 14 — `get_item` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da53377d10819bbba31660a02f8b9b`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_yXZKGzu9XKEb9ybwgCInWYhm",
    "output": "{\"ok\": true, \"result\": [[\"BASE\", \"Summary dataset for the DistilBERT CLS cosine-similarity evaluation on the GLUE MRPC validation split. It contains aggregate evaluation results computed by comparing thresholded cosine-similarity predictions from sentence-pair embeddings against the ground-truth MRPC labels. The record list has three fields: accuracy (float), f1 (float), and classification_report (string with per-class precision/recall/F1 and support). In this workflow, it serves as the experiment-level evaluation artifact: a compact summary of model performance derived from the glue_mrpc_validation inputs and the per-example predictions stored in cosine_mrpc_threshold_score.\", \"distilbert_cls_cosine_mrpc_summary\", \"record_list\"], [\"BASE\", \"Summary dataset for the MRPC validation run using distilbert-base-uncased sentence embeddings. It contains aggregate evaluation results for paraphrase prediction on glue_mrpc_validation, where sentence1 and sentence2 are encoded separately, token embeddings are mean-pooled while excluding special tokens ([CLS], [SEP]), cosine similarity is computed between the two sentence embeddings, and a fixed threshold of 0.85 is used to produce binary paraphrase predictions.\\n\\nStructure: one record with fields accuracy (float), f1 (float), and classification_report (string). The record is linked to the full glue_mrpc_validation input range and to the no_special_cosine_mrpc_similarity_prediction dataset that stores per-example predictions and cosine scores.\\n\\nRole in workflow: this dataset is the experiment-level evaluation summary, used to capture the overall performance of the no-special-token mean-pooled cosine-similarity baseline on MRPC validation.\", \"distilbert_no_special_tokens_mean_cosine_mrpc_summary\", \"record_list\"], [\"BASE\", \"Per-example prediction dataset for the GLUE MRPC validation split. Each record corresponds to one sentence pair from glue_mrpc_validation and stores the model output from this notebook\\u2019s similarity-based paraphrase detection pipeline using distilbert-base-uncased embeddings. The fields are: prediction (binary label, 1 if the cosine similarity between the two sentence embeddings is at least 0.85, otherwise 0) and cosine_scores (the raw cosine similarity score as a float). The embeddings are produced by mean-pooling DistilBERT token representations while excluding special tokens such as [CLS] and [SEP], followed by L2 normalization. In this workflow, this dataset serves as the detailed per-row inference output that links back to the original MRPC validation examples and is then used to compute and document overall evaluation metrics in the summary dataset.\", \"no_special_cosine_mrpc_similarity_prediction\", \"record_list\"]]}"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da53377d10819bbba31660a02f8b9b`

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
    "call_id": "call_MFc5JXLPb8S2zQc5JOe2R4Pc",
    "arguments": {
      "item_name": "distilbert_cls_cosine_mrpc_summary",
      "start_position": 0,
      "end_position": 5
    }
  }
]
```

### Tool Call
**Tool:** `get_item` | **call_id:** `call_MFc5JXLPb8S2zQc5JOe2R4Pc`

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
| 20277 | 48 | 9 | 18450 | 1.807s | 0.023s |

---

## Turn 15 — `description_search` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da5339545c819bae90b08e71ae69d5`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_MFc5JXLPb8S2zQc5JOe2R4Pc",
    "output": "{\"ok\": true, \"result\": [{\"accuracy\": 0.6862745098039216, \"f1\": 0.8134110787172012, \"classification_report\": \"                precision    recall  f1-score   support\\n\\nnot_paraphrase       1.00      0.01      0.02       129\\n    paraphrase       0.69      1.00      0.81       279\\n\\n      accuracy                           0.69       408\\n     macro avg       0.84      0.50      0.41       408\\n  weighted avg       0.78      0.69      0.56       408\\n\"}]}"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da5339545c819bae90b08e71ae69d5`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "description_search",
    "call_id": "call_MOqJSUK7kdoB7dVXxXjWrrWf",
    "arguments": {
      "description_text": "all-MiniLM-L6-v2 cosine threshold summary"
    }
  }
]
```

### Tool Call
**Tool:** `description_search` | **call_id:** `call_MOqJSUK7kdoB7dVXxXjWrrWf`

**Arguments:**
```json
{
  "description_text": "all-MiniLM-L6-v2 cosine threshold summary"
}
```

### Tool Output
```json
{
  "ok": true,
  "result": [
    [
      "BASE",
      "Binary paraphrase predictions for the GLUE MRPC validation set, generated by encoding each sentence pair with sentence-transformers/all-MiniLM-L6-v2 using max_seq_length=64, computing the cosine similarity between the normalized sentence1 and sentence2 embeddings, and applying a threshold of 0.80. This record list contains one row per validation example with a single field, prediction, where 1 indicates predicted paraphrase and 0 indicates predicted non-paraphrase. Each record is linked back to the corresponding source example in glue_mrpc_validation and to the two embedding lists sentence-transformers-sentence-1-max64 and sentence-transformers-sentence-2-max64. In this workflow, the dataset serves as the stored model output used for downstream evaluation, error analysis, and experiment summary reporting.",
      "sentence_transformers_mrpc_prediction_max64",
      "record_list"
    ],
    [
      "BASE",
      "Summary dataset for the MRPC validation experiment using sentence-transformers/all-MiniLM-L6-v2 with max_seq_length=64 and cosine-similarity thresholding. It contains aggregate evaluation results for the prediction run, not per-example data. The record list has three fields: accuracy (float), f1 (float), and classification_report (string with the full class-wise sklearn report for not_paraphrase vs paraphrase). In this workflow, it stores the final performance summary of the predicted paraphrase labels generated from cosine scores between sentence1 and sentence2 embeddings on glue_mrpc_validation, providing a compact experiment-level result linked back to the source validation set and prediction outputs.",
      "st_all_minilm_l6_max_seq_len_64_cosine_mrpc_summary",
      "record_list"
    ]
  ]
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 20491 | 831 | 800 | 18664 | 13.410s | 0.039s |

---

## Turn 16 — `description_search` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da5346c85c819b8a2b2c83818eb57e`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_MOqJSUK7kdoB7dVXxXjWrrWf",
    "output": "{\"ok\": true, \"result\": [[\"BASE\", \"Binary paraphrase predictions for the GLUE MRPC validation set, generated by encoding each sentence pair with sentence-transformers/all-MiniLM-L6-v2 using max_seq_length=64, computing the cosine similarity between the normalized sentence1 and sentence2 embeddings, and applying a threshold of 0.80. This record list contains one row per validation example with a single field, prediction, where 1 indicates predicted paraphrase and 0 indicates predicted non-paraphrase. Each record is linked back to the corresponding source example in glue_mrpc_validation and to the two embedding lists sentence-transformers-sentence-1-max64 and sentence-transformers-sentence-2-max64. In this workflow, the dataset serves as the stored model output used for downstream evaluation, error analysis, and experiment summary reporting.\", \"sentence_transformers_mrpc_prediction_max64\", \"record_list\"], [\"BASE\", \"Summary dataset for the MRPC validation experiment using sentence-transformers/all-MiniLM-L6-v2 with max_seq_length=64 and cosine-similarity thresholding. It contains aggregate evaluation results for the prediction run, not per-example data. The record list has three fields: accuracy (float), f1 (float), and classification_report (string with the full class-wise sklearn report for not_paraphrase vs paraphrase). In this workflow, it stores the final performance summary of the predicted paraphrase labels generated from cosine scores between sentence1 and sentence2 embeddings on glue_mrpc_validation, providing a compact experiment-level result linked back to the source validation set and prediction outputs.\", \"st_all_minilm_l6_max_seq_len_64_cosine_mrpc_summary\", \"record_list\"]]}"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da5346c85c819b8a2b2c83818eb57e`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "description_search",
    "call_id": "call_fm7mAsNsdZ99BJed8Sz96Lu8",
    "arguments": {
      "description_text": "threshold sweep paraphrase similarity MRPC"
    }
  }
]
```

### Tool Call
**Tool:** `description_search` | **call_id:** `call_fm7mAsNsdZ99BJed8Sz96Lu8`

**Arguments:**
```json
{
  "description_text": "threshold sweep paraphrase similarity MRPC"
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
| 21683 | 46 | 19 | 19856 | 1.611s | 0.052s |

---

## Turn 17 — `description_search` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da534871a8819b81705e6fccb6eecf`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_fm7mAsNsdZ99BJed8Sz96Lu8",
    "output": "{\"ok\": true, \"result\": []}"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da534871a8819b81705e6fccb6eecf`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "description_search",
    "call_id": "call_pEpkRuLzhalXRGmeqGunw8dw",
    "arguments": {
      "description_text": "distilbert cosine threshold 0.8 MRPC summary"
    }
  }
]
```

### Tool Call
**Tool:** `description_search` | **call_id:** `call_pEpkRuLzhalXRGmeqGunw8dw`

**Arguments:**
```json
{
  "description_text": "distilbert cosine threshold 0.8 MRPC summary"
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
| 21750 | 1567 | 1535 | 19923 | 24.160s | 0.056s |

---

## Turn 18 — `description_search` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da5360aa40819bac3d9cfcfd7b428e`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_pEpkRuLzhalXRGmeqGunw8dw",
    "output": "{\"ok\": true, \"result\": []}"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da5360aa40819bac3d9cfcfd7b428e`

**Output items:**
```json
[
  {
    "type": "reasoning",
    "summary": []
  },
  {
    "type": "function_call",
    "name": "description_search",
    "call_id": "call_iY9jG3C82mtvH5OmTujLijEc",
    "arguments": {
      "description_text": "cosine threshold 0.70 similarity summary"
    }
  }
]
```

### Tool Call
**Tool:** `description_search` | **call_id:** `call_iY9jG3C82mtvH5OmTujLijEc`

**Arguments:**
```json
{
  "description_text": "cosine threshold 0.70 similarity summary"
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
| 23338 | 50 | 21 | 21511 | 1.976s | 0.042s |

---

## Turn 19 — `finalize_result` [ok]

### Model Input
**previous_response_id:** `resp_0eadf82ded6a90600069da5362b2d8819bbb601a56d3924cef`

**Pending messages:**
```json
[
  {
    "type": "function_call_output",
    "call_id": "call_iY9jG3C82mtvH5OmTujLijEc",
    "output": "{\"ok\": true, \"result\": []}"
  }
]
```

### Model Output
**response_id:** `resp_0eadf82ded6a90600069da5362b2d8819bbb601a56d3924cef`

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
    "call_id": "call_AhB1Y70esdzz4HI3vF6PNv3e",
    "arguments": {
      "summary": "{\"rows\":[{\"family\":\"Raw DistilBERT embedding similarity\",\"model_or_variant\":\"distilbert-base-uncased CLS pooling\",\"decision_rule\":\"cosine >= 0.85\",\"accuracy\":0.686,\"paraphrase_f1\":0.813,\"not_paraphrase_recall\":0.01,\"paraphrase_recall\":1.0,\"summary_item\":\"distilbert_cls_cosine_mrpc_summary\"},{\"family\":\"Raw DistilBERT embedding similarity\",\"model_or_variant\":\"distilbert-base-uncased last-4-layer mean pooling\",\"decision_rule\":\"cosine >= 0.85\",\"accuracy\":0.684,\"paraphrase_f1\":0.812,\"not_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"summary_item\":\"distilbert_last4_mean_cosine_mrpc_summary\"},{\"family\":\"Raw DistilBERT embedding similarity\",\"model_or_variant\":\"distilbert-base-uncased mean pooling without special tokens\",\"decision_rule\":\"cosine >= 0.85\",\"accuracy\":0.703,\"paraphrase_f1\":0.821,\"not_paraphrase_recall\":0.07,\"paraphrase_recall\":1.0,\"summary_item\":\"distilbert_no_special_tokens_mean_cosine_mrpc_summary\"},{\"family\":\"Raw DistilBERT embedding similarity\",\"model_or_variant\":\"distilbert-base-uncased mean pooling\",\"decision_rule\":\"cosine >= median similarity of validation set\",\"accuracy\":0.65,\"paraphrase_f1\":0.704,\"not_paraphrase_recall\":0.74,\"paraphrase_recall\":0.61,\"summary_item\":\"distilbert_mean_cosine_median_threshold_mrpc_summary\"},{\"family\":\"SentenceTransformer bi-encoder\",\"model_or_variant\":\"sentence-transformers/paraphrase-MiniLM-L3-v2\",\"decision_rule\":\"cosine >= 0.74\",\"accuracy\":0.713,\"paraphrase_f1\":0.793,\"not_paraphrase_recall\":0.52,\"paraphrase_recall\":0.8,\"summary_item\":\"st_paraphrase_minilm_l3_cosine_threshold_mrpc_summary\"},{\"family\":\"SentenceTransformer bi-encoder\",\"model_or_variant\":\"sentence-transformers/paraphrase-MiniLM-L6-v2\",\"decision_rule\":\"cosine >= 0.78\",\"accuracy\":0.701,\"paraphrase_f1\":0.771,\"not_paraphrase_recall\":0.63,\"paraphrase_recall\":0.73,\"summary_item\":\"st_paraphrase_minilm_l6_cosine_threshold_mrpc_summary\"},{\"family\":\"SentenceTransformer bi-encoder\",\"model_or_variant\":\"sentence-transformers/all-MiniLM-L6-v2 (max_seq_length=64)\",\"decision_rule\":\"cosine >= 0.80\",\"accuracy\":0.676,\"paraphrase_f1\":0.744,\"not_paraphrase_recall\":0.65,\"paraphrase_recall\":0.69,\"summary_item\":\"st_all_minilm_l6_max_seq_len_64_cosine_mrpc_summary\"},{\"family\":\"SentenceTransformer bi-encoder\",\"model_or_variant\":\"sentence-transformers/all-distilroberta-v1\",\"decision_rule\":\"cosine >= 0.72\",\"accuracy\":0.723,\"paraphrase_f1\":0.806,\"not_paraphrase_recall\":0.47,\"paraphrase_recall\":0.84,\"summary_item\":\"st_all_distilroberta_v1_cosine_threshold_mrpc_summary\"}],\"summary\":\"Repository evidence from GLUE MRPC validation summaries indicates that similarity-based paraphrase classifiers are quite sensitive to the decision threshold, but the degree of sensitivity differs markedly by model family. On this split, the class balance is skewed toward paraphrases (279 paraphrase vs 129 not_paraphrase), which makes threshold calibration especially important. For raw DistilBERT embedding-similarity baselines, a fixed cosine threshold of 0.85 is poorly calibrated: across CLS, last-4 mean, and no-special-token mean pooling, paraphrase recall is 1.00 while not-paraphrase recall collapses to 0.00-0.07. These runs therefore behave almost like an always-paraphrase classifier, even though their reported paraphrase-class F1 remains deceptively high (0.812-0.821) because the positive class dominates the validation set. When the thresholding rule is changed within the same DistilBERT family\u2014from fixed 0.85 to the validation-set median similarity\u2014the operating point shifts sharply: not-paraphrase recall jumps to 0.74 while paraphrase recall falls to 0.61, and overall accuracy changes only modestly (0.684 to 0.650). This is strong evidence that raw-embedding cosine classifiers are highly threshold-sensitive and that class-wise metrics are more informative than paraphrase F1 alone. In contrast, SentenceTransformer bi-encoders appear less brittle at their chosen thresholds. Across paraphrase-MiniLM-L3-v2 (0.74), paraphrase-MiniLM-L6-v2 (0.78), all-MiniLM-L6-v2 max64 (0.80), and all-distilroberta-v1 (0.72), both-class recalls remain moderate rather than collapsing, with not-paraphrase recall between 0.47 and 0.65 and paraphrase recall between 0.69 and 0.84. Their accuracies cluster in a narrower and generally stronger range (0.676-0.723), suggesting that sentence-similarity-tuned bi-encoders produce score distributions that are easier to threshold sensibly. The best stored SentenceTransformer result is all-distilroberta-v1 at cosine >= 0.72 (accuracy 0.723, paraphrase F1 0.806), followed closely by paraphrase-MiniLM-L3-v2 at cosine >= 0.74. Overall, the repository suggests that threshold choice matters substantially, but especially for raw DistilBERT embedding baselines; SentenceTransformer families are still threshold-dependent, yet they show more stable and balanced behavior at their selected cutoffs. A key limitation is that the repository stores only a few discrete thresholded runs rather than full threshold sweeps, ROC curves, or PR curves, so the evidence supports comparative sensitivity claims but not a precise estimate of each model's optimal threshold or full calibration profile. The table should therefore be read as discrete operating-point evidence, not as a complete threshold-response curve.\"}"
    }
  }
]
```

### Tool Call
**Tool:** `finalize_result` | **call_id:** `call_AhB1Y70esdzz4HI3vF6PNv3e`

**Arguments:**
```json
{
  "summary": "{\"rows\":[{\"family\":\"Raw DistilBERT embedding similarity\",\"model_or_variant\":\"distilbert-base-uncased CLS pooling\",\"decision_rule\":\"cosine >= 0.85\",\"accuracy\":0.686,\"paraphrase_f1\":0.813,\"not_paraphrase_recall\":0.01,\"paraphrase_recall\":1.0,\"summary_item\":\"distilbert_cls_cosine_mrpc_summary\"},{\"family\":\"Raw DistilBERT embedding similarity\",\"model_or_variant\":\"distilbert-base-uncased last-4-layer mean pooling\",\"decision_rule\":\"cosine >= 0.85\",\"accuracy\":0.684,\"paraphrase_f1\":0.812,\"not_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"summary_item\":\"distilbert_last4_mean_cosine_mrpc_summary\"},{\"family\":\"Raw DistilBERT embedding similarity\",\"model_or_variant\":\"distilbert-base-uncased mean pooling without special tokens\",\"decision_rule\":\"cosine >= 0.85\",\"accuracy\":0.703,\"paraphrase_f1\":0.821,\"not_paraphrase_recall\":0.07,\"paraphrase_recall\":1.0,\"summary_item\":\"distilbert_no_special_tokens_mean_cosine_mrpc_summary\"},{\"family\":\"Raw DistilBERT embedding similarity\",\"model_or_variant\":\"distilbert-base-uncased mean pooling\",\"decision_rule\":\"cosine >= median similarity of validation set\",\"accuracy\":0.65,\"paraphrase_f1\":0.704,\"not_paraphrase_recall\":0.74,\"paraphrase_recall\":0.61,\"summary_item\":\"distilbert_mean_cosine_median_threshold_mrpc_summary\"},{\"family\":\"SentenceTransformer bi-encoder\",\"model_or_variant\":\"sentence-transformers/paraphrase-MiniLM-L3-v2\",\"decision_rule\":\"cosine >= 0.74\",\"accuracy\":0.713,\"paraphrase_f1\":0.793,\"not_paraphrase_recall\":0.52,\"paraphrase_recall\":0.8,\"summary_item\":\"st_paraphrase_minilm_l3_cosine_threshold_mrpc_summary\"},{\"family\":\"SentenceTransformer bi-encoder\",\"model_or_variant\":\"sentence-transformers/paraphrase-MiniLM-L6-v2\",\"decision_rule\":\"cosine >= 0.78\",\"accuracy\":0.701,\"paraphrase_f1\":0.771,\"not_paraphrase_recall\":0.63,\"paraphrase_recall\":0.73,\"summary_item\":\"st_paraphrase_minilm_l6_cosine_threshold_mrpc_summary\"},{\"family\":\"SentenceTransformer bi-encoder\",\"model_or_variant\":\"sentence-transformers/all-MiniLM-L6-v2 (max_seq_length=64)\",\"decision_rule\":\"cosine >= 0.80\",\"accuracy\":0.676,\"paraphrase_f1\":0.744,\"not_paraphrase_recall\":0.65,\"paraphrase_recall\":0.69,\"summary_item\":\"st_all_minilm_l6_max_seq_len_64_cosine_mrpc_summary\"},{\"family\":\"SentenceTransformer bi-encoder\",\"model_or_variant\":\"sentence-transformers/all-distilroberta-v1\",\"decision_rule\":\"cosine >= 0.72\",\"accuracy\":0.723,\"paraphrase_f1\":0.806,\"not_paraphrase_recall\":0.47,\"paraphrase_recall\":0.84,\"summary_item\":\"st_all_distilroberta_v1_cosine_threshold_mrpc_summary\"}],\"summary\":\"Repository evidence from GLUE MRPC validation summaries indicates that similarity-based paraphrase classifiers are quite sensitive to the decision threshold, but the degree of sensitivity differs markedly by model family. On this split, the class balance is skewed toward paraphrases (279 paraphrase vs 129 not_paraphrase), which makes threshold calibration especially important. For raw DistilBERT embedding-similarity baselines, a fixed cosine threshold of 0.85 is poorly calibrated: across CLS, last-4 mean, and no-special-token mean pooling, paraphrase recall is 1.00 while not-paraphrase recall collapses to 0.00-0.07. These runs therefore behave almost like an always-paraphrase classifier, even though their reported paraphrase-class F1 remains deceptively high (0.812-0.821) because the positive class dominates the validation set. When the thresholding rule is changed within the same DistilBERT family\u2014from fixed 0.85 to the validation-set median similarity\u2014the operating point shifts sharply: not-paraphrase recall jumps to 0.74 while paraphrase recall falls to 0.61, and overall accuracy changes only modestly (0.684 to 0.650). This is strong evidence that raw-embedding cosine classifiers are highly threshold-sensitive and that class-wise metrics are more informative than paraphrase F1 alone. In contrast, SentenceTransformer bi-encoders appear less brittle at their chosen thresholds. Across paraphrase-MiniLM-L3-v2 (0.74), paraphrase-MiniLM-L6-v2 (0.78), all-MiniLM-L6-v2 max64 (0.80), and all-distilroberta-v1 (0.72), both-class recalls remain moderate rather than collapsing, with not-paraphrase recall between 0.47 and 0.65 and paraphrase recall between 0.69 and 0.84. Their accuracies cluster in a narrower and generally stronger range (0.676-0.723), suggesting that sentence-similarity-tuned bi-encoders produce score distributions that are easier to threshold sensibly. The best stored SentenceTransformer result is all-distilroberta-v1 at cosine >= 0.72 (accuracy 0.723, paraphrase F1 0.806), followed closely by paraphrase-MiniLM-L3-v2 at cosine >= 0.74. Overall, the repository suggests that threshold choice matters substantially, but especially for raw DistilBERT embedding baselines; SentenceTransformer families are still threshold-dependent, yet they show more stable and balanced behavior at their selected cutoffs. A key limitation is that the repository stores only a few discrete thresholded runs rather than full threshold sweeps, ROC curves, or PR curves, so the evidence supports comparative sensitivity claims but not a precise estimate of each model's optimal threshold or full calibration profile. The table should therefore be read as discrete operating-point evidence, not as a complete threshold-response curve.\"}"
}
```

### Tool Output
```json
{
  "summary": "{\"rows\":[{\"family\":\"Raw DistilBERT embedding similarity\",\"model_or_variant\":\"distilbert-base-uncased CLS pooling\",\"decision_rule\":\"cosine >= 0.85\",\"accuracy\":0.686,\"paraphrase_f1\":0.813,\"not_paraphrase_recall\":0.01,\"paraphrase_recall\":1.0,\"summary_item\":\"distilbert_cls_cosine_mrpc_summary\"},{\"family\":\"Raw DistilBERT embedding similarity\",\"model_or_variant\":\"distilbert-base-uncased last-4-layer mean pooling\",\"decision_rule\":\"cosine >= 0.85\",\"accuracy\":0.684,\"paraphrase_f1\":0.812,\"not_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"summary_item\":\"distilbert_last4_mean_cosine_mrpc_summary\"},{\"family\":\"Raw DistilBERT embedding similarity\",\"model_or_variant\":\"distilbert-base-uncased mean pooling without special tokens\",\"decision_rule\":\"cosine >= 0.85\",\"accuracy\":0.703,\"paraphrase_f1\":0.821,\"not_paraphrase_recall\":0.07,\"paraphrase_recall\":1.0,\"summary_item\":\"distilbert_no_special_tokens_mean_cosine_mrpc_summary\"},{\"family\":\"Raw DistilBERT embedding similarity\",\"model_or_variant\":\"distilbert-base-uncased mean pooling\",\"decision_rule\":\"cosine >= median similarity of validation set\",\"accuracy\":0.65,\"paraphrase_f1\":0.704,\"not_paraphrase_recall\":0.74,\"paraphrase_recall\":0.61,\"summary_item\":\"distilbert_mean_cosine_median_threshold_mrpc_summary\"},{\"family\":\"SentenceTransformer bi-encoder\",\"model_or_variant\":\"sentence-transformers/paraphrase-MiniLM-L3-v2\",\"decision_rule\":\"cosine >= 0.74\",\"accuracy\":0.713,\"paraphrase_f1\":0.793,\"not_paraphrase_recall\":0.52,\"paraphrase_recall\":0.8,\"summary_item\":\"st_paraphrase_minilm_l3_cosine_threshold_mrpc_summary\"},{\"family\":\"SentenceTransformer bi-encoder\",\"model_or_variant\":\"sentence-transformers/paraphrase-MiniLM-L6-v2\",\"decision_rule\":\"cosine >= 0.78\",\"accuracy\":0.701,\"paraphrase_f1\":0.771,\"not_paraphrase_recall\":0.63,\"paraphrase_recall\":0.73,\"summary_item\":\"st_paraphrase_minilm_l6_cosine_threshold_mrpc_summary\"},{\"family\":\"SentenceTransformer bi-encoder\",\"model_or_variant\":\"sentence-transformers/all-MiniLM-L6-v2 (max_seq_length=64)\",\"decision_rule\":\"cosine >= 0.80\",\"accuracy\":0.676,\"paraphrase_f1\":0.744,\"not_paraphrase_recall\":0.65,\"paraphrase_recall\":0.69,\"summary_item\":\"st_all_minilm_l6_max_seq_len_64_cosine_mrpc_summary\"},{\"family\":\"SentenceTransformer bi-encoder\",\"model_or_variant\":\"sentence-transformers/all-distilroberta-v1\",\"decision_rule\":\"cosine >= 0.72\",\"accuracy\":0.723,\"paraphrase_f1\":0.806,\"not_paraphrase_recall\":0.47,\"paraphrase_recall\":0.84,\"summary_item\":\"st_all_distilroberta_v1_cosine_threshold_mrpc_summary\"}],\"summary\":\"Repository evidence from GLUE MRPC validation summaries indicates that similarity-based paraphrase classifiers are quite sensitive to the decision threshold, but the degree of sensitivity differs markedly by model family. On this split, the class balance is skewed toward paraphrases (279 paraphrase vs 129 not_paraphrase), which makes threshold calibration especially important. For raw DistilBERT embedding-similarity baselines, a fixed cosine threshold of 0.85 is poorly calibrated: across CLS, last-4 mean, and no-special-token mean pooling, paraphrase recall is 1.00 while not-paraphrase recall collapses to 0.00-0.07. These runs therefore behave almost like an always-paraphrase classifier, even though their reported paraphrase-class F1 remains deceptively high (0.812-0.821) because the positive class dominates the validation set. When the thresholding rule is changed within the same DistilBERT family\u2014from fixed 0.85 to the validation-set median similarity\u2014the operating point shifts sharply: not-paraphrase recall jumps to 0.74 while paraphrase recall falls to 0.61, and overall accuracy changes only modestly (0.684 to 0.650). This is strong evidence that raw-embedding cosine classifiers are highly threshold-sensitive and that class-wise metrics are more informative than paraphrase F1 alone. In contrast, SentenceTransformer bi-encoders appear less brittle at their chosen thresholds. Across paraphrase-MiniLM-L3-v2 (0.74), paraphrase-MiniLM-L6-v2 (0.78), all-MiniLM-L6-v2 max64 (0.80), and all-distilroberta-v1 (0.72), both-class recalls remain moderate rather than collapsing, with not-paraphrase recall between 0.47 and 0.65 and paraphrase recall between 0.69 and 0.84. Their accuracies cluster in a narrower and generally stronger range (0.676-0.723), suggesting that sentence-similarity-tuned bi-encoders produce score distributions that are easier to threshold sensibly. The best stored SentenceTransformer result is all-distilroberta-v1 at cosine >= 0.72 (accuracy 0.723, paraphrase F1 0.806), followed closely by paraphrase-MiniLM-L3-v2 at cosine >= 0.74. Overall, the repository suggests that threshold choice matters substantially, but especially for raw DistilBERT embedding baselines; SentenceTransformer families are still threshold-dependent, yet they show more stable and balanced behavior at their selected cutoffs. A key limitation is that the repository stores only a few discrete thresholded runs rather than full threshold sweeps, ROC curves, or PR curves, so the evidence supports comparative sensitivity claims but not a precise estimate of each model's optimal threshold or full calibration profile. The table should therefore be read as discrete operating-point evidence, not as a complete threshold-response curve.\"}"
}
```

### Metrics
| tokens_in | tokens_out | reasoning | conv_tokens | api_latency | exec_latency |
|-----------|------------|-----------|-------------|-------------|--------------|
| 23409 | 5680 | 4297 | 21582 | 83.485s | 0.000s |

---

# Run Summary

**Final Result:**
```json
{
  "summary": "{\"rows\":[{\"family\":\"Raw DistilBERT embedding similarity\",\"model_or_variant\":\"distilbert-base-uncased CLS pooling\",\"decision_rule\":\"cosine >= 0.85\",\"accuracy\":0.686,\"paraphrase_f1\":0.813,\"not_paraphrase_recall\":0.01,\"paraphrase_recall\":1.0,\"summary_item\":\"distilbert_cls_cosine_mrpc_summary\"},{\"family\":\"Raw DistilBERT embedding similarity\",\"model_or_variant\":\"distilbert-base-uncased last-4-layer mean pooling\",\"decision_rule\":\"cosine >= 0.85\",\"accuracy\":0.684,\"paraphrase_f1\":0.812,\"not_paraphrase_recall\":0.0,\"paraphrase_recall\":1.0,\"summary_item\":\"distilbert_last4_mean_cosine_mrpc_summary\"},{\"family\":\"Raw DistilBERT embedding similarity\",\"model_or_variant\":\"distilbert-base-uncased mean pooling without special tokens\",\"decision_rule\":\"cosine >= 0.85\",\"accuracy\":0.703,\"paraphrase_f1\":0.821,\"not_paraphrase_recall\":0.07,\"paraphrase_recall\":1.0,\"summary_item\":\"distilbert_no_special_tokens_mean_cosine_mrpc_summary\"},{\"family\":\"Raw DistilBERT embedding similarity\",\"model_or_variant\":\"distilbert-base-uncased mean pooling\",\"decision_rule\":\"cosine >= median similarity of validation set\",\"accuracy\":0.65,\"paraphrase_f1\":0.704,\"not_paraphrase_recall\":0.74,\"paraphrase_recall\":0.61,\"summary_item\":\"distilbert_mean_cosine_median_threshold_mrpc_summary\"},{\"family\":\"SentenceTransformer bi-encoder\",\"model_or_variant\":\"sentence-transformers/paraphrase-MiniLM-L3-v2\",\"decision_rule\":\"cosine >= 0.74\",\"accuracy\":0.713,\"paraphrase_f1\":0.793,\"not_paraphrase_recall\":0.52,\"paraphrase_recall\":0.8,\"summary_item\":\"st_paraphrase_minilm_l3_cosine_threshold_mrpc_summary\"},{\"family\":\"SentenceTransformer bi-encoder\",\"model_or_variant\":\"sentence-transformers/paraphrase-MiniLM-L6-v2\",\"decision_rule\":\"cosine >= 0.78\",\"accuracy\":0.701,\"paraphrase_f1\":0.771,\"not_paraphrase_recall\":0.63,\"paraphrase_recall\":0.73,\"summary_item\":\"st_paraphrase_minilm_l6_cosine_threshold_mrpc_summary\"},{\"family\":\"SentenceTransformer bi-encoder\",\"model_or_variant\":\"sentence-transformers/all-MiniLM-L6-v2 (max_seq_length=64)\",\"decision_rule\":\"cosine >= 0.80\",\"accuracy\":0.676,\"paraphrase_f1\":0.744,\"not_paraphrase_recall\":0.65,\"paraphrase_recall\":0.69,\"summary_item\":\"st_all_minilm_l6_max_seq_len_64_cosine_mrpc_summary\"},{\"family\":\"SentenceTransformer bi-encoder\",\"model_or_variant\":\"sentence-transformers/all-distilroberta-v1\",\"decision_rule\":\"cosine >= 0.72\",\"accuracy\":0.723,\"paraphrase_f1\":0.806,\"not_paraphrase_recall\":0.47,\"paraphrase_recall\":0.84,\"summary_item\":\"st_all_distilroberta_v1_cosine_threshold_mrpc_summary\"}],\"summary\":\"Repository evidence from GLUE MRPC validation summaries indicates that similarity-based paraphrase classifiers are quite sensitive to the decision threshold, but the degree of sensitivity differs markedly by model family. On this split, the class balance is skewed toward paraphrases (279 paraphrase vs 129 not_paraphrase), which makes threshold calibration especially important. For raw DistilBERT embedding-similarity baselines, a fixed cosine threshold of 0.85 is poorly calibrated: across CLS, last-4 mean, and no-special-token mean pooling, paraphrase recall is 1.00 while not-paraphrase recall collapses to 0.00-0.07. These runs therefore behave almost like an always-paraphrase classifier, even though their reported paraphrase-class F1 remains deceptively high (0.812-0.821) because the positive class dominates the validation set. When the thresholding rule is changed within the same DistilBERT family\u2014from fixed 0.85 to the validation-set median similarity\u2014the operating point shifts sharply: not-paraphrase recall jumps to 0.74 while paraphrase recall falls to 0.61, and overall accuracy changes only modestly (0.684 to 0.650). This is strong evidence that raw-embedding cosine classifiers are highly threshold-sensitive and that class-wise metrics are more informative than paraphrase F1 alone. In contrast, SentenceTransformer bi-encoders appear less brittle at their chosen thresholds. Across paraphrase-MiniLM-L3-v2 (0.74), paraphrase-MiniLM-L6-v2 (0.78), all-MiniLM-L6-v2 max64 (0.80), and all-distilroberta-v1 (0.72), both-class recalls remain moderate rather than collapsing, with not-paraphrase recall between 0.47 and 0.65 and paraphrase recall between 0.69 and 0.84. Their accuracies cluster in a narrower and generally stronger range (0.676-0.723), suggesting that sentence-similarity-tuned bi-encoders produce score distributions that are easier to threshold sensibly. The best stored SentenceTransformer result is all-distilroberta-v1 at cosine >= 0.72 (accuracy 0.723, paraphrase F1 0.806), followed closely by paraphrase-MiniLM-L3-v2 at cosine >= 0.74. Overall, the repository suggests that threshold choice matters substantially, but especially for raw DistilBERT embedding baselines; SentenceTransformer families are still threshold-dependent, yet they show more stable and balanced behavior at their selected cutoffs. A key limitation is that the repository stores only a few discrete thresholded runs rather than full threshold sweeps, ROC curves, or PR curves, so the evidence supports comparative sensitivity claims but not a precise estimate of each model's optimal threshold or full calibration profile. The table should therefore be read as discrete operating-point evidence, not as a complete threshold-response curve.\"}"
}
```

**Metrics Summary:**
```json
{
  "tokens": {
    "input": 321469,
    "output": 10414,
    "reasoning": 8360,
    "total": 331883,
    "system_estimate": 1827,
    "conversation": 285068
  },
  "code": {
    "executions": 0,
    "failed_executions": 0,
    "total_lines": 0
  },
  "timing": {
    "api_latency_s": 180.181,
    "exec_latency_s": 0.557,
    "wall_time_s": 180.739
  },
  "api_calls": 20,
  "cost": null
}
```
