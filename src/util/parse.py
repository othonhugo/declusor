import shlex
from argparse import ArgumentParser
from typing import NoReturn

from config import ArgumentParsingError


class DeclusorArgumentParser(ArgumentParser):
    """Custom ArgumentParser that raises ArgumentParsingError on errors."""

    def error(self, message: str) -> NoReturn:
        """Overrides the default error method to raise a custom exception."""

        raise ArgumentParsingError(message)


def parse_command_arguments(
    line: str, definitions: dict[str, type], allow_unknown: bool = False
) -> tuple[dict[str, str], list[str]]:
    """Parses command arguments from a string based on provided definitions."""

    if not definitions and not line.strip():
        return {}, []

    parser = DeclusorArgumentParser(add_help=False, exit_on_error=False)

    for arg_name, arg_type in definitions.items():
        if arg_type not in [str, int]:
            raise TypeError(f"Argument type {arg_type!r} for {arg_name!r} is not supported.")

        parser.add_argument(arg_name, type=arg_type)

    parser_args_list = shlex.split(line)

    if allow_unknown:
        parsed_namespace, unknown_arguments = parser.parse_known_args(parser_args_list)
    else:
        parsed_namespace = parser.parse_args(parser_args_list)
        unknown_arguments = []

    parsed_arguments = {k: v for k, v in vars(parsed_namespace).items()}

    return parsed_arguments, unknown_arguments
