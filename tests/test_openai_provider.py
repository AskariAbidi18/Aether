import os

import pytest

from aether.llms.config import ChatRequest
from aether.llms.message import ChatMessage, MessageRole
from aether.llms.providers.openai import OpenAIProvider


@pytest.mark.asyncio
async def test_openai_generate():
    api_key = os.environ["OPENAI_API_KEY"]

    provider = OpenAIProvider(api_key=api_key)

    request = ChatRequest(
        messages=[
            ChatMessage(
                role=MessageRole.USER,
                content="Say hello from Aether in one short sentence.",
            )
        ]
    )

    response = await provider.generate(request)

    print("\nAether:", response.output)

    assert response.output
    