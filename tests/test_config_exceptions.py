"""Tests for declusor.config.exceptions module.

This module tests the custom exception hierarchy:
- DeclusorException: Base exception class
- InvalidOperation: Invalid operation description
- ParserError: Argument parsing errors
- RouterError: Route not found errors
- PromptError: Invalid prompt argument errors
- ControllerError: Controller execution errors
- ExitRequest: Graceful exit signal
"""

import pytest

# =============================================================================
# Tests: DeclusorException (base class)
# =============================================================================


def test_declusor_exception_is_exception() -> None:
    """
    Given: DeclusorException class
    When: Checking inheritance
    Then: Inherits from Exception
    """


def test_declusor_exception_can_be_raised() -> None:
    """
    Given: DeclusorException("message")
    When: Raised
    Then: Can be caught as Exception
    """


# =============================================================================
# Tests: InvalidOperation
# =============================================================================


def test_invalid_operation_stores_description() -> None:
    """
    Given: InvalidOperation("file not found") is created
    When: description attribute is accessed
    Then: Returns "file not found"
    """


def test_invalid_operation_str_format() -> None:
    """
    Given: InvalidOperation("permission denied")
    When: str(exception) is called
    Then: Returns "invalid operation: permission denied"
    """


def test_invalid_operation_inherits_declusor_exception() -> None:
    """
    Given: InvalidOperation class
    When: Checking inheritance
    Then: Inherits from DeclusorException
    """


def test_invalid_operation_with_empty_description() -> None:
    """
    Given: InvalidOperation("")
    When: str(exception) is called
    Then: Returns "invalid operation: "
    """


# =============================================================================
# Tests: ParserError
# =============================================================================


def test_parser_error_stores_message() -> None:
    """
    Given: ParserError("unclosed quote") is created
    When: message attribute is accessed
    Then: Returns "unclosed quote"
    """


def test_parser_error_str_format() -> None:
    """
    Given: ParserError("invalid syntax")
    When: str(exception) is called
    Then: Returns descriptive error message
    """


def test_parser_error_inherits_declusor_exception() -> None:
    """
    Given: ParserError class
    When: Checking inheritance
    Then: Inherits from DeclusorException
    """


# =============================================================================
# Tests: RouterError
# =============================================================================


def test_router_error_stores_route() -> None:
    """
    Given: RouterError("unknown") is created
    When: route attribute is accessed
    Then: Returns "unknown"
    """


def test_router_error_str_format() -> None:
    """
    Given: RouterError("foobar")
    When: str(exception) is called
    Then: Returns "invalid route: 'foobar'"
    """


def test_router_error_optional_description() -> None:
    """
    Given: RouterError("cmd", description="not implemented")
    When: description attribute is accessed
    Then: Returns "not implemented"
    """


def test_router_error_str_with_description() -> None:
    """
    Given: RouterError("cmd", description="deprecated")
    When: str(exception) is called
    Then: Includes description in message
    """


def test_router_error_inherits_declusor_exception() -> None:
    """
    Given: RouterError class
    When: Checking inheritance
    Then: Inherits from DeclusorException
    """


# =============================================================================
# Tests: PromptError
# =============================================================================


def test_prompt_error_stores_argument() -> None:
    """
    Given: PromptError("badarg") is created
    When: argument attribute is accessed
    Then: Returns "badarg"
    """


def test_prompt_error_str_format() -> None:
    """
    Given: PromptError("invalid")
    When: str(exception) is called
    Then: Returns "invalid argument: 'invalid'"
    """


def test_prompt_error_inherits_declusor_exception() -> None:
    """
    Given: PromptError class
    When: Checking inheritance
    Then: Inherits from DeclusorException
    """


# =============================================================================
# Tests: ControllerError
# =============================================================================


def test_controller_error_stores_description() -> None:
    """
    Given: ControllerError("execution failed") is created
    When: description attribute is accessed
    Then: Returns "execution failed"
    """


def test_controller_error_str_format() -> None:
    """
    Given: ControllerError("timeout")
    When: str(exception) is called
    Then: Returns "controller error: timeout"
    """


def test_controller_error_inherits_declusor_exception() -> None:
    """
    Given: ControllerError class
    When: Checking inheritance
    Then: Inherits from DeclusorException
    """


# =============================================================================
# Tests: ExitRequest
# =============================================================================


def test_exit_request_inherits_declusor_exception() -> None:
    """
    Given: ExitRequest class
    When: Checking inheritance
    Then: Inherits from DeclusorException
    """


def test_exit_request_can_be_raised() -> None:
    """
    Given: ExitRequest exception
    When: Raised and caught
    Then: Can be caught as DeclusorException
    """


def test_exit_request_is_distinct_from_other_exceptions() -> None:
    """
    Given: ExitRequest, InvalidOperation, ParserError
    When: isinstance checks are done
    Then: ExitRequest is not InvalidOperation or ParserError
    """


def test_exit_request_default_message() -> None:
    """
    Given: ExitRequest() with no arguments
    When: str(exception) is called
    Then: Returns default message or empty string
    """
