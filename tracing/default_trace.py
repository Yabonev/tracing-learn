# The Trace class implementation, care about __slots__

from trace import Trace
from types import TracebackType
from typing import Any, Optional, Self

from tracing.types import TraceExport


class DefaultTrace(Trace):
    # TODO: So what does a trace do and not do?
    # - is the equivilent of container for all spans
    # - Is only 1, meaning no child traces, at least for now. I don't need nested trace complixity at this point.
    # should have spans list, metadata prop for the export
    # should handle and log exceptions to the metadata? or data? or spans handle exceptions? but what if exception before first span?
    # so add methods for adding metadata or metadata is part of factory constructor, but how to add during runtime, another method that appends?

    def __init__(self, trace_name: str, trace_id: str, metadata: dict[str, Any] | None = None) -> None:
        self._name = trace_name
        self._trace_id = trace_id
        self._metadata = metadata.copy() if metadata else {}
        self._started: bool = False

    def __enter__(self) -> Self: 
        self.start()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None ,
        exc_tb: TracebackType | None
    ) -> None:
       self.finish()
        


    def start(self) -> None:
        if self._started:
            return
        
        self._started = True
        # TODO: Other init logic?

    def finish(self) -> None:
        if not self._started:
            return

    def export(self) -> TraceExport | None: 
        return {
            "name": self.name,
            "trace_id": self.trace_id,
            "metadata": self.metadata.copy()
        }

    @property
    def name(self) -> str:
        return self._name

    @property
    def trace_id(self) -> str:
        return self._trace_id 
    
    @property
    def metadata(self) -> dict[str, Any]:
        """ Return real metadata so the users can mutate it """
        return self._metadata
    
