from declusor.interface import IRouter, ISession


async def call_exit(session: ISession, router: IRouter, line: str) -> None:
    """Exit the program."""

    raise SystemExit
