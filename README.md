## Technical Writing Assistant Using CrewAI

A minimal CrewAI project with two agents:
- Research Analyst: analyzes latest AI/data science trends
- Technical Writing Expert: writes an engaging article based on the research

This project is configured to run with a local LLM via Ollama ( tested with `mistral:latest and gemma3:12b`).

### Setup
```bash
# 1) Create and activate a virtual environment (recommended)
virtualenv ResearchAgentCrewAI
source ResearchAgentCrewAI/bin/activate

# 2) Install dependencies
pip install -r requirements.txt
```

### Configure a local LLM (Ollama)
Start Ollama and pull a model:
```bash
# Start Ollama service (separate terminal is fine)
ollama serve

# Pull a model (choose one)
ollama pull mistral:latest
# or
ollama pull gemma3:12b
```

By default, `main.py` uses `langchain_ollama.OllamaLLM` with:
```python
llm = OllamaLLM(
    model="ollama/mistral:latest",
)
```
Change `model` to any pulled Ollama model (e.g., `"gemma3:12b"`).

### Run
```bash
python main.py
```
#### You can also download and run the docker image using the commands below
```bash
docker pull tayyabwahab/crewai-research-agents
docker run tayyabwahab/crewai-research-agents
```
