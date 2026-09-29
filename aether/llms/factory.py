from typing import Any

from aether.llms.base import BaseLLM

from aether.llms.providers.openai import OpenAIProvider
from aether.llms.providers.anthropic import AnthropicProvider
from aether.llms.providers.xai import XAIProvider
from aether.llms.providers.google import GoogleProvider
from aether.llms.providers.deepseek import DeepSeekProvider
from aether.llms.providers.qwen import QwenProvider
from aether.llms.providers.ollama import OllamaProvider

def create(provider: str, configuration: dict[str, Any]) -> BaseLLM:
    if provider == "openai":
        return OpenAIProvider(**configuration)
    elif provider == "anthropic":
        return AnthropicProvider(**configuration)
    elif provider == "xai":
        return XAIProvider(**configuration)
    elif provider == "google":
        return GoogleProvider(**configuration)
    elif provider == "deepseek":
        return DeepSeekProvider(**configuration)
    elif provider == "qwen":
        return QwenProvider(**configuration)
    elif provider == "ollama":
        return OllamaProvider(**configuration)
    else:
        raise ValueError(f"Unknown LLM provider: {provider}")
