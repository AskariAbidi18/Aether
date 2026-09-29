from collections.abc import AsyncIterator

from aether.llms.base import BaseLLM 
from aether.kernel.request import Request
from aether.kernel.response import Response

class GoogleProvider(BaseLLM):
    def __init__(self, api_key : str, model : str = "gemini-3.8-flash"):
        self.api_key = api_key
        self.model = model

    def generate(self, request : Request) -> Response:
        pass

    def stream(self, request : Request) -> AsyncIterator[Response]:
        pass
