class Data:
    """Define the database."""

    def sorted_actors(actors_table):
        """Sort all actors by alphabetic order or by rank."""
        actors = actors_table.all()
        sorted_choice = int(input("Sorted by Last Name (1) or by Rank (2) ? "))
        if sorted_choice == 1:
            return sorted(actors, key=lambda actor: actor["last name"])
        else:
            return sorted(actors, key=lambda actor: actor["rank"])

    def request_tournament(tournament_table, user):
        """Request for a tournament to display its rounds or matchs."""
        date = input("Tournament's date ? (format : DD/MM/YYYY)")
        choice = tournament_table.search(user["date"] == date)
        request_tournament = int(input("Display ROUNDS(1) or MATCHS(2) ? "))
        if request_tournament == 1:
            return choice[0].get("rounds")
        else:
            return choice[0].get("matchs")

    def request_players(tournament_table, user):
        """Request for a tournament to display its players by alpha order or rank."""
        date = input("Tournament's date ? (format : DD/MM/YYYY) ")
        choice = tournament_table.search(user["date"] == date)
        players = choice[0].get("players")
        sorted_choice = int(input("Sorted by Last Name (1) or by Rank (2) ? "))
        if sorted_choice == 1:
            return sorted(players, key=lambda players: players["last name"])
        else:
            return sorted(players, key=lambda players: players["rank"])
