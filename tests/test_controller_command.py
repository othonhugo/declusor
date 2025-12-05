"""Tests for declusor.controller.command module (call_command function).

This module tests:
- call_command: Execute single command on remote system
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def mock_session() -> AsyncMock:
    """Create a mock ISession with read/write methods."""


@pytest.fixture
def mock_router() -> MagicMock:
    """Create a mock IRouter."""


@pytest.fixture
def mock_console(monkeypatch: pytest.MonkeyPatch) -> MagicMock:
    """Mock core.console for output capture."""


# =============================================================================
# Tests: call_command - Argument parsing
# =============================================================================


@pytest.mark.asyncio
async def test_call_command_parses_command_argument(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_command with line="ls -la"
    When: Controller parses arguments
    Then: arguments["command"] is "ls -la"
    """


@pytest.mark.asyncio
async def test_call_command_parses_quoted_command(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_command with line='"echo hello world"'
    When: Controller parses arguments
    Then: arguments["command"] is "echo hello world"
    """


@pytest.mark.asyncio
async def test_call_command_missing_argument_raises(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_command with empty line ""
    When: Controller parses arguments
    Then: Raises ParserError (command is required)
    """


# =============================================================================
# Tests: call_command - Execution
# =============================================================================


@pytest.mark.asyncio
async def test_call_command_creates_execute_command(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_command with valid command
    When: Controller executes
    Then: ExecuteCommand is instantiated with the command
    """


@pytest.mark.asyncio
async def test_call_command_executes_on_session(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_command with command "whoami"
    When: Controller executes
    Then: session.write is called with encoded command
    """


# =============================================================================
# Tests: call_command - Response handling
# =============================================================================


@pytest.mark.asyncio
async def test_call_command_reads_response(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: Session returns response data
    When: call_command completes execution
    Then: Iterates over session.read()
    """


@pytest.mark.asyncio
async def test_call_command_writes_response_to_console(mock_session: AsyncMock, mock_router: MagicMock, mock_console: MagicMock) -> None:
    """
    Given: Session read yields b"response data"
    When: call_command processes response
    Then: console.write_binary_data(b"response data") is called
    """


@pytest.mark.asyncio
async def test_call_command_handles_empty_response(mock_session: AsyncMock, mock_router: MagicMock, mock_console: MagicMock) -> None:
    """
    Given: Session read yields no data
    When: call_command processes response
    Then: No output written to console
    """


@pytest.mark.asyncio
async def test_call_command_handles_multipart_response(mock_session: AsyncMock, mock_router: MagicMock, mock_console: MagicMock) -> None:
    """
    Given: Session read yields multiple chunks
    When: call_command processes response
    Then: Each chunk is written to console
    """
