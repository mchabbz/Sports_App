# Author: TOLU_OLUSEGUN
# Date: 4/24/2026
# File: nba_controller.py
# Description:

from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user

from app.sport.sport import Sport
from app.nba.nba_manager import NBAManager


class NBAController:
    # Controller for NBA pages.
    # The controller receives requests from routes, calls manager methods
    # to work with the database, and returns templates to the user.
    @staticmethod
    def index():
        # Display the NBA list page.
        # The page supports filtering by team and sorting by selected fields.
        team = request.args.get("team", "").strip()
        sort_by = request.args.get("sort", "").strip()

        players = NBAManager.get_all_players(
            team=team,
            sort_by=sort_by
        )

        total_count = NBAManager.get_player_count()
        filtered_count = NBAManager.get_filtered_count(team=team)
        teams = NBAManager.get_all_teams()

        return render_template(
            "nba/index.html",
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

        players = NBAManager.search_players(
            query_text=query,
            search_field=search_field
        )

        return render_template(
            "nba/search.html",
            query=query,
            search_field=search_field,
            players=players
        )

    @staticmethod
    def detail(player_id):
        # Display player form.
        player = NBAManager.get_player_by_id(player_id)

        return render_template(
            "nba/detail.html",
            player=player
        )

    @staticmethod
    def create():
        # Display and process the create form.
        # GET request: show the blank form.
        # POST request: validate form data, create a new record, and save it.
        if request.method == "POST":
            errors = NBAManager.validate_form_data(request.form)

            if errors:
                return render_template(
                    "nba/create.html",
                    errors=errors,
                    form_data=request.form
                )

            sport = Sport.query.filter_by(league="NBA").first()

            if not sport:
                flash("NBA sport record was not found.", "error")
                return redirect(url_for("nba.index"))

            NBAManager.create_player(
                request.form,
                sport.id,
                current_user.id
            )

            flash("NBA player created successfully.", "success")

            return redirect(url_for("nba.index"))

        return render_template(
            "nba/create.html",
            errors=[],
            form_data={}
        )

    @staticmethod
    def edit(player_id):
        # Display and process the edit form.
        player = NBAManager.get_player_by_id(player_id)

        if not NBAManager.can_manage_player(current_user, player):
            flash("You are not allowed to edit this NBA player.", "error")
            return redirect(url_for("nba.detail", player_id=player.id))

        if request.method == "POST":
            errors = NBAManager.validate_form_data(request.form)

            if errors:
                return render_template(
                    "nba/edit.html",
                    player=player,
                    errors=errors,
                    form_data=request.form
                )

            NBAManager.update_player(player, request.form)
            flash("NBA player updated successfully.", "success")

            return redirect(url_for("nba.detail", player_id=player.id))

        return render_template(
            "nba/edit.html",
            player=player,
            errors=[],
            form_data={}
        )

    @staticmethod
    def delete(player_id):
        # Display and process the delete form.
        player = NBAManager.get_player_by_id(player_id)

        if not NBAManager.can_manage_player(current_user, player):
            flash("You are not allowed to delete this NBA player.", "error")
            return redirect(url_for("nba.detail", player_id=player.id))

        if request.method == "POST":
            NBAManager.delete_player(player)
            flash("NBA player deleted successfully.", "success")

            return redirect(url_for("nba.index"))

        return render_template(
            "nba/delete.html",
            player=player
        )