"""Tests for declusor.core.console module (Console class).

This module tests console I/O operations including:
- Console: Main console handler with readline integration
- read_line/read_stripped_line: Async input reading
- write_message/write_binary_data/write_error_message: Output methods
- setup_completer: Readline tab completion
- enable_history: History file persistence
"""

from pathlib import Path
from unittest.mock import MagicMock

import pytest

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def console():
    """Create a fresh Console instance for testing."""


@pytest.fixture
def mock_readline(monkeypatch: pytest.MonkeyPatch) -> MagicMock:
    """Mock readline module for completer tests."""


@pytest.fixture
def temp_history_file(tmp_path: Path) -> Path:
    """Create a temporary history file path."""


# =============================================================================
# Tests: Console initialization
# =============================================================================


def test_console_init_history_file_none() -> None:
    """
    Given: Console is instantiated
    When: __init__ is called
    Then: _history_file is None by default
    """


# =============================================================================
# Tests: Console.read_line
# =============================================================================


@pytest.mark.asyncio
async def test_console_read_line_returns_input() -> None:
    """
    Given: User types "hello" at prompt
    When: read_line() is called
    Then: Returns the string "hello"
    """


@pytest.mark.asyncio
async def test_console_read_line_with_prompt() -> None:
    """
    Given: read_line(prompt=">> ") is called
    When: Input is awaited
    Then: Prompt ">> " is displayed before input
    """


@pytest.mark.asyncio
async def test_console_read_line_uses_thread_executor() -> None:
    """
    Given: read_line() is called
    When: Awaiting input
    Then: Uses asyncio.to_thread to avoid blocking event loop
    """


# =============================================================================
# Tests: Console.read_stripped_line
# =============================================================================


@pytest.mark.asyncio
async def test_console_read_stripped_line_strips_whitespace() -> None:
    """
    Given: User enters "  hello  " (with spaces)
    When: read_stripped_line() is called
    Then: Returns "hello" (stripped)
    """


@pytest.mark.asyncio
async def test_console_read_stripped_line_handles_empty_input() -> None:
    """
    Given: User enters only whitespace or empty string
    When: read_stripped_line() is called
    Then: Returns empty string ""
    """


# =============================================================================
# Tests: Console.write_message
# =============================================================================


def test_console_write_message_outputs_to_stdout(capsys) -> None:
    """
    Given: write_message("test") is called
    When: Output is captured
    Then: "test\\n" appears on stdout
    """


def test_console_write_message_appends_newline(capsys) -> None:
    """
    Given: write_message("no newline") is called
    When: Output is captured
    Then: Newline is automatically appended
    """


def test_console_write_message_flushes_stdout() -> None:
    """
    Given: write_message is called
    When: Output is written
    Then: stdout is flushed immediately
    """


# =============================================================================
# Tests: Console.write_binary_data
# =============================================================================


def test_console_write_binary_data_outputs_bytes(capsys) -> None:
    """
    Given: write_binary_data(b"hello") is called
    When: Output is captured
    Then: Raw bytes appear on stdout.buffer
    """


def test_console_write_binary_data_no_newline() -> None:
    """
    Given: write_binary_data(b"data") is called
    When: Output is written
    Then: No automatic newline is appended
    """


def test_console_write_binary_data_flushes_buffer() -> None:
    """
    Given: write_binary_data is called
    When: Output is written
    Then: stdout.buffer is flushed immediately
    """


# =============================================================================
# Tests: Console.write_error_message
# =============================================================================


def test_console_write_error_message_outputs_to_stderr(capsys) -> None:
    """
    Given: write_error_message("fail") is called
    When: Output is captured
    Then: "error: fail\\n" appears on stderr
    """


def test_console_write_error_message_accepts_exception() -> None:
    """
    Given: write_error_message(ValueError("oops")) is called
    When: Output is written
    Then: Exception message is included in output
    """


def test_console_write_error_message_prefix() -> None:
    """
    Given: write_error_message("msg") is called
    When: Output is captured
    Then: Message is prefixed with "error: "
    """


# =============================================================================
# Tests: Console.write_warning_message
# =============================================================================


def test_console_write_warning_message_outputs_to_stderr(capsys) -> None:
    """
    Given: write_warning_message("warn") is called
    When: Output is captured
    Then: "warning: warn\\n" appears on stderr
    """


def test_console_write_warning_message_accepts_exception() -> None:
    """
    Given: write_warning_message(RuntimeError("caution")) is called
    When: Output is written
    Then: Exception message is included in output
    """


# =============================================================================
# Tests: Console.setup_completer
# =============================================================================


def test_console_setup_completer_sets_delims(mock_readline: MagicMock) -> None:
    """
    Given: setup_completer is called with routes
    When: Readline is configured
    Then: set_completer_delims is called with " \\t\\n;"
    """


def test_console_setup_completer_registers_function(mock_readline: MagicMock) -> None:
    """
    Given: setup_completer is called
    When: Readline is configured
    Then: set_completer is called with completer function
    """


def test_console_setup_completer_binds_tab(mock_readline: MagicMock) -> None:
    """
    Given: setup_completer is called
    When: Readline is configured
    Then: parse_and_bind("tab: complete") is called
    """


def test_console_setup_completer_command_completion() -> None:
    """
    Given: Completer is set up with routes ["load", "shell", "exit"]
    When: User types "lo" and presses TAB
    Then: "load" is suggested as completion
    """


def test_console_setup_completer_file_completion() -> None:
    """
    Given: User has typed "load " (command with space)
    When: User types partial filename and presses TAB
    Then: File paths are suggested for completion
    """


def test_console_setup_completer_handles_no_readline() -> None:
    """
    Given: readline module is not available (None)
    When: setup_completer is called
    Then: Returns early without error
    """


# =============================================================================
# Tests: Console.enable_history
# =============================================================================


def test_console_enable_history_sets_file_path(temp_history_file: Path) -> None:
    """
    Given: enable_history(history_file) is called
    When: History is configured
    Then: _history_file is set to the path
    """


def test_console_enable_history_reads_existing_file(temp_history_file: Path) -> None:
    """
    Given: History file exists with prior commands
    When: enable_history is called
    Then: read_history_file is called to load history
    """


def test_console_enable_history_handles_missing_file(temp_history_file: Path) -> None:
    """
    Given: History file does not exist
    When: enable_history is called
    Then: No error raised (FileNotFoundError caught)
    """


def test_console_enable_history_registers_atexit(temp_history_file: Path) -> None:
    """
    Given: enable_history is called
    When: History is configured
    Then: atexit.register is called with _save_history
    """


def test_console_save_history_writes_file(temp_history_file: Path) -> None:
    """
    Given: History is enabled and commands were entered
    When: _save_history is called
    Then: write_history_file is called with history file path
    """
