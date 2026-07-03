from extensions import db
from app.mlb.mlb import MLBPlayer


class MLBManager:
    # Manager for MLB database operations.
    # This class keeps database queries separate from routes and templates.
    @staticmethod
    def get_all_players(team=None, sort_by=None):
        # Return MLB players with optional team filtering and sorting
        # This method uses SQLAlchemy ORM queries instead of raw SQL.
        query = MLBPlayer.query

        if team:
            # Filter records if the user selected a specific team.
            query = query.filter(MLBPlayer.team == team)
            # Sort records based on the selected dropdown option.
        if sort_by == "player":
            query = query.order_by(MLBPlayer.player.asc())
        elif sort_by == "team":
            query = query.order_by(MLBPlayer.team.asc())
        elif sort_by == "metric_1":
            query = query.order_by(MLBPlayer.metric_1.desc())
        elif sort_by == "metric_2":
            query = query.order_by(MLBPlayer.metric_2.desc())
        elif sort_by == "metric_3":
            query = query.order_by(MLBPlayer.metric_3.desc())
        elif sort_by == "metric_4":
            query = query.order_by(MLBPlayer.metric_4.desc())
        else:
            query = query.order_by(MLBPlayer.team.asc(), MLBPlayer.player.asc())

        return query.all()

    @staticmethod
    def search_players(query_text=None, search_field="all"):
        # Search only this sport's player table
        # Search a specific field if the user selected one
        # Search all searchable fields if the user selected All Properties.
        query = MLBPlayer.query

        if not query_text:
            return []

        search_pattern = f"%{query_text}%"

        if search_field == "game_id":
            query = query.filter(MLBPlayer.game_id.ilike(search_pattern))
        elif search_field == "league":
            query = query.filter(MLBPlayer.league.ilike(search_pattern))
        elif search_field == "team":
            query = query.filter(MLBPlayer.team.ilike(search_pattern))
        elif search_field == "player":
            query = query.filter(MLBPlayer.player.ilike(search_pattern))
        else:
            query = query.filter(
                (MLBPlayer.game_id.ilike(search_pattern)) |
                (MLBPlayer.league.ilike(search_pattern)) |
                (MLBPlayer.team.ilike(search_pattern)) |
                (MLBPlayer.player.ilike(search_pattern))
            )

        return query.order_by(MLBPlayer.team.asc(), MLBPlayer.player.asc()).all()

    @staticmethod
    def get_player_count():
        return MLBPlayer.query.count()

    @staticmethod
    def get_filtered_count(team=None):
        query = MLBPlayer.query

        if team:
            query = query.filter(MLBPlayer.team == team)

        return query.count()

    @staticmethod
    def get_all_teams():
        teams = MLBPlayer.query.with_entities(MLBPlayer.team).distinct().order_by(MLBPlayer.team.asc()).all()
        return [team[0] for team in teams]

    @staticmethod
    def get_player_by_id(player_id):
        # Get one player by ID or return a 404 error if not found.
        return MLBPlayer.query.get_or_404(player_id)

    @staticmethod
    def can_manage_player(user, player):
        # Check whether a user is allowed to edit or delete a player.
        # Admin users can manage all records. Regular users can only manage records they created.
        if not user.is_authenticated:
            return False

        if user.is_admin:
            return True

        return player.created_by_user_id == user.id

    @staticmethod
    def validate_form_data(form):
        # Validate the create/edit form before saving data.
        errors = []

        required_fields = ["game_id", "league", "team", "player", "metric_1", "metric_2", "metric_3", "metric_4"]

        for field in required_fields:
            if not form.get(field, "").strip():
                errors.append(f"{field.replace('_', ' ').title()} is required.")

        try:
            int(form.get("metric_1", ""))
        except ValueError:
            errors.append("Metric 1 must be a whole number.")

        try:
            int(form.get("metric_2", ""))
        except ValueError:
            errors.append("Metric 2 must be a whole number.")

        try:
            float(form.get("metric_3", ""))
        except ValueError:
            errors.append("Metric 3 must be a decimal number.")

        try:
            int(form.get("metric_4", ""))
        except ValueError:
            errors.append("Metric 4 must be a whole number.")

        return errors

    @staticmethod
    def create_player(form, sport_id, user_id):
        # Create a new player record from form data.
        player = MLBPlayer(
            game_id=form.get("game_id").strip(),
            league=form.get("league").strip(),
            team=form.get("team").strip(),
            player=form.get("player").strip(),
            metric_1=int(form.get("metric_1")),
            metric_2=int(form.get("metric_2")),
            metric_3=float(form.get("metric_3")),
            metric_4=int(form.get("metric_4")),
            sport_id=sport_id,
            created_by_user_id=user_id
        )

        db.session.add(player)
        db.session.commit()

        return player

    @staticmethod
    def update_player(player, form):
        # Update an existing player record using submitted form data.
        player.game_id = form.get("game_id").strip()
        player.league = form.get("league").strip()
        player.team = form.get("team").strip()
        player.player = form.get("player").strip()
        player.metric_1 = int(form.get("metric_1"))
        player.metric_2 = int(form.get("metric_2"))
        player.metric_3 = float(form.get("metric_3"))
        player.metric_4 = int(form.get("metric_4"))

        db.session.commit()

        return player

    @staticmethod
    def delete_player(player):
        # Delete a player record from the database.
        db.session.delete(player)
        db.session.commit()
