from __future__ import annotations

from .registry import Registry
from .request import Request
from .response import Response


class Runtime:
    """The Aether Runtime orchestrates the execution of registered modules."""
    def __init__(self, registry : Registry) -> None:
        self._registry = registry

    def execute(self, module_name : str, request : Request) -> Response:
        module = self._registry.retrieve(module_name)
        return module.execute(request)
        
