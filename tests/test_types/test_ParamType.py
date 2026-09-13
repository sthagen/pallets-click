import typing as t

import click


def test_param_type_input_parameter_defaults_at_runtime():
    """Omitting the input type parameter works at runtime on every
    supported Python. The ``Any`` default is native (PEP 696) on Python
    3.13+, and backfilled by ``ParamType.__class_getitem__`` before
    that."""
    assert t.get_args(click.ParamType[int]) == (int, t.Any)
    assert t.get_args(click.ParamType[int, str]) == (int, str)


def test_param_type_subclass_omitting_input_parameter():
    class DoublingType(click.ParamType[int]):
        name = "doubling"

        def convert(self, value, param, ctx):
            return int(value) * 2

    doubling = DoublingType()
    assert doubling("21") == 42
    assert doubling(None) is None
