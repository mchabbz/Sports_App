# Author: TOLU_OLUSEGUN
# Date: 4/24/2026
# File: auth_manager.py
# Description:

from extensions import db
from app.user.user import User


class AuthManager:
    # AuthManager handles user registration and login database logic.
    @staticmethod
    def get_user_by_email(email):
        # Look up a user by email for login.
        return User.query.filter_by(email=email.lower().strip()).first()

    @staticmethod
    def get_user_by_username(username):
        # Look up a user by username to prevent duplicate accounts.
        return User.query.filter_by(username=username.strip()).first()

    @staticmethod
    def validate_registration(form):
        # Validate registration form fields before creating a user.
        errors = []

        username = form.get("username", "").strip()
        email = form.get("email", "").lower().strip()
        password = form.get("password", "")
        confirm_password = form.get("confirm_password", "")

        if not username:
            errors.append("Username is required.")

        if not email:
            errors.append("Email is required.")

        if not password:
            errors.append("Password is required.")

        if len(password) < 6:
            errors.append("Password must be at least 6 characters long.")

        if password != confirm_password:
            errors.append("Passwords do not match.")

        if username and AuthManager.get_user_by_username(username):
            errors.append("That username is already taken.")

        if email and AuthManager.get_user_by_email(email):
            errors.append("That email is already registered.")

        return errors

    @staticmethod
    def create_user(form):
        # The first registered user is automatically assigned admin privileges
        # Create a new user and hash their password before saving.
        username = form.get("username").strip()
        email = form.get("email").lower().strip()
        password = form.get("password")

        first_user = User.query.count() == 0

        user = User(
            username=username,
            email=email,
            is_admin=first_user
        )

        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return user

    @staticmethod
    def validate_login(form):
        # Validate login credentials and return the matching user if successful.
        errors = []

        email = form.get("email", "").lower().strip()
        password = form.get("password", "")

        if not email:
            errors.append("Email is required.")

        if not password:
            errors.append("Password is required.")

        user = AuthManager.get_user_by_email(email)

        if not user or not user.check_password(password):
            errors.append("Invalid email or password.")
            return errors, None

        return errors, user