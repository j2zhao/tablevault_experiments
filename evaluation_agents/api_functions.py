import os

from tablevault.tablevault import Vault
from openai import OpenAI

def _get_embeddings(text):
    client = OpenAI()
    return client.embeddings.create(
            input=text,
            model="text-embedding-3-large"
        ).data[0].embedding

def initialization(vault_name, new_arango_db=False): # okay
    from tablevault import tablevault
    from openai import OpenAI

    vault = tablevault.Vault(user_id="jinjin",
                                process_name="experiment_1a",
                                arango_url="http://localhost:8629",
                                arango_db=vault_name,
                                arango_username="tablevault_user",
                                arango_password="tablevault_password",
                                new_arango_db=new_arango_db,
                                arango_root_username="root",
                                arango_root_password="passwd",
                                description_embedding_size=3072,
                            )

    
    openai_key_file = "/Users/jinjinzhao/Documents/work_projects/my_keys/my_keys/openai_jinjin.key"
    with open(openai_key_file, 'r') as f:
        openai_key = f.read()
    os.environ["OPENAI_API_KEY"] = openai_key
    return vault

def get_code(vault, name): # DONE
    ltype = vault.query_item_type(name)
    if ltype != "process_list":
        raise ValueError("Name given isn't a registered code process")
    results = vault.query_item_content(name)
    code = []
    for result in results:
        code.append(result["text"])
    return code

def get_item(vault, item_name, start_position = None, end_position = None): # DONE
    ltype = vault.query_item_type(item_name)
    if ltype is None or ltype == "process_list":
        raise ValueError("Name given isn't a registered item list")
    return vault.query_item_content(item_name, start_position = start_position, end_position = end_position)

def get_code_names(vault): # DONE
    return vault.query_item_names(item_type = "process_list")

def get_item_names(vault, item_type): # DONE
    if item_type == "process_list":
        raise ValueError("Name given isn't a valid item type.")
    return vault.query_item_names(item_type)

def code_search(vault, code): # DONE
    results = vault.query_process_list(code_text = code)
    names = set()
    for result in results:
        names.add(result[0])
    return list(names)

def embedding_search(vault, embedding):
    results = vault.query_embedding_list(embedding = embedding)
    names = []
    for result in results:
        names.append([result[0], result[2]])
    return names

def record_search(vault, record_text):
    results = vault.query_record_list(record_text = record_text)
    names = []
    for result in results:
        names.append(result[0])
    return names

def document_search(vault, document_text):
    results =  vault.query_document_list(document_text = document_text)
    names = []
    for result in results:
        names.append([result[0], result[2]])
    return names

def description_search(vault, description_text):
    descriptions = vault.query_description(description_text)
    results = []
    for dname, dtext, list_name, list_type in descriptions:
        if "BASE" in dname and list_type != "process_list":
            results.append([dname, dtext, list_name, list_type])
    return results

def description_embedding_search(vault, description_text):
    description_embedding = _get_embeddings(description_text)
    descriptions = vault.query_description_embedding(description_embedding)
    results = []
    for dname, dtext, list_name, list_type in descriptions:
        if "BASE" in dname and list_type != "process_list":
            results.append([dname, dtext, list_name, list_type])
    return results

def properties_search(vault, description_text):
    description_embedding = _get_embeddings(description_text)
    descriptions = vault.query_description_embedding(description_embedding)
    results = []
    for dname, dtext, list_name, list_type in descriptions:
        if "BASE" not in dname and list_type != "process_list":
            results.append([dname, dtext, list_name, list_type])
    return results

def get_item_code_name(vault, name):
    results = vault.query_item_creation_process(name)
    names = set()
    for result in results:
        names.add(result["process_id"].split("/")[-1])
    return list(names)

def get_item_parent_names(vault, name, start_position= None, end_position=None): # update if we change implementation later
    if start_position is None:
        results = vault.query_item_parent(name)
        names = set()
        for result in results:
            names.add(result[3])
        return list(names)
    else:
        return vault.query_item_parent(name, start_position = start_position, end_position = end_position)

def get_item_children_names(vault, name, start_position = None, end_position = None):
    if start_position is None:
        results = vault.query_item_child(name)
        names = set()
        for result in results:
            names.add(result[3])
        return list(names)
    else:
        return vault.query_item_child(name, start_position = start_position, end_position = end_position)

def get_item_description(vault, name):
    ltype = vault.query_item_type(name)
    if ltype is None or ltype == "process_list":
        raise ValueError("Name given isn't a registered item list")

    results = vault.query_item_description(name)
    for result in results:
        if "BASE" in result[0]:
            return result[1]
    return None

