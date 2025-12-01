from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Awaitable, Callable

if TYPE_CHECKING:
    from declusor.interface.session import ISession

Controller = Callable[["ISession", "IRouter", str], Awaitable[None]]


class IRouter(ABC):
    """Router interface."""

    @property
    @abstractmethod
    def routes(self) -> tuple[str, ...]:
        """Returns all registered routes."""

        raise NotImplementedError

    @property
    @abstractmethod
    def documentation(self) -> str:
        """Returns the documentation of all registered routes."""

        raise NotImplementedError

    @abstractmethod
    def get_controller_documentation(self, route: str) -> str:
        """Returns the documentation of the controller associated with the given route."""

        raise NotImplementedError

    @abstractmethod
    def connect(self, route: str, controller: Controller) -> None:
        """Connects a route to a controller."""

        raise NotImplementedError

    @abstractmethod
    def locate(self, route: str) -> Controller:
        """Locates the controller associated with the given route."""

        raise NotImplementedError
