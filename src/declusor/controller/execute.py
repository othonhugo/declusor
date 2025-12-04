from declusor import command, core, interface, util


async def call_execute(session: interface.ISession, router: interface.IRouter, line: str) -> None:
    """Execute a program or script from the local system on the remote system."""

    arguments, _ = util.parse_command_arguments(line, {"filepath": str})
    filepath = util.ensure_file_exists(arguments["filepath"])

    await command.ExecuteFile(filepath).execute(session)

    async for data in session.read():
        core.console.write_binary_data(data)
