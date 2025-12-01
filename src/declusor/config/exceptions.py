class DeclusorException(Exception):
    """Base exception for declusor-related errors."""


class ArgumentParsingError(DeclusorException):
    """Error parsing command-line arguments."""


class InvalidRoute(DeclusorException):
    """Route cannot be processed for any reason."""

    def __init__(self, route: str) -> None:
        super().__init__(f"invalid route: {route}")


class InvalidArgument(DeclusorException):
    """Argument cannot be processed for any reason."""

    def __init__(self, message: str) -> None:
        super().__init__(f"invalid argument: {message}")
