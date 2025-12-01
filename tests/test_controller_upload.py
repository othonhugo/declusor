import unittest
from typing import AsyncGenerator
from unittest.mock import AsyncMock, MagicMock, patch

from declusor.controller.upload import call_upload


class TestUploadController(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.mock_session = AsyncMock()
        self.mock_router = MagicMock()

    @patch("declusor.controller.upload.write_binary_message")
    @patch("declusor.controller.upload.format_bash_function_call")
    @patch("declusor.controller.upload.load_file_safely")
    @patch("declusor.controller.upload.parse_command_arguments")
    async def test_upload_success(self, mock_parse: MagicMock, mock_load: MagicMock, mock_format: MagicMock, mock_write_bin: MagicMock) -> None:
        """Test successful file upload with base64 encoding."""

        # Setup
        mock_parse.return_value = ({"filepath": "local_file.txt"}, [])
        mock_load.return_value = b"file_content"
        mock_format.return_value = "bash_command"

        async def mock_read() -> AsyncGenerator[bytes, None]:
            yield b"response"

        self.mock_session.read = mock_read

        # Execute
        await call_upload(self.mock_session, self.mock_router, "local_file.txt")

        # Verify
        mock_load.assert_called_with("local_file.txt")
        mock_format.assert_called_with("store_base64_encoded_value", "ZmlsZV9jb250ZW50")

        self.mock_session.write.assert_called_with(b"bash_command")

        mock_write_bin.assert_called_with(b"response")

    @patch("declusor.controller.upload.load_file_safely")
    @patch("declusor.controller.upload.parse_command_arguments")
    async def test_upload_invalid_argument(self, mock_parse: MagicMock, mock_load: MagicMock) -> None:
        """Test that upload handles missing files gracefully."""

        # Setup
        mock_parse.return_value = ({"filepath": "missing.txt"}, [])
        mock_load.return_value = None

        # Execute
        await call_upload(self.mock_session, self.mock_router, "missing.txt")

        # Verify
        mock_load.assert_called_with("missing.txt")
        self.mock_session.write.assert_not_called()