def get_item_properties(vault, name):
    ltype = vault.query_item_type(name)
    if ltype is None or ltype == "process_list":
        raise ValueError("Name given isn't a registered item list")
    results = vault.query_item_description(name)
    descriptions = {}
    for result in results:
        if "BASE" not in result[0]:
            descriptions[result[0]] = result[1]
    return descriptions

def code_description_search(vault, description_text):
    descriptions = vault.query_description(description_text)
    results = []
    for dname, dtext, list_name, list_type in descriptions:
        if "BASE" in dname and list_type == "process_list":
            results.append([dname, dtext, list_name, list_type])
    return results

def code_description_embedding_search(vault, description_text): # add openai embedding
    description_embedding = _get_embeddings(description_text)
    descriptions = vault.query_description_embedding(description_embedding)
    results = []
    for dname, dtext, list_name, list_type in descriptions:
        if "BASE" in dname and list_type == "process_list":
            results.append([dname, dtext, list_name, list_type])
    return results

def code_properties_search(vault, description_text):  # add openai embedding
    description_embedding = _get_embeddings(description_text)
    descriptions = vault.query_description_embedding(description_embedding)
    results = []
    for dname, dtext, list_name, list_type in descriptions:
        if "BASE" not in dname and list_type == "process_list":
            results.append([dname, dtext, list_name, list_type])
    return results

def get_code_description(vault, name):
    ltype = vault.query_item_type(name)
    if ltype is None or ltype != "process_list":
        raise ValueError("Name given isn't a registered code process")
    results = vault.query_item_description(name)
    for result in results:
        if "BASE" in result[0]:
            return result[1]
    return None

def get_code_properties(vault, name):
    ltype = vault.query_item_type(name)
    if ltype is None or ltype != "process_list":
        raise ValueError("Name given isn't a registered code process")
    results = vault.query_item_description(name)
    descriptions = {}
    for result in results:
        if "BASE" not in result[0]:
            descriptions[result[0]] = result[1]
    return descriptions

