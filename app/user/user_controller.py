# Author: TOLU_OLUSEGUN
# Date: 4/24/2026
# File: user_controller.py
# Description:

from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from app.user.user_manager import UserManager


class UserController:
    # The user dashboard redirects to the profile page.
    @staticmethod
    @login_required
    def index():
        # Profile page requires the user to be logged in.
        return redirect(url_for("user.profile"))

    @staticmethod
    @login_required
    def profile():
        # Gather user-created records and counts for display on the profile page.
        counts = UserManager.get_user_created_counts(current_user)
        mlb_players = UserManager.get_user_mlb_players(current_user)
        nba_players = UserManager.get_user_nba_players(current_user)
        nfl_players = UserManager.get_user_nfl_players(current_user)

        return render_template(
            "user/profile.html",
            counts=counts,
            mlb_players=mlb_players,
            nba_players=nba_players,
            nfl_players=nfl_players
        )