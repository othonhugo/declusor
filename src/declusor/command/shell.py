import asyncio
from asyncio import Event

from declusor import core, interface


class LaunchShell(interface.ICommand):
    """Command to launch an interactive shell session."""

    def __init__(self) -> None:
        """Initialize the LaunchShell command."""

        self._stop_event = Event()

    async def execute(self, session: interface.ISession, /) -> None:
        """
        Execute the interactive shell session.

        Args:
            session: The active session.
        """

        input_task = asyncio.create_task(self._handle_command_request(session))
        output_task = asyncio.create_task(self._handle_command_response(session))

        try:
            await asyncio.wait([input_task, output_task], return_when=asyncio.FIRST_COMPLETED)
        except (asyncio.CancelledError, KeyboardInterrupt):
            pass
        finally:
            self._stop_event.set()

            input_task.cancel()
            output_task.cancel()

            try:
                await input_task
            except asyncio.CancelledError:
                pass

            try:
                await output_task
            except asyncio.CancelledError:
                pass

    async def _handle_command_request(self, session: interface.ISession) -> None:
        """
        Handle reading commands from user input and sending them to the session.

        Args:
            session: The active session.
        """

        while not self._stop_event.is_set():
            try:
                command_request = await core.console.read_stripped_line()

                if command_request.strip():
                    await session.write(command_request.strip().encode())
            except EOFError:
                break

    async def _handle_command_response(self, session: interface.ISession) -> None:
        """
        Handle reading responses from the session and displaying them to the user.

        Args:
            session: The active session.
        """

        try:
            while not self._stop_event.is_set():
                async for data in session.read():
                    if self._stop_event.is_set():
                        break

                    if data:
                        core.console.write_binary_data(data)
        finally:
            self._stop_event.set()
