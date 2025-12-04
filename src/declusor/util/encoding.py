def convert_bytes_to_hex(data: bytes, /) -> str:
    """
    Convert a bytes object to its hexadecimal string representation.

    Args:
        data: The bytes object to convert.

    Returns:
        The hexadecimal string representation of the bytes.
    """

    return "".join(f"\\x{i:02x}" for i in data)
