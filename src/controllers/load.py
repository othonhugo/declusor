from config import InvalidArgument
from interfaces import IRouter, ISession
from util import (
    load_payload,
    parse_command_arguments,
    write_binary_message,
    write_error_message,
)


def call_load(session: ISession, router: IRouter, line: str) -> None:
    """Load and execute a payload file on the target host."""

    arguments, _ = parse_command_arguments(line, {"payload": str})

    try:
        payload = load_payload(arguments["payload"])
    except InvalidArgument as err:
        write_error_message(str(err))
        return

    session.write(payload)

    for data in session.read():
        write_binary_message(data)
