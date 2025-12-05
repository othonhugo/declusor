"""Tests for declusor.core.parser module (Parser class).

This module tests:
- Parser: Custom ArgumentParser with ParserError instead of SystemExit
"""

import pytest

# =============================================================================
# Tests: Parser initialization
# =============================================================================


def test_parser_init_accepts_prog() -> None:
    """
    Given: Parser(prog="mycommand") is created
    When: __init__ is called
    Then: prog attribute is set to "mycommand"
    """


def test_parser_init_default_add_help_false() -> None:
    """
    Given: Parser() is created without add_help argument
    When: __init__ is called
    Then: add_help defaults to False
    """


def test_parser_init_with_add_help_true() -> None:
    """
    Given: Parser(add_help=True) is created
    When: __init__ is called
    Then: -h/--help flags are available
    """


# =============================================================================
# Tests: Parser.error
# =============================================================================


def test_parser_error_raises_parser_error() -> None:
    """
    Given: Parser instance
    When: error("invalid input") is called
    Then: Raises ParserError (not SystemExit)
    """


def test_parser_error_includes_message() -> None:
    """
    Given: Parser instance
    When: error("missing argument") is called
    Then: ParserError contains "missing argument"
    """


def test_parser_error_message_format() -> None:
    """
    Given: Parser.error raised
    When: Checking exception
    Then: Message format matches expected pattern
    """


# =============================================================================
# Tests: Parser.get_formatter_class
# =============================================================================


def test_parser_get_formatter_class_returns_callable() -> None:
    """
    Given: Parser instance
    When: get_formatter_class() is called
    Then: Returns a callable
    """


def test_parser_get_formatter_class_creates_formatter() -> None:
    """
    Given: get_formatter_class() result
    When: Called with prog name
    Then: Returns HelpFormatter instance
    """


# =============================================================================
# Tests: Parser - Argument parsing
# =============================================================================


def test_parser_parse_args_success() -> None:
    """
    Given: Parser with positional argument defined
    When: parse_args(["value"]) is called
    Then: Returns namespace with argument
    """


def test_parser_parse_args_missing_required() -> None:
    """
    Given: Parser with required positional argument
    When: parse_args([]) is called (no args)
    Then: Raises ParserError
    """


def test_parser_parse_known_args_success() -> None:
    """
    Given: Parser with one argument defined
    When: parse_known_args(["val", "extra"]) is called
    Then: Returns (namespace, ["extra"])
    """


# =============================================================================
# Tests: Parser - Comparison with argparse
# =============================================================================


def test_parser_does_not_exit_on_error() -> None:
    """
    Given: Parser vs standard ArgumentParser
    When: error() is called
    Then: Parser raises exception, argparse calls sys.exit
    """


def test_parser_does_not_print_to_stderr() -> None:
    """
    Given: Parser instance
    When: error() is called
    Then: Does not print usage to stderr
    """


# =============================================================================
# Tests: Parser - Integration with parse_command_arguments
# =============================================================================


def test_parser_used_by_parse_command_arguments() -> None:
    """
    Given: parse_command_arguments function
    When: Parsing fails
    Then: ParserError is raised (via custom Parser)
    """
