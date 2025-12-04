import socket
from contextlib import contextmanager
from typing import Generator, Type


@contextmanager
def await_connection(host: str, port: int) -> Generator[socket.socket, None, None]:
    """
    Context manager that listens for incoming connections on a specified host and port.

    Args:
        host: The hostname or IP address to bind to.
        port: The port number to bind to.

    Yields:
        The connected socket object.

    Raises:
        SystemExit: If a socket error occurs (e.g., invalid address, port out of range, permission denied).
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((host, port))
            sock.listen(1)

            with sock.accept()[0] as connection:
                yield connection
        except Exception as err:
            _handle_socket_exception(err)


def _handle_socket_exception(err: Exception) -> None:
    """
    Handle socket-related exceptions and provide user-friendly error messages.

    Args:
        err: The exception that was raised.

    Raises:
        SystemExit: With a user-friendly error message if the exception is known.
        Exception: Re-raises the original exception if it is not handled.
    """

    exception_message_table: dict[Type[BaseException], str] = {
        socket.gaierror: "invalid address/hostname.",
        OverflowError: "port must be 0-65535.",
        PermissionError: "permission denied.",
    }

    for exception_type, exception_message in exception_message_table.items():
        if isinstance(err, exception_type):
            raise SystemExit(exception_message)

    raise err from err
