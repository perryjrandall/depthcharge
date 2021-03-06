import byteasm
from contextlib import contextmanager
from unittest.mock import _get_target


@contextmanager
def deep_patch(target, return_value):
    getter, attr = _get_target(target)
    fun = getattr(getter(), attr)
    if not callable(fun):
        raise Exception("Can only patch simple functions")

    builder = byteasm.FunctionBuilder()
    builder.emit_load_const(return_value)
    builder.emit_return_value()
    new_fun = builder.make(fun.__name__)

    try:
        previous = fun.__code__
        fun.__code__ = new_fun.__code__
        yield
    finally:
        fun.__code__ = previous
