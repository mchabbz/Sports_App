# Author: TOLU_OLUSEGUN
# Date: 4/24/2026
# File: __init__.py
# Description:

from flask import Blueprint

bp = Blueprint('nfl', __name__,
               url_prefix="/nfl",
               static_folder="static",
               template_folder='templates'
)

# Import routes after the Blueprint is defined to associate routes with the blueprint.
# Ignore the "module level import not at top of file" warning.
from . import nfl_routes
