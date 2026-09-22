"""Grounding guardrails for retrieval-backed generation."""
from dataclasses import dataclass
import math
from .evidence import Evidence
@dataclass(frozen=True)
class GroundingDecision:
    allowed: bool
    evidence_count: int
    reason: str
def decide(evidence: list[Evidence], minimum_score: float = 0.5) -> GroundingDecision:
    if not math.isfinite(minimum_score) or not 0 <= minimum_score <= 1: raise ValueError("minimum_score must be a finite value between 0 and 1")
    valid = [item for item in evidence if math.isfinite(item.score) and 0 <= item.score <= 1 and item.score >= minimum_score and item.citation.strip()]
    if not valid: return GroundingDecision(False, 0, "insufficient_grounded_evidence")
    return GroundingDecision(True, len(valid), "grounded")