# Author: TOLU_OLUSEGUN
# Date: 4/24/2026
# File: nfl_routes.py
# Description:

from flask import Blueprint
from flask_login import login_required

from app.nfl.nfl_controller import NFLController


nfl_bp = Blueprint(
    "nfl",
    __name__,
    url_prefix="/nfl",
    template_folder="templates",
    static_folder="static"
)


@nfl_bp.route("/")
def index():
    # Display the NFL player list page
    return NFLController.index()


@nfl_bp.route("/search")
def search():
    # Display the NFL-only search page
    return NFLController.search()


@nfl_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    # Display and process the NFL create form.
    # This route is protected, only logged-in users can create new player records.
    return NFLController.create()


@nfl_bp.route("/<int:player_id>")
def detail(player_id):
    # Display one NFL player record by ID
    return NFLController.detail(player_id)


@nfl_bp.route("/<int:player_id>/edit", methods=["GET", "POST"])
@login_required
def edit(player_id):
    # Display and process the NFL edit form.
    # This route is protected. Only authenticated and authorized users can edit records
    return NFLController.edit(player_id)


@nfl_bp.route("/<int:player_id>/delete", methods=["GET", "POST"])
@login_required
def delete(player_id):
    # Display and process the NBA delete form.
    # This route is protected. Only authenticated and authorized users can delete records
    return NFLController.delete(player_id)