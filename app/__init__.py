from flask import Flask, render_template, request

from extensions import db, login_manager
from database import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev-secret-key-change-later"
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to access this page."
    login_manager.login_message_category = "error"

    from app.user.user import User
    from app.sport.sport import Sport
    from app.mlb.mlb import MLBPlayer
    from app.nba.nba import NBAPlayer
    from app.nfl.nfl import NFLPlayer

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.auth.auth_routes import auth_bp
    from app.user.user_routes import user_bp
    from app.mlb.mlb_routes import mlb_bp
    from app.nba.nba_routes import nba_bp
    from app.nfl.nfl_routes import nfl_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(mlb_bp)
    app.register_blueprint(nba_bp)
    app.register_blueprint(nfl_bp)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/search")
    def global_search():
        query = request.args.get("q", "").strip()

        mlb_results = []
        nba_results = []
        nfl_results = []

        if query:
            search_pattern = f"%{query}%"

            mlb_results = MLBPlayer.query.filter(
                (MLBPlayer.game_id.ilike(search_pattern)) |
                (MLBPlayer.league.ilike(search_pattern)) |
                (MLBPlayer.team.ilike(search_pattern)) |
                (MLBPlayer.player.ilike(search_pattern))
            ).order_by(MLBPlayer.team.asc(), MLBPlayer.player.asc()).all()

            nba_results = NBAPlayer.query.filter(
                (NBAPlayer.game_id.ilike(search_pattern)) |
                (NBAPlayer.league.ilike(search_pattern)) |
                (NBAPlayer.team.ilike(search_pattern)) |
                (NBAPlayer.player.ilike(search_pattern))
            ).order_by(NBAPlayer.team.asc(), NBAPlayer.player.asc()).all()

            nfl_results = NFLPlayer.query.filter(
                (NFLPlayer.game_id.ilike(search_pattern)) |
                (NFLPlayer.league.ilike(search_pattern)) |
                (NFLPlayer.team.ilike(search_pattern)) |
                (NFLPlayer.player.ilike(search_pattern))
            ).order_by(NFLPlayer.team.asc(), NFLPlayer.player.asc()).all()

        return render_template(
            "search.html",
            query=query,
            mlb_results=mlb_results,
            nba_results=nba_results,
            nfl_results=nfl_results
        )

    @app.errorhandler(401)
    def unauthorized(error):
        return render_template("errors/401.html"), 401

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        db.session.rollback()
        return render_template("errors/500.html"), 500

    with app.app_context():
        db.create_all()
        print("Database tables created successfully.")

    return app