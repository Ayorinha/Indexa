from dataclasses import dataclass
from hashlib import sha256
@dataclass(frozen=True)
class Evidence: source_id:str; text:str; score:float
def fingerprint(e): return sha256(e.text.encode()).hexdigest()[:16]
def rank(q,items,limit=5):
 t=set(q.lower().split()); return sorted(items,key=lambda e:(len(t&set(e.text.lower().split())),e.score),reverse=True)[:limit]
