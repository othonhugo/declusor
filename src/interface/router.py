from abc import ABC, abstractmethod
from typing import Callable

from interface.session import ISession

Controller = Callable[["ISession", "IRouter", str], None]


class IRouter(ABC):
    @property
    @abstractmethod
    def routes(self) -> tuple[str, ...]:
        raise NotImplementedError

    @property
    @abstractmethod
    def documentation(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_controller_documentation(self, route: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def connect(self, route: str, controller: Controller) -> None:
        raise NotImplementedError

    @abstractmethod
    def locate(self, route: str) -> Controller:
        raise NotImplementedError
