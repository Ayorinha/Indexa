from indexa.core import Chunk, Retriever

def test_retrieval_is_ranked():
    r = Retriever([Chunk("alpha beta", "a", 0), Chunk("beta", "b", 1)])
    assert [c.source for c in r.search("alpha beta")] == ["a", "b"]

def test_invalid_query():
    try: Retriever([]).search("")
    except ValueError: pass
    else: raise AssertionError("empty query accepted")
