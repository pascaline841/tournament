from tinydb import TinyDB, Query

from .player import Player
from .round import Round


class Tournament:
    """
    Define the characteristics of a chess tournament.
    Attrs:
        name (str)
        location (str)
        date (int) : AUTOMATIC
        mode (str)
        nb_rounds (int): 4 (by default)
        description (str)
        players (list) : list of player's  stored in the database.
    """

    def __init__(
        self, name, location, date, mode, nb_rounds, rounds, description, players
    ):
        """Init."""
        self.name = name
        self.location = location
        self.date = date
        self.mode = mode
        self.nb_rounds = 4
        self.rounds = rounds
        self.description = description
        self.players = players

    def __str__(self):
        return (
            f"NAME : {self.name}\n LOCATION : {self.location}\n MODE : {self.mode}\n"
            f"DATE : {self.date}\n ROUNDS : {self.rounds}\n "
            f"DESCRIPTION : {self.description}\n PLAYERS :\n{self.players}\n"
        )

    def save(self):
        """Store tournament's informations in the database."""
        db = TinyDB("TOURNAMENTS.json")
        players = [player.serialized() for player in self.players]
        tournament_copy = Tournament(
            self.name,
            self.location,
            self.date,
            self.mode,
            self.nb_rounds,
            self.rounds,
            self.description,
            players=players,
        )
        serialized_tournament = vars(tournament_copy)
        db.insert(serialized_tournament)

    @classmethod
    def deserialized(cls, serialized_tournament):
        """Pull tournament's datas from the database to continue it."""
        name = serialized_tournament["name"]
        location = serialized_tournament["location"]
        date = serialized_tournament["date"]
        mode = serialized_tournament["mode"]
        rounds = [
            Round.deserialized(serialized_round)
            for serialized_round in serialized_tournament["rounds"]
        ]
        nb_rounds = serialized_tournament["nb_rounds"] - len(rounds)
        description = serialized_tournament["description"]
        players = [
            Player.deserialized(serialized_player)
            for serialized_player in serialized_tournament["players"]
        ]
        return Tournament(
            name, location, date, mode, nb_rounds, rounds, description, players
        )

    @classmethod
    def get(cls, name):
        """Get a tournament from the database if exists."""
        db = TinyDB("TOURNAMENTS.json")
        query = Query()
        serialized_tournament = db.get(query["name"] == name)
        if serialized_tournament:
            return Tournament.deserialized(serialized_tournament)
        return None

    def update_round(self, serialized_rounds):
        """Update round's informations in the database."""
        db = TinyDB("TOURNAMENTS.json")
        query = Query()
        db.update({"rounds": serialized_rounds}, query["name"] == self.name)

    def update_players(self, players):
        """Update players' informations in the database."""
        db = TinyDB("TOURNAMENTS.json")
        query = Query()
        serialized_players = []
        for player in players:
            serialized_player = Player.serialized(player)
            serialized_players.append(serialized_player)
        db.update(
            {
                "players": serialized_players,
            },
            query["name"] == self.name,
        )
        del serialized_players[:]
