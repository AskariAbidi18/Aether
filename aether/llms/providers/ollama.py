from __future__ import annotations

from collections.abc import AsyncIterator

from aether.kernel.response import Response
from aether.llms.base import BaseLLM
from aether.llms.config import ChatRequest


class OllamaProvider(BaseLLM):

    def __init__(
        self,
        model: str = "llama3.2",
        endpoint: str = "http://localhost:11434",
    ):
        self.model = model
        self.endpoint = endpoint

    async def generate(self, request: ChatRequest) -> Response:
        pass

    async def stream(self, request: ChatRequest) -> AsyncIterator[Response]:
        pass
    