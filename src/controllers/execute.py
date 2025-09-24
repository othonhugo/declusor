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


def call_execute(session: ISession, router: IRouter, line: str) -> None:
    """Upload and execute a file on the target host."""

    arguments, unknown_arguments = parse_command_arguments(
        line, {"filepath": str}, split=True, allow_unknown=True
    )

    try:
        file_content = load_file(arguments["filepath"])
    except InvalidArgument as err:
        write_error_message(str(err))
        return

    function_call = format_bash_function_call(
        "execute_base64_encoded_value",
        b64encode(file_content).decode(),
        *unknown_arguments,
    )

    session.write(function_call.encode())

    for data in session.read():
        write_binary_message(data)
