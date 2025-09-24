from abc import ABC, abstractmethod


class IPrompt(ABC):
    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError
