from flask import Blueprint
from flask_login import login_required

from app.mlb.mlb_controller import MLBController


mlb_bp = Blueprint(
    "mlb",
    __name__,
    url_prefix="/mlb",
    template_folder="templates",
    static_folder="static"
)


@mlb_bp.route("/")
def index():
    # Display the MLB player list page
    return MLBController.index()


@mlb_bp.route("/search")
def search():
    # Display the MLB-only search page
    return MLBController.search()


@mlb_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    # Display and process the MLB create form.
    # This route is protected, only logged-in users can create new player records.
    return MLBController.create()


@mlb_bp.route("/<int:player_id>")
def detail(player_id):
    # Display one MLB player record by ID
    return MLBController.detail(player_id)


@mlb_bp.route("/<int:player_id>/edit", methods=["GET", "POST"])
@login_required
def edit(player_id):
    # Display and process the MLB edit form.
    # This route is protected. Only authenticated and authorized users can edit records
    return MLBController.edit(player_id)


@mlb_bp.route("/<int:player_id>/delete", methods=["GET", "POST"])
@login_required
def delete(player_id):
    # Display and process the MLB delete form.
    # This route is protected. Only authenticated and authorized users can delete records
    return MLBController.delete(player_id)