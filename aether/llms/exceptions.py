class LLMError(Exception):
    """Base class for all LLM-related exceptions."""
    pass

class ProviderError(LLMError):
    """Raised when there is an error with the LLM provider."""
    pass

class ConfigurationError(LLMError):
    """Raised when there is a configuration issue with the LLM."""
    pass

class ModelNotFoundError(LLMError):
    """Raised when a requested model does not exist."""
    pass
