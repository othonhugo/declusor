from enum import StrEnum


class FileFunc(StrEnum):
    """Enumeration of file operation functions."""

    EXEC_FILE = "execute_base64_encoded_value"
    STORE_FILE = "store_base64_encoded_value"
