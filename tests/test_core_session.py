import asyncio
import unittest
from unittest.mock import AsyncMock, MagicMock, patch

from declusor.core.session import Session


class TestSession(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.mock_reader = AsyncMock(spec=asyncio.StreamReader)
        self.mock_writer = MagicMock(spec=asyncio.StreamWriter)

        # Mock drain to be awaitable
        self.mock_writer.drain = AsyncMock()

        self.server_ack = b"<ACK>"
        self.client_ack = b"<CLT>"

        self.session = Session(self.mock_reader, self.mock_writer, self.server_ack, self.client_ack)

    async def test_initialize_sends_library(self) -> None:
        """Test that initialization sends the library data."""

        with patch("declusor.core.session.load_library", return_value=b"init_data"):
            # Mock read to timeout or return nothing to simulate success
            self.mock_reader.read.side_effect = asyncio.TimeoutError

            await self.session.initialize()

            self.mock_writer.write.assert_called()
            self.mock_writer.drain.assert_awaited()

    async def test_write_sends_content_and_ack(self) -> None:
        """Test that write sends content followed by client ACK."""

        content = b"hello"

        await self.session.write(content)

        expected_payload = content + self.client_ack
        self.mock_writer.write.assert_called_with(expected_payload)
        self.mock_writer.drain.assert_awaited()

    async def test_read_yields_data_until_ack(self) -> None:
        """Test reading data that arrives in chunks, ending with ACK."""

        # Setup mock to return chunks
        # Chunk 1: "Hello "
        # Chunk 2: "World" + ACK
        self.mock_reader.read.side_effect = [b"Hello ", b"World" + self.server_ack, b""]

        received_chunks: list[bytes] = []

        async for chunk in self.session.read():
            received_chunks.append(chunk)

        full_data = b"".join(received_chunks)

        self.assertEqual(full_data, b"Hello World")

    async def test_read_handles_split_ack(self) -> None:
        """Test reading when the ACK is split across chunks."""

        # ACK is <ACK> (5 bytes)
        # Chunk 1: "Data" + "<AC"
        # Chunk 2: "K>"
        self.mock_reader.read.side_effect = [b"Data<AC", b"K>", b""]

        received_chunks: list[bytes] = []

        async for chunk in self.session.read():
            received_chunks.append(chunk)

        full_data = b"".join(received_chunks)

        self.assertEqual(full_data, b"Data")

    async def test_read_connection_closed(self) -> None:
        """Test that ConnectionResetError is raised if peer closes connection."""

        self.mock_reader.read.return_value = b""

        with self.assertRaises(ConnectionResetError):
            async for _ in self.session.read():
                pass
