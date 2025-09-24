#!/usr/bin/env python3

from config import parse_opt
from main import run_service, handle_exception
from version import __version__, PROJECT_DESCRIPTION, PROJECT_NAME

if __name__ == "__main__":
    opt = parse_opt(PROJECT_NAME, PROJECT_DESCRIPTION, __version__)

    try:
        run_service(opt.host, opt.port, opt.client)
    except (Exception, KeyboardInterrupt) as err:
        handle_exception(err)
