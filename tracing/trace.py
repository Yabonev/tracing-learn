import abc
from types import TracebackType
from typing import Any, Self

from tracing.types import TraceExport


class Trace(abc.ABC):
    """
    TODO: Add user readable comment with the purpose, example usage and other comments
    """

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

    @property
    @abc.abstractmethod
    def metadata(self) -> dict[str, Any]: ...

