"""Tests for declusor.controller.help module.

This module tests the help controller factory:
- create_help_controller: Factory that creates help controllers with injected documentation providers
"""

from typing import Callable
from unittest.mock import AsyncMock, MagicMock

import pytest

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def mock_session() -> AsyncMock:
    """Create a mock ISession."""


@pytest.fixture
def mock_console() -> MagicMock:
    """Create a mock IConsole for output verification."""


@pytest.fixture
def mock_get_documentation() -> Callable[[], str]:
    """Create a mock documentation provider."""


@pytest.fixture
def mock_get_route_usage() -> Callable[[str], str]:
    """Create a mock route usage provider."""


# =============================================================================
# Tests: create_help_controller - Factory function
# =============================================================================


def test_create_help_controller_returns_callable(mock_get_documentation: Callable[[], str], mock_get_route_usage: Callable[[str], str]) -> None:
    """
    Given: Documentation providers are provided
    When: create_help_controller is called
    Then: Returns a callable controller function
    """


def test_create_help_controller_returns_async_function(mock_get_documentation: Callable[[], str], mock_get_route_usage: Callable[[str], str]) -> None:
    """
    Given: Documentation providers are provided
    When: create_help_controller is called
    Then: Returns an async function
    """


# =============================================================================
# Tests: call_help - No arguments (global help)
# =============================================================================


@pytest.mark.asyncio
async def test_call_help_no_args_displays_all_commands(
    mock_session: AsyncMock, mock_console: MagicMock, mock_get_documentation: Callable[[], str], mock_get_route_usage: Callable[[str], str]
) -> None:
    """
    Given: call_help is called with empty line ""
    When: Controller executes
    Then: Displays full documentation (all commands)
    """


@pytest.mark.asyncio
async def test_call_help_no_args_writes_to_console(
    mock_session: AsyncMock, mock_console: MagicMock, mock_get_documentation: Callable[[], str], mock_get_route_usage: Callable[[str], str]
) -> None:
    """
    Given: call_help is called with empty line
    When: Documentation is retrieved
    Then: console.write_message is called with documentation
    """


# =============================================================================
# Tests: call_help - With command argument
# =============================================================================


@pytest.mark.asyncio
async def test_call_help_with_command_displays_specific_help(
    mock_session: AsyncMock, mock_console: MagicMock, mock_get_documentation: Callable[[], str], mock_get_route_usage: Callable[[str], str]
) -> None:
    """
    Given: call_help is called with line="load"
    When: Controller executes
    Then: Displays help for "load" command only
    """


@pytest.mark.asyncio
async def test_call_help_with_command_uses_get_route_usage(
    mock_session: AsyncMock, mock_console: MagicMock, mock_get_documentation: Callable[[], str], mock_get_route_usage: Callable[[str], str]
) -> None:
    """
    Given: call_help is called with line="shell"
    When: Controller executes
    Then: Calls get_route_usage("shell")
    """


@pytest.mark.asyncio
async def test_call_help_with_command_writes_usage_to_console(
    mock_session: AsyncMock, mock_console: MagicMock, mock_get_documentation: Callable[[], str], mock_get_route_usage: Callable[[str], str]
) -> None:
    """
    Given: call_help is called with line="load"
    When: Route usage is retrieved
    Then: console.write_message is called with the usage text
    """


# =============================================================================
# Tests: call_help - Argument parsing
# =============================================================================


@pytest.mark.asyncio
async def test_call_help_parses_optional_command_arg(
    mock_session: AsyncMock, mock_console: MagicMock, mock_get_documentation: Callable[[], str], mock_get_route_usage: Callable[[str], str]
) -> None:
    """
    Given: call_help uses parse_command_arguments with Optional[str]
    When: No argument provided
    Then: Uses get_documentation (command is None)
    """


@pytest.mark.asyncio
async def test_call_help_parses_provided_command_arg(
    mock_session: AsyncMock, mock_console: MagicMock, mock_get_documentation: Callable[[], str], mock_get_route_usage: Callable[[str], str]
) -> None:
    """
    Given: call_help is called with line="upload"
    When: Arguments are parsed
    Then: Uses get_route_usage with "upload"
    """


# =============================================================================
# Tests: call_help - Closure behavior
# =============================================================================


@pytest.mark.asyncio
async def test_call_help_uses_injected_documentation_provider(mock_session: AsyncMock, mock_console: MagicMock) -> None:
    """
    Given: create_help_controller is called with specific providers
    When: The returned controller is executed
    Then: Uses the injected documentation provider
    """


@pytest.mark.asyncio
async def test_call_help_uses_injected_route_usage_provider(mock_session: AsyncMock, mock_console: MagicMock) -> None:
    """
    Given: create_help_controller is called with specific providers
    When: The returned controller is executed with a command
    Then: Uses the injected route usage provider
    """
