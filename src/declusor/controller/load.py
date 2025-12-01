from declusor.config import InvalidArgument
from declusor.interface import IRouter, ISession
from declusor.util import load_payload, parse_command_arguments, write_binary_message, write_error_message


async def call_load(session: ISession, router: IRouter, line: str) -> None:
    """Load a payload from a file and send it to the remote system."""

    arguments, _ = parse_command_arguments(line, {"payload": str})

    try:
        payload = load_payload(arguments["payload"])
    except InvalidArgument as err:
        write_error_message(err)
        return

    await session.write(payload)

    async for data in session.read():
        write_binary_message(data)
