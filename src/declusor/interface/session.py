from abc import ABC, abstractmethod
from typing import AsyncGenerator


class ISession(ABC):
    """Abstract base class defining the session interface.

    Sessions manage network connections with clients, handling data
    transmission and timeout configuration.
    """

    @abstractmethod
    def set_timeout(self, value: float, /) -> None:
        """Set the session timeout.

        Args:
            value: Timeout duration in seconds.
        """

        raise NotImplementedError

    @abstractmethod
    def read(self) -> AsyncGenerator[bytes, None]:
        """Read data from the session.

        Returns:
            Async generator yielding bytes received from the session.
        """

        raise NotImplementedError

    @abstractmethod
    async def write(self, content: bytes, /) -> None:
        """Write data to the session.

        Args:
            content: Binary data to send to the session.
        """

        raise NotImplementedError
