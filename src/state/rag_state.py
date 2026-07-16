"""State schema shared by the RAG workflow nodes."""

from dataclasses import dataclass, field

from langchain_core.documents import Document


@dataclass
class RAGState:
    """Data passed between the retrieval and response nodes."""

    question: str
    retrieved_docs: list[Document] = field(default_factory=list)
    answer: str | None = None
