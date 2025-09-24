from interface import IRouter, ISession


def call_exit(session: ISession, router: IRouter, line: str) -> None:
    """Exit the program."""

    raise SystemExit
