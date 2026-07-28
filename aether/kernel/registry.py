from __future__ import annotations

from types import MappingProxyType

from .exceptions import (
    ModuleAlreadyRegisteredError,
    ModuleNotFoundError,
)
from .interfaces import Module


class Registry:
    """Stores and provides access to runtime modules."""
    def __init__(self) -> None:
        self._modules: dict[str, Module] = {}

    @property
    def modules(self) -> MappingProxyType[str, Module]:
        """Read-only view of all registered modules."""
        return MappingProxyType(self._modules)

    @staticmethod
    def _validate_name(name: str) -> None:
        """Validate a module name."""
        if not name.strip():
            raise ValueError("Module name cannot be empty.")

    def register(self, name: str, module: Module) -> None:
        """Register a module under a unique name."""
        self._validate_name(name)

        if name in self._modules:
            raise ModuleAlreadyRegisteredError(
                f"Module '{name}' is already registered."
            )

        self._modules[name] = module

    def retrieve(self, name: str) -> Module:
        """Retrieve a registered module."""
        self._validate_name(name)

        try:
            return self._modules[name]

        except KeyError:
            raise ModuleNotFoundError(
                f"Module '{name}' is not registered."
            ) from None

    def is_registered(self, name: str) -> bool:
        """Return True if a module exists in the registry."""
        return name in self._modules
    