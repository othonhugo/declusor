"""Tests for declusor.controller.load module (call_load function).

This module tests:
- call_load: Load payload file from local system and execute on remote
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
def temp_payload(tmp_path: Path) -> Path:
    """Create a temporary payload file for testing."""


# =============================================================================
# Tests: call_load - Argument parsing
# =============================================================================


@pytest.mark.asyncio
async def test_call_load_parses_filepath_argument(mock_session: AsyncMock, mock_router: MagicMock, temp_payload: Path) -> None:
    """
    Given: call_load with line=str(temp_payload)
    When: Controller parses arguments
    Then: arguments["filepath"] contains the path
    """


@pytest.mark.asyncio
async def test_call_load_missing_filepath_raises(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_load with empty line ""
    When: Controller parses arguments
    Then: Raises ParserError (filepath is required)
    """


@pytest.mark.asyncio
async def test_call_load_parses_relative_path(mock_session: AsyncMock, mock_router: MagicMock, temp_payload: Path) -> None:
    """
    Given: call_load with relative path "discovery/dev_tools.sh"
    When: Controller parses arguments
    Then: Path is parsed correctly
    """


# =============================================================================
# Tests: call_load - File validation
# =============================================================================


@pytest.mark.asyncio
async def test_call_load_validates_file_exists(mock_session: AsyncMock, mock_router: MagicMock, temp_payload: Path) -> None:
    """
    Given: call_load with valid filepath
    When: Controller validates file
    Then: ensure_file_exists is called
    """


@pytest.mark.asyncio
async def test_call_load_nonexistent_file_raises(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_load with "/nonexistent/payload.sh"
    When: Controller validates file
    Then: Raises InvalidOperation
    """


# =============================================================================
# Tests: call_load - Execution
# =============================================================================


@pytest.mark.asyncio
async def test_call_load_creates_load_payload_command(mock_session: AsyncMock, mock_router: MagicMock, temp_payload: Path) -> None:
    """
    Given: call_load with valid payload
    When: Controller executes
    Then: LoadPayload command is instantiated
    """


@pytest.mark.asyncio
async def test_call_load_sends_raw_content(mock_session: AsyncMock, mock_router: MagicMock, temp_payload: Path) -> None:
    """
    Given: call_load with payload containing "echo test"
    When: Controller executes
    Then: session.write receives raw script bytes
    """


# =============================================================================
# Tests: call_load - Response handling
# =============================================================================


@pytest.mark.asyncio
async def test_call_load_reads_output(mock_session: AsyncMock, mock_router: MagicMock, temp_payload: Path) -> None:
    """
    Given: Payload produces output on target
    When: call_load completes
    Then: Response is read from session
    """


@pytest.mark.asyncio
async def test_call_load_writes_output_to_console(
    mock_session: AsyncMock, mock_router: MagicMock, mock_console: MagicMock, temp_payload: Path
) -> None:
    """
    Given: Session returns payload output
    When: call_load processes response
    Then: Output is written to console via write_binary_data
    """


@pytest.mark.asyncio
async def test_call_load_handles_multiline_output(
    mock_session: AsyncMock, mock_router: MagicMock, mock_console: MagicMock, temp_payload: Path
) -> None:
    """
    Given: Payload produces multi-line output
    When: call_load processes response
    Then: All lines are written to console
    """
