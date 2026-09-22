from indexa.core import Evidence,rank

def test_rank_and_fingerprint_are_deterministic():
    e=[Evidence("a","python rag provenance",.8),Evidence("b","database",.9)]
    r=rank("python provenance",e)
    assert r[0].source_id=="a" and r[0].fingerprint=="3f0f9b0b1a9b4f1d"
