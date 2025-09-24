import socket
from contextlib import contextmanager
from typing import Generator


@contextmanager
def await_connection(
    host: str, port: int
) -> Generator[socket.socket, None, None]:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((host, port))
            sock.listen(1)

            with sock.accept()[0] as connection:
                yield connection
        except Exception as err:
            handle_socket_exception(err)


def handle_socket_exception(err: Exception) -> None:
    exception_message_table = {
        socket.gaierror: "invalid address/hostname.",
        OverflowError: "port must be 0-65535.",
        PermissionError: "permission denied.",
    }

    for exception_type, exception_message in exception_message_table.items():
        if exception_type is type(err):
            raise SystemExit(exception_message)

    raise err
