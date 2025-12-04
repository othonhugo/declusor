import asyncio
import sys


class Console:
    """A robust and modular console handler for asynchronous I/O."""

    def __init__(self) -> None:
        pass

    async def read_line(self, prompt: str = "") -> str:
        """Read a line from standard input asynchronously using a thread executor.

        Args:
            prompt: The prompt to display to the user.

        Returns:
            The input string.
        """

        return await asyncio.to_thread(input, prompt)

    async def read_stripped_line(self, prompt: str = "") -> str:
        """Read a line from standard input asynchronously and strip whitespace.

        Args:
            prompt: The prompt to display to the user.

        Returns:
            The stripped input string.
        """

        return (await self.read_line(prompt)).strip()

    async def write_message(self, message: str) -> None:
        """
        Write a message to standard output.

        Args:
            message: The message string to write.
        """

        sys.stdout.write(message + "\n")
        sys.stdout.flush()

    async def write_binary_data(self, message: bytes) -> None:
        """
        Write a binary message to standard output.

        Args:
            message: The binary data to write.
        """

        sys.stdout.buffer.write(message)
        sys.stdout.buffer.flush()

    async def write_error_message(self, message: str | BaseException) -> None:
        """
        Write an error message to standard error.

        Args:
            message: The error message or exception to write.
        """

        sys.stderr.write(f"error: {message}\n")
        sys.stderr.flush()

    async def write_warning_message(self, message: str | BaseException) -> None:
        """
        Write a warning message to standard error.

        Args:
            message: The warning message or exception to write.
        """

        sys.stderr.write(f"warning: {message}\n")
        sys.stderr.flush()


console = Console()
"""Global instance for easy access."""
