import asyncio
import unittest
from asyncio import Event
from typing import AsyncGenerator
from unittest.mock import AsyncMock, MagicMock, patch

from declusor.controller.shell import call_shell, handle_input_data, handle_socket_data
from declusor.interface import ISession


class TestShellController(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.mock_session = AsyncMock()
        self.mock_router = MagicMock()

    @patch("declusor.controller.shell.parse_command_arguments")
    async def test_call_shell_orchestration(self, mock_parse: MagicMock) -> None:
        """Test that call_shell orchestrates async tasks correctly."""

        # Setup
        mock_parse.return_value = ({}, [])

        # Mock session.read to return immediately
        async def _mock_read() -> AsyncGenerator[bytes, None]:
            yield b"test"

        self.mock_session.read = _mock_read

        # Create a task that will complete quickly
        async def _quick_task(session: ISession, stop_event: Event) -> None:
            await asyncio.sleep(0.01)

            stop_event.set()

        with patch("declusor.controller.shell.handle_input_data", side_effect=_quick_task):
            with patch("declusor.controller.shell.handle_socket_data", side_effect=_quick_task):
                # Execute with timeout to prevent hanging
                try:
                    await asyncio.wait_for(call_shell(self.mock_session, self.mock_router, ""), timeout=0.5)
                except asyncio.TimeoutError:
                    pass

        # Verify parse was called
        mock_parse.assert_called()

    @patch("declusor.controller.shell.read_message")
    async def test_handle_input_data(self, mock_read: MagicMock) -> None:
        """Test that handle_input_data reads and writes commands."""

        # Setup
        stop_event = Event()

        mock_read.return_value = "cmd1"

        # Run handle_input_data in a task and stop it after one iteration
        async def _run_with_timeout() -> None:
            task = asyncio.create_task(handle_input_data(self.mock_session, stop_event))

            await asyncio.sleep(0.05)  # Let it run one iteration

            stop_event.set()

            await asyncio.sleep(0.01)

            task.cancel()

            try:
                await task
            except asyncio.CancelledError:
                pass

        await _run_with_timeout()

        # Verify write was called
        self.mock_session.write.assert_called()

    @patch("declusor.controller.shell.write_binary_message")
    async def test_handle_socket_data(self, mock_write: MagicMock) -> None:
        """Test that handle_socket_data reads from socket and writes messages."""

        # Setup
        stop_event = Event()

        async def _mock_read() -> AsyncGenerator[bytes, None]:
            yield b"data1"
            stop_event.set()

        self.mock_session.read = _mock_read

        # Execute
        await handle_socket_data(self.mock_session, stop_event)

        # Verify
        mock_write.assert_any_call(b"data1")
