from indexa.provenance import build_provenance

def test_provenance_is_deterministic():
    a = build_provenance("doc-1", "hello", 1)
    b = build_provenance("doc-1", "hello", 1)
    assert a == b
    assert len(a.fingerprint) == 64
