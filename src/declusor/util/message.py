import asyncio
import os
import sys


async def read_stripped_line_async(prompt: str = "") -> str:
    """
    Read a line from standard input asynchronously.

    Args:
        prompt: The prompt to display to the user.

    Returns:
        The input string.
    """

    if prompt:
        sys.stdout.write(prompt)
        sys.stdout.flush()

    loop = asyncio.get_running_loop()
    future: asyncio.Future[str] = loop.create_future()

    try:
        fd = sys.stdin.fileno()
    except (AttributeError, ValueError):
        return await asyncio.to_thread(sys.stdin.readline)

    def on_stdin() -> None:
        try:
            data = os.read(fd, 4096)

            if not data:
                if not future.done():
                    future.set_exception(EOFError())
                return

            if not future.done():
                future.set_result(data.decode())
        except Exception as e:
            if not future.done():
                future.set_exception(e)

    loop.add_reader(fd, on_stdin)

    try:
        return await future
    finally:
        loop.remove_reader(fd)


def read_stripped_line(prompt: str = "") -> str:
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
