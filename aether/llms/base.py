from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator

from aether.kernel.response import Response
from aether.llms.config import ChatRequest


class BaseLLM(ABC):
    """Abstract interface for all LLM providers in Aether."""

    @abstractmethod
    async def generate(self, request: ChatRequest) -> Response:
        ...

    @abstractmethod
    async def stream(self, request: ChatRequest) -> AsyncIterator[Response]:
        ...
        