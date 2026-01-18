import abc
from types import TracebackType
from typing import Self

from tracing.types import TraceExport


class BaseTrace(abc.ABC):
    @abc.abstractmethod
    def __enter__(self) -> Self: ...

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None ,
        exc_tb: TracebackType | None
    ) -> None: ...

    @abc.abstractmethod
    def start(self) -> None: ...

    @abc.abstractmethod
    def finish(self) -> None: ...

    @abc.abstractmethod
    def export(self) -> TraceExport | None: ...

    @property
    @abc.abstractmethod
    def name(self) -> str: ...

    @property
    @abc.abstractmethod
    def trace_id(self) -> str: ...

