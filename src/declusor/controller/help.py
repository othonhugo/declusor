from typing import Callable, Optional

from declusor import interface, util

DocumentationProvider = Callable[[], str]
RouteUsageProvider = Callable[[str], str]


def create_help_controller(get_documentation: DocumentationProvider, get_route_usage: RouteUsageProvider) -> interface.Controller:
    """Create a help controller with documentation providers.

    Args:
        get_documentation: Function that returns full documentation.
        get_route_usage: Function that returns usage for a specific route.

    Returns:
        Help controller function.
    """

    async def call_help(session: interface.ISession, console: interface.IConsole, line: str) -> None:
        """Display detailed information about available commands or a specific command."""

        arguments, _ = util.parse_command_arguments(line, {"command": Optional[str]})

        if help_command := arguments["command"]:
            console.write_message(get_route_usage(help_command))
        else:
            console.write_message(get_documentation())

    return call_help
