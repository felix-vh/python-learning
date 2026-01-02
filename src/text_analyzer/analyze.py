from __future__ import annotations

from collections import Counter
from pathlib import Path
import re


WORD_RE = re.compile(r"[a-záéíóúñ]+", re.IGNORECASE)


def load_text(path: str) -> str:
    """Read a UTF-8 text file and return its contents."""
    return Path(path).read_text(encoding="utf-8")


def tokenize(text: str) -> list[str]:
    """
    Convert raw text into a list of normalized tokens (words).

    - lowercase
    - removes punctuation by extracting only letters (incl. accents)
    """
    return [m.group(0).lower() for m in WORD_RE.finditer(text)]


def build_report(tokens: list[str], top_n: int = 10) -> dict:
    """Create a simple stats report from tokens."""
    counter = Counter(tokens)
    return {
        "total_words": len(tokens),
        "unique_words": len(counter),
        "top_words": counter.most_common(top_n),  # list of (word, count)
    }


def analyze_file(input_path: str, top_n: int = 10) -> dict:
    """Convenience function: read -> tokenize -> report."""
    text = load_text(input_path)
    tokens = tokenize(text)
    return build_report(tokens, top_n=top_n)