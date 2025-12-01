import unittest
from unittest.mock import MagicMock

from declusor.controller.exit import call_exit


class TestExitController(unittest.IsolatedAsyncioTestCase):
    async def test_exit_raises_system_exit(self) -> None:
        """Test that calling exit raises SystemExit."""

        with self.assertRaises(SystemExit):
            await call_exit(MagicMock(), MagicMock(), "")
