def handle_exception(err: Exception | KeyboardInterrupt) -> None:
    """Handle exceptions and exit the program with an appropriate message."""

    exception_message_table = {
        FileNotFoundError: "file or directory not found: {}".format(err),
        NotADirectoryError: "not a directory: {}".format(err),
        KeyboardInterrupt: "",
        SystemExit: str(err),
        OSError: str(err),
    }

    for exception_type, exception_message in exception_message_table.items():
        if exception_type is type(err):
            sysexit = SystemExit(exception_message)
            sysexit.code = 1

            raise sysexit

    raise err
