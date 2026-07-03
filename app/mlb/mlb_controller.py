from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user

from app.sport.sport import Sport
from app.mlb.mlb_manager import MLBManager


class MLBController:
    # Controller for MLB pages.
    # The controller receives requests from routes, calls manager methods
    # to work with the database, and returns templates to the user.
    @staticmethod
    def index():
        # Display the MLB list page.
        # The page supports filtering by team and sorting by selected fields.
        team = request.args.get("team", "").strip()
        sort_by = request.args.get("sort", "").strip()

        players = MLBManager.get_all_players(
            team=team,
            sort_by=sort_by
        )

        total_count = MLBManager.get_player_count()
        filtered_count = MLBManager.get_filtered_count(team=team)
        teams = MLBManager.get_all_teams()

        return render_template(
            "mlb/index.html",
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

        players = MLBManager.search_players(
            query_text=query,
            search_field=search_field
        )

        return render_template(
            "mlb/search.html",
            query=query,
            search_field=search_field,
            players=players
        )

    @staticmethod
    def detail(player_id):
        # Display player form.
        player = MLBManager.get_player_by_id(player_id)

        return render_template(
            "mlb/detail.html",
            player=player
        )

    @staticmethod
    def create():
        # Display and process the create form.
        # GET request: show the blank form.
        # POST request: validate form data, create a new record, and save it.
        if request.method == "POST":
            errors = MLBManager.validate_form_data(request.form)

            if errors:
                return render_template(
                    "mlb/create.html",
                    errors=errors,
                    form_data=request.form
                )

            sport = Sport.query.filter_by(league="MLB").first()

            if not sport:
                flash("MLB sport record was not found.", "error")
                return redirect(url_for("mlb.index"))

            MLBManager.create_player(request.form, sport.id, current_user.id)
            flash("MLB player created successfully.", "success")

            return redirect(url_for("mlb.index"))

        return render_template(
            "mlb/create.html",
            errors=[],
            form_data={}
        )

    @staticmethod
    def edit(player_id):
        # Display and process the edit form.
        player = MLBManager.get_player_by_id(player_id)

        if not MLBManager.can_manage_player(current_user, player):
            flash("You are not allowed to edit this MLB player.", "error")
            return redirect(url_for("mlb.detail", player_id=player.id))

        if request.method == "POST":
            errors = MLBManager.validate_form_data(request.form)

            if errors:
                return render_template(
                    "mlb/edit.html",
                    player=player,
                    errors=errors,
                    form_data=request.form
                )

            MLBManager.update_player(player, request.form)
            flash("MLB player updated successfully.", "success")

            return redirect(url_for("mlb.detail", player_id=player.id))

        return render_template(
            "mlb/edit.html",
            player=player,
            errors=[],
            form_data={}
        )

    @staticmethod
    def delete(player_id):
        # Display and process the delete form.
        player = MLBManager.get_player_by_id(player_id)

        if not MLBManager.can_manage_player(current_user, player):
            flash("You are not allowed to delete this MLB player.", "error")
            return redirect(url_for("mlb.detail", player_id=player.id))

        if request.method == "POST":
            MLBManager.delete_player(player)
            flash("MLB player deleted successfully.", "success")

            return redirect(url_for("mlb.index"))

        return render_template(
            "mlb/delete.html",
            player=player
        )