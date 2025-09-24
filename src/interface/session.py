from abc import ABC, abstractmethod
from typing import Generator


class ISession(ABC):
    @abstractmethod
    def set_blocking(self, flag: bool) -> None:
        raise NotImplementedError

    @abstractmethod
    def set_timeout(self, value: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def read(self) -> Generator[bytes, None, None]:
        raise NotImplementedError

    @abstractmethod
    def write(self, data: bytes) -> None:
        raise NotImplementedError
