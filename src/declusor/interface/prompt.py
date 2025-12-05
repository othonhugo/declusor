from abc import ABC, abstractmethod


class IPrompt(ABC):
    """Abstract base class defining the prompt interface.

    Prompts handle the interactive command-line interface loop,
    reading user input and dispatching commands.
    """

    @abstractmethod
    async def run(self) -> None:
        """Run the prompt loop.

        Starts the interactive prompt, continuously reading and processing
        user commands until termination.
        """

        raise NotImplementedError
