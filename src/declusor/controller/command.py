from declusor.interface import IRouter, ISession
from declusor.util import parse_command_arguments, write_binary_message


async def call_command(session: ISession, router: IRouter, line: str) -> None:
    """Execute a command on the remote system."""

    arguments, _ = parse_command_arguments(line, {"command": str})

    await session.write(arguments["command"].encode())

    async for data in session.read():
        write_binary_message(data)
