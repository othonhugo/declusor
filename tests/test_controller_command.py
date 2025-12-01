import unittest
from typing import AsyncGenerator
from unittest.mock import AsyncMock, MagicMock, patch

from declusor.controller.command import call_command


class TestCommandController(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.mock_session = AsyncMock()
        self.mock_router = MagicMock()

    @patch("declusor.controller.command.write_binary_message")
    @patch("declusor.controller.command.parse_command_arguments")
    async def test_command_execution(self, mock_parse: MagicMock, mock_write_bin: MagicMock) -> None:
        """Test that command execution sends command and reads output."""

        # Setup mocks
        mock_parse.return_value = ({"command": "ls -la"}, [])

        # Mock async generator for read
        async def _async_read() -> AsyncGenerator[bytes, None]:
            yield b"output line 1\n"
            yield b"output line 2\n"

        self.mock_session.read = MagicMock()
        self.mock_session.read.return_value = _async_read()

        # Execute
        await call_command(self.mock_session, self.mock_router, "ls -la")

        # Verify
        mock_parse.assert_called_with("ls -la", {"command": str})
        self.mock_session.write.assert_called_with(b"ls -la")

        self.assertEqual(mock_write_bin.call_count, 2)

        mock_write_bin.assert_any_call(b"output line 1\n")
        mock_write_bin.assert_any_call(b"output line 2\n")
