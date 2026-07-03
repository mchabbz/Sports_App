# Author: TOLU_OLUSEGUN
# Date: 4/24/2026
# File: user_manager.py
# Description:

from app.mlb.mlb import MLBPlayer
from app.nba.nba import NBAPlayer
from app.nfl.nfl import NFLPlayer


class UserManager:
    # UserManager retrieves data related to the logged-in user.
    @staticmethod
    def get_user_mlb_players(user):
        # Get MLB records created by the current user.
        return MLBPlayer.query.filter_by(
            created_by_user_id=user.id
        ).order_by(MLBPlayer.player.asc()).all()

    @staticmethod
    def get_user_nba_players(user):
        # Get NBA records created by the current user.
        return NBAPlayer.query.filter_by(
            created_by_user_id=user.id
        ).order_by(NBAPlayer.player.asc()).all()

    @staticmethod
    def get_user_nfl_players(user):
        # Get NFL records created by the current user.
        return NFLPlayer.query.filter_by(
            created_by_user_id=user.id
        ).order_by(NFLPlayer.player.asc()).all()

    @staticmethod
    def get_user_created_counts(user):
        # Count how many records the current user created in each league.
        mlb_count = MLBPlayer.query.filter_by(created_by_user_id=user.id).count()
        nba_count = NBAPlayer.query.filter_by(created_by_user_id=user.id).count()
        nfl_count = NFLPlayer.query.filter_by(created_by_user_id=user.id).count()

        return {
            "mlb_count": mlb_count,
            "nba_count": nba_count,
            "nfl_count": nfl_count,
            "total_count": mlb_count + nba_count + nfl_count
        }