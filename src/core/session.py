from select import select
from socket import socket
from typing import Generator

from interface import ISession
from util import load_library, write_warninig_message


class Session(ISession):
    bufsize = 64

    def __init__(
        self, connection: socket, server_ack: bytes, client_ack: bytes
    ) -> None:

        self.connection = connection
        self.server_ack = server_ack
        self.client_ack = client_ack
        self.timeout = 0.75

        self.write(load_library())

        if b"".join(self.read()):
            write_warninig_message("the library import may have failed.")

    def set_blocking(self, flag: bool) -> None:
        self.connection.setblocking(flag)

    def set_timeout(self, value: float) -> None:
        self.connection.settimeout(value)

    def read_all(self, bufsize: int = bufsize) -> Generator[bytes, None, None]:
        """Read and yield all data until the connection is closed."""

        while True:
            readable = select([self.connection], [], [], self.timeout)[0]

            if not readable:
                yield b""

            for _ in readable:
                if data := self.connection.recv(bufsize):
                    yield data
                else:
                    raise ConnectionResetError

    def read(self) -> Generator[bytes, None, None]:
        """Read and yield data until the server ACK is received."""

        buffer = b""

        for data in self.read_all():
            # append data to a reduced size buffer
            buffer = buffer[len(buffer) - len(self.server_ack):] + data

            # assign the index value of where the ACK could be
            ack_index = len(buffer) - len(self.server_ack)

            # check if the ACK reply was received
            if flag := buffer[ack_index:] == self.server_ack:
                # assign the index value of where the data is stored
                buffer_data_index = len(buffer) - len(data)

                # reassign data value without ACK response
                data = buffer[buffer_data_index: -len(self.server_ack)]

            yield data

            if flag:
                break

    def write(self, content: bytes) -> None:
        """Write/send data to session connection."""

        self.connection.send(content)
        self.connection.send(self.client_ack)
