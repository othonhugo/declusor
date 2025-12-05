"""Tests for declusor.core.router module (Router class).

This module tests the command router including:
- Router: Route table management and controller dispatch
- connect: Register routes to controllers
- locate: Find controller for a given route
- documentation: Generate help text for all routes
"""

from unittest.mock import AsyncMock

import pytest

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def router():
    """Create a fresh Router instance for testing."""


@pytest.fixture
def sample_controller() -> AsyncMock:
    """Create a sample async controller function with docstring."""


# =============================================================================
# Tests: Router initialization
# =============================================================================


def test_router_init_empty_route_table() -> None:
    """
    Given: Router is instantiated
    When: __init__ is called
    Then: route_table is empty dict
    """


# =============================================================================
# Tests: Router.routes property
# =============================================================================


def test_router_routes_returns_tuple() -> None:
    """
    Given: Router with registered routes
    When: routes property is accessed
    Then: Returns tuple of route names
    """


def test_router_routes_empty_router() -> None:
    """
    Given: Router with no registered routes
    When: routes property is accessed
    Then: Returns empty tuple ()
    """


def test_router_routes_preserves_order() -> None:
    """
    Given: Routes registered in order ["a", "b", "c"]
    When: routes property is accessed
    Then: Returns tuple in same order
    """


# =============================================================================
# Tests: Router.connect
# =============================================================================


def test_router_connect_registers_route(sample_controller: AsyncMock) -> None:
    """
    Given: Router with no routes
    When: connect("load", controller) is called
    Then: "load" route is registered in route_table
    """


def test_router_connect_strips_route_name(sample_controller: AsyncMock) -> None:
    """
    Given: connect(" load ", controller) with spaces
    When: Route is registered
    Then: Route name is stripped to "load"
    """


def test_router_connect_duplicate_raises(sample_controller: AsyncMock) -> None:
    """
    Given: Route "exit" already registered
    When: connect("exit", another_controller) is called
    Then: Raises ValueError "route already exists"
    """


def test_router_connect_multiple_routes(sample_controller: AsyncMock) -> None:
    """
    Given: Empty router
    When: Multiple routes are connected
    Then: All routes are registered correctly
    """


# =============================================================================
# Tests: Router.locate
# =============================================================================


def test_router_locate_returns_controller(sample_controller: AsyncMock) -> None:
    """
    Given: Route "shell" registered with controller
    When: locate("shell") is called
    Then: Returns the registered controller
    """


def test_router_locate_strips_route_name(sample_controller: AsyncMock) -> None:
    """
    Given: Route "shell" registered
    When: locate(" shell ") is called with spaces
    Then: Returns controller (route name stripped)
    """


def test_router_locate_not_found_raises() -> None:
    """
    Given: Route "unknown" not registered
    When: locate("unknown") is called
    Then: Raises RouterError with route name
    """


# =============================================================================
# Tests: Router.get_route_usage
# =============================================================================


def test_router_get_route_usage_returns_docstring(sample_controller: AsyncMock) -> None:
    """
    Given: Controller with docstring "Execute a command."
    When: get_route_usage("command") is called
    Then: Returns "Execute a command."
    """


def test_router_get_route_usage_joins_multiline(sample_controller: AsyncMock) -> None:
    """
    Given: Controller with multi-line docstring
    When: get_route_usage is called
    Then: Lines are joined with single space
    """


def test_router_get_route_usage_no_docstring() -> None:
    """
    Given: Controller with no docstring (None)
    When: get_route_usage is called
    Then: Returns empty string ""
    """


def test_router_get_route_usage_invalid_route() -> None:
    """
    Given: Route not registered
    When: get_route_usage("invalid") is called
    Then: Raises RouterError (calls locate internally)
    """


# =============================================================================
# Tests: Router.documentation property
# =============================================================================


def test_router_documentation_lists_all_routes(sample_controller: AsyncMock) -> None:
    """
    Given: Routes ["load", "shell", "exit"] registered
    When: documentation property is accessed
    Then: Returns formatted string with all routes
    """


def test_router_documentation_aligns_columns() -> None:
    """
    Given: Routes with different name lengths
    When: documentation is generated
    Then: Route names are left-padded for alignment
    """


def test_router_documentation_includes_descriptions(sample_controller: AsyncMock) -> None:
    """
    Given: Controllers with docstrings
    When: documentation is generated
    Then: Each route line includes its description
    """


def test_router_documentation_empty_router() -> None:
    """
    Given: Router with no routes
    When: documentation is accessed
    Then: Returns empty string or handles gracefully
    """


def test_router_documentation_strips_trailing_newline() -> None:
    """
    Given: Multiple routes registered
    When: documentation is generated
    Then: Result has no trailing newline (rstrip applied)
    """
