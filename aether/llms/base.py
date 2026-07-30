from __future__ import annotations

from aether.kernel.request import Request
from aether.kernel.response import Response

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator

class BaseLLM(ABC):
    """Abstract interface for all LLM providers in Aether."""
    @abstractmethod
    async def generate(self, request : Request) -> Response:
        ...

    @abstractmethod
    async def stream(self, request: Request) -> AsyncIterator[Response]:
        ...
