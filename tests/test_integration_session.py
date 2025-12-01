import asyncio
import socket
import threading
import unittest
from unittest.mock import patch

from declusor.core.session import Session


class TestSessionIntegration(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        # Create a real TCP server
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.bind(("127.0.0.1", 0))
        self.server_sock.listen(1)
        self.port = self.server_sock.getsockname()[1]

        self.server_ack = b"<SACK>"
        self.client_ack = b"<CACK>"

        self.running = True
        self.server_thread = threading.Thread(target=self._run_server)
        self.server_thread.start()

    def tearDown(self) -> None:
        self.running = False

        # Connect to server to unblock accept if needed
        try:
            # Create a dummy connection to unblock accept() if it's hanging
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(("127.0.0.1", self.port))
        except OSError:
            pass

        self.server_sock.close()
        self.server_thread.join(timeout=2)

    def _run_server(self) -> None:
        try:
            self.server_sock.settimeout(1)

            while self.running:
                try:
                    conn, addr = self.server_sock.accept()
                except socket.timeout:
                    continue
                except OSError:
                    break

                with conn:
                    # Read initial handshake (library)
                    try:
                        # Just read some bytes, we don't validate content here
                        conn.recv(4096)
                    except OSError:
                        pass

                    while self.running:
                        try:
                            data = conn.recv(4096)

                            if not data:
                                break

                            # Simple echo protocol:
                            # If we receive "ping<CACK>", we send "pong<SACK>"
                            if b"ping" + self.client_ack in data:
                                conn.sendall(b"pong" + self.server_ack)
                        except OSError:
                            break
        except OSError:
            pass

    async def test_session_handshake_and_echo(self) -> None:
        """Test session initialization and bidirectional communication with echo protocol."""

        # Patch load_library to avoid filesystem dependency and return known data
        with patch("declusor.core.session.load_library", return_value=b"init_lib"):
            reader, writer = await asyncio.open_connection("127.0.0.1", self.port)
            session = Session(reader, writer, self.server_ack, self.client_ack)

            await session.initialize()

            # Test write
            await session.write(b"ping")

            # Test read
            # We expect "pong"
            responses: list[bytes] = []

            async for chunk in session.read():
                responses.append(chunk)

            full_response = b"".join(responses)

            self.assertEqual(full_response, b"pong")

            writer.close()

            await writer.wait_closed()
