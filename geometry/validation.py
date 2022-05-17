from typing import Any

from abc import ABC, abstractmethod


class FigureValidation(ABC):

    def __init__(self, *args: Any, **kwargs: Any):
        pass

    @abstractmethod
    def validate(self) -> None:
        raise NotImplementedError()
