from declusor import error, interface, util


class PromptCLI(interface.IPrompt):
    """CLI prompt implementation."""

    def __init__(self, name: str, router: interface.IRouter, session: interface.ISession) -> None:
        self._prompt = f"[{name}] "

        self._router = router
        self._session = session

    async def read_command(self) -> str:
        """Read command from user input."""

        while not (command := await util.read_stripped_line_async(self._prompt)):
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
                util.write_error_message(command)

    async def run(self) -> None:
        """Run the CLI prompt loop."""

        while True:
            try:
                await self.handle_route(await self.read_command())
            except (error.ExitRequest, KeyboardInterrupt):
                break
            except error.DeclusorException as e:
                util.write_error_message(str(e))
