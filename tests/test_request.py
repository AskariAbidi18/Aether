from __future__ import annotations

from aether.kernel.request import Request


def test_request_creation():
    request = Request(
        input="Hello",
    )

    assert request.input == "Hello"
    assert request.context == {}
    