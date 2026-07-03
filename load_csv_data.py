import csv
import os

from app import create_app
from extensions import db

from app.sport.sport import Sport
from app.mlb.mlb import MLBPlayer
from app.nba.nba import NBAPlayer
from app.nfl.nfl import NFLPlayer


app = create_app()


def get_or_create_sport(league):
    sport = Sport.query.filter_by(league=league).first()

    if sport:
        return sport

    if league == "MLB":
        sport = Sport(
            league="MLB",
            name="Baseball",
            description="Major League Baseball top players"
        )
    elif league == "NBA":
        sport = Sport(
            league="NBA",
            name="Basketball",
            description="National Basketball Association top players"
        )
    elif league == "NFL":
        sport = Sport(
            league="NFL",
            name="Football",
            description="National Football League top players"
        )
    else:
        sport = Sport(
            league=league,
            name=league,
            description=f"{league} top players"
        )

    db.session.add(sport)
    db.session.commit()

    return sport


def load_mlb_csv(file_path):
    sport = get_or_create_sport("MLB")

    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            player = MLBPlayer(
                game_id=row["Game_ID"],
                league=row["League"],
                team=row["Teams"],
                player=row["Players"],
                metric_1=int(row["Metric_1"]),
                metric_2=int(row["Metric_2"]),
                metric_3=float(row["Metric_3"]),
                metric_4=int(row["Metric_4"]),
                sport_id=sport.id
            )

            db.session.add(player)

    db.session.commit()
    print("MLB data loaded.")


def load_nba_csv(file_path):
    sport = get_or_create_sport("NBA")

    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            player = NBAPlayer(
                game_id=row["Game_ID"],
                league=row["League"],
                team=row["Teams"],
                player=row["Players"],
                metric_1=int(row["Metric_1"]),
                metric_2=int(row["Metric_2"]),
                metric_3=float(row["Metric_3"]),
                metric_4=int(row["Metric_4"]),
                sport_id=sport.id
            )

            db.session.add(player)

    db.session.commit()
    print("NBA data loaded.")


def load_nfl_csv(file_path):
    sport = get_or_create_sport("NFL")

    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            player = NFLPlayer(
                game_id=row["Game_ID"],
                league=row["League"],
                team=row["Teams"],
                player=row["Players"],
                metric_1=int(row["Metric_1"]),
                metric_2=int(row["Metric_2"]),
                metric_3=float(row["Metric_3"]),
                metric_4=int(row["Metric_4"]),
                sport_id=sport.id
            )

            db.session.add(player)

    db.session.commit()
    print("NFL data loaded.")


with app.app_context():
    db.drop_all()
    db.create_all()

    load_mlb_csv(os.path.join("app", "sport", "mlb.csv"))
    load_nba_csv(os.path.join("app", "sport", "nba.csv"))
    load_nfl_csv(os.path.join("app", "sport", "nfl.csv"))

    print("All CSV data loaded successfully.")