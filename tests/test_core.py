from indexa.core import Chunk, Retriever

def test_retrieval():
    retriever = Retriever([Chunk("alpha beta", "a", 0)])
    assert retriever.search("alpha")[0].source == "a"
