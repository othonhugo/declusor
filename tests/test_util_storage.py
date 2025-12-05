"""Tests for declusor.util.storage module.

This module tests file system operations including:
- load_file: Reading file contents as bytes
- try_load_file: Safe file loading with None on failure
- load_payload: Loading payload scripts with validation
- load_library: Concatenating library scripts
- ensure_file_exists: Validating file existence
- ensure_directory_exists: Validating directory existence
"""

from pathlib import Path

import pytest

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def temp_file(tmp_path: Path) -> Path:
    """Create a temporary file with known content for testing."""


@pytest.fixture
def temp_directory(tmp_path: Path) -> Path:
    """Create a temporary directory structure for testing."""


@pytest.fixture
def mock_modules_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Mock BasePath.MODULES_DIR to a temporary directory with test payloads."""


@pytest.fixture
def mock_library_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Mock BasePath.LIBRARY_DIR to a temporary directory with test library scripts."""


# =============================================================================
# Tests: load_file
# =============================================================================


def test_load_file_returns_bytes_content(temp_file: Path) -> None:
    """
    Given: A valid file with known byte content
    When: load_file is called with the file path
    Then: Returns the exact byte content of the file
    """


def test_load_file_accepts_string_path(temp_file: Path) -> None:
    """
    Given: A valid file path as a string (not Path object)
    When: load_file is called with the string path
    Then: Returns the file content successfully
    """


def test_load_file_raises_on_nonexistent_file() -> None:
    """
    Given: A path to a file that does not exist
    When: load_file is called
    Then: Raises InvalidOperation with descriptive message
    """


def test_load_file_raises_on_directory(temp_directory: Path) -> None:
    """
    Given: A path to a directory (not a file)
    When: load_file is called
    Then: Raises InvalidOperation indicating path is not a file
    """


def test_load_file_raises_on_permission_denied(temp_file: Path) -> None:
    """
    Given: A file with no read permissions
    When: load_file is called
    Then: Raises InvalidOperation with read error details
    """


def test_load_file_handles_binary_content(temp_file: Path) -> None:
    """
    Given: A file containing binary data (non-UTF8)
    When: load_file is called
    Then: Returns the raw binary content without modification
    """


def test_load_file_handles_empty_file(temp_file: Path) -> None:
    """
    Given: An empty file (0 bytes)
    When: load_file is called
    Then: Returns empty bytes b''
    """


# =============================================================================
# Tests: try_load_file
# =============================================================================


def test_try_load_file_returns_content_on_success(temp_file: Path) -> None:
    """
    Given: A valid, readable file
    When: try_load_file is called
    Then: Returns the file content as bytes
    """


def test_try_load_file_returns_none_on_nonexistent_file() -> None:
    """
    Given: A path to a file that does not exist
    When: try_load_file is called
    Then: Returns None (does not raise an exception)
    """


def test_try_load_file_returns_none_on_permission_error(temp_file: Path) -> None:
    """
    Given: A file with no read permissions
    When: try_load_file is called
    Then: Returns None (does not raise an exception)
    """


# =============================================================================
# Tests: load_payload
# =============================================================================


def test_load_payload_returns_script_content(mock_modules_dir: Path) -> None:
    """
    Given: A valid .sh payload file in the modules directory
    When: load_payload is called with the filename
    Then: Returns the script content as bytes
    """


def test_load_payload_accepts_relative_path(mock_modules_dir: Path) -> None:
    """
    Given: A payload file in a subdirectory (e.g., "discovery/dev_tools.sh")
    When: load_payload is called with the relative path
    Then: Returns the script content
    """


def test_load_payload_raises_on_unsupported_extension(mock_modules_dir: Path) -> None:
    """
    Given: A file with disallowed extension (e.g., .py, .exe)
    When: load_payload is called
    Then: Raises InvalidOperation about unsupported extension
    """


