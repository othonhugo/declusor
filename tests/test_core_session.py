"""Tests for declusor.core.session module (Session class).

This module tests the async session management including:
- Session: Manages asyncio connection for reading/writing data
- ACK-based protocol for message framing
- Timeout and buffer size configuration
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def mock_reader() -> AsyncMock:
    """Create a mock asyncio.StreamReader."""


@pytest.fixture
def mock_writer() -> MagicMock:
    """Create a mock asyncio.StreamWriter with drain()."""


@pytest.fixture
def session(mock_reader: AsyncMock, mock_writer: MagicMock):
    """Create a Session instance with mocked streams."""


# =============================================================================
# Tests: Session initialization
# =============================================================================


def test_session_init_stores_reader_writer(mock_reader: AsyncMock, mock_writer: MagicMock) -> None:
    """
    Given: Session is created with reader and writer
    When: __init__ is called
    Then: reader and writer attributes are set
    """


def test_session_init_default_timeout() -> None:
    """
    Given: Session is created without timeout argument
    When: __init__ is called
    Then: _timeout is set to default 0.75 seconds
    """


def test_session_init_default_bufsize() -> None:
    """
    Given: Session is created without bufsize argument
    When: __init__ is called
    Then: _bufsize is set to default 4096 bytes
    """


def test_session_init_custom_timeout(mock_reader: AsyncMock, mock_writer: MagicMock) -> None:
    """
    Given: Session is created with timeout=2.0
    When: __init__ is called
    Then: _timeout is set to 2.0
    """


def test_session_init_custom_bufsize(mock_reader: AsyncMock, mock_writer: MagicMock) -> None:
    """
    Given: Session is created with bufsize=8192
    When: __init__ is called
    Then: _bufsize is set to 8192
    """


# =============================================================================
# Tests: Session.initialize
# =============================================================================


@pytest.mark.asyncio
async def test_session_initialize_loads_library(mock_reader: AsyncMock, mock_writer: MagicMock) -> None:
    """
    Given: Session.initialize() is called
    When: Initialization runs
    Then: Writes library content via session.write()
    """


@pytest.mark.asyncio
async def test_session_initialize_checks_ack(mock_reader: AsyncMock, mock_writer: MagicMock) -> None:
    """
    Given: Client sends proper ACK after library load
    When: initialize() reads response
    Then: No warning is displayed
    """


@pytest.mark.asyncio
async def test_session_initialize_warns_on_bad_ack(mock_reader: AsyncMock, mock_writer: MagicMock) -> None:
    """
    Given: Client sends unexpected response (not ACK)
    When: initialize() reads response
    Then: Warning about library import failure is displayed
    """


@pytest.mark.asyncio
async def test_session_initialize_handles_timeout(mock_reader: AsyncMock, mock_writer: MagicMock) -> None:
    """
    Given: Client does not respond within timeout
    When: initialize() times out
    Then: Continues without error (timeout is expected)
    """


@pytest.mark.asyncio
async def test_session_initialize_handles_exception(mock_reader: AsyncMock, mock_writer: MagicMock) -> None:
    """
    Given: Exception occurs during initialization
    When: initialize() catches exception
    Then: Silently continues (does not propagate)
    """


# =============================================================================
# Tests: Session.set_timeout
# =============================================================================


def test_session_set_timeout_updates_value() -> None:
    """
    Given: Session with default timeout
    When: set_timeout(5.0) is called
    Then: _timeout is updated to 5.0
    """


# =============================================================================
# Tests: Session.read
# =============================================================================


@pytest.mark.asyncio
async def test_session_read_yields_data_chunks(mock_reader: AsyncMock) -> None:
    """
    Given: Client sends data followed by ACK
    When: read() async generator is iterated
    Then: Yields data chunks (excluding ACK)
    """


@pytest.mark.asyncio
async def test_session_read_stops_at_ack(mock_reader: AsyncMock) -> None:
    """
    Given: Client sends "data" + ACK_CLIENT_VALUE
    When: read() is iterated
    Then: Yields "data" and stops (ACK marks end)
    """


@pytest.mark.asyncio
async def test_session_read_handles_split_ack(mock_reader: AsyncMock) -> None:
    """
    Given: ACK is split across two read() calls
    When: read() processes chunks
    Then: Correctly detects ACK spanning buffer boundary
    """


@pytest.mark.asyncio
async def test_session_read_raises_on_connection_closed(mock_reader: AsyncMock) -> None:
    """
    Given: reader.read() returns empty bytes (connection closed)
    When: read() processes
    Then: Raises ConnectionResetError
    """


@pytest.mark.asyncio
async def test_session_read_continues_on_timeout(mock_reader: AsyncMock) -> None:
    """
    Given: reader.read() times out (asyncio.TimeoutError)
    When: read() handles timeout
    Then: Continues reading (does not break loop)
    """


@pytest.mark.asyncio
async def test_session_read_yields_partial_buffer(mock_reader: AsyncMock) -> None:
    """
    Given: Large data arriving in multiple chunks before ACK
    When: read() processes data
    Then: Yields safe portions while ACK might span chunks
    """


# =============================================================================
# Tests: Session.write
# =============================================================================


@pytest.mark.asyncio
async def test_session_write_sends_content(mock_writer: MagicMock) -> None:
    """
    Given: write(b"command") is called
    When: Data is sent
    Then: writer.write(b"command") is called
    """


@pytest.mark.asyncio
async def test_session_write_appends_server_ack(mock_writer: MagicMock) -> None:
    """
    Given: write(b"data") is called
    When: Data is sent
    Then: ACK_SERVER_VALUE is appended after content
    """


@pytest.mark.asyncio
async def test_session_write_drains_writer(mock_writer: MagicMock) -> None:
    """
    Given: write() is called
    When: Data is sent
    Then: writer.drain() is awaited
    """


@pytest.mark.asyncio
async def test_session_write_raises_on_oserror(mock_writer: MagicMock) -> None:
    """
    Given: writer.write() raises OSError
    When: write() attempts to send
    Then: Raises ConnectionError with descriptive message
    """


@pytest.mark.asyncio
async def test_session_write_preserves_exception_chain(mock_writer: MagicMock) -> None:
    """
    Given: OSError is raised during write
    When: ConnectionError is raised
    Then: Original OSError is chained with 'from'
    """
