def convert_bytes_to_hex(data: bytes, /) -> str:
    """Convert a bytes object to its hexadecimal string representation."""

    return "".join(f"\\x{i:02x}" for i in data)
