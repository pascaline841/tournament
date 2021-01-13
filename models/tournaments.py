import datetime
from models.players import Player
from models.rounds import Round


class Tournament:
    """Define the characteristics of a chess tournament."""

    def __init__(self, name, location, mode, description, players):
        """
        Name :
        Location :
        Date : AUTO
        Mode : bullet / blitz / fast
        Rounds : 4 (default)
        Description : general remarks from the tournament director.
        Players : list of player's  stored in the database.
        """
        self.name = name
        self.location = location
        self.date = datetime.date.today().strftime("%d/%m/%Y")
        self.mode = mode
        self.nb_rounds = 4
        self.rounds = []
        self.matchs = []
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

    def store_data_tournament(self, players, user, actors_table, tournament_table):
        """Store tournament's informations in the database."""
        serialized_players = []
        serialized_rounds = []
        for player in players:
            ser_player = Player.store_data_actors(player, user, actors_table)
            serialized_players.append(ser_player)
        Tournament.serialized_tournament(self)
        tournament_table.insert(
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

    def update_round(self, serialized_rounds, tournament_table, user):
        """Update round's informations in the database."""
        tournament_table.update(
            {"rounds": serialized_rounds},
            user["name"] == self.name,
        )

    @classmethod
    def deserialized_tournament(cls, serialized_tournament):
        """Pull tournament's informations from the database to continue it."""
        name = serialized_tournament["name"]
        location = serialized_tournament["location"]
        date = serialized_tournament["date"]
        mode = serialized_tournament["mode"]
        rounds = [
            Round.deserialized_round(ser_round)
            for ser_round in serialized_tournament["rounds"]
        ]
        description = serialized_tournament["description"]
        players = [
            Player.deserialized_player(ser_player)
            for ser_player in serialized_tournament["players"]
        ]
        return Tournament(name, location, date, mode, rounds, description, players)
