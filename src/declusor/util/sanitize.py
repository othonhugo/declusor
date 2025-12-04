from pathlib import Path
from typing import Iterable


def validate_file_extension(file: str | Path, allowed_extensions: Iterable[str]) -> bool:
    """
    Check if a file extension is in the set of allowed extensions.

    Args:
        file: The file path or name to check.
        allowed_extensions: An iterable of allowed extension strings (e.g., ['.txt', '.py']).

    Returns:
        True if the file extension is allowed, False otherwise.
    """

    file = Path(file)
    file_extension = file.suffix

    allowed_extensions = {ext.casefold() for ext in allowed_extensions}

    return file_extension.casefold() in allowed_extensions


def validate_file_relative(filepath: str | Path, base_dir: str | Path) -> bool:
    """
    Check if a file path is relative to a given base directory.

    Args:
        filepath: The file path to check.
        base_dir: The base directory path.

    Returns:
        True if the file path is relative to the base directory, False otherwise.
    """

    filepath = Path(filepath).resolve()
    base_dir = Path(base_dir).resolve()

    return filepath.is_relative_to(base_dir)
