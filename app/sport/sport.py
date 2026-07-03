# Author: TOLU_OLUSEGUN
# Date: 4/23/2026
# File: sport.py
# Description: The parent model for MLB, NBA, and NFL.

from extensions import db


class Sport(db.Model):
    # Each Sport record represents one league category, such as MLB, NBA, or NFL.
    __tablename__ = "sports"

    id = db.Column(db.Integer, primary_key=True)
    league = db.Column(db.String(20), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    # Relationships connect each sport to its related player records.
    mlb_players = db.relationship("MLBPlayer", back_populates="sport", lazy=True)
    nba_players = db.relationship("NBAPlayer", back_populates="sport", lazy=True)
    nfl_players = db.relationship("NFLPlayer", back_populates="sport", lazy=True)

    def __repr__(self):
        return f"<Sport {self.league}>"