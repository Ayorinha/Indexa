from indexa.evidence import Evidence
from indexa.grounding import decide

def test_grounding_blocks_weak_evidence():
    assert not decide([Evidence("x","text",.2,"x")]).allowed
