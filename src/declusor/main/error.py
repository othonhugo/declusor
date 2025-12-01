from typing import Callable, Type


def handle_exception(err: BaseException) -> None:
    """Handle exceptions and exit the program with an appropriate message."""

    handler_table: dict[Type[BaseException], Callable[[BaseException], str]] = {
        FileNotFoundError: lambda e: f"file or directory not found: {e}",
        NotADirectoryError: lambda e: f"not a directory: {e}",
        KeyboardInterrupt: lambda e: "",
        SystemExit: str,
        OSError: str,
    }

    for exception_type, get_message in handler_table.items():
        if isinstance(err, exception_type):
            sysexit = SystemExit(get_message(err))
            sysexit.code = 1

            raise sysexit

    raise err from err
