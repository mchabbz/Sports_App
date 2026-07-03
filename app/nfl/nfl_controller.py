# Author: TOLU_OLUSEGUN
# Date: 4/24/2026
# File: nfl_controller.py
# Description:

from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user

from app.sport.sport import Sport
from app.nfl.nfl_manager import NFLManager


class NFLController:
    # Controller for NFL pages.
    # The controller receives requests from routes, calls manager methods
    # to work with the database, and returns templates to the user.
    @staticmethod
    def index():
        # Display the NFL list page.
        # The page supports filtering by team and sorting by selected fields.
        team = request.args.get("team", "").strip()
        sort_by = request.args.get("sort", "").strip()

        players = NFLManager.get_all_players(
            team=team,
            sort_by=sort_by
        )

        total_count = NFLManager.get_player_count()
        filtered_count = NFLManager.get_filtered_count(team=team)
        teams = NFLManager.get_all_teams()

        return render_template(
            "nfl/index.html",
            players=players,
            total_count=total_count,
            filtered_count=filtered_count,
            teams=teams,
            selected_team=team,
            selected_sort=sort_by
        )

    @staticmethod
    def search():
        # Search and Display player in the sport
        query = request.args.get("q", "").strip()
        search_field = request.args.get("field", "all").strip()

        players = NFLManager.search_players(
            query_text=query,
            search_field=search_field
        )

        return render_template(
            "nfl/search.html",
            query=query,
            search_field=search_field,
            players=players
        )

    @staticmethod
    def detail(player_id):
        # Display player form.
        player = NFLManager.get_player_by_id(player_id)

        return render_template(
            "nfl/detail.html",
            player=player
        )

    @staticmethod
    def create():
        # Display and process the create form.
        # GET request: show the blank form.
        # POST request: validate form data, create a new record, and save it.
        if request.method == "POST":
            errors = NFLManager.validate_form_data(request.form)

            if errors:
                return render_template(
                    "nfl/create.html",
                    errors=errors,
                    form_data=request.form
                )

            sport = Sport.query.filter_by(league="NFL").first()

            if not sport:
                flash("NFL sport record was not found.", "error")
                return redirect(url_for("nfl.index"))

            NFLManager.create_player(
                request.form,
                sport.id,
                current_user.id
            )

            flash("NFL player created successfully.", "success")

            return redirect(url_for("nfl.index"))

        return render_template(
            "nfl/create.html",
            errors=[],
            form_data={}
        )

    @staticmethod
    def edit(player_id):
        # Display and process the edit form.
        player = NFLManager.get_player_by_id(player_id)

        if not NFLManager.can_manage_player(current_user, player):
            flash("You are not allowed to edit this NFL player.", "error")
            return redirect(url_for("nfl.detail", player_id=player.id))

        if request.method == "POST":
            errors = NFLManager.validate_form_data(request.form)

            if errors:
                return render_template(
                    "nfl/edit.html",
                    player=player,
                    errors=errors,
                    form_data=request.form
                )

            NFLManager.update_player(player, request.form)
            flash("NFL player updated successfully.", "success")

            return redirect(url_for("nfl.detail", player_id=player.id))

        return render_template(
            "nfl/edit.html",
            player=player,
            errors=[],
            form_data={}
        )

    @staticmethod
    def delete(player_id):
        # Display and process the delete form.
        player = NFLManager.get_player_by_id(player_id)

        if not NFLManager.can_manage_player(current_user, player):
            flash("You are not allowed to delete this NFL player.", "error")
            return redirect(url_for("nfl.detail", player_id=player.id))

        if request.method == "POST":
            NFLManager.delete_player(player)
            flash("NFL player deleted successfully.", "success")

            return redirect(url_for("nfl.index"))

        return render_template(
            "nfl/delete.html",
            player=player
        )