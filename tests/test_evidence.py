from indexa.evidence import Evidence, select_grounded

def test_select_grounded_is_deterministic():
    items=[Evidence("b","B",.8,"b"),Evidence("a","A",.8,"a"),Evidence("c","C",.2,"c")]
    assert [x.source_id for x in select_grounded(items,.5)] == ["a","b"]
