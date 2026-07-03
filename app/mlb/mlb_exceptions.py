class MLBError(Exception):
    """Base exception for MLB-related errors."""
    pass


class MLBValidationError(MLBError):
    """Raised when MLB form data is invalid."""
    pass


class MLBPermissionError(MLBError):
    """Raised when a user is not allowed to manage an MLB record."""
    pass


class MLBPlayerNotFoundError(MLBError):
    """Raised when an MLB player record cannot be found."""
    pass


class MLBSportNotFoundError(MLBError):
    """Raised when the MLB sport record is missing."""
    pass