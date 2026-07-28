from __future__ import annotations

import pytest

from aether.kernel.exceptions import ModuleNotFoundError
from aether.kernel.registry import Registry
from aether.kernel.request import Request
from aether.kernel.response import Response
from aether.kernel.runtime import Runtime


class EchoModule:
    @property
    def name(self) -> str:
        return "echo"

    def execute(self, request: Request) -> Response:
        return Response(
            output=f"Echo: {request.input}"
        )


def test_runtime_executes_registered_module():
    # Arrange
    registry = Registry()
    runtime = Runtime(registry)

    registry.register("echo", EchoModule())

    request = Request(
        input="Hello Aether!"
    )

    # Act
    response = runtime.execute("echo", request)

    # Assert
    assert response.output == "Echo: Hello Aether!"

def test_runtime_unknown_module():
    registry = Registry()
    runtime = Runtime(registry)

    request = Request(input="Hello")

    with pytest.raises(ModuleNotFoundError):
        runtime.execute("missing", request)
    