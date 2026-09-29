from collections.abc import AsyncIterator

from aether.llms.base import BaseLLM 
from aether.kernel.request import Request
from aether.kernel.response import Response

class OllamaProvider(BaseLLM):
    def __init__(
        self,
        model: str = "llama3.2",
        endpoint: str = "http://localhost:11434",
    ):
        self.model = model
        self.endpoint = endpoint

    async def generate(self, request: Request) -> Response:
        pass

    async def stream(self, request: Request) -> AsyncIterator[Response]:
        pass
