from declusor import error, interface
from declusor.core.console import console


class PromptCLI(interface.IPrompt):
    """CLI prompt implementation."""

    def __init__(self, name: str, router: interface.IRouter, session: interface.ISession) -> None:
        self._prompt = f"[{name}] "

        self._router = router
        self._session = session

    async def read_command(self) -> str:
        """Read command from user input."""

        while not (command := await console.read_stripped_line(self._prompt)):
            continue

        return command

    async def handle_route(self, command: str) -> None:
        """Handle routing based on user command."""

        match command.split(" ", 1):
            case [route, argument]:
                await self._router.locate(route)(self._session, self._router, argument.strip())
            case [route]:
                await self._router.locate(route)(self._session, self._router, "")
            case _:
                console.write_error_message(command)

    async def run(self) -> None:
        """Run the CLI prompt loop."""

        while True:
            try:
                await self.handle_route(await self.read_command())
            except (error.ExitRequest, KeyboardInterrupt):
                break
            except error.DeclusorException as e:
                console.write_error_message(str(e))
