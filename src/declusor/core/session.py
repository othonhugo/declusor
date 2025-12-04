import asyncio
from typing import AsyncGenerator

from declusor import config, interface, util
from declusor.core.console import console


class Session(interface.ISession):
    """Manages a session over an asyncio connection, handling reading and writing of data."""

    _DEFAULT_CLIENT_ACKNOWLEDGE = b"\x00"
    _DEFAULT_SERVER_ACKNOWLEDGE = config.DEFAULT_ACK_VALUE
    _DEFAULT_BUFFER_SIZE = 4096
    _DEFAULT_TIMEOUT = 0.75

    def __init__(
        self,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
        /,
        *,
        timeout: float = _DEFAULT_TIMEOUT,
        bufsize: int = _DEFAULT_BUFFER_SIZE,
    ) -> None:
        """
        Initialize the Session.

        Args:
            reader: The asyncio StreamReader.
            writer: The asyncio StreamWriter.
            timeout: Socket timeout in seconds.
            bufsize: Buffer size for reading data in bytes.
        """

        self.reader = reader
        self.writer = writer

        self._timeout = timeout
        self._bufsize = bufsize

    async def initialize(self) -> None:
        """Perform initial handshake/setup."""

        try:
            await self.write(util.load_library())

            try:
                initial_data = await asyncio.wait_for(self.reader.read(self._bufsize), timeout=self._timeout)

                if initial_data != self._DEFAULT_SERVER_ACKNOWLEDGE:
                    console.write_warning_message("the library import may have failed.")
            except asyncio.TimeoutError:
                pass
        except Exception:
            pass

    def set_timeout(self, value: float, /) -> None:
        """Set the timeout for socket operations."""

        self._timeout = value

    def read(self) -> AsyncGenerator[bytes, None]:
        """Read data from the connection until the server ACK is received. Yields chunks of data as they arrive, excluding the ACK."""

        async def _read_generator() -> AsyncGenerator[bytes, None]:
            buffer = bytearray()
            ack_len = len(self._DEFAULT_SERVER_ACKNOWLEDGE)

            while True:
                try:
                    chunk = await asyncio.wait_for(self.reader.read(self._bufsize), timeout=self._timeout)

                    if not chunk:
                        raise ConnectionResetError("Connection closed by peer")

                    buffer.extend(chunk)

                    search_start = max(0, len(buffer) - len(chunk) - ack_len)
                    ack_index = buffer.find(self._DEFAULT_SERVER_ACKNOWLEDGE, search_start)

                    if ack_index != -1:
                        yield bytes(buffer[:ack_index])
                        break

                    if len(buffer) > ack_len:
                        safe_len = len(buffer) - ack_len

                        yield bytes(buffer[:safe_len])
                        del buffer[:safe_len]

                except asyncio.TimeoutError:
                    continue

        return _read_generator()

    async def write(self, content: bytes, /) -> None:
        """
        Write data to the connection followed by the client ACK.

        Args:
            content: The bytes to send.
        """

        try:
            self.writer.write(content)
            self.writer.write(self._DEFAULT_CLIENT_ACKNOWLEDGE)

            await self.writer.drain()
        except OSError as e:
            raise ConnectionError(f"Failed to write to connection: {e}") from e
