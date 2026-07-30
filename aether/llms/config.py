from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

from .config import GenerationConfig
from .message import ChatMessage


@dataclass(frozen=True, slots=True, init=False)
class ChatRequest:
    messages: tuple[ChatMessage, ...]
    model: str | None
    generation_config: GenerationConfig

    def __init__(
        self,
        messages: Iterable[ChatMessage],
        model: str | None = None,
        generation_config: GenerationConfig = GenerationConfig(),
    ) -> None:
        object.__setattr__(self, "messages", tuple(messages))
        object.__setattr__(self, "model", model)
        object.__setattr__(self, "generation_config", generation_config)
        