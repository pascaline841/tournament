import datetime


class Tournament:
    """ Define the characteristics of a tournament."""

    def __init__(self, name, location, mode, description, players):
        """
        Name :
        Location :
        Date :
        Mode : bullet / blitz / fast
        Rounds : 4 (default)
        Players : list of indices corresponding to player's instances stored in memory
        Description : general remarks from the tournament director.
        """
        self.name = name
        self.location = location
        self.date = datetime.date.today().strftime("%d/%m/%Y")
        self.mode = mode
        self.nb_rounds = 4
        self.rounds = []
        self.matches = []
        self.description = description
        self.players = players

    def __repr__(self):
        return " NAME : {}\n LOCATION : {}\n MODE : {}\n DATE : {}\n ROUNDS : {}\n DESCRIPTION : {}\n PLAYERS :{}\n".format(
            self.name,
            self.location,
            self.mode,
            self.date,
            self.rounds,
            self.description,
            self.players,
        )

    def serialized_tournament(self):
        """serialized tournament's data"""
        return {
            "name": self.name,
            "location": self.location,
            "date": self.date,
            "mode": self.mode,
            "rounds": self.rounds,
            "matches": self.matches,
            "description": self.description,
            "players": self.players,
        }
