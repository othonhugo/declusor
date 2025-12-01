import sys
from typing import Any


def read_message(prompt: Any = "") -> str:
    """Read a message from standard input and strip whitespace."""

    return input(prompt).strip()


def write_message(message: Any) -> None:
    """Write a message to standard output."""

    sys.stdout.write(str(message).lower() + "\n")
    sys.stdout.buffer.flush()


def write_binary_message(message: bytes) -> None:
    """Write a binary message to standard output."""

    sys.stdout.buffer.write(message)
    sys.stdout.buffer.flush()


def write_error_message(message: Any) -> None:
    """Write an error message to standard error."""

    sys.stderr.write(f"error: {str(message).lower()}\n")
    sys.stderr.flush()


def write_warning_message(message: Any) -> None:
    """Write a warning message to standard error."""

    sys.stderr.write(f"warning: {str(message).lower()}\n")
    sys.stderr.flush()
