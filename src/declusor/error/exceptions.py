class DeclusorException(Exception):
    """Base exception for Declusor-related errors."""


class InvalidOperation(DeclusorException):
    """An internal operation cannot be performed for any reason."""

    def __init__(self, /, description: str) -> None:
        self.description = description

        super().__init__(f"invalid operation: {self.description}")


class ParserError(DeclusorException):
    """Error parsing command-line arguments."""


class RouterError(DeclusorException):
    """Route cannot be processed for any reason."""

    def __init__(self, /, route: str, *, description: str | None = None) -> None:
        self.route = route
        self.description = description

        super().__init__(f"invalid route: {self.route!r}")


class PromptError(DeclusorException):
    """User supplied argument cannot be processed for any reason."""

    def __init__(self, /, argument: str, *, description: str | None = None) -> None:
        self.argument = argument
        self.description = description

        super().__init__(f"invalid argument: {self.argument!r}")


class ControllerError(DeclusorException):
    """An error occurred in the controller."""

    def __init__(self, /, description: str) -> None:
        self.description = description

        super().__init__(f"controller error: {self.description}")


class ExitRequest(DeclusorException):
    """Request to exit the application."""
