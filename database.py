import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# The SQLite database file is stored inside the instance folder.
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")

os.makedirs(INSTANCE_DIR, exist_ok=True)

DATABASE_NAME = "sports_app.db"

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(INSTANCE_DIR, DATABASE_NAME)

# SQLALCHEMY_TRACK_MODIFICATIONS is disabled to avoid unnecessary overhead.
SQLALCHEMY_TRACK_MODIFICATIONS = False