from argparse import ArgumentParser, HelpFormatter
from typing import TYPE_CHECKING

from config.default import DEFAULT_CLIENT

if TYPE_CHECKING:
    from argparse import Namespace


def parse_opt(name: str, description: str, version: str) -> "Namespace":
    """Parse command-line arguments."""

    HELP = {
        "host": "IP address or hostname where the service should run",
        "port": "port number to listen on for incoming connections",
        "client": "agent responsible for handling requests"
    }

    parser = ArgumentParser(
        prog=name,
        description=f"{name} {version}: {description}",
        formatter_class=lambda prog: HelpFormatter(prog, max_help_position=30),
    )

    parser.add_argument("host", help=HELP["host"], type=str)
    parser.add_argument("port", help=HELP["port"], type=int)
    parser.add_argument(
        "-c", "--client", help=HELP["client"], type=str, default=DEFAULT_CLIENT
    )

    return parser.parse_args()
