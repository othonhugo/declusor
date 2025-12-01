import asyncio
from typing import AsyncGenerator

from declusor.interface import ISession
from declusor.util import load_library, write_warning_message


class Session(ISession):
    """
    Manages a session over an asyncio connection, handling reading and writing
    of data with specific acknowledgement (ACK) protocols.
    """

    DEFAULT_BUFSIZE = 4096
    DEFAULT_TIMEOUT = 0.75

    def __init__(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter, server_ack: bytes, client_ack: bytes) -> None:
        """
        Initialize the Session.

        Args:
            reader: The asyncio StreamReader.
            writer: The asyncio StreamWriter.
            server_ack: The byte sequence expected from the server to signal end of message.
            client_ack: The byte sequence sent to the client after writing data.
            timeout: Socket timeout in seconds.
        """

        self.reader = reader
        self.writer = writer
        self.server_ack = server_ack
        self.client_ack = client_ack

        self._timeout = self.DEFAULT_TIMEOUT

    async def initialize(self) -> None:
        """Perform initial handshake/setup."""

        try:
            await self.write(load_library())
            # Check for immediate response indicating failure
            try:
                # Wait for a short time to see if there's an error response
                initial_data = await asyncio.wait_for(self.reader.read(self.DEFAULT_BUFSIZE), timeout=0.1)
                if initial_data:
                    write_warning_message("the library import may have failed.")
            except asyncio.TimeoutError:
                pass  # No data means likely success in this context
        except Exception:
            # Log or handle initialization errors if necessary
            pass

    def set_timeout(self, value: float) -> None:
        """Set the timeout for socket operations."""

        self._timeout = value

    def read(self) -> AsyncGenerator[bytes, None]:
        """
        Read data from the connection until the server ACK is received.
        Yields chunks of data as they arrive, excluding the ACK.
        """

        async def _read_generator() -> AsyncGenerator[bytes, None]:
            buffer = bytearray()
            ack_len = len(self.server_ack)

            while True:
                try:
                    # Use wait_for to implement timeout
                    chunk = await asyncio.wait_for(self.reader.read(self.DEFAULT_BUFSIZE), timeout=self._timeout)

                    if not chunk:
                        raise ConnectionResetError("Connection closed by peer")

                    buffer.extend(chunk)

                    # Check if ACK is present in the buffer
                    search_start = max(0, len(buffer) - len(chunk) - ack_len)
                    ack_index = buffer.find(self.server_ack, search_start)

                    if ack_index != -1:
                        # ACK found. Yield data up to ACK and stop.
                        yield bytes(buffer[:ack_index])
                        break

                    # If buffer is larger than ACK length, we can safely yield the beginning
                    if len(buffer) > ack_len:
                        safe_len = len(buffer) - ack_len

                        yield bytes(buffer[:safe_len])
                        del buffer[:safe_len]

                except asyncio.TimeoutError:
                    continue

        return _read_generator()

    async def write(self, content: bytes) -> None:
        """
        Write data to the connection followed by the client ACK.

        Args:
            content: The bytes to send.
        """

        try:
            payload = content + self.client_ack
            self.writer.write(payload)

            await self.writer.drain()
        except OSError as e:
            raise ConnectionError(f"Failed to write to connection: {e}") from e
