import asyncio
from os import chdir
from os.path import exists, isdir

from declusor import config, controller
from declusor.core import PromptCLI, Router, Session
from declusor.interface import IRouter
from declusor.util import format_client_bash_code


def set_routes(router: IRouter) -> None:
    """Set up the routes for the router."""

    router.connect("load", controller.call_load)
    router.connect("command", controller.call_command)
    router.connect("shell", controller.call_shell)
    router.connect("upload", controller.call_upload)
    router.connect("execute", controller.call_execute)
    router.connect("help", controller.call_help)
    router.connect("exit", controller.call_exit)


async def run_service(host: str, port: int, client: str) -> None:
    """Run the main service loop."""

    directories = [config.CLIENTS_DIR, config.SCRIPTS_DIR, config.LIBRARY_DIR]

    set_routes(router := Router())

    for directory in directories:
        if exists(directory):
            if not isdir(directory):
                raise NotADirectoryError(directory)
        else:
            raise FileNotFoundError(config.CLIENTS_DIR)

    chdir(config.SCRIPTS_DIR)
    config.set_line_completer(*router.routes)

    print(format_client_bash_code(client, HOST=host, PORT=port))

    first_session_future: asyncio.Future[Session] = asyncio.Future()

    async def client_handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        session = Session(reader, writer, config.DEFAULT_SRV_ACK, config.DEFAULT_CLT_ACK)
        await session.initialize()

        if not first_session_future.done():
            first_session_future.set_result(session)

        try:
            await session.writer.wait_closed()
        except Exception:
            pass

    server = await asyncio.start_server(client_handler, host, port)

    async with server:
        # Wait for the first session to connect
        session = await first_session_future

        prompt = PromptCLI(router, session)
        await prompt.run()
