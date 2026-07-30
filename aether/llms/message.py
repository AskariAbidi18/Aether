from __future__ import annotations 
from dataclasses import dataclass 
from enum import Enum 

class MessageRole(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"

@dataclass(frozen = True, slots = True)
class ChatMessage:
    role : MessageRole
    content : str

