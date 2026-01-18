from tracing.trace_factory import create_trace
from tracing.trace import Trace

def main():

    with create_trace("test") as t:
        result = async_op()
        t.metadata["test"] = "new metadata:" + result
        print(t.export())

def async_op() -> str:
    return "async op result!"

if __name__ == "__main__":
    main()
