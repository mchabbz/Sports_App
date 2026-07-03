# Author: TOLU_OLUSEGUN
# Date: 4/23/2026
# File: nfl.py
# Description:

from extensions import db


class NFLPlayer(db.Model):
    __tablename__ = "nfl_players"

    id = db.Column(db.Integer, primary_key=True)

    game_id = db.Column(db.String(50), nullable=False)
    league = db.Column(db.String(20), nullable=False)
    team = db.Column(db.String(120), nullable=False)
    player = db.Column(db.String(120), nullable=False)
    # metric_1 to metric_4 store the universal performance statistics from the CSV.
    metric_1 = db.Column(db.Integer, nullable=False)
    metric_2 = db.Column(db.Integer, nullable=False)
    metric_3 = db.Column(db.Float, nullable=False)
    metric_4 = db.Column(db.Integer, nullable=False)
    # sport_id links this player record to the Sport table.
    sport_id = db.Column(db.Integer, db.ForeignKey("sports.id"), nullable=False)
    sport = db.relationship("Sport", back_populates="nfl_players")
    # created_by_user_id links this record to the user who created it.
    created_by_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    creator = db.relationship("User", back_populates="nfl_players")

    def __repr__(self):
        return f"<NFLPlayer {self.player}>"