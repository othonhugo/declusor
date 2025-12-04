import pytest


@pytest.fixture
def mock_config(monkeypatch: pytest.MonkeyPatch) -> None:
    """Mock config constants."""


def test_read_stripped_line_async() -> None:
    """Test asynchronous reading of stripped line."""
