from declusor import config, interface


class Router(interface.IRouter):
    """Router implementation."""

    def __init__(self) -> None:
        self.route_table: dict[str, interface.Controller] = {}

    @property
    def routes(self) -> tuple[str, ...]:
        """Returns all registered routes."""

        return tuple(self.route_table.keys())

    def get_route_usage(self, route: str, /) -> str:
        """Returns the documentation of the controller associated with the given route."""

        controller_doc = self.locate(route).__doc__

        if controller_doc:
            documentation = " ".join(map(str.strip, controller_doc.split("\n")))
        else:
            documentation = ""

        return documentation

    def connect(self, route: str, controller: interface.Controller, /) -> None:
        """Connects a route to a controller."""

        route = route.strip()

        if route in self.route_table:
            raise ValueError("route already exists.")

        self.route_table[route] = controller

    def locate(self, route: str, /) -> interface.Controller:
        """Locates the controller associated with the given route."""

        if controller := self.route_table.get(route.strip()):
            return controller

        raise config.RouterError(route)

    @property
    def documentation(self) -> str:
        """Returns the documentation of all registered routes."""

        key_length = max(map(len, self.route_table.keys())) + 1

        documentation = ""

        for route in self.route_table:
            documentation += f"{route:<{key_length}}: "
            documentation += f"{self.get_route_usage(route)}\n"

        return documentation.rstrip()
