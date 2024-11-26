

from abc import ABC, abstractmethod
from typing import Any

import pandas as pd

not_implemented_error = NotImplementedError("ABC class has not implementation for methods, please consider using a concrete class.")

class ABCAnalyze(ABC):

    def __init__(self, dataset: pd.DataFrame) -> None:
        raise not_implemented_error

    @abstractmethod
    def perform(self) -> None:
        raise not_implemented_error


    @property
    @abstractmethod
    def results(self) -> Any:
        raise not_implemented_error

    @property
    @abstractmethod
    def short_summary(self) -> str:
        raise not_implemented_error
