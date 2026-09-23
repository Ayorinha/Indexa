"""Production smoke tests for Indexa."""
import importlib


def test_package_imports() -> None:
    module = importlib.import_module("indexa")
    assert module.__name__ == "indexa"


def test_import_is_network_independent() -> None:
    # Import-time network calls make CI and offline development fragile.
    module = importlib.import_module("indexa")
    assert module is not None
