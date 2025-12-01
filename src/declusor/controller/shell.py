import asyncio
from asyncio import Event

from declusor.interface import IRouter, ISession
from declusor.util import parse_command_arguments, read_message, write_binary_message


async def call_shell(session: ISession, router: IRouter, line: str) -> None:
    """Open an interactive shell session with the target device."""

    parse_command_arguments(line, {})

    stop_event = Event()

    # Create tasks for handling input and socket data
    input_task = asyncio.create_task(handle_input_data(session, stop_event))
    socket_task = asyncio.create_task(handle_socket_data(session, stop_event))

    try:
        # Wait for either task to complete (likely socket task if connection closes)
        # or for a KeyboardInterrupt (handled by the caller of PromptCLI usually, but here we might need to catch it if we want to exit shell cleanly)
        # Actually PromptCLI catches DeclusorException. KeyboardInterrupt might propagate.

        # We wait for socket_task. input_task runs forever until cancelled.
        # But if user wants to exit shell, how do they do it?
        # The original code caught KeyboardInterrupt in call_shell.
        await asyncio.wait([input_task, socket_task], return_when=asyncio.FIRST_COMPLETED)

    except asyncio.CancelledError:
        pass
    finally:
        stop_event.set()

        # Cancel input task. Note: input() in thread might not stop immediately.
        input_task.cancel()
        socket_task.cancel()

        try:
            await input_task
        except asyncio.CancelledError:
            pass
        try:
            await socket_task
        except asyncio.CancelledError:
            pass


async def handle_input_data(session: ISession, stop_event: Event) -> None:
    """Handle input data from the user."""

    while not stop_event.is_set():
        # Run blocking input in a separate thread
        try:
            command = await asyncio.to_thread(read_message)

            if command.strip():
                await session.write(command.strip().encode())
        except EOFError:
            break


async def handle_socket_data(session: ISession, stop_event: Event) -> None:
    """Handle socket data from the target device."""

    try:
        async for data in session.read():
            if stop_event.is_set():
                break
            if data:
                write_binary_message(data)
    except Exception:
        pass
    finally:
        stop_event.set()
