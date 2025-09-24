import sys

from os import scandir
from os.path import exists, isfile, join, splitext

from config import LIBRARY_DIR, SCRIPTS_DIR, InvalidArgument


def load_payload(module: str) -> bytes:
    """Load a payload script from the scripts directory."""

    if (extension := splitext(module)[1].casefold()) != ".sh":
        raise InvalidArgument(f"{extension!r} is not supported")

    module_filepath = join(SCRIPTS_DIR, module)

    if not exists(module_filepath):
        raise InvalidArgument(f"file not found: {module}")

    if not isfile(module_filepath):
        raise InvalidArgument(f"expecting a file: {module}")

    # # uncomment to restrict third-party payloads
    #
    # from os.path import commonpath
    # if commonpath([PAYLOAD_DIR, module_filepath]) != PAYLOAD_DIR:
    #     raise InvalidArgument(module)

    with open(module_filepath, "rb") as f:
        return f.read()


def load_library() -> bytes:
    """Load all library scripts from the library directory."""

    modules = []

    for file in scandir(LIBRARY_DIR):
        if not file.is_file():
            continue

        if not file.name.casefold().endswith(".sh"):
            continue

        modules.append(load_file(file.path))

    return b"\n\n".join(modules)


def load_file(filepath: str) -> bytes:
    """Load a file from the filesystem."""

    if not exists(filepath):
        raise InvalidArgument(f"file not found: {filepath}")

    elif not isfile(filepath):
        raise InvalidArgument(f"expecting a file: {filepath}")

    else:
        with open(filepath, "rb") as f:
            return f.read()


def read_message(prompt: str = "") -> str:
    """Read a message from standard input and strip whitespace."""

    return input(prompt).strip()


def write_message(message: str) -> None:
    """Write a message to standard output."""

    sys.stdout.write(message + "\n")
    sys.stdout.buffer.flush()


def write_binary_message(message: bytes) -> None:
    """Write a binary message to standard output."""

    sys.stdout.buffer.write(message)
    sys.stdout.buffer.flush()


def write_error_message(message: str) -> None:
    """Write an error message to standard error."""

    sys.stderr.write(f"error: {message}\n".lower())
    sys.stderr.flush()


def write_warninig_message(message: str) -> None:
    """Write a warning message to standard error."""

    sys.stderr.write(f"warning: {message}\n".lower())
    sys.stderr.flush()
