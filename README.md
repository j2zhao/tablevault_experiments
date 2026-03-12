# Install and Run Experiment 1

Note running notebooks out of order might result in errors. If there's anything wrong with the workflow, just re-running `experiment_1a.ipynb` will recreate the TableVault repository

## Install Dependencies

```
pip install tablevault

pip install pandas datasets openai tqdm 
```

## Setup Arango Docker Environment

From the repository root, start the ArangoDB container with:

```bash
docker compose -f tv_initialization/docker-compose.yml up -d
```

After startup, ArangoDB will be available at `http://localhost:8629`.

- Username: `root`
- Password: `passwd`

## Change OpenAI Account

In the three notebooks (`experiment_1*.ipynb`) and query agent file (`query_agent*.py`), change the relevant lines below so that `os.environ["OPENAI_API_KEY"]` is your openai key.

```
openai_key_file = "/Users/jinjinzhao/Documents/work_projects/my_keys/my_keys/openai_jinjin.key"
with open(openai_key_file, 'r') as f:
    openai_key = f.read()

os.environ["OPENAI_API_KEY"] = openai_key
```

## Run Notebooks

Run all the cells in (1) `experiment_1a.ipynb`, (2) `experiment_1b.ipynb`, and (3) `experiment_1a.ipynb` sequentially. 

This creates a TableVault repository, and stores data in it.

Again, you can view the backend database at: `http://localhost:8629`. 

## Run Query Agent

You can run `query_agent.py` to have an OpenAI model probe the TableVault repository to answer a data-driven question.