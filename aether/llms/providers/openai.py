from __future__ import annotations

from collections.abc import AsyncIterator

from aether.kernel.response import Response
from aether.llms.base import BaseLLM
from aether.llms.config import ChatRequest

from openai import AsyncOpenAI

class OpenAIProvider(BaseLLM):

    def __init__(
        self,
        api_key: str,
        model: str = "gpt-5-mini",
    ):
        self.client = AsyncOpenAI(api_key=api_key)
        self.model = model

    async def generate(self, request: ChatRequest) -> Response:
        # pick the model based on the request parameters
        if request.model is not None:
            model = request.model
        else:
            model = self.model

        # Convert Aether messages → OpenAI messages
        messages = []
        for message in request.messages:
            openai_message = {
                "role": message.role.value,
                "content": message.content
            }

            messages.append(openai_message)

        # Get generation configuration
        config = request.generation_config 

        # Ask OpenAI for a response
        response = await self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=config.temperature,
            max_tokens=config.max_tokens,
            top_p=config.top_p,
            stop=config.stop_sequences,
        )

        # Extract generated text
        output = response.choices[0].message.content

        # Return Aether response
        return Response(
            output=output
        )

    async def stream(self, request: ChatRequest) -> AsyncIterator[Response]:
        pass
