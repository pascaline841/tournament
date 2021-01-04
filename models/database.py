from models.players import Player
from models.tournaments import Tournament
from models.rounds import Round
from tinydb import TinyDB, Query


class Data:
    def data_actors(self, actors_table):
        """ Enter actor's informations in the database."""
        ser_player = Player.serialized_player(self)
        if ser_player in actors_table:
            actors_table.update(ser_player)
        else:
            actors_table.insert(ser_player)
        return ser_player

    def data_tournament(self, players, actors_table, players_table, tournament_table):
        """ Enter players and tournament informations in the database."""

        list_players = []
        for player in players:
            ser_player = Data.data_actors(player, actors_table)
            list_players.append(ser_player)
            players_table.insert(ser_player)
        Tournament.serialized_tournament(self)
        tournament_table.insert(
            {
                "name": self.name,
                "location": self.location,
                "date": self.date,
                "mode": self.mode,
                "rounds": self.rounds,
                "matches": self.matches,
                "description": self.description,
                "players": list_players,
            }
        )

    def update_tournament(self, tournament_table, players_table, tournament):
        """ Update tournament's rounds and matches in the database."""

        ser_round = Round.serialized_round(self)

        tournament_table.update(
            {
                "rounds": ser_round,
            },
            doc_ids=[tournament.name],
        )

        """
        for player in ser_players:
            players_table.update(
                {"rank", "score game"},
            )
        """

    def update_rank(actors_table, players_table, user):
        """Update actor/player rank in the datatbase."""
        first_name = input("First name ? ").capitalize()
        last_name = input("Last name ? ").capitalize()
        new_rank = int(input("New rank ? "))
        actors_table.update(
            {"rank": new_rank},
            user["first name"] == first_name and user["last name"] == last_name,
        )
        players_table.update(
            {"rank": new_rank},
            user["first name"] == first_name and user["last name"] == last_name,
        )

    def update_score(actors_table, players_table, score):
        """Update actor/player score in the database."""
        actors_table.update({"score": score})
        players_table.update({"score": score})

    def sorted_actors(actors_table):
        """Sort all actors by alphabetic order or by rank."""
        actors = actors_table.all()
        sorted_choice = int(input("Sorted by Last Name (1) or by Rank (2) ? "))
        if sorted_choice == 1:
            return sorted(actors, key=lambda actor: actor["last name"])
        else:
            return sorted(actors, key=lambda actor: actor["rank"])

    def request_tournament(tournament_table, user):
        """Request for a tournament to display its rounds or matches."""
        date = input("Tournament's date ? (format : DD/MM/YYYY)")
        choice = tournament_table.search(user["date"] == date)
        request_tournament = int(input("Display ROUNDS(1) or MATCHES(2) ? "))
        if request_tournament == 1:
            return choice[0].get("rounds")
        else:
            return choice[0].get("matches")

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

    def truncate_data(players_table):
        """Allows you to delete the tables from the database."""
        players_table.truncate()
