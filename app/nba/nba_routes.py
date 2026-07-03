# Author: TOLU_OLUSEGUN
# Date: 4/23/2026
# File: nba_routes.py
# Description:

from flask import Blueprint
from flask_login import login_required

from app.nba.nba_controller import NBAController


nba_bp = Blueprint(
    "nba",
    __name__,
    url_prefix="/nba",
    template_folder="templates",
    static_folder="static"
)


@nba_bp.route("/")
def index():
    # Display the NBA player list page
    return NBAController.index()


@nba_bp.route("/search")
def search():
    # Display the NBA-only search page
    return NBAController.search()


@nba_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    # Display and process the NBA create form.
    # This route is protected, only logged-in users can create new player records.
    return NBAController.create()


@nba_bp.route("/<int:player_id>")
def detail(player_id):
    # Display one NBA player record by ID
    return NBAController.detail(player_id)


@nba_bp.route("/<int:player_id>/edit", methods=["GET", "POST"])
@login_required
def edit(player_id):
    # Display and process the NBA edit form.
    # This route is protected. Only authenticated and authorized users can edit records
    return NBAController.edit(player_id)


@nba_bp.route("/<int:player_id>/delete", methods=["GET", "POST"])
@login_required
def delete(player_id):
    # Display and process the NBA delete form.
    # This route is protected. Only authenticated and authorized users can delete records
    return NBAController.delete(player_id)