FUNCTION_DESCRIPTIONS = {
    "get_item": (
        "get_item(vault, item_name, start_position=None, end_position=None)\n"
        "Retrieve stored data from an item list by name.\n"
        "Always returns a List sorted by position:\n"
        "- Without start_position/end_position: returns all entries in the list.\n"
        "- With start_position and end_position: returns entries whose position overlaps "
        "the half-open range [start_position, end_position).\n"
        "Element type depends on the list type:\n"
        "  document_list  → str (the text of the chunk)\n"
        "  embedding_list → List[float] (the vector)\n"
        "  record_list    → dict {column_name: value} with keys matching the list's schema\n"
        "  file_list      → str (file location path)\n"
        "Example (all): get_item(vault, 'sst2_documents') → ['text 0', 'text 1', ...]\n"
        "Example (range): get_item(vault, 'sst2_documents', 4, 7) → ['text 4', 'text 5', 'text 6']"
    ),
    "get_item_names": (
        "get_item_names(vault, item_type)\n"
        "Return a sorted List[str] of all item list names of a given type.\n"
        "item_type must be one of: 'embedding_list', 'document_list', 'record_list', 'file_list'.\n"
        "Example: get_item_names(vault, 'record_list') → ['clf_outputs', 'eval_scores', ...]"
    ),
    "get_code": (
        "get_code(vault, name)\n"
        "Return the source-code blocks stored under the given code name.\n"
        "Returns List[str], one code string per execution run recorded under that name.\n"
        "Example: blocks = get_code(vault, 'embed_sentences'); blocks[0] contains the "
        "first recorded code block."
    ),
    "get_code_names": (
        "get_code_names(vault)\n"
        "Return a sorted List[str] of all registered names of executed code processes in the vault.\n"
        "Example: ['build_embeddings', 'classify_articles', 'score_predictions']"
    ),
    "code_search": (
        "code_search(vault, code)\n"
        "Full-text search over registered code by source-code content.\n"
        "Returns List[str] of unique code process names whose source matches the query string.\n"
        "Example: code_search(vault, 'cosine_similarity') → ['build_embeddings', 'rank_docs']"
    ),
    "embedding_search": (
        "embedding_search(vault, embedding)\n"
        "Nearest-neighbour search over embedding_list items using a pre-computed vector.\n"
        "embedding must be a List[float] matching the vault's configured vector dimensionality. "
        "To discover the dimensionality, fetch any entry from a known embedding list: "
        "ndim = len(get_item(vault, emb_list_name, 0, 1)[0]).\n"
        "Returns List[[item_name: str, start_position: int]] ranked by cosine similarity.\n"
        "start_position is the index of the matching entry within that list.\n"
        "Example: results = embedding_search(vault, my_vec); "
        "item_name, pos = results[0][0], results[0][1]; "
        "entry = get_item(vault, item_name, pos, pos+1)[0]"
    ),
    "record_search": (
        "record_search(vault, record_text)\n"
        "Full-text search over record_list items by their field values.\n"
        "Returns List[str] of item list names (not individual row identifiers) "
        "whose records contain text matching the query.\n"
        "Example: record_search(vault, 'World') → ['ag_news_clf_outputs', 'topic_records']"
    ),
    "document_search": (
        "document_search(vault, document_text)\n"
        "Full-text search over document_list items by text content.\n"
        "Returns List[[item_name: str, start_position: int]] for each matching document chunk.\n"
        "start_position is the index of the matching chunk within that list.\n"
        "Example: results = document_search(vault, 'neural network'); "
        "name, pos = results[0][0], results[0][1]; "
        "chunk = get_item(vault, name, pos, pos+1)[0]"
    ),
    "description_search": (
        "description_search(vault, description_text)\n"
        "Full-text keyword search over the primary (BASE) descriptions of data item lists "
        "(document_list, embedding_list, record_list, file_list).\n"
        "Each item list may have a long free-text description summarising its contents, "
        "schema, provenance, and intended use. For example: 'This list stores sentence-level "
        "embeddings for the imdb_train split produced by all-mpnet-base-v2. Each embedding is "
        "a 768-dimensional float vector for a movie review sentence. Embeddings are linked to "
        "source documents in imdb_documents and are used for nearest-neighbour retrieval and "
        "few-shot sentiment classification.'\n"
        "Returns List[[label: str, text: str, item_name: str, item_type: str]].\n"
        "  label     — 'BASE' (primary description identifier)\n"
        "  text      — the full description text\n"
        "  item_name — name of the matching item list\n"
        "  item_type — one of 'embedding_list', 'document_list', 'record_list', 'file_list'\n"
        "Example: results = description_search(vault, 'sentiment'); item_name = results[0][2]"
    ),
    "description_embedding_search": (
        "description_embedding_search(vault, description_text)\n"
        "Semantic similarity search over the primary (BASE) descriptions of data item lists. "
        "Accepts a plain-text query; internally converts it to an OpenAI embedding and searches "
        "by cosine similarity.\n"
        "Each item list may have a long free-text description summarising its contents, schema, "
        "provenance, and intended use — e.g. 'This list stores sentence-level embeddings for "
        "the imdb_train split produced by all-mpnet-base-v2. Each embedding is a 768-dimensional "
        "float vector for a movie review sentence used for nearest-neighbour retrieval.'\n"
        "Returns List[[label: str, text: str, item_name: str, item_type: str]] ranked by similarity.\n"
        "  label     — 'BASE' (primary description identifier)\n"
        "  text      — the full description text\n"
        "  item_name — name of the matching item list (index [2])\n"
        "  item_type — one of 'embedding_list', 'document_list', 'record_list', 'file_list'\n"
        "Example: results = description_embedding_search(vault, 'text vectors for reviews'); "
        "item_name = results[0][2]"
    ),
    "properties_search": (
        "properties_search(vault, description_text)\n"
        "Semantic similarity search over the property names (labels) of data item lists. "
        "Properties are short key-value metadata attached to an item list, separate from its "
        "primary description. The property name (label) describes what the value represents — "
        "for example: label='ai_model', value='gpt-4o-mini'; label='dataset', value='ag_news'; "
        "label='experiment', value='1b'. This function searches semantically over the property "
        "names (labels), not their values.\n"
        "Accepts a plain-text query; internally converts it to an OpenAI embedding.\n"
        "Returns List[[label: str, text: str, item_name: str, item_type: str]] ranked by "
        "similarity of the property name to the query.\n"
        "  label     — the property name (e.g. 'ai_model', 'split', 'experiment')\n"
        "  text      — the property value (e.g. 'gpt-4o-mini', 'train', '1b')\n"
        "  item_name — name of the item list that has this property\n"
        "  item_type — one of 'embedding_list', 'document_list', 'record_list', 'file_list'\n"
        "Example: results = properties_search(vault, 'language model'); "
        "prop_name, prop_value, item_name = results[0][0], results[0][1], results[0][2]"
    ),
    "get_item_description": (
        "get_item_description(vault, name)\n"
        "Return the primary (BASE) description text for the item list identified by name.\n"
        "Descriptions are long free-text paragraphs summarising contents, schema, provenance, "
        "and intended use — e.g. 'This list stores sentence-level embeddings for the imdb_train "
        "split produced by all-mpnet-base-v2. Each embedding is a 768-dimensional float vector "
        "for a movie review sentence used for nearest-neighbour retrieval.'\n"
        "Returns str if a BASE description exists, or None if none is set.\n"
        "Example: get_item_description(vault, 'imdb_embeddings') → 'This list stores ...'"
    ),
    "get_item_properties": (
        "get_item_properties(vault, name)\n"
        "Return all named properties attached to the item list as a dict.\n"
        "Properties are short key-value metadata where the key is a property name such as "
        "'ai_model', 'dataset', 'split', or 'experiment', and the value is a string — "
        "e.g. {'ai_model': 'gpt-4o-mini', 'dataset': 'ag_news', 'split': 'train'}.\n"
        "Returns Dict[str, str] mapping property label → property value.\n"
        "Example: get_item_properties(vault, 'clf_outputs') "
        "→ {'ai_model': 'gpt-4o-mini', 'dataset': 'ag_news', 'experiment': '1b'}"
    ),
    "get_item_code_name": (
        "get_item_code_name(vault, name)\n"
        "Return the list of code names whose execution created the entries in the item list.\n"
        "Returns List[str] of code names.\n"
        "Example: get_item_code_name(vault, 'imdb_embeddings') → ['build_embeddings']"
    ),
    "get_item_parent_names": (
        "get_item_parent_names(vault, name, start_position=None, end_position=None)\n"
        "Return the upstream dependencies that entries in this list were derived from. "
        "Parents may be either data item list names or code names.\n"
        "- Without range: returns List[str] of parent names (mix of item list and code names).\n"
        "- With start_position and end_position: returns List of 6-element dependency records "
        "for entries in [start_position, end_position); element [3] of each record is the "
        "parent name (str).\n"
        "Example (names only): get_item_parent_names(vault, 'imdb_embeddings') "
        "→ ['imdb_documents', 'build_embeddings']\n"
        "Example (range): records = get_item_parent_names(vault, 'imdb_embeddings', 0, 10); "
        "parent_name = records[0][3]"
    ),
    "get_item_children_names": (
        "get_item_children_names(vault, name, start_position=None, end_position=None)\n"
        "Return the downstream dependents derived from entries in this list. "
        "Children may be either data item list names or code names.\n"
        "- Without range: returns List[str] of child names (mix of item list and code names).\n"
        "- With start_position and end_position: returns List of 6-element dependency records "
        "for entries in [start_position, end_position); element [3] of each record is the "
        "child name (str).\n"
        "Example (names only): get_item_children_names(vault, 'imdb_documents') "
        "→ ['imdb_embeddings', 'imdb_summaries']\n"
        "Example (range): records = get_item_children_names(vault, 'imdb_documents', 0, 5); "
        "child_name = records[0][3]"
    ),
    "code_description_search": (
        "code_description_search(vault, description_text)\n"
        "Full-text keyword search over the primary (BASE) descriptions of registered code.\n"
        "Each code entry may have a long free-text description summarising what the code does, "
        "its inputs/outputs, and its role in the pipeline. For example: 'This code classifies "
        "news articles from sst2_documents using gpt-4o-mini via zero-shot prompting. It reads "
        "each document, queries the model for a sentiment label (positive/negative), and writes "
        "a record containing the predicted_label and confidence_score to clf_outputs. Intended "
        "for baseline evaluation and error analysis.'\n"
        "Returns List[[label: str, text: str, code_name: str, _type: str]].\n"
        "  label     — 'BASE' (primary description identifier)\n"
        "  text      — the full description text\n"
        "  code_name — name of the matching code entry (index [2])\n"
        "Example: results = code_description_search(vault, 'zero-shot classification'); "
        "code_name = results[0][2]"
    ),
    "code_description_embedding_search": (
        "code_description_embedding_search(vault, description_text)\n"
        "Semantic similarity search over the primary (BASE) descriptions of registered code. "
        "Accepts a plain-text query; internally converts it to an OpenAI embedding and searches "
        "by cosine similarity.\n"
        "Each code entry may have a long free-text description summarising what the code does, "
        "its inputs/outputs, and its role in the pipeline — e.g. 'This code classifies news "
        "articles from sst2_documents using gpt-4o-mini via zero-shot prompting. It reads each "
        "document, queries the model for a sentiment label, and writes a record containing the "
        "predicted_label and confidence_score to clf_outputs.'\n"
        "Returns List[[label: str, text: str, code_name: str, _type: str]] ranked by similarity.\n"
        "  label     — 'BASE' (primary description identifier)\n"
        "  text      — the full description text\n"
        "  code_name — name of the matching code entry (index [2])\n"
        "Example: results = code_description_embedding_search(vault, 'LLM-based labelling'); "
        "code_name = results[0][2]"
    ),
    "code_properties_search": (
        "code_properties_search(vault, description_text)\n"
        "Semantic similarity search over the property names (labels) of registered code. "
        "Code entries can have short key-value properties describing metadata about the "
        "execution — for example: label='ai_model', value='gpt-4o-mini'; "
        "label='framework', value='openai'; label='experiment', value='1a'. "
        "This function searches semantically over the property names (labels), not their values.\n"
        "Accepts a plain-text query; internally converts it to an OpenAI embedding.\n"
        "Returns List[[label: str, text: str, code_name: str, _type: str]] ranked by "
        "similarity of the property name to the query.\n"
        "  label     — the property name (e.g. 'ai_model', 'framework')\n"
        "  text      — the property value (e.g. 'gpt-4o-mini', 'openai')\n"
        "  code_name — name of the code entry that has this property (index [2])\n"
        "Example: results = code_properties_search(vault, 'language model'); "
        "prop_name, prop_value, code_name = results[0][0], results[0][1], results[0][2]"
    ),
    "get_code_description": (
        "get_code_description(vault, name)\n"
        "Return the primary (BASE) description text for the code entry identified by name.\n"
        "Descriptions are long free-text paragraphs summarising what the code does, its "
        "inputs/outputs, and its role in the pipeline — e.g. 'This code classifies news "
        "articles from sst2_documents using gpt-4o-mini via zero-shot prompting. It reads each "
        "document, queries the model for a sentiment label, and writes a record containing the "
        "predicted_label and confidence_score to clf_outputs.'\n"
        "Returns str if a BASE description exists, or None if none is set.\n"
        "Example: get_code_description(vault, 'classify_articles') → 'This code classifies ...'"
    ),
    "get_code_properties": (
        "get_code_properties(vault, name)\n"
        "Return all named properties attached to the code entry as a dict.\n"
        "Properties are short key-value metadata where the key is a property name such as "
        "'ai_model', 'framework', or 'experiment', and the value is a string — "
        "e.g. {'ai_model': 'gpt-4o-mini', 'framework': 'openai', 'experiment': '1a'}.\n"
        "Returns Dict[str, str] mapping property label → property value.\n"
        "Example: get_code_properties(vault, 'classify_articles') "
        "→ {'ai_model': 'gpt-4o-mini', 'framework': 'openai', 'experiment': '1a'}"
    ),
}


