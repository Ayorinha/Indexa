from dataclasses import dataclass
import re
@dataclass(frozen=True)
class Chunk: text:str; source:str; index:int
class Retriever:
    def __init__(self,chunks): self.chunks=chunks
    def search(self,query,k=5):
        if k<1: raise ValueError("k must be positive")
        terms=set(re.findall(r"\w+",query.lower()))
        ranked=[]
        for c in self.chunks: ranked.append((sum(t in c.text.lower() for t in terms),c))
        return [c for score,c in sorted(ranked,key=lambda x:(x[0],-x[1].index),reverse=True)[:k] if score>0]