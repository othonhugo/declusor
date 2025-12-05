"""Tests for declusor.command.load module (LoadPayload class).

This module tests:
- LoadPayload: Load and execute payload script on target
"""

from pathlib import Path
from unittest.mock import AsyncMock

import pytest

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def mock_session() -> AsyncMock:
    """Create a mock ISession with write method."""


@pytest.fixture
def temp_payload(tmp_path: Path) -> Path:
    """Create a temporary payload script with known content."""


# =============================================================================
# Tests: LoadPayload initialization
# =============================================================================


def test_load_payload_init_validates_file_exists(temp_payload: Path) -> None:
    """
    Given: LoadPayload(valid_path) is created
    When: __init__ is called
    Then: File existence is validated via ensure_file_exists
    """


def test_load_payload_init_accepts_string_path(temp_payload: Path) -> None:
    """
    Given: LoadPayload(str(path)) with string path
    When: __init__ is called
    Then: Converts to Path and validates
    """


def test_load_payload_init_accepts_path_object(temp_payload: Path) -> None:
    """
    Given: LoadPayload(Path) with Path object
    When: __init__ is called
    Then: Accepts Path directly
    """


def test_load_payload_init_raises_on_nonexistent() -> None:
    """
    Given: LoadPayload("/nonexistent/payload.sh")
    When: __init__ is called
    Then: Raises InvalidOperation (file not found)
    """


def test_load_payload_init_stores_filepath(temp_payload: Path) -> None:
    """
    Given: LoadPayload(valid_path)
    When: __init__ is called
    Then: _filepath attribute stores resolved path
    """


# =============================================================================
# Tests: LoadPayload.execute
# =============================================================================


@pytest.mark.asyncio
async def test_load_payload_execute_writes_file_content(mock_session: AsyncMock, temp_payload: Path) -> None:
    """
    Given: LoadPayload with payload containing "echo test"
    When: execute(session) is called
    Then: Writes raw script content to session
    """


@pytest.mark.asyncio
async def test_load_payload_execute_writes_bytes(mock_session: AsyncMock, temp_payload: Path) -> None:
    """
    Given: LoadPayload with valid payload
    When: execute(session) is called
    Then: session.write receives bytes (not string)
    """


@pytest.mark.asyncio
async def test_load_payload_execute_reads_file_at_execution_time(mock_session: AsyncMock, temp_payload: Path) -> None:
    """
    Given: LoadPayload initialized with valid file
    When: File is modified before execute()
    Then: Reads current file content (not cached)
    """


@pytest.mark.asyncio
async def test_load_payload_execute_raises_on_load_failure(mock_session: AsyncMock, temp_payload: Path) -> None:
    """
    Given: File becomes unreadable between init and execute
    When: execute() calls try_load_file and gets None
    Then: Raises InvalidOperation about load failure
    """


@pytest.mark.asyncio
async def test_load_payload_execute_raises_with_filepath_in_message(mock_session: AsyncMock, temp_payload: Path) -> None:
    """
    Given: File load fails
    When: InvalidOperation is raised
    Then: Exception message includes filepath
    """


# =============================================================================
# Tests: LoadPayload vs ExecuteFile comparison
# =============================================================================


def test_load_payload_sends_raw_content() -> None:
    """
    Given: LoadPayload with script content
    When: Comparing to ExecuteFile
    Then: LoadPayload sends raw bytes, ExecuteFile sends base64
    """


def test_load_payload_does_not_use_file_func() -> None:
    """
    Given: LoadPayload class
    When: Checking for FUNC_NAME attribute
    Then: Does not have FUNC_NAME (unlike ExecuteFile/UploadFile)
    """


# =============================================================================
# Tests: Edge cases
# =============================================================================


@pytest.mark.asyncio
async def test_load_payload_handles_empty_file(mock_session: AsyncMock, tmp_path: Path) -> None:
    """
    Given: Empty payload file
    When: execute() is called
    Then: Writes empty bytes to session
    """


@pytest.mark.asyncio
async def test_load_payload_handles_binary_content(mock_session: AsyncMock, tmp_path: Path) -> None:
    """
    Given: Payload with binary content
    When: execute() is called
    Then: Binary content is written unchanged
    """


@pytest.mark.asyncio
async def test_load_payload_handles_multiline_script(mock_session: AsyncMock, temp_payload: Path) -> None:
    """
    Given: Multi-line bash script
    When: execute() is called
    Then: All lines are preserved in output
    """
