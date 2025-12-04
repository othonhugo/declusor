import shlex
from argparse import ArgumentParser
from typing import Any, Mapping, Type

from declusor import config

ArgumentDefinitions = Mapping[str, Type[Any]]
"""The definitions: `argument name` -> `expected type`"""

ParsedArguments = dict[str, Any]
"""The parsed result: `argument name` -> `actual value`"""


def parse_command_arguments(line: str, definitions: ArgumentDefinitions, allow_unknown: bool = False) -> tuple[ParsedArguments, list[str]]:
    """
    Parses command arguments from a string based on provided definitions.

    Args:
        line: The command line string to parse.
        definitions: A mapping of argument names to their expected types (str or int).
        allow_unknown: If True, unknown arguments are returned instead of raising an error.

    Returns:
        A tuple containing:
            - dict of parsed arguments
            - list of unknown arguments (if allow_unknown=True)

    Raises:
        InvalidOperation: If an argument type is not supported or if there is a parsing error.
    """

    if not definitions and not line.strip():
        return {}, []

    parser = ArgumentParser(add_help=False, exit_on_error=False)

    for arg_name, arg_type in definitions.items():
        if arg_type not in {str, int}:
            raise config.InvalidOperation(f"Argument type {arg_type!r} for {arg_name!r} is not supported.")

        parser.add_argument(arg_name, type=arg_type)

    try:
        args_list = shlex.split(line)
    except ValueError as e:
        raise config.InvalidOperation(f"Parsing error: {e}") from e

    if allow_unknown:
        namespace, unrecognized_args = parser.parse_known_args(args_list)
    else:
        namespace = parser.parse_args(args_list)
        unrecognized_args = []

    parsed_args: dict[str, Any] = {}

    for k, v in vars(namespace).items():
        parsed_args[k] = v

    return parsed_args, unrecognized_args
