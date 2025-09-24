from os import chdir
from os.path import exists, isdir

import config
from infra import PromptCLI, Session, Router
from route import set_routes
from util import await_connection, format_client_bash_code


def run_service(host: str, port: int, client: str) -> None:
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
        session = Session(connection, config.SRV_ACK, config.CLT_ACK)

        prompt = PromptCLI(router, session)
        prompt.run()


def handle_exception(err: Exception | KeyboardInterrupt) -> None:
    exception_message_table = {
        FileNotFoundError: "file or directory not found: {}".format(err),
        NotADirectoryError: "not a directory: {}".format(err),
        KeyboardInterrupt: "",
        SystemExit: str(err),
        OSError: str(err),
    }

    for exception_type, exception_message in exception_message_table.items():
        if exception_type is type(err):
            sysexit = SystemExit(exception_message)
            sysexit.code = 1

            raise sysexit

    raise err
