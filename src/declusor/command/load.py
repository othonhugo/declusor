from pathlib import Path

from declusor import config, interface, util


class LoadPayload(interface.ICommand):
    """Command to load a payload file onto the target."""

    def __init__(self, filepath: str | Path) -> None:
        """
        Initialize the LoadPayload command.

        Args:
            filepath: Path to the payload file.
        """

        self._filepath = util.ensure_file_exists(filepath)

    async def execute(self, session: interface.ISession, /) -> None:
        """
        Execute the load payload command.

        Args:
            session: The active session.

        Raises:
            InvalidOperation: If the file content cannot be loaded.
        """

        if (file_content := util.try_load_file(self._filepath)) is None:
            raise config.InvalidOperation(f"failed to load file content: {self._filepath!r}")

        await session.write(file_content)
