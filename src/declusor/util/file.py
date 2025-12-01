from os import scandir
from os.path import exists, isfile, join, splitext

from declusor.config import LIBRARY_DIR, SCRIPTS_DIR, InvalidArgument
from declusor.util.io import write_error_message


def load_payload(module: str) -> bytes:
    """Load a payload script from the scripts directory."""

    if (extension := splitext(module)[1].casefold()) != ".sh":
        raise InvalidArgument(f"{extension!r} is not supported")

    module_filepath = join(SCRIPTS_DIR, module)

    if not exists(module_filepath):
        raise InvalidArgument(f"file not found: {module}")

    if not isfile(module_filepath):
        raise InvalidArgument(f"expecting a file: {module}")

    ## uncomment to restrict third-party payloads
    #
    # from os.path import commonpath
    # if commonpath([PAYLOAD_DIR, module_filepath]) != PAYLOAD_DIR:
    #     raise InvalidArgument(module)

    with open(module_filepath, "rb") as f:
        return f.read()


def load_library() -> bytes:
    """Load all library scripts from the library directory."""

    modules: list[bytes] = []

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

    if not isfile(filepath):
        raise InvalidArgument(f"expecting a file: {filepath}")

    with open(filepath, "rb") as f:
        return f.read()


def load_file_safely(filepath: str) -> bytes | None:
    """Load a file safely, writing an error message if it fails."""

    try:
        return load_file(filepath)
    except InvalidArgument as err:
        write_error_message(str(err))

        return None
