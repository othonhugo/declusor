from pathlib import Path

from declusor import config


def load_file(filepath: str | Path) -> bytes:
    """Read a file from the filesystem."""

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
    """Load a payload script from the default scripts directory."""

    module_filepath = (config.SCRIPTS_DIR / module_filename).resolve()
    module_extension = module_filepath.suffix

    if module_extension.casefold() not in config.ALLOW_PAYLOAD_EXTENSIONS:
        raise config.InvalidOperation(f"extension {module_extension!r} is not supported")

    if not module_filepath.is_relative_to(config.SCRIPTS_DIR):
        raise config.InvalidOperation(f"{module_filepath!r} is outside the scripts directory")

    return load_file(module_filepath)


def load_library() -> bytes:
    """Load all library scripts from the default library directory."""

    modules: list[bytes] = []

    for file in config.LIBRARY_DIR.iterdir():
        if not file.is_file():
            continue

        if not file.suffix.casefold() in config.ALLOW_LIBRARY_EXTENSIONS:
            continue

        modules.append(load_file(file.name))

    return b"\n".join(modules)
