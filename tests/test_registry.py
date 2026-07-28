from __future__ import annotations

import pytest

from aether.kernel.exceptions import (
    ModuleAlreadyRegisteredError,
    ModuleNotFoundError,
)
from aether.kernel.registry import Registry
from aether.kernel.request import Request
from aether.kernel.response import Response


class DummyModule:
    @property
    def name(self) -> str:
        return "dummy"

    def execute(self, request: Request) -> Response:
        return Response(output="ok")


def test_register_module():
    registry = Registry()

    registry.register("dummy", DummyModule())

    assert registry.is_registered("dummy")


def test_duplicate_registration_raises():
    registry = Registry()

    registry.register("dummy", DummyModule())

    with pytest.raises(ModuleAlreadyRegisteredError):
        registry.register("dummy", DummyModule())


def test_retrieve_registered_module():
    registry = Registry()

    module = DummyModule()

    registry.register("dummy", module)

    assert registry.retrieve("dummy") is module


def test_retrieve_missing_module_raises():
    registry = Registry()

    with pytest.raises(ModuleNotFoundError):
        registry.retrieve("missing")


def test_is_registered():
    registry = Registry()

    assert not registry.is_registered("dummy")

    registry.register("dummy", DummyModule())

    assert registry.is_registered("dummy")
    