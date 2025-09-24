from threading import Event, Thread

from interface import IRouter, ISession
from util import parse_command_arguments, read_message, write_binary_message


def call_shell(session: ISession, router: IRouter, line: str) -> None:
    """Open an interactive shell session with the target device."""

    parse_command_arguments(line, {})

    thread_event = Event()

    thread = Thread(target=handle_socket_data, args=(session, thread_event))
    thread.start()

    try:
        handle_input_data(session)
    except KeyboardInterrupt:
        pass
    finally:
        thread_event.set()
        thread.join()


def handle_input_data(session: ISession) -> None:
    while True:
        if command := read_message().strip():
            session.write(command.encode())


def handle_socket_data(session: ISession, flag: Event) -> None:
    while not flag.is_set():
        for data in session.read():
            if data:
                write_binary_message(data)
            elif flag.is_set():
                break
