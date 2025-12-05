from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class IParser(ABC, Generic[T]):
    """Abstract base class defining the argument parser interface.

    Generic parser interface for parsing command-line arguments into
    a specific type T.
    """

    @abstractmethod
    def parse(self) -> T:
        """Parse command-line arguments.

        Returns:
            Parsed arguments of type T.
        """

        raise NotImplementedError
