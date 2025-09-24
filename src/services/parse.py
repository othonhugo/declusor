import shlex
from argparse import ArgumentParser
from typing import NoReturn

from config import ArgumentParsingError


class DeclusorArgumentParser(ArgumentParser):
    """
    A custom ArgumentParser that raises ArgumentParsingError on parsing errors.

    This class overrides the default error handling of ArgumentParser to raise
    a custom exception instead of exiting the program, allowing for more flexible
    error management in the calling code.
    """

    def error(self, message: str) -> NoReturn:
        """Overrides the default error method to raise a custom exception."""

        raise ArgumentParsingError(message)


def parse_command_arguments(
    line: str,
    arg_definitions: dict[str, type],
    allow_unknown: bool = False
) -> tuple[dict[str, str], list[str]]:
    """
    Parses a string of command-line-like arguments using a custom ArgumentParser.

    This function takes a string, splits it into arguments using shlex, and then
    parses these arguments based on the provided argument definitions. It allows
    for custom error handling by raising `ArgumentParsingError`.
    """

    if not arg_definitions and not line.strip():
        return {}, []

    parser = DeclusorArgumentParser(add_help=False, exit_on_error=False)

    for arg_name, arg_type in arg_definitions.items():
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
