from interface import IRouter, ISession
from util import parse_command_arguments, write_binary_message


def call_command(session: ISession, router: IRouter, line: str) -> None:
    """Execute a command on the remote system."""

    arguments, _ = parse_command_arguments(line, {"command": str})

    session.write(arguments["command"].encode())

    for data in session.read():
        write_binary_message(data)
