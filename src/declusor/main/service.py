import asyncio
from os import chdir

from declusor import config, controller, core, interface, util, version


def set_routes(router: interface.IRouter) -> None:
    """Set up the routes for the router."""

    call_help = controller.create_help_controller(lambda: router.documentation, router.get_route_usage)

    router.connect("help", call_help)
    router.connect("load", controller.call_load)
    router.connect("command", controller.call_command)
    router.connect("shell", controller.call_shell)
    router.connect("upload", controller.call_upload)
    router.connect("execute", controller.call_execute)
    router.connect("exit", controller.call_exit)


async def run_service(options: config.DeclusorOptions, console: interface.IConsole) -> None:
    """Run the main service loop."""

    directories = [config.BasePath.CLIENTS_DIR, config.BasePath.MODULES_DIR, config.BasePath.LIBRARY_DIR]

    set_routes(router := core.Router())

    for directory in directories:
        if directory.exists():
            if not directory.is_dir():
                raise NotADirectoryError(directory)
        else:
            raise FileNotFoundError(config.BasePath.CLIENTS_DIR)

    chdir(config.BasePath.MODULES_DIR)
    console.setup_completer(router.routes)

    print(util.format_client_script(options["client"], HOST=options["host"], PORT=options["port"]))

    first_session_future: asyncio.Future[interface.ISession] = asyncio.Future()

    async def _client_handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        session = core.Session(reader, writer)

        try:
            await session.initialize()
        except config.DeclusorWarning as e:
            console.write_warning_message(e)

        if not first_session_future.done():
            first_session_future.set_result(session)

        try:
            await session.writer.wait_closed()
        except Exception:
            pass

    server = await asyncio.start_server(_client_handler, options["host"], options["port"])

    async with server:
        session = await first_session_future

        prompt = core.PromptCLI(version.PROJECT_NAME, router, session, console)

        await prompt.run()
