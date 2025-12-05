"""Tests for declusor.controller.upload module (call_upload function).

This module tests:
- call_upload: Upload file from local system to remote
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
def temp_file(tmp_path: Path) -> Path:
    """Create a temporary file for upload testing."""


# =============================================================================
# Tests: call_upload - Argument parsing
# =============================================================================


@pytest.mark.asyncio
async def test_call_upload_parses_filepath_argument(mock_session: AsyncMock, mock_router: MagicMock, temp_file: Path) -> None:
    """
    Given: call_upload with line=str(temp_file)
    When: Controller parses arguments
    Then: arguments["filepath"] contains the path
    """


@pytest.mark.asyncio
async def test_call_upload_missing_filepath_raises(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_upload with empty line ""
    When: Controller parses arguments
    Then: Raises ParserError (filepath is required)
    """


@pytest.mark.asyncio
async def test_call_upload_parses_quoted_path(mock_session: AsyncMock, mock_router: MagicMock, temp_file: Path) -> None:
    """
    Given: call_upload with path containing spaces in quotes
    When: Controller parses arguments
    Then: Path is correctly parsed
    """


# =============================================================================
# Tests: call_upload - File validation
# =============================================================================


@pytest.mark.asyncio
async def test_call_upload_validates_file_exists(mock_session: AsyncMock, mock_router: MagicMock, temp_file: Path) -> None:
    """
    Given: call_upload with valid filepath
    When: Controller validates file
    Then: ensure_file_exists is called with filepath
    """


@pytest.mark.asyncio
async def test_call_upload_nonexistent_file_raises(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_upload with "/nonexistent/file.txt"
    When: Controller validates file
    Then: Raises InvalidOperation
    """


@pytest.mark.asyncio
async def test_call_upload_directory_raises(mock_session: AsyncMock, mock_router: MagicMock, tmp_path: Path) -> None:
    """
    Given: call_upload with directory path
    When: Controller validates file
    Then: Raises InvalidOperation (not a file)
    """


# =============================================================================
# Tests: call_upload - Execution
# =============================================================================


@pytest.mark.asyncio
async def test_call_upload_creates_upload_file_command(mock_session: AsyncMock, mock_router: MagicMock, temp_file: Path) -> None:
    """
    Given: call_upload with valid file
    When: Controller executes
    Then: UploadFile command is instantiated
    """


@pytest.mark.asyncio
async def test_call_upload_sends_to_session(mock_session: AsyncMock, mock_router: MagicMock, temp_file: Path) -> None:
    """
    Given: call_upload with valid file
    When: Controller executes
    Then: session.write is called with base64-encoded store command
    """


# =============================================================================
# Tests: call_upload - Response handling
# =============================================================================


@pytest.mark.asyncio
async def test_call_upload_reads_response(mock_session: AsyncMock, mock_router: MagicMock, temp_file: Path) -> None:
    """
    Given: Upload produces response (e.g., stored filepath)
    When: call_upload completes
    Then: Response is read from session
    """


@pytest.mark.asyncio
async def test_call_upload_writes_response_to_console(
    mock_session: AsyncMock, mock_router: MagicMock, mock_console: MagicMock, temp_file: Path
) -> None:
    """
    Given: Session returns upload confirmation
    When: call_upload processes response
    Then: Response is written to console
    """


@pytest.mark.asyncio
async def test_call_upload_shows_stored_path(mock_session: AsyncMock, mock_router: MagicMock, mock_console: MagicMock, temp_file: Path) -> None:
    """
    Given: Target returns "/tmp/abc123.temp" after upload
    When: call_upload processes response
    Then: Path is displayed to user
    """
