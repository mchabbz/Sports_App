# Author: TOLU_OLUSEGUN
# Date: 4/23/2026
# File: auth_routes.py
# Description:

from flask import Blueprint

from app.auth.auth_controller import AuthController


auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
    template_folder="templates",
    static_folder="static"
)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    # Register route allows new users to create accounts.
    return AuthController.register()


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    # Login route allows existing users to sign in.
    return AuthController.login()


@auth_bp.route("/logout")
def logout():
    # Logout route ends the current user's session.
    return AuthController.logout()