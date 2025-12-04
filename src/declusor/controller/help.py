from typing import Optional

from declusor import core, interface, util


async def call_help(session: interface.ISession, router: interface.IRouter, line: str) -> None:
    """Display detailed information about available commands or a specific command."""

    arguments, _ = util.parse_command_arguments(line, {"command": Optional[str]})

    if help_command := arguments["command"]:
        core.console.write_message(router.get_route_usage(help_command))
    else:
        core.console.write_message(router.documentation)
