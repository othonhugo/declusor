from base64 import b64encode

from declusor.interface import IRouter, ISession
from declusor.util import format_bash_function_call, load_file_safely, parse_command_arguments, write_binary_message


async def call_execute(session: ISession, _: IRouter, line: str) -> None:
    """Execute a file on the remote system."""

    arguments, unknown_arguments = parse_command_arguments(line, {"filepath": str}, allow_unknown=True)

    if (file_content := load_file_safely(arguments["filepath"])) is None:
        return

    function_call = format_bash_function_call("execute_base64_encoded_value", b64encode(file_content).decode(), *unknown_arguments)

    await session.write(function_call.encode())

    async for data in session.read():
        write_binary_message(data)
