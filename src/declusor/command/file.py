from pathlib import Path

from declusor import enums, interface, util


class _BaseFileCommand(interface.ICommand):
    """Base command for file operations (execution or upload)."""

    FUNC_NAME: enums.FileFunc = NotImplemented

    def __init__(self, filepath: str | Path, language: enums.Language = enums.Language.BASH) -> None:
        """
        Initialize the file command.

        Args:
            filepath: Path to the file to operate on.
            language: The language of the target environment.
        """

        self._filepath = util.ensure_file_exists(filepath)
        self._language = language

    async def execute(self, session: interface.ISession, /) -> None:
        """
        Execute the command on the session.

        Args:
            session: The active session.
        """

        await session.write(self._command)

    @property
    def _command(self) -> bytes:
        """
        Generate the encoded command bytes to send to the target.

        Returns:
            The base64 encoded command string ready for transmission.
        """

        file_content = util.load_file(self._filepath)
        file_base64 = util.convert_to_base64(file_content)

        return util.format_function_call(self._language, self.FUNC_NAME, file_base64).encode()


class ExecuteFile(_BaseFileCommand):
    """Command to execute a file on the target machine."""

    FUNC_NAME = enums.FileFunc.EXEC_FILE


class UploadFile(_BaseFileCommand):
    """Command to upload a file to the target machine."""

    FUNC_NAME = enums.FileFunc.STORE_FILE
