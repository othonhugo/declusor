from pathlib import Path

from declusor import config
from declusor.util import security


def load_file(filepath: str | Path, /) -> bytes:
    """Read a file from the filesystem.

    Args:
        filepath: The path to the file to read.

    Returns:
        The content of the file as bytes.

    Raises:
        InvalidOperation: If the file does not exist, is not a file, or cannot be read.
    """

    filepath = ensure_file_exists(filepath)

    try:
        with open(filepath, "rb") as f:
            return f.read()
    except OSError as e:
        raise config.InvalidOperation(f"could not read file {filepath!r}: {e}") from e


def try_load_file(filepath: str | Path, /) -> bytes | None:
    """Try to read a file from the filesystem.

    Args:
        filepath (str | Path): The path to the file to read.

    Returns:
        bytes | None: The content of the file as bytes, or None if the file could not be read.
    """

    try:
        return load_file(filepath)
    except config.InvalidOperation:
        return None


def load_payload(module_name: str, /) -> bytes:
    """Load a payload script from the default scripts directory.

    Args:
        module_filename: The name of the payload script file.

    Returns:
        The content of the payload script as bytes.

    Raises:
        InvalidOperation: If the file extension is not supported or the file is outside the scripts directory.
    """

    module_filepath = (config.BasePath.MODULES_DIR / module_name).resolve()

    if not security.validate_file_extension(module_name, config.Settings.ALLOWED_PAYLOAD_EXTENSIONS):
        raise config.InvalidOperation(f"extension of {module_filepath.name!r} is not supported")

    if not security.validate_file_relative(module_filepath, config.BasePath.MODULES_DIR):
        raise config.InvalidOperation(f"{module_filepath!r} is outside the scripts directory")

    return load_file(module_filepath)


def load_library() -> bytes:
    """Load all library scripts from the default library directory.

    Returns:
        The concatenated content of all library scripts as bytes.
    """

    modules: list[bytes] = []

    for file in config.BasePath.LIBRARY_DIR.iterdir():
        if not file.is_file():
            continue

        if not security.validate_file_extension(file, config.Settings.ALLOWED_LIBRARY_EXTENSIONS):
            continue

        if module_content := try_load_file(file):
            modules.append(module_content)

    return b"\n\n".join(modules)


def ensure_file_exists(filepath: str | Path, /) -> Path:
    """Ensure file existence or raise an error.

    Args:
        filepath (str | Path): The path to the file.

    Returns:
        Path: The resolved file path.

    Raises:
        core.InvalidOperation: If the file does not exist or is not a file.
    """

    filepath = Path(filepath).resolve()

    if not filepath.exists():
        raise config.InvalidOperation(f"file {filepath!r} does not exist")

    if not filepath.is_file():
        raise config.InvalidOperation(f"{filepath!r} is not a file")

    return filepath


def ensure_directory_exists(dirpath: str | Path, /) -> Path:
    """Ensure directory existence or raise an error.

    Args:
        dirpath (str | Path): The path to the directory.

    Returns:
        Path: The resolved directory path.

    Raises:
        core.InvalidOperation: If the directory does not exist or is not a directory.
    """

    dirpath = Path(dirpath).resolve()

    if not dirpath.exists():
        raise config.InvalidOperation(f"directory {dirpath!r} does not exist")

    if not dirpath.is_dir():
        raise config.InvalidOperation(f"{dirpath!r} is not a directory")

    return dirpath
