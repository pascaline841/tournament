from models.players import Player
from models.rounds import Round


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
        return {
            " NAME : {}\n LOCATION : {}\n MODE : {}\n DATE : {}\n ROUNDS : {}\n DESCRIPTION : {}\n PLAYERS :{}\n".format(
                self.name,
                self.location,
                self.mode,
                self.date,
                self.rounds,
                self.description,
                self.players,
            )
        }

    def serialized_tournament(self):
        """Serialize tournament's data."""
        return {
            "name": self.name,
            "location": self.location,
            "date": self.date,
            "mode": self.mode,
            "rounds": self.rounds,
            "description": self.description,
            "players": self.players,
        }

    @classmethod
    def deserialized_tournament(cls, serialized_tournament):
        """Pull tournament's informations from the database to continue it."""
        name = serialized_tournament["name"]
        location = serialized_tournament["location"]
        date = serialized_tournament["date"]
        mode = serialized_tournament["mode"]
        players = [
            Player.deserialized_player(ser_player)
            for ser_player in serialized_tournament["players"]
        ]
        rounds = [
            Round.deserialized_round(serialized_round)
            for serialized_round in serialized_tournament["rounds"]
        ]
        description = serialized_tournament["description"]

        return Tournament(name, location, date, mode, rounds, description, players)

    def store_data_tournament(self, players, user, actors_table, tournaments_table):
        """Store tournament's informations in the database."""
        serialized_players = []
        serialized_rounds = []
        for player in players:
            ser_player = Player.store_data_actors(player, user, actors_table)
            serialized_players.append(ser_player)
        Tournament.serialized_tournament(self)
        tournaments_table.insert(
            {
                "name": self.name,
                "location": self.location,
                "date": self.date,
                "mode": self.mode,
                "rounds": serialized_rounds,
                "description": self.description,
                "players": serialized_players,
            }
        )

    def update_round(self, serialized_rounds, tournaments_table, user):
        """Update round's informations in the database."""
        tournaments_table.update(
            {"rounds": serialized_rounds}, user["name"] == self.name
        )

    def update_players(self, players, tournaments_table, user):
        """Update players's informations in the database."""
        serialized_players = []
        for player in players:
            ser_player = Player.serialized_player(player)
            serialized_players.append(ser_player)
        tournaments_table.update(
            {
                "players": serialized_players,
            },
            user["name"] == self.name,
        )
        del serialized_players[:]
