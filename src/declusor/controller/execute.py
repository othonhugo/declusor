from declusor import interface, util, command


async def call_execute(session: interface.ISession, router: interface.IRouter, line: str) -> None:
    """Execute a file on the remote system."""

    arguments, _ = util.parse_command_arguments(line, {"filepath": str})
    filepath = util.ensure_file_exists(arguments["filepath"])

    await command.ExecuteFile(filepath).execute(session)

    async for data in session.read():
        util.write_binary_data(data)
