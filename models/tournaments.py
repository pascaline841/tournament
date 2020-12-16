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
        self.rounds = 4
        self.description = description
        self.players = players

    def __repr__(self):
        """
        Display :
        NAME :[] LOCATION : [] MODE : [] DATE : [] DESCRIPTION : [] PLAYERS[].
        """
        return " NAME : {}\n LOCATION : {}\n MODE : {}\n DATE : {}\n DESCRIPTION : {}\n PLAYERS :{}\n".format(
            self.name,
            self.location,
            self.mode,
            self.date,
            self.description,
            self.players,
        )
