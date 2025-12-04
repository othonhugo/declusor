from declusor import command, core, interface, util


async def call_load(session: interface.ISession, router: interface.IRouter, line: str) -> None:
    """Load a payload file from your local system and execute it on the remote system"""

    arguments, _ = util.parse_command_arguments(line, {"filepath": str})
    filepath = util.ensure_file_exists(arguments["filepath"])

    await command.LoadPayload(filepath).execute(session)

    async for data in session.read():
        core.console.write_binary_data(data)
