import pytest
from indexa.grounding import decide
def test_grounding_rejects_non_finite_threshold():
    with pytest.raises(ValueError): decide([], float("nan"))
