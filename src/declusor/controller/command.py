from declusor import command, interface, util


async def call_command(session: interface.ISession, router: interface.IRouter, line: str) -> None:
    """Execute a single command on the remote system."""

    arguments, _ = util.parse_command_arguments(line, {"command": str})
    command_line = arguments["command"]

    await command.ExecuteCommand(command_line).execute(session)

    async for data in session.read():
        util.write_binary_data(data)
