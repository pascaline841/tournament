from models.players import Player


class Data:
    """Define the database."""

    @classmethod
    def sorted_actors(cls, actors_table):
        """Sort all actors by alphabetic order or by rank."""
        actors = actors_table.all()
        sorted_choice = int(input("Sorted by Last Name (1) or by Rank (2) ? "))
        if sorted_choice == 1:
            return sorted(actors, key=lambda actor: actor["last name"])
        else:
            return sorted(actors, key=lambda actor: actor["rank"])

    @classmethod
    def request_rounds(cls, tournament_table, user):
        """Request for a tournament to display its rounds or matchs."""
        name = input("What is it name ? ")
        choice = tournament_table.search(user["name"] == name)
        return choice[0].get("rounds")

    @classmethod
    def request_players(cls, tournament_table, user):
        """Request for a tournament to display its players by alpha order or rank."""
        name = input("What is it name ? ")
        choice = tournament_table.search(user["name"] == name)
        players = choice[0].get("players")
        sorted_choice = int(input("Sorted by Last Name (1) or by Rank (2) ? "))
        if sorted_choice == 1:
            return sorted(players, key=lambda players: players["last name"])
        else:
            return sorted(players, key=lambda players: players["rank"])

    @classmethod
    def update_players(cls, players, tournament_table, tournament, user):
        """ Update players's informations in the database."""
        serialized_players = []
        for player in players:
            ser_player = Player.serialized_player(player)
            serialized_players.append(ser_player)
        tournament_table.update(
            {
                "players": serialized_players,
            },
            user["name"] == tournament.name,
        )
        del serialized_players[:]

    @classmethod
    def update_rank(cls, actors_table, tournament_table, user):
        """Update actor's rank in the datatbase and in the current tournament."""
        first_name = input("First name ? ").capitalize()
        last_name = input("Last name ? ").capitalize()
        new_rank = int(input("New rank ? "))
        actors_table.update(
            {"rank": new_rank},
            user["first name"] == first_name and user["last name"] == last_name,
        )
        tournament_table.update(
            {"rank": new_rank},
            user["first name"] == first_name and user["last name"] == last_name,
        )