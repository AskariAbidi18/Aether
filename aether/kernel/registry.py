from __future__ import annotations

from types import MappingProxyType
from typing import Generic, TypeVar

from .exceptions import (
    ModuleAlreadyRegisteredError,
    ModuleNotFoundError,
)

T = TypeVar("T")


class Registry(Generic[T]):
    """Stores and provides access to named framework components."""

    def __init__(self) -> None:
        self._items: dict[str, T] = {}

    @property
    def items(self) -> MappingProxyType[str, T]:
        """Read-only view of all registered items."""
        return MappingProxyType(self._items)

    @staticmethod
    def _validate_name(name: str) -> None:
        """Validate a registry key."""
        if not name.strip():
            raise ValueError("Module name cannot be empty.")

    def register(self, name: str, item: T) -> None:
        """Register an item under a unique name."""
        self._validate_name(name)

        if name in self._items:
            raise ModuleAlreadyRegisteredError(
                f"Module '{name}' is already registered."
            )

        self._items[name] = item

    def retrieve(self, name: str) -> T:
        """Retrieve a registered item."""
        self._validate_name(name)

        try:
            return self._items[name]

        except KeyError:
            raise ModuleNotFoundError(
                f"Module '{name}' is not registered."
            ) from None

    def is_registered(self, name: str) -> bool:
        """Return True if an item exists in the registry."""
        return name in self._items
    