FUNCTION_EXPERIMENTS = {
    "items_only": ["get_item", "get_item_names"],
    "dataset_search": ["get_item", "get_item_names", "embedding_search", "record_search", "document_search"],
    "dataset_description": ["get_item", "get_item_description", "description_search"],
    "dataset_description_embedding": ["get_item", "get_item_description", "description_embedding_search"],
    "dataset_properties": ["get_item", "get_item_properties", "properties_search"],
    "items_and_code": ["get_item", "get_code", "get_item_names", "get_code_names"],
    "items_and_lineage": ["get_item", "get_code", "get_item_names", "get_code_names", "get_item_children_names", "get_item_parent_names", "get_item_code_name"],
    "code_search": ["get_item", "get_code", "code_search"],
    "code_description": ["get_item", "get_code", "code_description_search"],
    "code_description_embedding": ["get_item", "get_code", "code_description_embedding_search"],
    "code_properties": ["get_item", "get_code", "code_properties_search"],
    "all_functions": [
            "get_code",
            "get_item",
            "get_code_names",
            "get_item_names",
            "code_search",
            "embedding_search",
            "record_search",
            "document_search",
            "description_search",
            "description_embedding_search",
            "properties_search",
            "get_item_code_name",
            "get_item_parent_names",
            "get_item_children_names",
            "get_item_description",
            "get_item_properties",
            "code_description_search",
            "code_description_embedding_search",
            "code_properties_search",
            "get_code_description",
            "get_code_properties",
        ]
}
