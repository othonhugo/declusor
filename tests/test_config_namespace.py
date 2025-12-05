"""Tests for declusor.config.enums module.

This module tests the enum classes:
- FileFunc: File function names for shell commands
- Language: Supported shell languages
"""

import pytest

# =============================================================================
# Tests: FileFunc enum
# =============================================================================


def test_file_func_exec_file_value() -> None:
    """
    Given: FileFunc.EXEC_FILE
    When: .value is accessed
    Then: Returns "execute_base64_encoded_value"
    """


def test_file_func_store_file_value() -> None:
    """
    Given: FileFunc.STORE_FILE
    When: .value is accessed
    Then: Returns "store_base64_encoded_value"
    """


def test_file_func_is_str_enum() -> None:
    """
    Given: FileFunc enum member
    When: Used as string (e.g., in f-string)
    Then: Behaves as string value
    """


def test_file_func_str_conversion() -> None:
    """
    Given: FileFunc.EXEC_FILE
    When: str() is called
    Then: Returns the value string
    """


def test_file_func_equality_with_string() -> None:
    """
    Given: FileFunc.EXEC_FILE
    When: Compared to "execute_base64_encoded_value"
    Then: Returns True (StrEnum behavior)
    """


def test_file_func_all_members() -> None:
    """
    Given: FileFunc enum
    When: All members are listed
    Then: Contains EXEC_FILE and STORE_FILE
    """


# =============================================================================
# Tests: Language enum
# =============================================================================


def test_language_bash_value() -> None:
    """
    Given: Language.BASH
    When: .value is accessed
    Then: Returns "bash"
    """


def test_language_sh_value() -> None:
    """
    Given: Language.SH
    When: .value is accessed
    Then: Returns "sh"
    """


def test_language_is_str_enum() -> None:
    """
    Given: Language enum member
    When: Used as string
    Then: Behaves as string value
    """


def test_language_str_conversion() -> None:
    """
    Given: Language.BASH
    When: str() is called
    Then: Returns "bash"
    """


def test_language_equality_with_string() -> None:
    """
    Given: Language.SH
    When: Compared to "sh"
    Then: Returns True (StrEnum behavior)
    """


def test_language_all_members() -> None:
    """
    Given: Language enum
    When: All members are listed
    Then: Contains BASH and SH
    """


def test_language_bash_and_sh_are_different() -> None:
    """
    Given: Language.BASH and Language.SH
    When: Compared
    Then: Are not equal
    """


# =============================================================================
# Tests: Enum usage patterns
# =============================================================================


def test_file_func_usable_in_match() -> None:
    """
    Given: match statement with FileFunc
    When: Case FileFunc.EXEC_FILE is matched
    Then: Correct branch is executed
    """


def test_language_usable_in_match() -> None:
    """
    Given: match statement with Language
    When: Case Language.BASH is matched
    Then: Correct branch is executed
    """


def test_file_func_hashable() -> None:
    """
    Given: FileFunc members
    When: Used as dict keys
    Then: Works correctly (hashable)
    """


def test_language_hashable() -> None:
    """
    Given: Language members
    When: Used in set
    Then: Works correctly (hashable)
    """
