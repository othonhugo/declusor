import asyncio

from declusor.config import DeclusorException
from declusor.interface import IPrompt, IRouter, ISession
from declusor.util import read_message, write_error_message
from declusor.version import PROJECT_NAME


class PromptCLI(IPrompt):
    """CLI prompt implementation."""

    prompt = f"[{PROJECT_NAME}] "

    def __init__(self, router: IRouter, session: ISession) -> None:
        self.router = router
        self.session = session

    async def read_command(self) -> str:
        """Read command from user input."""

        while not (command := await asyncio.to_thread(read_message, self.prompt)):
            continue

        return command

    async def handle_route(self, command: str) -> None:
        """Handle routing based on user command."""

        match command.split(" ", 1):
            case [route, argument]:
                await self.router.locate(route)(self.session, self.router, argument.strip())
            case [route]:
                await self.router.locate(route)(self.session, self.router, "")
            case _:
                write_error_message(command)

    async def run(self) -> None:
        """Run the CLI prompt loop."""

        while True:
            try:
                await self.handle_route(await self.read_command())
            except DeclusorException as err:
                write_error_message(str(err))
