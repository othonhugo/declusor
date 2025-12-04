from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from declusor.interface.session import ISession


class ICommand(ABC):
    """Command interface."""

    @abstractmethod
    async def execute(self, session: "ISession", /) -> None:
        """Execute the command in the given session."""

        raise NotImplementedError
