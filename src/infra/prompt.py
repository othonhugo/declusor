from config import DeclusorException
from interfaces import IPrompt, IRouter, ISession
from util import read_message, write_error_message


class PromptCLI(IPrompt):
    prompt = "[declusor] "

    def __init__(self, router: IRouter, session: ISession) -> None:
        self.router = router
        self.session = session

        self.session.set_blocking(True)

    def read_command(self) -> str:
        while not (command := read_message(self.prompt)):
            continue

        return command

    def handle_route(self, command: str) -> None:
        match command.split(" ", 1):
            case [route, argument]:
                self.router.locate(route)(
                    self.session, self.router, argument.strip()
                )
            case [route]:
                self.router.locate(route)(self.session, self.router, "")
            case _:
                write_error_message(command)

    def run(self) -> None:
        while True:
            try:
                self.handle_route(self.read_command())
            except DeclusorException as err:
                write_error_message(str(err))
