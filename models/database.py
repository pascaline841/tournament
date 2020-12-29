from models.players import Player
from models.tournaments import Tournament
from models.rounds import Round
from tinydb import TinyDB, Query


class Data:
    def __init__(self, db):
        self.db = TinyDB("db.json")
        self.tournament_table = db.table("TOURNAMENTS")
        self.actors_table = db.table("ACTORS")
        self.players_by_tournament = db.table("PLAYERS")
        self.rounds_table = db.table("ROUNDS")
        self.matches_table = db.table("MATCHES")
        self.user = Query()

    def data_tournament(
        self, players, actors_table, players_by_tournament, tournament_table
    ):
        """ Enter players and tournament informations in the database."""
        Tournament.serialized_tournament(self)
        list_players = []
        for player in players:
            ser_player = Player.serialized_player(player)
            if ser_player not in actors_table:
                actors_table.insert(ser_player)
            list_players.append(ser_player)
            players_by_tournament.insert(ser_player)

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

    def data_actors(self, actors_table):
        """ Enter actor's informations in the database."""
        ser_player = Player.serialized_player(self)
        if ser_player not in actors_table:
            actors_table.insert(ser_player)

    def update_tournament(
        rounds,
        tournament_table,
        players_by_tournement,
        rounds_table,
        matches_table,
    ):
        """ Update tournament's rounds and matches in the database."""
        ser_players = players_by_tournement.all()
        ser_match = matches_table.all()
        tournament = tournament_table.all()
        for round in rounds:
            ser_round = Round.serialized_round(round)
            rounds_table.insert(ser_round)
            """for match in round.list_match:
                ser_match = {
                    "player 1": player.first_name,
                    "score payer 1": player.score_game,
                    "player 2": player.first_name,
                    "score payer 2": player.score_game,
                }
                matches_table.insert(ser_match)
        for player in ser_players:
            players_by_tournement.update(
                {
                    "rank": self.rank,
                    "score game": self.score_game,
                },
            )"""

        id_tournament = len(tournament)
        tournament_table.update(
            {
                "rounds": ser_round,
                "matches": ser_match,
                "players": ser_players,
            },
            doc_ids=[id_tournament],
        )

    def update_rank(actors_table, players_by_tournament, user):
        """Update actor/player rank in the datatbase."""
        first_name = input("First name ? ").capitalize()
        last_name = input("Last name ? ").capitalize()
        new_rank = int(input("New rank ? "))
        actors_table.update(
            {"rank": new_rank},
            user["first name"] == first_name and user["last name"] == last_name,
        )
        players_by_tournament.update(
            {"rank": new_rank},
            user["first name"] == first_name and user["last name"] == last_name,
        )

    def update_score(actors_table, players_by_tournament, score):
        """Update actor/player score in the database."""
        actors_table.update({"score": score})
        players_by_tournament.update({"score": score})

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

    def truncate_data(players_by_tournament, matches_table, rounds_table):
        """Allows you to delete the tables from the database"""
        players_by_tournament.truncate("PLAYERS")
        matches_table.truncate("MATCHES")
        rounds_table.truncate("ROUNDS")
