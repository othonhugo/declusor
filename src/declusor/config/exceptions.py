class DeclusorException(Exception):
    """Base exception class for all Declusor-related errors.

    All custom exceptions in the Declusor application should inherit from this class
    to allow for centralized exception handling.
    """


class DeclusorWarning(Warning):
    """Base warning for Declusor-related warnings.

    Used to signal non-critical issues that don't prevent operation but should be brought to the user's attention.
    """

    def __init__(self, /, description: str) -> None:
        """Initialize the warning.

        Args:
            description: Human-readable description of the warning.
        """
        self.description = description

        super().__init__(self.description)


class InvalidOperation(DeclusorException):
    """Raised when an internal operation cannot be performed.

    This exception indicates that a requested operation is not valid
    in the current context or state of the application.
    """

    def __init__(self, /, description: str) -> None:
        """Initialize the exception.

        Args:
            description: Detailed explanation of why the operation is invalid.
        """
        self.description = description

        super().__init__(f"invalid operation: {self.description}")


class ParserError(DeclusorException):
    """Raised when command-line argument parsing fails.

    This exception is raised when the parser encounters invalid syntax,
    missing required arguments, or type conversion errors.
    """


class RouterError(DeclusorException):
    """Raised when a route cannot be processed.

    This exception indicates that a requested route is invalid, not found,
    or cannot be executed in the current context.
    """

    def __init__(self, /, route: str, *, description: str | None = None) -> None:
        """Initialize the exception.

        Args:
            route: The route that caused the error.
            description: Optional detailed explanation of the error.
        """
        self.route = route
        self.description = description

        super().__init__(f"invalid route: {self.route!r}")


class PromptError(DeclusorException):
    """Raised when a user-supplied argument cannot be processed.

    This exception is raised when user input is invalid, malformed,
    or cannot be processed by the command handler.
    """

    def __init__(self, /, argument: str, *, description: str | None = None) -> None:
        """Initialize the exception.

        Args:
            argument: The invalid argument that was provided.
            description: Optional detailed explanation of why the argument is invalid.
        """
        self.argument = argument
        self.description = description

        super().__init__(f"invalid argument: {self.argument!r}")


class ControllerError(DeclusorException):
    """Raised when an error occurs during controller execution.

    This exception indicates that a controller encountered an error
    while processing a command or performing an operation.
    """

    def __init__(self, /, description: str) -> None:
        """Initialize the exception.

        Args:
            description: Detailed explanation of the controller error.
        """
        self.description = description

        super().__init__(f"controller error: {self.description}")


class ExitRequest(DeclusorException):
    """Raised to signal a request to exit the application gracefully.

    This exception is used as a control flow mechanism to cleanly
    terminate the application when the user requests to exit.
    """
