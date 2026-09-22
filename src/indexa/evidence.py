"""Evidence ranking and grounding primitives."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Evidence:
    source_id: str
    text: str
    score: float
    citation: str

def select_grounded(items: list[Evidence], threshold: float = 0.0) -> list[Evidence]:
    if not 0.0 <= threshold <= 1.0:
        raise ValueError("threshold must be between 0 and 1")
    return sorted((x for x in items if x.score >= threshold), key=lambda x: (-x.score, x.source_id))
