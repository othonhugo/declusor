from interfaces import IRouter, ISession


def call_exit(session: ISession, router: IRouter, line: str) -> None:
    """Log out from the current terminal session"""

    raise SystemExit
