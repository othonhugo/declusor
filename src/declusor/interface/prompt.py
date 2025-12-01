from abc import ABC, abstractmethod


class IPrompt(ABC):
    """Prompt interface."""

    @abstractmethod
    async def run(self) -> None:
        """Run the prompt loop."""

        raise NotImplementedError
