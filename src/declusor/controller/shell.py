from declusor import command, interface, util


async def call_shell(session: interface.ISession, router: interface.IRouter, line: str) -> None:
    """Initiate an interactive shell session on the remote system."""

    util.parse_command_arguments(line, {})

    await command.LaunchShell().execute(session)
