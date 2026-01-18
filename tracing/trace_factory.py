

from trace import Trace
from uuid import uuid4

from tracing.default_trace import DefaultTrace

def create_trace(name: str) -> Trace:
    # somehow get a config?
    # if tracing is disabled , return NoOpTrace,
    # otherwise return a default trace
    print("trace")
    trace_id = f"trace_{uuid4().hex}"
    return DefaultTrace(name, trace_id)