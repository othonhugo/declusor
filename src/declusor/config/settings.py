from pathlib import Path


class Settings:
    """Configuration settings for Declusor."""

    __allowed_payload_extensions = [".sh"]
    __allowed_library_extensions = [".sh"]

    ALLOWED_PAYLOAD_EXTENSIONS = tuple(map(str.casefold, __allowed_payload_extensions))
    """Allowed file extensions for payload scripts."""

    ALLOWED_LIBRARY_EXTENSIONS = tuple(map(str.casefold, __allowed_library_extensions))
    """Allowed file extensions for library scripts."""

    DEFAULT_CLIENT = "reverse_bash.sh"
    """Default client script filename."""

    ACK_CLIENT_PLACEHOLDER = "ACKNOWLEDGE"
    """Placeholder string for acknowledgment in client scripts."""

    ACK_CLIENT_VALUE = b"\xba\xdc\x00\xff\xee"
    """Acknowledgment byte sequence sent by the client."""

    ACK_SERVER_VALUE = b"\x00"
    """Acknowledgment byte sequence sent by the server."""


class BasePath:
    """Base paths for Declusor project directories."""

    ROOT_DIR = Path(__file__).resolve().parents[3]
    """Normalized root directory of the project."""

    DATA_DIR = (ROOT_DIR / "data").resolve()
    """Normalized data directory path."""

    CLIENTS_DIR = (DATA_DIR / "clients").resolve()
    """Normalized clients directory path."""

    MODULES_DIR = (DATA_DIR / "modules").resolve()
    """Normalized modules directory path."""

    LIBRARY_DIR = (DATA_DIR / "library").resolve()
    """Normalized library directory path."""
