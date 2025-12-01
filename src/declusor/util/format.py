from os.path import join
from string import Template

from declusor.config import CLIENTS_DIR, DEFAULT_SRV_ACK


def convert_bytes_to_hex(data: bytes) -> str:
    """Converts bytes to a hex string representation."""

    return "".join(f"\\x{i:02x}" for i in data)


def format_client_bash_code(filepath: str, **kwargs: str | int) -> str:
    """Formats client code by reading a file, removing comments, and substituting variables."""

    client_code = ""

    with open(join(CLIENTS_DIR, filepath), "r", encoding="utf-8") as f:
        for line in f.readlines():
            if not line.lstrip().startswith("#"):
                client_code += line

    kwargs.update({"acknowledge": convert_bytes_to_hex(DEFAULT_SRV_ACK)})

    client_code = " ".join(client_code.split())
    client_code = Template(client_code).safe_substitute(**format_bash_arguments(**kwargs))

    return client_code


def format_bash_arguments(**kwargs: str | int) -> dict[str, str]:
    """Formats keyword arguments into a dictionary suitable for Bash-like environment variables."""

    return {k.upper(): str(v) for k, v in kwargs.items()}


def escape_single_quotes(value: str) -> str:
    """Escapes single quotes and backslashes for safe use in single-quoted Bash strings."""

    return value.replace("\\", "\\\\").replace("'", "\\'")


def escape_double_quotes(value: str) -> str:
    """Escapes double quotes and backslashes for safe use in double-quoted Bash strings."""

    return value.replace("\\", "\\\\").replace('"', '\\"')


def format_bash_function_call(function: str, *args: str, use_double_quotes: bool = False) -> str:
    """Formats a Bash function call with properly escaped arguments."""

    escaped_args: list[str] = []

    for arg in args:
        if use_double_quotes:
            escaped_args.append(f'"{escape_double_quotes(arg)}"')
        else:
            escaped_args.append(f"'{escape_single_quotes(arg)}'")

    return f"{function} {' '.join(escaped_args)}"
