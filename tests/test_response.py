from __future__ import annotations

from aether.kernel.response import Response


def test_response_creation():
    response = Response(
        output="Hello",
    )

    assert response.output == "Hello"
    