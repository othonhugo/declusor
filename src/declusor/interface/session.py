from abc import ABC, abstractmethod
from typing import AsyncGenerator


class ISession(ABC):
    """Session interface."""

    @abstractmethod
    def set_timeout(self, value: float) -> None:
        """Set the session timeout."""

        raise NotImplementedError

    @abstractmethod
    def read(self) -> AsyncGenerator[bytes, None]:
        """Read data from the session."""

        raise NotImplementedError

    @abstractmethod
    async def write(self, content: bytes) -> None:
        """Write data to the session."""

        raise NotImplementedError
