from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Awaitable, Callable

if TYPE_CHECKING:
    from declusor.interface.console import IConsole
    from declusor.interface.session import ISession

Controller = Callable[["ISession", "IConsole", str], Awaitable[None]]


class IRouter(ABC):
    """Abstract base class defining the router interface.

    Routers map command routes to their corresponding controller functions,
    managing command registration and dispatch.
    """

    @property
    @abstractmethod
    def routes(self) -> tuple[str, ...]:
        """Returns all registered routes.

        Returns:
            Tuple of all registered route names.
        """

        raise NotImplementedError

    @property
    @abstractmethod
    def documentation(self) -> str:
        """Returns the documentation of all registered routes.

        Returns:
            Formatted documentation string for all routes.
        """

        raise NotImplementedError

    @abstractmethod
    def get_route_usage(self, route: str, /) -> str:
        """Returns the documentation of the controller associated with the given route.

        Args:
            route: The route name to get usage documentation for.

        Returns:
            Usage documentation string for the specified route.
        """

        raise NotImplementedError

    @abstractmethod
    def connect(self, route: str, controller: Controller, /) -> None:
        """Connects a route to a controller.

        Args:
            route: The route name to register.
            controller: The controller function to associate with the route.
        """

        raise NotImplementedError

    @abstractmethod
    def locate(self, route: str, /) -> Controller:
        """Locates the controller associated with the given route.

        Args:
            route: The route name to locate.

        Returns:
            The controller function associated with the route.
        """

        raise NotImplementedError
