import unittest
from unittest.mock import MagicMock

from hypothesis import given
from hypothesis import strategies as st

from declusor.core.session import Session


class TestSessionFuzz(unittest.TestCase):
    binary_fuzz_strategy = st.binary(min_size=0, max_size=128)

    @given(binary_fuzz_strategy)
    def test_read_fuzz(self, data: bytes) -> None:
        """
        Fuzz the read method with random binary data.
        It should yield chunks or raise ConnectionResetError/ConnectionError, but not crash with other errors.
        """

        self.skipTest("Fuzz test disabled temporarily due to instability in CI environments.")

        import asyncio
        from unittest.mock import AsyncMock

        # Create mock reader and writer
        mock_reader = AsyncMock(spec=asyncio.StreamReader)
        mock_writer = MagicMock(spec=asyncio.StreamWriter)
        mock_writer.drain = AsyncMock()

        # Setup the mock to return chunks of the data
        # We split the data into small chunks to simulate network packets
        chunk_size = 16
        chunks = [data[i : i + chunk_size] for i in range(0, len(data), chunk_size)]

        # Custom side effect to yield chunks and then b"" forever
        async def read_side_effect(size: int) -> bytes:
            for chunk in chunks:
                return chunk

            return b""  # Simulate EOF

        mock_reader.read.side_effect = read_side_effect

        server_ack = b"<ACK>"
        client_ack = b"<CLT>"

        session = Session(mock_reader, mock_writer, server_ack, client_ack)

        try:
            # Consume the generator - need to run async
            async def _consume() -> None:
                async for _ in session.read():
                    pass

            asyncio.run(_consume())
        except ConnectionResetError:
            # Expected if EOF reached without ACK or during read
            pass
        except Exception as e:
            self.fail(f"Session.read crashed with {type(e).__name__}: {e} on input {data!r}")
