from base64 import b64encode

from declusor.interface import IRouter, ISession
from declusor.util import format_bash_function_call, load_file_safely, parse_command_arguments, write_binary_message


async def call_upload(session: ISession, router: IRouter, line: str) -> None:
    """Uploads a file to the target machine."""

    arguments, _ = parse_command_arguments(line, {"filepath": str})

    if (file_content := load_file_safely(arguments["filepath"])) is None:
        return

    function_call = format_bash_function_call("store_base64_encoded_value", b64encode(file_content).decode())

    await session.write(function_call.encode())

    async for data in session.read():
        write_binary_message(data)
