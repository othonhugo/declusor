"""Tests for declusor.command.command module (ExecuteCommand class).

This module tests:
- ExecuteCommand: Execute raw command line on target
"""

from unittest.mock import AsyncMock

import pytest

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def mock_session() -> AsyncMock:
    """Create a mock ISession with write method."""


# =============================================================================
# Tests: ExecuteCommand initialization
# =============================================================================


def test_execute_command_init_encodes_command_to_bytes() -> None:
    """
    Given: ExecuteCommand("ls -la") is created
    When: __init__ is called
    Then: _command_line is set to b"ls -la"
    """


def test_execute_command_init_handles_empty_string() -> None:
    """
    Given: ExecuteCommand("") is created
    When: __init__ is called
    Then: _command_line is set to b""
    """


def test_execute_command_init_handles_unicode() -> None:
    """
    Given: ExecuteCommand("echo 你好") is created
    When: __init__ encodes command
    Then: UTF-8 bytes are stored correctly
    """


def test_execute_command_init_handles_special_characters() -> None:
    """
    Given: ExecuteCommand("echo $PATH && ls") is created
    When: __init__ encodes command
    Then: Special chars are preserved in bytes
    """


# =============================================================================
# Tests: ExecuteCommand.execute
# =============================================================================


@pytest.mark.asyncio
async def test_execute_command_execute_writes_to_session(mock_session: AsyncMock) -> None:
    """
    Given: ExecuteCommand with command "whoami"
    When: execute(session) is called
    Then: session.write(b"whoami") is called
    """


@pytest.mark.asyncio
async def test_execute_command_execute_awaits_write(mock_session: AsyncMock) -> None:
    """
    Given: ExecuteCommand instance
    When: execute(session) is called
    Then: Awaits session.write() (async call)
    """


@pytest.mark.asyncio
async def test_execute_command_execute_does_not_read_response(mock_session: AsyncMock) -> None:
    """
    Given: ExecuteCommand instance
    When: execute(session) is called
    Then: session.read() is NOT called (response handled by caller)
    """
