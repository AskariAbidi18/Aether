from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen = True, slots = True)
class Request:
    """A single requuest entering the Aether Runtime. """
    input : str
    user_id : str | None = None
    session_id : str | None = None
    metadata : dict[str, Any] = field(default_factory = dict)
    context : dict[str, Any] = field(default_factory = dict)
