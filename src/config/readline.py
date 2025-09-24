import readline
from glob import glob
from os.path import basename, dirname, isdir, isfile, join


def search_file(search_term: str) -> list[str]:
    """Search for files and directories matching the search term."""

    files = list()

    searching_dir = dirname(search_term)
    searching_file = basename(search_term)

    for filename in glob(searching_file + "*", root_dir=searching_dir):
        filepath = join(searching_dir, filename)

        if isdir(filepath):
            files.append(join(filename, ""))

        elif isfile(filepath):
            files.append(filename)

    return files


def set_line_completer(*command_routes: str) -> None:
    """Set up the readline completer for command line input."""

    def find_file(text: str, state: int) -> str | None:
        return (search_file(text) + [None])[state]

    def find_command(text: str, state: int) -> str | None:
        matches = [line for line in command_routes if line.startswith(text)]

        if state < len(matches):
            return matches[state] if matches[state] != text else None

        return None

    def complete_line(text: str, state: int) -> str | None:
        commands = readline.get_line_buffer().split(" ", 1)

        match len(commands):
            case 0 | 1:
                return find_command(text, state)
            case 2:
                if commands[0] in command_routes:
                    return find_file(commands[1].strip(), state)

        return None

    readline.set_completer_delims(" /\t\n;")
    readline.set_completer(complete_line)
    readline.parse_and_bind("tab: complete")
