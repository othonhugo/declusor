import pytest


@pytest.fixture
def mock_config(monkeypatch: pytest.MonkeyPatch) -> None:
    """Mock config constants."""


def test_call_exit_raises_exit_request() -> None:
    """Test that call_exit raises ExitRequest."""
