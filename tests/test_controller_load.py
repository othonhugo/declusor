import unittest
from typing import AsyncGenerator
from unittest.mock import AsyncMock, MagicMock, patch

from declusor.config import InvalidArgument
from declusor.controller.load import call_load


class TestLoadController(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.mock_session = AsyncMock()
        self.mock_router = MagicMock()

    @patch("declusor.controller.load.write_error_message")
    @patch("declusor.controller.load.write_binary_message")
    @patch("declusor.controller.load.load_payload")
    @patch("declusor.controller.load.parse_command_arguments")
    async def test_load_success(self, mock_parse: MagicMock, mock_load: MagicMock, mock_write_bin: MagicMock, mock_error: MagicMock) -> None:
        """Test successful payload loading and execution."""

        # Setup
        mock_parse.return_value = ({"payload": "test_payload.sh"}, [])
        mock_load.return_value = b"payload_content"

        async def _mock_read() -> AsyncGenerator[bytes, None]:
            yield b"response"

        self.mock_session.read = _mock_read

        # Execute
        await call_load(self.mock_session, self.mock_router, "test_payload.sh")

        # Verify
        mock_parse.assert_called_with("test_payload.sh", {"payload": str})
        mock_load.assert_called_with("test_payload.sh")

        self.mock_session.write.assert_called_with(b"payload_content")

        mock_write_bin.assert_called_with(b"response")
        mock_error.assert_not_called()

    @patch("declusor.controller.load.write_error_message")
    @patch("declusor.controller.load.load_payload")
    @patch("declusor.controller.load.parse_command_arguments")
    async def test_load_invalid_argument(self, mock_parse: MagicMock, mock_load: MagicMock, mock_error: MagicMock) -> None:
        """Test that load handles invalid payload files with error messages."""

        # Setup
        mock_parse.return_value = ({"payload": "bad.sh"}, [])
        mock_load.side_effect = InvalidArgument("file not found")

        # Execute
        await call_load(self.mock_session, self.mock_router, "bad.sh")

        # Verify
        mock_error.assert_called()
        self.mock_session.write.assert_not_called()
