from dataclasses import dataclass
from hashlib import sha256

@dataclass(frozen=True)
class Evidence:
    source_id:str; text:str; score:float
    @property
    def fingerprint(self)->str: return sha256(self.text.encode()).hexdigest()[:16]

def rank(query:str, evidences:list[Evidence], limit:int=5)->list[Evidence]:
    terms=set(query.lower().split())
    return sorted(evidences,key=lambda e:(len(terms & set(e.text.lower().split())),e.score),reverse=True)[:limit]
