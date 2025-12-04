import sys


def read_stripped_message(prompt: str = "") -> str:
    """
    Read a message from standard input and strip whitespace.

    Args:
        prompt: The prompt to display to the user.

    Returns:
        The input string with leading and trailing whitespace removed.
    """

    return input(prompt).strip()


def write_string_message(message: str) -> None:
    """
    Write a message to standard output.

    Args:
        message: The message string to write.
    """

    sys.stdout.write(message + "\n")
    sys.stdout.flush()


def write_binary_data(message: bytes) -> None:
    """
    Write a binary message to standard output.

    Args:
        message: The binary data to write.
    """

    sys.stdout.buffer.write(message)
    sys.stdout.buffer.flush()


def write_error_message(message: str | BaseException) -> None:
    """
    Write an error message to standard error.

    Args:
        message: The error message or exception to write.
    """

    sys.stderr.write(f"error: {message}\n")
    sys.stderr.flush()


def write_warning_message(message: str | BaseException) -> None:
    """
    Write a warning message to standard error.

    Args:
        message: The warning message or exception to write.
    """

    sys.stderr.write(f"warning: {message}\n")
    sys.stderr.flush()
