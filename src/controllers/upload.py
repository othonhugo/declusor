from base64 import b64encode

from config import InvalidArgument
from interfaces import IRouter, ISession
from util import (
    format_bash_function_call,
    load_file,
    parse_command_arguments,
    write_binary_message,
    write_error_message,
)


def call_upload(session: ISession, router: IRouter, line: str) -> None:
    """Upload a file to the target host."""

    arguments, _ = parse_command_arguments(line, {"filepath": str}, split=False)

    try:
        file_content = load_file(arguments["filepath"])
    except InvalidArgument as err:
        write_error_message(str(err))
        return

    function_call = format_bash_function_call(
        "store_base64_encoded_value", b64encode(file_content).decode()
    )

    session.write(function_call.encode())

    for data in session.read():
        write_binary_message(data)
