# Author: TOLU_OLUSEGUN
# Date: 4/24/2026
# File: user.py
# Description:

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from extensions import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)

    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    mlb_players = db.relationship("MLBPlayer", back_populates="creator", lazy=True)
    nba_players = db.relationship("NBAPlayer", back_populates="creator", lazy=True)
    nfl_players = db.relationship("NFLPlayer", back_populates="creator", lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"