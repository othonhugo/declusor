import shlex
from argparse import ArgumentParser, HelpFormatter
from typing import Any, Callable, Mapping, NoReturn, Type, Union, get_args, get_origin

from declusor import config

ArgumentDefinitions = Mapping[str, Type[Any] | Union[Any]]
"""The definitions: `argument name` -> `expected type`"""

ParsedArguments = dict[str, Any]
"""The parsed result: `argument name` -> `actual value`"""


class Parser(ArgumentParser):
    """Custom argument parser that extends argparse.ArgumentParser."""

    def __init__(
        self,
        /,
        prog: str | None = None,
        usage: str | None = None,
        description: str | None = None,
        add_help: bool = True,
    ) -> None:
        formatter_class = self.get_formatter_class()

        super().__init__(
            prog=prog,
            usage=usage,
            description=description,
            formatter_class=formatter_class,
            add_help=add_help,
        )

    def error(self, message: str) -> NoReturn:
        """Overrides the default ArgumentParser error behavior."""

        raise config.ParserError(message)

    def get_formatter_class(self) -> Callable[..., HelpFormatter]:
        """Subclasses can override this to customize help formatting."""

        return self._default_formatter_factory

    @staticmethod
    def _default_formatter_factory(*, prog: str) -> HelpFormatter:
        return HelpFormatter(prog, max_help_position=30)


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

    supported_types: set[Type[Any]] = {str, int}

    if not definitions and not line.strip():
        return {}, []

    parser = Parser(add_help=False)

    for arg_name, arg_type in definitions.items():
        origin, is_optional = get_origin(arg_type), False

        if origin is Union:
            origin_types = get_args(arg_type)

            if type(None) in origin_types:
                is_optional = True

                if actual_types := [a for a in origin_types if a is not type(None)]:
                    arg_type = actual_types[0]

        if arg_type not in supported_types:
            raise config.InvalidOperation(f"Argument type {arg_type!r} for {arg_name!r} is not supported.")

        kwargs: dict[str, Any] = {"type": arg_type}

        if is_optional:
            kwargs["nargs"] = "?"

        parser.add_argument(arg_name, **kwargs)

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
