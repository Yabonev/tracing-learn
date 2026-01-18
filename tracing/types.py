# Useful types (TypedDict) for autocomplete, etc.

from typing import Any, NotRequired, TypedDict


class TraceExport(TypedDict):
    name: str 
    trace_id: str
    metadata: NotRequired[dict[str, Any]]