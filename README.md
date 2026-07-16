# Agentic RAG Document Search

A Streamlit application that answers questions from a small document corpus using retrieval-augmented generation (RAG). It loads the configured web sources, splits them into chunks, indexes them in FAISS with OpenAI embeddings, and uses a LangGraph-powered agent to answer questions with either retrieved context or Wikipedia.

## Features

- Loads and chunks web pages from the configured source list.
- Creates a local FAISS vector index using OpenAI embeddings.
- Uses a LangGraph workflow to retrieve relevant passages and generate an answer.
- Provides two agent tools: a document retriever and Wikipedia search.
- Includes a Streamlit interface with recent-search history and retrieved-source previews.

## Architecture

```text
Configured URLs / local documents
            |
     DocumentProcessor
            |
        FAISS index
            |
      LangGraph workflow
  retrieve -> agent response
            |
        Streamlit UI
```

## Prerequisites

- Python 3.13 or newer
- An OpenAI API key
- `uv` (recommended) or `pip`

## Setup

Clone the repository and create a local environment:

```bash
git clone https://github.com/TarunG1122/RAG-End-to-end-project.git
cd RAG-End-to-end-project
uv sync
```

Alternatively, use `pip`:

```bash
python -m venv .venv
.venv\\Scripts\\activate  # Windows PowerShell
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
```

Do not commit `.env`; it is already ignored by Git.

## Run the app

```bash
streamlit run streamlit_app.py
```

On first startup, the app downloads the sources in `Config.DEFAULT_URLS`, creates embeddings, and builds the in-memory FAISS index. This requires an active internet connection and incurs OpenAI API usage.

## Configuration

Update `src/config/config.py` to customize:

- `LLM_MODEL` — the chat model used to generate answers.
- `CHUNK_SIZE` and `CHUNK_OVERLAP` — document splitting behavior.
- `DEFAULT_URLS` — web pages loaded into the knowledge base.

## Project structure

```text
streamlit_app.py                 # Streamlit user interface
src/config/config.py             # Environment, model, and source settings
src/document_ingestion/          # Loaders and document chunking
src/vectorstore/                 # FAISS embeddings and retrieval
src/graph_builder/               # LangGraph workflow and agent tools
src/state/                       # Shared RAG state definition
```

## Notes

- The FAISS index is held in memory and is rebuilt when the Streamlit resource cache is cleared or the app restarts.
- Place private PDFs or other local source files in `data/`; the directory is ignored by Git to prevent uploading private documents.
- The Wikipedia tool is intended for general context. For questions about your loaded sources, the agent is prompted to prefer the document retriever.
