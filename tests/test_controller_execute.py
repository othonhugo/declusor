"""Tests for declusor.controller.execute module (call_execute function).

This module tests:
- call_execute: Execute program/script from local system on remote
"""

from pathlib import Path
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


@pytest.fixture
def temp_script(tmp_path: Path) -> Path:
    """Create a temporary script file for testing."""


# =============================================================================
# Tests: call_execute - Argument parsing
# =============================================================================


@pytest.mark.asyncio
async def test_call_execute_parses_filepath_argument(mock_session: AsyncMock, mock_router: MagicMock, temp_script: Path) -> None:
    """
    Given: call_execute with line=str(temp_script)
    When: Controller parses arguments
    Then: arguments["filepath"] contains the path
    """


@pytest.mark.asyncio
async def test_call_execute_missing_filepath_raises(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_execute with empty line ""
    When: Controller parses arguments
    Then: Raises ParserError (filepath is required)
    """


# =============================================================================
# Tests: call_execute - File validation
# =============================================================================


@pytest.mark.asyncio
async def test_call_execute_validates_file_exists(mock_session: AsyncMock, mock_router: MagicMock, temp_script: Path) -> None:
    """
    Given: call_execute with valid filepath
    When: Controller validates file
    Then: ensure_file_exists is called
    """


@pytest.mark.asyncio
async def test_call_execute_nonexistent_file_raises(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_execute with "/nonexistent/script.sh"
    When: Controller validates file
    Then: Raises InvalidOperation
    """


@pytest.mark.asyncio
async def test_call_execute_directory_raises(mock_session: AsyncMock, mock_router: MagicMock, tmp_path: Path) -> None:
    """
    Given: call_execute with directory path
    When: Controller validates file
    Then: Raises InvalidOperation (not a file)
    """


# =============================================================================
# Tests: call_execute - Execution
# =============================================================================


@pytest.mark.asyncio
async def test_call_execute_creates_execute_file_command(mock_session: AsyncMock, mock_router: MagicMock, temp_script: Path) -> None:
    """
    Given: call_execute with valid script
    When: Controller executes
    Then: ExecuteFile command is instantiated
    """


@pytest.mark.asyncio
async def test_call_execute_sends_to_session(mock_session: AsyncMock, mock_router: MagicMock, temp_script: Path) -> None:
    """
    Given: call_execute with valid script
    When: Controller executes
    Then: session.write is called with base64-encoded command
    """


# =============================================================================
# Tests: call_execute - Response handling
# =============================================================================


@pytest.mark.asyncio
async def test_call_execute_reads_response(mock_session: AsyncMock, mock_router: MagicMock, temp_script: Path) -> None:
    """
    Given: Script produces output on target
    When: call_execute completes
    Then: Response is read from session
    """


@pytest.mark.asyncio
async def test_call_execute_writes_response_to_console(
    mock_session: AsyncMock, mock_router: MagicMock, mock_console: MagicMock, temp_script: Path
) -> None:
    """
    Given: Session returns script output
    When: call_execute processes response
    Then: Output is written to console
    """
