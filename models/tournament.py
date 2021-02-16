from tinydb import TinyDB, Query

from models.player import Player


class Tournament:
    """Define the characteristics of a chess tournament."""

    def __init__(self, name, location, date, mode, rounds, description, players):
        """
        Name :
        Location :
        Date : AUTO
        Mode : bullet / blitz / fast
        Nb_Rounds : 4 (default)
        Description : general remarks from the tournament director.
        Players : list of player's  stored in the database.
        """
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
            f"DESCRIPTION : {self.description}\n PLAYERS :{self.players}\n"
        )

    def save(self, players):
        """Store tournament's informations in the database."""
        db = TinyDB("TOURNAMENTS.json")
        serialized_players = []
        for player in players:
            serialized_player = Player.save(player)
            serialized_players.append(serialized_player)
        serialized_tournament = vars(self)
        db.insert(serialized_tournament)

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
            serialized_player = Player.save(player)
            serialized_players.append(serialized_player)
        db.update(
            {
                "players": serialized_players,
            },
            query["name"] == self.name,
        )
        del serialized_players[:]
