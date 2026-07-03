# Author: TOLU_OLUSEGUN
# Date: 4/23/2026
# File: user_routes.py
# Description:

from flask import Blueprint

from app.user.user_controller import UserController


user_bp = Blueprint(
    "user",
    __name__,
    url_prefix="/user",
    template_folder="templates",
    static_folder="static"
)


@user_bp.route("/")
def index():
    return UserController.index()


@user_bp.route("/profile")
def profile():
    # The profile route displays account information and user-created records.
    return UserController.profile()