def test_load_payload_raises_on_path_traversal_attempt(mock_modules_dir: Path) -> None:
    """
    Given: A path attempting directory traversal (e.g., "../../../etc/passwd")
    When: load_payload is called
    Then: Raises InvalidOperation about path being outside scripts directory
    """


def test_load_payload_raises_on_nonexistent_file(mock_modules_dir: Path) -> None:
    """
    Given: A module name that does not exist
    When: load_payload is called
    Then: Raises InvalidOperation about file not found
    """


# =============================================================================
# Tests: load_library
# =============================================================================


def test_load_library_concatenates_all_scripts(mock_library_dir: Path) -> None:
    """
    Given: A library directory with multiple .sh files
    When: load_library is called
    Then: Returns all scripts concatenated with double newlines
    """


def test_load_library_ignores_non_sh_files(mock_library_dir: Path) -> None:
    """
    Given: A library directory with .sh and non-.sh files
    When: load_library is called
    Then: Only .sh files are included in the result
    """


def test_load_library_ignores_subdirectories(mock_library_dir: Path) -> None:
    """
    Given: A library directory containing subdirectories
    When: load_library is called
    Then: Subdirectories are skipped (only top-level files loaded)
    """


def test_load_library_returns_empty_bytes_when_no_valid_files(mock_library_dir: Path) -> None:
    """
    Given: A library directory with no .sh files
    When: load_library is called
    Then: Returns empty bytes (or join of empty list)
    """


def test_load_library_handles_unreadable_file(mock_library_dir: Path) -> None:
    """
    Given: A library directory with one readable and one unreadable .sh file
    When: load_library is called
    Then: Returns content of readable files, skips unreadable ones
    """


# =============================================================================
# Tests: ensure_file_exists
# =============================================================================


def test_ensure_file_exists_returns_resolved_path(temp_file: Path) -> None:
    """
    Given: A valid file path
    When: ensure_file_exists is called
    Then: Returns the resolved (absolute) Path object
    """


def test_ensure_file_exists_resolves_relative_path(temp_file: Path) -> None:
    """
    Given: A relative file path (e.g., "./file.txt")
    When: ensure_file_exists is called
    Then: Returns the fully resolved absolute Path
    """


def test_ensure_file_exists_raises_on_nonexistent() -> None:
    """
    Given: A path to a file that does not exist
    When: ensure_file_exists is called
    Then: Raises InvalidOperation with "does not exist" message
    """


def test_ensure_file_exists_raises_on_directory(temp_directory: Path) -> None:
    """
    Given: A path pointing to a directory
    When: ensure_file_exists is called
    Then: Raises InvalidOperation with "is not a file" message
    """


def test_ensure_file_exists_accepts_string_input(temp_file: Path) -> None:
    """
    Given: A valid file path as a string
    When: ensure_file_exists is called with string input
    Then: Returns the Path object successfully
    """


# =============================================================================
# Tests: ensure_directory_exists
# =============================================================================


def test_ensure_directory_exists_returns_resolved_path(temp_directory: Path) -> None:
    """
    Given: A valid directory path
    When: ensure_directory_exists is called
    Then: Returns the resolved (absolute) Path object
    """


def test_ensure_directory_exists_resolves_relative_path(temp_directory: Path) -> None:
    """
    Given: A relative directory path (e.g., "./subdir")
    When: ensure_directory_exists is called
    Then: Returns the fully resolved absolute Path
    """


def test_ensure_directory_exists_raises_on_nonexistent() -> None:
    """
    Given: A path to a directory that does not exist
    When: ensure_directory_exists is called
    Then: Raises InvalidOperation with "does not exist" message
    """


def test_ensure_directory_exists_raises_on_file(temp_file: Path) -> None:
    """
    Given: A path pointing to a file (not a directory)
    When: ensure_directory_exists is called
    Then: Raises InvalidOperation with "is not a directory" message
    """


def test_ensure_directory_exists_accepts_string_input(temp_directory: Path) -> None:
    """
    Given: A valid directory path as a string
    When: ensure_directory_exists is called with string input
    Then: Returns the Path object successfully
    """
