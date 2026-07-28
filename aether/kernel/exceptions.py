class ModuleAlreadyRegisteredError(Exception):
    """Raised when attempting to register a module that already exists."""
    pass


class ModuleNotFoundError(Exception):
    """Raised when a requested module does not exist."""
    pass
