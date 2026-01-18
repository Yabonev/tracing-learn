# TODO: NoOpTrace + Singleton pattern, check the __new__ 

from trace import Trace
from types import TracebackType
from typing import Self


class NoOpTrace(Trace):
    """
    TODO: Explain NoOpTrace purpose and behavior
    """

    def __enter__(self) -> Self:
        """
        TODO: Add meaningful explanation for methods that are continuations of the class doc
        """
        pass

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None
    ) -> None:
        """TODO: comment"""
        pass