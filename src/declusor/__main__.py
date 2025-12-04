import asyncio

from declusor import core, main, version

if __name__ == "__main__":
    opt = core.DeclusorParser(version.PROJECT_NAME, version.PROJECT_DESCRIPTION, version.__version__).parse()

    try:
        asyncio.run(main.run_service(opt["host"], opt["port"], opt["client"]))
    except Exception as e:
        main.handle_exception(e)
    except KeyboardInterrupt:
        pass
