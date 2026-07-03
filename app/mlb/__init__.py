from flask import Blueprint

bp = Blueprint('mlb', __name__,
               url_prefix="/nfl",
               static_folder="static",
               template_folder='templates'
)

# Import routes after the Blueprint is defined to associate routes with the blueprint.
# Ignore the "module level import not at top of file" warning.
from . import mlb_routes
