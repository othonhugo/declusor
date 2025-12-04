from pathlib import Path

from declusor import config
from declusor.util import sanitize


def load_file(filepath: str | Path) -> bytes:
    """
    Read a file from the filesystem.

    Args:
        filepath: The path to the file to read.

    Returns:
        The content of the file as bytes.

    Raises:
        InvalidOperation: If the file does not exist, is not a file, or cannot be read.
    """

    filepath = Path(filepath).resolve()

    if not filepath.exists():
        raise config.InvalidOperation(f"file {filepath!r} does not exist")

    if not filepath.is_file():
        raise config.InvalidOperation(f"{filepath!r} is not a file")

    try:
        with open(filepath, "rb") as f:
            return f.read()
    except OSError as e:
        raise config.InvalidOperation(f"could not read file {filepath!r}: {e}") from e


def load_payload(module_filename: str) -> bytes:
    """
    Load a payload script from the default scripts directory.

    Args:
        module_filename: The name of the payload script file.

    Returns:
        The content of the payload script as bytes.

    Raises:
        InvalidOperation: If the file extension is not supported or the file is outside the scripts directory.
    """

    module_filepath = (config.SCRIPTS_DIR / module_filename).resolve()

    if not sanitize.validate_file_extension(module_filename, config.ALLOW_PAYLOAD_EXTENSIONS):
        raise config.InvalidOperation(f"extension of {module_filepath.name!r} is not supported")

    if not sanitize.validate_file_relative(module_filepath, config.SCRIPTS_DIR):
        raise config.InvalidOperation(f"{module_filepath!r} is outside the scripts directory")

    return load_file(module_filepath)


def load_library() -> bytes:
    """
    Load all library scripts from the default library directory.

    Returns:
        The concatenated content of all library scripts as bytes.
    """

    modules: list[bytes] = []

    for file in config.LIBRARY_DIR.iterdir():
        if not file.is_file():
            continue

        if not sanitize.validate_file_extension(file, config.ALLOW_LIBRARY_EXTENSIONS):
            continue

        modules.append(load_file(file.name))

    return b"\n".join(modules)
