# Author: TOLU_OLUSEGUN
# Date: 4/24/2026
# File: auth_controller.py
# Description:

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from app.auth.auth_manager import AuthManager


class AuthController:
    # AuthController handles registration, login, and logout request logic.
    @staticmethod
    def register():
        if current_user.is_authenticated:
            return redirect(url_for("user.profile"))

        if request.method == "POST":
            errors = AuthManager.validate_registration(request.form)

            if errors:
                return render_template(
                    "auth/register.html",
                    errors=errors,
                    form_data=request.form
                )

            user = AuthManager.create_user(request.form)
            login_user(user)

            if user.is_admin:
                flash("Account created successfully. You are the admin user.", "success")
            else:
                flash("Account created successfully.", "success")

            return redirect(url_for("user.profile"))

        return render_template(
            "auth/register.html",
            errors=[],
            form_data={}
        )

    @staticmethod
    def login():
        # If a logged-in user visits register or login, redirect them to their profile
        # Log the user in after successful registration.
        if current_user.is_authenticated:
            return redirect(url_for("user.profile"))

        if request.method == "POST":
            errors, user = AuthManager.validate_login(request.form)

            if errors:
                return render_template(
                    "auth/login.html",
                    errors=errors,
                    form_data=request.form
                )

            login_user(user)
            flash("You logged in successfully.", "success")

            return redirect(url_for("user.profile"))

        return render_template(
            "auth/login.html",
            errors=[],
            form_data={}
        )

    @staticmethod
    @login_required
    def logout():
        # logout_user clears the current user's login session.
        logout_user()
        flash("You logged out successfully.", "success")
        return redirect(url_for("index"))