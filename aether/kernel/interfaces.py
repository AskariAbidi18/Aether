from __future__ import annotations

from typing import Protocol

from .request import Request
from .response import Response


class Module(Protocol):
    """Base protocol for every runtime module."""
    @property
    def name(self) -> str:
        ...

    def execute(self, request: Request) -> Response:
        ...
