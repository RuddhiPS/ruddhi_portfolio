"""
digital_twin_embedder.py

Local custom model for Ruddhi's Digital Twin:
- Loads fine-tuned sentence-transformer
- Loads canonical question/answer index
- Provides answer_query(text: str) -> str
"""

import os
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Paths
BASE_DIR = os.path.dirname(__file__)
MODEL_DIR = os.path.join(BASE_DIR, "models", "digital_twin_embedder")
QA_INDEX_PATH = os.path.join(MODEL_DIR, "qa_index.npz")

# Globals (lazy-loaded)
_model = None
_questions = None
_answers = None
_question_embeddings = None


def _load_all():
    global _model, _questions, _answers, _question_embeddings

    if _model is None:
        if not os.path.isdir(MODEL_DIR):
            raise FileNotFoundError(f"MODEL_DIR not found: {MODEL_DIR}")
        if not os.path.exists(QA_INDEX_PATH):
            raise FileNotFoundError(f"qa_index.npz not found at: {QA_INDEX_PATH}")

        _model = SentenceTransformer(MODEL_DIR)
        data = np.load(QA_INDEX_PATH, allow_pickle=True)
        _questions = data["questions"].tolist()
        _answers = data["answers"].tolist()
        _question_embeddings = data["embeddings"]

    return _model, _questions, _answers, _question_embeddings


def answer_query(text: str, min_similarity: float = 0.3) -> str:
    """
    Given a user question, return the best-matching answer from the Q/A index.
    """
    model, questions, answers, question_embeddings = _load_all()

    text = text.strip()
    if not text:
        return "Could you please rephrase your question?"

    query_vec = model.encode([text], convert_to_numpy=True)
    sims = cosine_similarity(query_vec, question_embeddings)[0]

    best_idx = int(np.argmax(sims))
    best_sim = sims[best_idx]

    if best_sim < min_similarity:
        return "I am not sure how to answer that based on my current profile."

    return answers[best_idx]
