from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# db is the SQLAlchemy database object used by all models.
db = SQLAlchemy()
# login_manager handles user login sessions for Flask-Login.
login_manager = LoginManager()