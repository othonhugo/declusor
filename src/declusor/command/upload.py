from declusor import schema, interface, util

from pathlib import Path


class UploadFile(interface.ICommand):
    FUNCTION_NAME = schema.STORE_FILE_FUNCTION

    def __init__(self, filepath: str | Path, language: str = "bash") -> None:
        self._filepath = util.ensure_file_exists(filepath)
        self._language = language

    @property
    def command(self) -> bytes:
        file_content = util.load_file(self._filepath)
        file_base64 = util.convert_to_base64(file_content)

        return util.format_function_call(self._language, schema.STORE_FILE_FUNCTION, file_base64).encode()

    async def execute(self, session: interface.ISession) -> None:
        await session.write(self.command)
