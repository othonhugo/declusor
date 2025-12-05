from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from declusor.interface.console import IConsole
    from declusor.interface.session import ISession


class ICommand(ABC):
    """Abstract base class defining the command interface.

    Commands encapsulate executable actions that can be performed
    within a session context.
    """

    @abstractmethod
    async def execute(self, session: "ISession", console: "IConsole", /) -> None:
        """Execute the command in the given session.

        Args:
            session: The session context in which to execute the command.
        """

        raise NotImplementedError
