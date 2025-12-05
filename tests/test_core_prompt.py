"""Tests for declusor.core.prompt module (PromptCLI class).

This module tests the CLI prompt loop including:
- PromptCLI: Main CLI prompt implementation
- read_command: Reading user commands
- handle_route: Dispatching commands to controllers
- run: Main event loop with exception handling
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def mock_router() -> MagicMock:
    """Create a mock IRouter with routes and locate method."""


@pytest.fixture
def mock_session() -> AsyncMock:
    """Create a mock ISession."""


@pytest.fixture
def mock_console(monkeypatch: pytest.MonkeyPatch) -> MagicMock:
    """Mock core.console for input/output control."""


@pytest.fixture
def prompt_cli(mock_router: MagicMock, mock_session: AsyncMock):
    """Create a PromptCLI instance with mocked dependencies."""


# =============================================================================
# Tests: PromptCLI initialization
# =============================================================================


def test_prompt_cli_init_sets_prompt_format() -> None:
    """
    Given: PromptCLI is created with name="myapp"
    When: __init__ is called
    Then: _prompt is set to "[myapp] "
    """


def test_prompt_cli_init_stores_router() -> None:
    """
    Given: PromptCLI is created with a router
    When: __init__ is called
    Then: _router attribute references the router
    """


def test_prompt_cli_init_stores_session() -> None:
    """
    Given: PromptCLI is created with a session
    When: __init__ is called
    Then: _session attribute references the session
    """


# =============================================================================
# Tests: PromptCLI.read_command
# =============================================================================


@pytest.mark.asyncio
async def test_prompt_cli_read_command_returns_input(mock_console: MagicMock) -> None:
    """
    Given: User enters "load file.sh"
    When: read_command() is called
    Then: Returns "load file.sh"
    """


@pytest.mark.asyncio
async def test_prompt_cli_read_command_skips_empty(mock_console: MagicMock) -> None:
    """
    Given: User enters empty lines then "exit"
    When: read_command() is called
    Then: Continues prompting until non-empty input received
    """


@pytest.mark.asyncio
async def test_prompt_cli_read_command_uses_prompt(mock_console: MagicMock) -> None:
    """
    Given: PromptCLI with name="declusor"
    When: read_command() is called
    Then: Displays "[declusor] " as prompt
    """


# =============================================================================
# Tests: PromptCLI.handle_route - Command parsing
# =============================================================================


@pytest.mark.asyncio
async def test_prompt_cli_handle_route_with_argument(mock_router: MagicMock) -> None:
    """
    Given: command="load myfile.sh"
    When: handle_route() is called
    Then: Locates "load" route and calls controller with "myfile.sh"
    """


@pytest.mark.asyncio
async def test_prompt_cli_handle_route_without_argument(mock_router: MagicMock) -> None:
    """
    Given: command="exit" (no argument)
    When: handle_route() is called
    Then: Locates "exit" route and calls controller with empty string
    """


@pytest.mark.asyncio
async def test_prompt_cli_handle_route_strips_argument(mock_router: MagicMock) -> None:
    """
    Given: command="load   file.sh  " (extra spaces)
    When: handle_route() is called
    Then: Argument is stripped to "file.sh"
    """


@pytest.mark.asyncio
async def test_prompt_cli_handle_route_passes_session_and_router(mock_router: MagicMock) -> None:
    """
    Given: Valid command
    When: handle_route() calls controller
    Then: Controller receives (session, router, argument)
    """


# =============================================================================
# Tests: PromptCLI.run - Main loop
# =============================================================================


@pytest.mark.asyncio
async def test_prompt_cli_run_loops_until_exit() -> None:
    """
    Given: PromptCLI.run() is started
    When: Multiple commands are entered
    Then: Continues prompting until exit condition
    """


@pytest.mark.asyncio
async def test_prompt_cli_run_exits_on_exit_request() -> None:
    """
    Given: Controller raises ExitRequest
    When: run() is executing
    Then: Loop breaks and run() returns normally
    """


@pytest.mark.asyncio
async def test_prompt_cli_run_exits_on_keyboard_interrupt() -> None:
    """
    Given: User presses Ctrl+C (KeyboardInterrupt)
    When: run() is executing
    Then: Loop breaks and run() returns normally
    """


@pytest.mark.asyncio
async def test_prompt_cli_run_catches_declusor_exception(mock_console: MagicMock) -> None:
    """
    Given: Controller raises DeclusorException (e.g., RouterError)
    When: run() is executing
    Then: Error is written to console, loop continues
    """


@pytest.mark.asyncio
async def test_prompt_cli_run_displays_error_message(mock_console: MagicMock) -> None:
    """
    Given: DeclusorException with message "invalid route"
    When: Exception is caught in run()
    Then: console.write_error_message("invalid route") is called
    """


# =============================================================================
# Tests: PromptCLI.handle_route - Error handling
# =============================================================================


@pytest.mark.asyncio
async def test_prompt_cli_handle_route_invalid_route(mock_router: MagicMock) -> None:
    """
    Given: command="unknown_command"
    When: handle_route() locates route
    Then: RouterError is raised (route not found)
    """


@pytest.mark.asyncio
async def test_prompt_cli_handle_route_empty_command(mock_console: MagicMock) -> None:
    """
    Given: Somehow empty command reaches handle_route
    When: Pattern matching occurs
    Then: Handles gracefully (should not happen in practice)
    """
