from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen = True, slots = True)
class Response:
    """A final output leaving the Aether Runtime."""
    output : str
    metadata : dict[str, Any] = field(default_factory = dict)
