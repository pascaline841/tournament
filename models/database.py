from models.players import Player
from models.tournaments import Tournament
from models.rounds import Round
from tinydb import TinyDB, Query


class Data:
    """Define the database."""

    def data_actors(self, user, actors_table):
        """ Store actor's informations in the database."""
        ser_player = Player.serialized_player(self)
        actors_table.update(
            {"rank": self.rank, "score": self.score},
            user["first name"] == self.first_name
            and user["last name"] == self.last_name,
        )
        if ser_player not in actors_table:
            actors_table.insert(ser_player)
        return ser_player

    def data_tournament(self, players, user, actors_table, tournament_table):
        """ Store tournament's informations in the database."""
        ser_players = []
        ser_rounds = []
        for player in players:
            ser_player = Data.data_actors(player, user, actors_table)
            ser_players.append(ser_player)
            Tournament.serialized_tournament(self)
        tournament_table.insert(
            {
                "name": self.name,
                "location": self.location,
                "date": self.date,
                "mode": self.mode,
                "rounds": ser_rounds,
                "description": self.description,
                "players": ser_players,
            }
        )

    def update_tournament(self, players, tournament_table, tournament, user):
        """ Update tournament's informations in the database after a round."""
        ser_rounds = []
        ser_players = []
        ser_round = Round.serialized_round(self)
        ser_rounds.append(ser_round)
        for player in players:
            ser_player = Player.serialized_player(player)
            ser_players.append(ser_player)
        tournament_table.update(
            {
                "rounds": ser_rounds,
                "players": ser_players,
            },
            user["name"] == tournament.name,
        )
        del ser_players[:]

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

    def update_score(self, actors_table, score, user):
        """Update actor's score in the database."""
        actors_table.update(
            {"score": score},
            user["first name"] == self.first_name
            and user["last name"] == self.last_name,
        )

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
