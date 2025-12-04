from declusor import command, core, interface, util


async def call_upload(session: interface.ISession, router: interface.IRouter, line: str) -> None:
    """Upload a file from the local system to the remote system."""

    arguments, _ = util.parse_command_arguments(line, {"filepath": str})
    filepath = util.ensure_file_exists(arguments["filepath"])

    await command.UploadFile(filepath).execute(session)

    async for data in session.read():
        core.console.write_binary_data(data)
