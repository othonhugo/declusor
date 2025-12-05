"""Tests for declusor.util.network module.

This module tests network utilities including:
- await_connection: Context manager for accepting socket connections
- _handle_socket_exception: Exception handling for socket errors
"""

import socket

import pytest

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def available_port() -> int:
    """Find and return an available port for testing."""


@pytest.fixture
def mock_socket(monkeypatch: pytest.MonkeyPatch):
    """Mock socket.socket for controlled testing."""


# =============================================================================
# Tests: await_connection - Success cases
# =============================================================================


def test_await_connection_yields_socket(available_port: int) -> None:
    """
    Given: Valid host and available port
    When: await_connection is used as context manager and client connects
    Then: Yields a connected socket object
    """


def test_await_connection_sets_reuse_addr(mock_socket) -> None:
    """
    Given: await_connection is called
    When: Socket is created
    Then: SO_REUSEADDR option is set (to allow quick port reuse)
    """


def test_await_connection_listens_on_port(mock_socket) -> None:
    """
    Given: await_connection with host and port
    When: Context manager is entered
    Then: Socket binds to host:port and calls listen(1)
    """


def test_await_connection_cleans_up_on_exit(available_port: int) -> None:
    """
    Given: Connection established via await_connection
    When: Context manager exits (normal or exception)
    Then: Socket is properly closed
    """


# =============================================================================
# Tests: await_connection - Error handling
# =============================================================================


def test_await_connection_invalid_host_raises_system_exit() -> None:
    """
    Given: Invalid hostname like "invalid.host.name.xyz"
    When: await_connection is called
    Then: Raises SystemExit with "invalid address/hostname" message
    """


def test_await_connection_port_out_of_range_raises_system_exit() -> None:
    """
    Given: Port number outside valid range (e.g., 99999)
    When: await_connection is called
    Then: Raises SystemExit with "port must be 0-65535" message
    """


def test_await_connection_negative_port_raises_system_exit() -> None:
    """
    Given: Negative port number (e.g., -1)
    When: await_connection is called
    Then: Raises SystemExit with appropriate error message
    """


def test_await_connection_permission_denied_raises_system_exit() -> None:
    """
    Given: Privileged port (e.g., 80) without root permissions
    When: await_connection is called
    Then: Raises SystemExit with "permission denied" message
    """


def test_await_connection_port_already_in_use() -> None:
    """
    Given: Port that is already bound by another process
    When: await_connection is called
    Then: Raises appropriate error (OSError for address in use)
    """


# =============================================================================
# Tests: _handle_socket_exception - Exception mapping
# =============================================================================


def test_handle_socket_exception_gaierror() -> None:
    """
    Given: socket.gaierror exception
    When: _handle_socket_exception is called
    Then: Raises SystemExit with "invalid address/hostname" message
    """


def test_handle_socket_exception_overflow_error() -> None:
    """
    Given: OverflowError exception (port out of range)
    When: _handle_socket_exception is called
    Then: Raises SystemExit with "port must be 0-65535" message
    """


def test_handle_socket_exception_permission_error() -> None:
    """
    Given: PermissionError exception
    When: _handle_socket_exception is called
    Then: Raises SystemExit with "permission denied" message
    """


def test_handle_socket_exception_unknown_error_reraises() -> None:
    """
    Given: An unhandled exception type (e.g., ValueError)
    When: _handle_socket_exception is called
    Then: Re-raises the original exception unchanged
    """


def test_handle_socket_exception_preserves_exception_chain() -> None:
    """
    Given: An unhandled exception
    When: _handle_socket_exception re-raises
    Then: Exception is raised with 'from' clause preserving chain
    """


# =============================================================================
# Tests: await_connection - Edge cases
# =============================================================================


def test_await_connection_localhost_binding() -> None:
    """
    Given: host="127.0.0.1" and valid port
    When: await_connection is called
    Then: Successfully binds to localhost
    """


def test_await_connection_all_interfaces_binding() -> None:
    """
    Given: host="0.0.0.0" (all interfaces) and valid port
    When: await_connection is called
    Then: Successfully binds to all interfaces
    """


def test_await_connection_ipv6_disabled() -> None:
    """
    Given: await_connection uses AF_INET (IPv4 only)
    When: Binding attempted
    Then: Only IPv4 addresses are supported
    """


def test_await_connection_single_connection_only() -> None:
    """
    Given: listen backlog is 1
    When: Multiple clients try to connect
    Then: Only one connection is accepted and yielded
    """
