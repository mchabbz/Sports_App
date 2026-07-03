# Author: TOLU_OLUSEGUN
# Date: 4/24/2026
# File: nfl_exceptions.py
# Description:

class NFLError(Exception):
    """Base exception for NFL-related errors."""
    pass


class NFLValidationError(NFLError):
    """Raised when NFL form data is invalid."""
    pass


class NFLPermissionError(NFLError):
    """Raised when a user is not allowed to manage an NFL record."""
    pass


class NFLPlayerNotFoundError(NFLError):
    """Raised when an NFL player record cannot be found."""
    pass


class NFLSportNotFoundError(NFLError):
    """Raised when the NFL sport record is missing."""
    pass