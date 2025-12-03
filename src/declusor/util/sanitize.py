from pathlib import Path
from typing import Iterable


def validate_file_extension(file: str | Path, allowed_extensions: Iterable[str]) -> bool:
    """Check if a file extension is in the set of allowed extensions."""

    file = Path(file)
    file_extension = file.suffix

    allowed_extensions = {ext.casefold() for ext in allowed_extensions}

    return file_extension.casefold() in allowed_extensions


def validate_file_relative(filepath: str | Path, base_dir: str | Path) -> bool:
    """Check if a file path is relative to a given base directory."""

    filepath = Path(filepath).resolve()
    base_dir = Path(base_dir).resolve()

    return filepath.is_relative_to(base_dir)
