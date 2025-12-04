from declusor import interface, util, command


async def call_shell(session: interface.ISession, router: interface.IRouter, line: str) -> None:
    """Open an interactive shell session with the target device."""

    util.parse_command_arguments(line, {})

    await command.LaunchShell().execute(session)
