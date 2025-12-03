from string import Template
from shlex import quote

from declusor import config
from declusor.util import encoding


def format_client_script(client_name: str, /, **kwargs: str | int) -> str:
    """Read a client script from the default clients directory, substitute variables, and format it for use."""

    client_filepath = (config.CLIENTS_DIR / client_name).resolve()

    with open(client_filepath, "r", encoding="utf-8") as f:
        client_script = f.read()

    kwargs[config.DEFAULT_ACK_PLACEHOLDER] = encoding.convert_bytes_to_hex(config.DEFAULT_ACK_VALUE)

    client_template = Template(client_script)

    return client_template.safe_substitute(**kwargs)


def format_function_call(function_name: str, language: str, /, *args: str) -> str:
    """Formats a function call with properly escaped arguments."""

    match language.lower():
        case "bash" | "sh":
            return _format_bash_function_call(function_name, *args)
        case _:
            raise config.InvalidOperation(f"Unsupported language: {language}")


def _format_bash_function_call(function_name: str, /, *args: str) -> str:
    """Formats a Bash function call with properly escaped arguments."""

    template = Template("$function_name $quoted_args")

    return template.safe_substitute(function_name=function_name, quoted_args=" ".join(quote(arg) for arg in args))
