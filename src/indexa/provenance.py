from dataclasses import dataclass
from hashlib import sha256

@dataclass(frozen=True)
class Provenance:
    source_id: str
    fingerprint: str
    rank: int

def build_provenance(source_id: str, text: str, rank: int) -> Provenance:
    if not source_id or rank < 1:
        raise ValueError("source_id and positive rank are required")
    digest = sha256(text.encode("utf-8")).hexdigest()
    return Provenance(source_id, digest, rank)
