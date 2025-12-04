import pytest


@pytest.fixture
def mock_config(monkeypatch: pytest.MonkeyPatch) -> None:
    """Mock config constants."""


def test_prompt_cli_run_exit_request() -> None:
    """Test that PromptCLI.run exits on ExitRequest."""


def test_prompt_cli_run_keyboard_interrupt() -> None:
    """Test that PromptCLI.run exits on KeyboardInterrupt."""
