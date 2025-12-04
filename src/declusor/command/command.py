from declusor import interface


class ExecuteCommand(interface.ICommand):
    """Command to execute a raw command line on the target."""

    def __init__(self, command_line: str) -> None:
        """
        Initialize the ExecuteCommand.

        Args:
            command_line: The raw command line string to execute.
        """

        self._command_line = command_line.encode()

    async def execute(self, session: interface.ISession, /) -> None:
        """
        Execute the command on the session.

        Args:
            session: The active session to execute the command on.
        """

        await session.write(self._command_line)
