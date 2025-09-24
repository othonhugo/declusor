from interface import IRouter, ISession
from util import write_message


def call_help(session: ISession, router: IRouter, line: str) -> None:
    """Display help information about available commands."""

    if line:
        write_message(router.get_controller_documentation(line))
    else:
        write_message(router.documentation)
