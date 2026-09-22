from __future__ import annotations
from dataclasses import dataclass
import re
@dataclass(frozen=True, slots=True)
class Chunk:
    text: str; source: str; index: int
    def __post_init__(self):
        if not self.text.strip() or not self.source.strip() or self.index < 0: raise ValueError("invalid chunk")
class Retriever:
    def __init__(self, chunks: list[Chunk]): self._chunks = tuple(chunks)
    def search(self, query: str, *, k: int = 5) -> list[Chunk]:
        if not query.strip() or k < 1: raise ValueError("query must be non-empty and k positive")
        terms = set(re.findall(r"\w+", query.casefold()))
        ranked = [(sum(term in c.text.casefold() for term in terms), -c.index, c) for c in self._chunks]
        ranked.sort(reverse=True, key=lambda x: (x[0], x[1]))
        return [c for score, _, c in ranked[:k] if score > 0]
