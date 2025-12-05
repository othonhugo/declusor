"""Tests for declusor.command.file module (ExecuteFile, UploadFile, _BaseFileCommand).

This module tests:
- _BaseFileCommand: Base class for file operations
- ExecuteFile: Execute a local file on target
- UploadFile: Upload a local file to target
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
def temp_script(tmp_path: Path) -> Path:
    """Create a temporary shell script file with known content."""


@pytest.fixture
def temp_binary_file(tmp_path: Path) -> Path:
    """Create a temporary binary file."""


# =============================================================================
# Tests: _BaseFileCommand (shared behavior)
# =============================================================================


def test_base_file_command_accepts_string_path(temp_script: Path) -> None:
    """
    Given: ExecuteFile(str(path)) with string path
    When: __init__ is called
    Then: Converts to Path and validates
    """


def test_base_file_command_accepts_path_object(temp_script: Path) -> None:
    """
    Given: ExecuteFile(Path) with Path object
    When: __init__ is called
    Then: Accepts Path directly
    """


def test_base_file_command_validates_file_exists(temp_script: Path) -> None:
    """
    Given: Valid file path
    When: __init__ is called
    Then: ensure_file_exists validates the file
    """


def test_base_file_command_raises_on_nonexistent() -> None:
    """
    Given: Nonexistent file path
    When: __init__ is called
    Then: Raises InvalidOperation
    """


def test_base_file_command_default_language_bash(temp_script: Path) -> None:
    """
    Given: ExecuteFile without language argument
    When: __init__ is called
    Then: _language defaults to Language.BASH
    """


def test_base_file_command_custom_language_sh(temp_script: Path) -> None:
    """
    Given: ExecuteFile(path, language=Language.SH)
    When: __init__ is called
    Then: _language is set to Language.SH
    """


# =============================================================================
# Tests: _BaseFileCommand._command property
# =============================================================================


def test_base_file_command_property_returns_bytes(temp_script: Path) -> None:
    """
    Given: ExecuteFile with valid script
    When: _command property is accessed
    Then: Returns bytes
    """


def test_base_file_command_property_encodes_base64(temp_script: Path) -> None:
    """
    Given: Script with known content
    When: _command property is accessed
    Then: File content is base64-encoded in the result
    """


def test_base_file_command_property_includes_function_name(temp_script: Path) -> None:
    """
    Given: ExecuteFile (uses EXEC_FILE function)
    When: _command property is accessed
    Then: Function name is included in command string
    """


# =============================================================================
# Tests: ExecuteFile
# =============================================================================


def test_execute_file_func_name_is_exec_file() -> None:
    """
    Given: ExecuteFile class
    When: FUNC_NAME is checked
    Then: Equals FileFunc.EXEC_FILE
    """


@pytest.mark.asyncio
async def test_execute_file_execute_sends_command(mock_session: AsyncMock, temp_script: Path) -> None:
    """
    Given: ExecuteFile with valid script
    When: execute(session) is called
    Then: Sends _command bytes to session
    """


def test_execute_file_command_format(temp_script: Path) -> None:
    """
    Given: Script with content "echo hello"
    When: _command property is accessed
    Then: Returns "execute_base64_encoded_value '<base64>'"
    """


# =============================================================================
# Tests: UploadFile
# =============================================================================


def test_upload_file_func_name_is_store_file() -> None:
    """
    Given: UploadFile class
    When: FUNC_NAME is checked
    Then: Equals FileFunc.STORE_FILE
    """


@pytest.mark.asyncio
async def test_upload_file_execute_sends_command(mock_session: AsyncMock, temp_script: Path) -> None:
    """
    Given: UploadFile with valid file
    When: execute(session) is called
    Then: Sends _command bytes to session
    """


def test_upload_file_command_format(temp_script: Path) -> None:
    """
    Given: File with known content
    When: _command property is accessed
    Then: Returns "store_base64_encoded_value '<base64>'"
    """


def test_upload_file_inherits_base_file_command() -> None:
    """
    Given: UploadFile class
    When: Checking inheritance
    Then: Inherits from _BaseFileCommand
    """


# =============================================================================
# Tests: Edge cases
# =============================================================================


def test_file_command_handles_binary_content(temp_binary_file: Path) -> None:
    """
    Given: Binary file (non-text content)
    When: _command is generated
    Then: Binary content is correctly base64-encoded
    """


def test_file_command_handles_empty_file(tmp_path: Path) -> None:
    """
    Given: Empty file (0 bytes)
    When: _command is generated
    Then: Empty base64 is encoded
    """


def test_file_command_handles_large_file(tmp_path: Path) -> None:
    """
    Given: Large file (e.g., 1MB)
    When: _command is generated
    Then: Full content is base64-encoded
    """
