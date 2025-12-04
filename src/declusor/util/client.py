from shlex import quote
from string import Template

from declusor import config
from declusor.util import encoding


def format_client_script(client_name: str, /, **kwargs: str | int) -> str:
    """
    Read a client script from the default clients directory, substitute variables, and format it for use.

    Args:
        client_name: The name of the client script file to read.
        **kwargs: Key-value pairs to substitute into the client script template.

    Returns:
        The formatted client script with variables substituted.
    """

    client_filepath = (config.BasePath.CLIENTS_DIR / client_name).resolve()

    with open(client_filepath, "r", encoding="utf-8") as f:
        client_script = f.read()

    kwargs[config.Settings.ACK_CLIENT_PLACEHOLDER] = encoding.convert_bytes_to_hex(config.Settings.ACK_CLIENT_VALUE)

    client_template = Template(client_script)

    return client_template.safe_substitute(**kwargs)


def format_function_call(language: config.Language, /, function_name: config.FileFunc, *args: str) -> str:
    """
    Format a function call with properly escaped arguments.

    Args:
        language: The programming language of the function (e.g., 'bash', 'sh').
        function_name: The name of the function to call.
        *args: Variable length argument list to pass to the function.

    Returns:
        The formatted function call string.

    Raises:
        InvalidOperation: If the specified language is not supported.
    """

    match language:
        case config.Language.BASH | config.Language.SH:
            return _format_bash_function_call(function_name.value, *args)
        case _:
            raise config.InvalidOperation(f"Unsupported language: {language}")


def _format_bash_function_call(function_name: str, /, *args: str) -> str:
    """
    Format a Bash function call with properly escaped arguments.

    Args:
        function_name: The name of the Bash function.
        *args: Variable length argument list to pass to the function.

    Returns:
        The formatted Bash function call string.
    """

    template = Template("$function_name $quoted_args")

    return template.safe_substitute(
        function_name=function_name,
        quoted_args=" ".join(quote(arg) for arg in args),
    )
