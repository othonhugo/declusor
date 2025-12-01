import socket
from contextlib import contextmanager
from typing import Generator, Type


@contextmanager
def await_connection(host: str, port: int) -> Generator[socket.socket, None, None]:
    """Context manager that listens for incoming connections on a specified host and port."""

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
    """Handle socket-related exceptions and provide user-friendly error messages."""

    exception_message_table: dict[Type[BaseException], str] = {
        socket.gaierror: "invalid address/hostname.",
        OverflowError: "port must be 0-65535.",
        PermissionError: "permission denied.",
    }

    for exception_type, exception_message in exception_message_table.items():
        if isinstance(err, exception_type):
            raise SystemExit(exception_message)

    raise err from err
