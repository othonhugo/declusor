import unittest
from unittest.mock import MagicMock, patch

from declusor.controller.help import call_help


class TestHelpController(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.mock_session = MagicMock()
        self.mock_router = MagicMock()

    @patch("declusor.controller.help.write_message")
    async def test_help_no_args_shows_all_docs(self, mock_write: MagicMock) -> None:
        """Test that calling help with no arguments displays documentation for all commands."""

        self.mock_router.documentation = "All commands"

        await call_help(self.mock_session, self.mock_router, "")

        mock_write.assert_called_with("All commands")

    @patch("declusor.controller.help.write_message")
    async def test_help_with_arg_shows_specific_doc(self, mock_write: MagicMock) -> None:
        """Test that calling help with a specific command argument displays documentation for that command."""

        self.mock_router.get_controller_documentation.return_value = "Specific command"

        await call_help(self.mock_session, self.mock_router, "cmd")

        self.mock_router.get_controller_documentation.assert_called_with("cmd")
        mock_write.assert_called_with("Specific command")
