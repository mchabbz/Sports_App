# Author: TOLU_OLUSEGUN
# Date: 4/24/2026
# File: nba_exceptions.py
# Description:

class NBAError(Exception):
    """Base exception for NBA-related errors."""
    pass


class NBAValidationError(NBAError):
    """Raised when NBA form data is invalid."""
    pass


class NBAPermissionError(NBAError):
    """Raised when a user is not allowed to manage an NBA record."""
    pass


class NBAPlayerNotFoundError(NBAError):
    """Raised when an NBA player record cannot be found."""
    pass


class NBASportNotFoundError(NBAError):
    """Raised when the NBA sport record is missing."""
    pass