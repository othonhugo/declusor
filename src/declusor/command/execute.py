from declusor import enums, interface, util

from pathlib import Path


class ExecuteFile(interface.ICommand):
    _FUNC_NAME = enums.ExecuteFunc.EXEC_FILE

    def __init__(self, filepath: str | Path, language: enums.Language = enums.Language.BASH) -> None:
        self._filepath = util.ensure_file_exists(filepath)
        self._language = language

    async def execute(self, session: interface.ISession, /) -> None:
        await session.write(self._command)

    @property
    def _command(self) -> bytes:
        file_content = util.load_file(self._filepath)
        file_base64 = util.convert_to_base64(file_content)

        return util.format_function_call(self._language, self._FUNC_NAME, file_base64).encode()
