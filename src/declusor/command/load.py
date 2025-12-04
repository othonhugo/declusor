from declusor import interface, util, error

from pathlib import Path


class LoadPayload(interface.ICommand):
    def __init__(self, filepath: str | Path) -> None:
        self._filepath = util.ensure_file_exists(filepath)

    async def execute(self, session: interface.ISession, /) -> None:
        if (file_content := util.try_load_file(self._filepath)) is None:
            raise error.InvalidOperation(f"failed to load file content: {self._filepath!r}")

        await session.write(file_content)
