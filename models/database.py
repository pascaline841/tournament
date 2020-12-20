from models.players import Player
from models.tournaments import Tournament
from models.rounds import Round
from tinydb import TinyDB, Query


class Data:
    def tournament_data(self):

        tournaments_table = db.table("Tournament")
        tournaments_table.insert(
            {
                "name": self.name,
                "location": self.location,
                "date": self.date,
                "mode": self.mode,
                "rounds": self.rounds,
                "description": self.description,
                "players": self.players,
            }
        )

    def player_data(self):
        players_table = db.table("Player")
        players_table.insert(
            {
                "firt name": self.first_name,
                "last name": self.last_name,
                "birth date": self.birth_date,
                "gender": self.gender,
                "rank": self.rank,
                "score": self.score,
            }
        )


"""
tournament = create_tournament(players)
Data.tournament_data(tournament)
tournament_table = db.table("TOURNAMENT")
tournament = Query()
tournament_table.update({"name": 1025}, tournament.location == "Paris")
"""