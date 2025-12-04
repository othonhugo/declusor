from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from declusor.interface.session import ISession


class ICommand(ABC):
    """Command interface."""

    @abstractmethod
    async def execute(self, session: "ISession") -> None:
        """Send the command to the supplied session."""

        raise NotImplementedError
