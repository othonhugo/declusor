"""Tests for declusor.util.parsing module.

This module tests command argument parsing including:
- Parser: Custom ArgumentParser subclass with ParserError handling
- parse_command_arguments: Type-aware argument parsing with optional support
"""

from typing import Optional

import pytest

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def simple_definitions() -> dict:
    """Return simple argument definitions: {"name": str, "count": int}."""


@pytest.fixture
def optional_definitions() -> dict:
    """Return definitions with optional args: {"command": Optional[str]}."""


# =============================================================================
# Tests: Parser class
# =============================================================================


def test_parser_error_raises_parser_error() -> None:
    """
    Given: A Parser instance
    When: error() method is called with a message
    Then: Raises ParserError (not SystemExit like default argparse)
    """


def test_parser_get_formatter_class_returns_callable() -> None:
    """
    Given: A Parser instance
    When: get_formatter_class() is called
    Then: Returns a callable that produces HelpFormatter
    """


def test_parser_custom_prog_name() -> None:
    """
    Given: A Parser with custom prog name
    When: Parser is initialized with prog="mycommand"
    Then: The prog attribute is set correctly
    """


def test_parser_without_help_flag() -> None:
    """
    Given: A Parser with add_help=False
    When: --help is passed to parse
    Then: Does not recognize -h/--help as valid options
    """


# =============================================================================
# Tests: parse_command_arguments - Basic usage
# =============================================================================


def test_parse_command_arguments_single_string_arg() -> None:
    """
    Given: definitions={"filepath": str} and line="test.txt"
    When: parse_command_arguments is called
    Then: Returns ({"filepath": "test.txt"}, [])
    """


def test_parse_command_arguments_single_int_arg() -> None:
    """
    Given: definitions={"count": int} and line="42"
    When: parse_command_arguments is called
    Then: Returns ({"count": 42}, [])
    """


def test_parse_command_arguments_multiple_args() -> None:
    """
    Given: definitions={"name": str, "age": int} and line='"John Doe" 30'
    When: parse_command_arguments is called
    Then: Returns ({"name": "John Doe", "age": 30}, [])
    """


def test_parse_command_arguments_empty_with_no_definitions() -> None:
    """
    Given: definitions={} and line=""
    When: parse_command_arguments is called
    Then: Returns ({}, []) without error
    """


def test_parse_command_arguments_empty_with_whitespace_only() -> None:
    """
    Given: definitions={} and line="   "
    When: parse_command_arguments is called
    Then: Returns ({}, []) (whitespace-only treated as empty)
    """


# =============================================================================
# Tests: parse_command_arguments - Optional arguments
# =============================================================================


def test_parse_command_arguments_optional_provided() -> None:
    """
    Given: definitions={"cmd": Optional[str]} and line="hello"
    When: parse_command_arguments is called
    Then: Returns ({"cmd": "hello"}, [])
    """


def test_parse_command_arguments_optional_omitted() -> None:
    """
    Given: definitions={"cmd": Optional[str]} and line=""
    When: parse_command_arguments is called
    Then: Returns ({"cmd": None}, [])
    """


def test_parse_command_arguments_mixed_required_and_optional() -> None:
    """
    Given: definitions={"required": str, "optional": Optional[int]}
    When: line="value" is parsed (no optional value)
    Then: Returns ({"required": "value", "optional": None}, [])
    """


def test_parse_command_arguments_mixed_all_provided() -> None:
    """
    Given: definitions={"required": str, "optional": Optional[int]}
    When: line="value 42" is parsed (both values)
    Then: Returns ({"required": "value", "optional": 42}, [])
    """


# =============================================================================
# Tests: parse_command_arguments - Error handling
# =============================================================================


def test_parse_command_arguments_unsupported_type_raises() -> None:
    """
    Given: definitions={"data": list} (unsupported type)
    When: parse_command_arguments is called
    Then: Raises InvalidOperation about unsupported type
    """


def test_parse_command_arguments_unclosed_quote_raises() -> None:
    """
    Given: line='unclosed "quote'
    When: parse_command_arguments is called
    Then: Raises InvalidOperation with parsing error details
    """


def test_parse_command_arguments_missing_required_arg_raises() -> None:
    """
    Given: definitions={"filepath": str} and line="" (empty)
    When: parse_command_arguments is called with required arg missing
    Then: Raises ParserError (from custom Parser.error)
    """


def test_parse_command_arguments_wrong_type_raises() -> None:
    """
    Given: definitions={"count": int} and line="not_a_number"
    When: parse_command_arguments is called
    Then: Raises ParserError about invalid int value
    """


# =============================================================================
# Tests: parse_command_arguments - Unknown arguments
# =============================================================================


def test_parse_command_arguments_allow_unknown_true() -> None:
    """
    Given: definitions={"name": str}, line="hello extra args", allow_unknown=True
    When: parse_command_arguments is called
    Then: Returns ({"name": "hello"}, ["extra", "args"])
    """


def test_parse_command_arguments_allow_unknown_false_raises() -> None:
    """
    Given: definitions={"name": str}, line="hello extra", allow_unknown=False
    When: parse_command_arguments is called
    Then: Raises ParserError about unrecognized arguments
    """


def test_parse_command_arguments_unknown_with_empty_definitions() -> None:
    """
    Given: definitions={}, line="some args", allow_unknown=True
    When: parse_command_arguments is called
    Then: Returns ({}, ["some", "args"])
    """


# =============================================================================
# Tests: parse_command_arguments - Edge cases
# =============================================================================


def test_parse_command_arguments_quoted_string_with_spaces() -> None:
    """
    Given: definitions={"path": str} and line='"path with spaces"'
    When: parse_command_arguments is called
    Then: Returns ({"path": "path with spaces"}, [])
    """


def test_parse_command_arguments_escaped_quotes() -> None:
    """
    Given: definitions={"text": str} and line='he said \\"hello\\"'
    When: parse_command_arguments is called
    Then: Returns the properly unescaped string
    """


def test_parse_command_arguments_preserves_argument_order() -> None:
    """
    Given: definitions={"first": str, "second": str, "third": int}
    When: line="a b 3" is parsed
    Then: Arguments are matched positionally in definition order
    """


def test_parse_command_arguments_negative_integer() -> None:
    """
    Given: definitions={"num": int} and line="-42"
    When: parse_command_arguments is called
    Then: Returns ({"num": -42}, []) - handles negative numbers
    """
