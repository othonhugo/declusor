from declusor import interface, error


async def call_exit(session: interface.ISession, router: interface.IRouter, line: str) -> None:
    """Exit the program."""

    raise error.ExitRequest
