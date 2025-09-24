from os import chdir
from os.path import exists, isdir

import config
import controller
from core import PromptCLI, Router, Session
from util import await_connection, format_client_bash_code
from interface import IRouter


def set_routes(router: IRouter) -> None:
    """Set up the routes for the router."""

    router.connect("load", controller.call_load)
    router.connect("command", controller.call_command)
    router.connect("shell", controller.call_shell)
    router.connect("upload", controller.call_upload)
    router.connect("execute", controller.call_execute)
    router.connect("help", controller.call_help)
    router.connect("exit", controller.call_exit)


def run_service(host: str, port: int, client: str) -> None:
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

    with await_connection(host, port) as connection:
        session = Session(connection, config.DEFAULT_SRV_ACK, config.DEFAULT_CLT_ACK)

        prompt = PromptCLI(router, session)
        prompt.run()
