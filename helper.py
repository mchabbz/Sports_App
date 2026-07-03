from app import create_app
from extensions import db

from app.user.user import User
from app.sport.sport import Sport
from app.mlb.mlb import MLBPlayer
from app.nba.nba import NBAPlayer
from app.nfl.nfl import NFLPlayer

app = create_app()