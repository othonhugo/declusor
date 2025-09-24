#!/usr/bin/env python3

from config import parse_opt
from main import run_service, handle_exception
from version import __version__, __description__, __name__


def main() -> None:
    opt = parse_opt(__name__, __description__, __version__)

    try:
        run_service(opt.host, opt.port, opt.client)
    except (Exception, KeyboardInterrupt) as err:
        handle_exception(err)


if __name__ == "__main__":
    main()
