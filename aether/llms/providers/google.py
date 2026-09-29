from __future__ import annotations

from collections.abc import AsyncIterator

from aether.kernel.response import Response
from aether.llms.base import BaseLLM
from aether.llms.config import ChatRequest


class GoogleProvider(BaseLLM):

    def __init__(
        self,
        api_key: str,
        model: str = "gemini-3.8-flash",
    ):
        self.api_key = api_key
        self.model = model

    async def generate(self, request: ChatRequest) -> Response:
        pass

    async def stream(self, request: ChatRequest) -> AsyncIterator[Response]:
        pass
    