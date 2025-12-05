"""Tests for declusor.command.shell module (LaunchShell command).

This module tests the interactive shell command including:
- LaunchShell: Command to launch an interactive shell session
- Async task management for input/output handling
- Stop event coordination between tasks
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def mock_session() -> AsyncMock:
    """Create a mock ISession with read/write async methods."""


@pytest.fixture
def mock_console(monkeypatch: pytest.MonkeyPatch) -> MagicMock:
    """Mock core.console for controlling input/output during tests."""


@pytest.fixture
def launch_shell():
    """Create a LaunchShell instance for testing."""


# =============================================================================
# Tests: LaunchShell initialization
# =============================================================================


def test_launch_shell_init_creates_stop_event() -> None:
    """
    Given: LaunchShell is instantiated
    When: __init__ is called
    Then: _stop_event is created as asyncio.Event (initially not set)
    """


# =============================================================================
# Tests: LaunchShell.execute - Task management
# =============================================================================


@pytest.mark.asyncio
async def test_launch_shell_execute_creates_both_tasks(mock_session: AsyncMock) -> None:
    """
    Given: LaunchShell.execute is called
    When: Execution starts
    Then: Creates asyncio tasks for input and output handlers
    """


@pytest.mark.asyncio
async def test_launch_shell_execute_cancels_tasks_on_exit(mock_session: AsyncMock) -> None:
    """
    Given: LaunchShell.execute is running both tasks
    When: Execution ends (for any reason)
    Then: Both tasks are cancelled and awaited for cleanup
    """


@pytest.mark.asyncio
async def test_launch_shell_execute_sets_stop_event(mock_session: AsyncMock) -> None:
    """
    Given: LaunchShell.execute is running
    When: Execution ends
    Then: _stop_event.set() is called to signal other tasks
    """


# =============================================================================
# Tests: LaunchShell.execute - Exception handling
# =============================================================================


@pytest.mark.asyncio
async def test_launch_shell_execute_handles_keyboard_interrupt(mock_session: AsyncMock) -> None:
    """
    Given: LaunchShell.execute is running
    When: KeyboardInterrupt (Ctrl+C) is raised
    Then: Exception is caught, stop_event is set, graceful exit
    """


@pytest.mark.asyncio
async def test_launch_shell_execute_handles_cancelled_error(mock_session: AsyncMock) -> None:
    """
    Given: LaunchShell.execute is running
    When: asyncio.CancelledError is raised
    Then: Exception is caught, cleanup occurs gracefully
    """


# =============================================================================
# Tests: LaunchShell._handle_command_request
# =============================================================================


@pytest.mark.asyncio
async def test_handle_command_request_writes_to_session(mock_session: AsyncMock) -> None:
    """
    Given: User enters a non-empty command
    When: _handle_command_request processes input
    Then: Calls session.write() with encoded command bytes
    """


@pytest.mark.asyncio
async def test_handle_command_request_skips_empty_input(mock_session: AsyncMock) -> None:
    """
    Given: User enters empty/whitespace-only input
    When: _handle_command_request processes input
    Then: Does NOT call session.write()
    """


@pytest.mark.asyncio
async def test_handle_command_request_breaks_on_eof_error(mock_session: AsyncMock) -> None:
    """
    Given: console.read_stripped_line() raises EOFError
    When: _handle_command_request processes input
    Then: Loop breaks (graceful exit on Ctrl+D)
    """


# =============================================================================
# Tests: LaunchShell._handle_command_response
# =============================================================================


@pytest.mark.asyncio
async def test_handle_command_response_writes_to_console(mock_session: AsyncMock) -> None:
    """
    Given: session.read() yields data
    When: _handle_command_response receives data
    Then: Calls console.write_binary_data() with received bytes
    """


@pytest.mark.asyncio
async def test_handle_command_response_skips_empty_data(mock_session: AsyncMock) -> None:
    """
    Given: session.read() yields empty bytes b''
    When: _handle_command_response processes data
    Then: Does NOT call console.write_binary_data()
    """


@pytest.mark.asyncio
async def test_handle_command_response_respects_stop_event(mock_session: AsyncMock) -> None:
    """
    Given: _stop_event is set during iteration
    When: _handle_command_response checks condition
    Then: Breaks out of loops and exits
    """
