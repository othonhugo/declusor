"""Tests for declusor.controller.exit module.

This module tests the exit controller:
- call_exit: Controller that raises ExitRequest to terminate the application
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def mock_session() -> AsyncMock:
    """Create a mock ISession."""


@pytest.fixture
def mock_router() -> MagicMock:
    """Create a mock IRouter."""


# =============================================================================
# Tests: call_exit
# =============================================================================


@pytest.mark.asyncio
async def test_call_exit_raises_exit_request(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_exit is called
    When: Controller executes
    Then: Raises ExitRequest exception
    """


@pytest.mark.asyncio
async def test_call_exit_ignores_line_argument(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_exit is called with line="ignored args"
    When: Controller executes
    Then: Line argument is ignored, still raises ExitRequest
    """


@pytest.mark.asyncio
async def test_call_exit_does_not_interact_with_session(mock_session: AsyncMock, mock_router: MagicMock) -> None:
    """
    Given: call_exit is called
    When: Controller executes
    Then: session.read() and session.write() are NOT called
    """


@pytest.mark.asyncio
async def test_call_exit_exit_request_is_declusor_exception() -> None:
    """
    Given: ExitRequest is raised
    When: Checking exception type
    Then: ExitRequest is subclass of DeclusorException
    """
