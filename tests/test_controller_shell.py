"""Tests for declusor.controller.shell module (call_shell function).

This module tests:
- call_shell: Start interactive shell session on remote
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


# =============================================================================
# Tests: call_shell - Argument parsing
# =============================================================================


@pytest.mark.asyncio
async def test_call_shell_accepts_empty_line(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_shell with empty line ""
    When: Controller parses arguments
    Then: No error (shell takes no arguments)
    """


@pytest.mark.asyncio
async def test_call_shell_rejects_extra_arguments(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_shell with line="unexpected args"
    When: Controller parses arguments
    Then: Raises ParserError (unrecognized arguments)
    """


@pytest.mark.asyncio
async def test_call_shell_uses_empty_definitions(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_shell function
    When: parse_command_arguments is called
    Then: Uses empty definitions {}
    """


# =============================================================================
# Tests: call_shell - Execution
# =============================================================================


@pytest.mark.asyncio
async def test_call_shell_creates_launch_shell(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_shell with valid invocation
    When: Controller executes
    Then: LaunchShell() is instantiated
    """


@pytest.mark.asyncio
async def test_call_shell_executes_on_session(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_shell is invoked
    When: Controller executes
    Then: LaunchShell.execute(session) is called
    """


@pytest.mark.asyncio
async def test_call_shell_awaits_shell_completion(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_shell is invoked
    When: Shell is running
    Then: Awaits until shell completes (user exits)
    """


# =============================================================================
# Tests: call_shell - Does NOT handle response
# =============================================================================


@pytest.mark.asyncio
async def test_call_shell_does_not_read_session_directly(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_shell is invoked
    When: Controller executes
    Then: Does NOT iterate session.read() (LaunchShell handles I/O)
    """


@pytest.mark.asyncio
async def test_call_shell_does_not_write_to_console(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_shell is invoked
    When: Controller executes
    Then: Does NOT call console.write_* (LaunchShell handles output)
    """
