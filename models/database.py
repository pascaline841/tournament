from models.players import Player
from models.tournaments import Tournament
from models.rounds import Round
from tinydb import TinyDB, Query


class Data:
    def tournament_data(self):
        db = TinyDB("tournament.json")
        tournament_table = db.table("TOURNAMENT")
        tournament_table.insert(
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
        return tournament_table

    def player_data(self):
        db = TinyDB("player.json")
        players_table = db.table("PLAYER")
        players_table.insert(
            {
                "first name": self.first_name,
                "last name": self.last_name,
                "birth date": self.birth_date,
                "gender": self.gender,
                "rank": self.rank,
                "score": self.score,
            }
        )
        return players_table

    def update_rank(self, players_table):
        """update rank."""
        self = Query()
        first_name = input("First name ?")
        last_name = input("Last name ?")
        new_rank = int(input("New rank ? "))
        players_table.update(
            {"rank": new_rank},
            self["first name"] == first_name and self["last name"] == last_name,
        )

    def update_score(self, players_table):
        """update score."""
        self = Query()
        first_name = input("First name ?")
        last_name = input("Last name ?")
        new_score = int(input("New score ? "))
        players_table.update(
            {"score": new_score},
            self["first name"] == first_name and self["last name"] == last_name,
        )


"""
tournament = create_tournament(players)
Data.tournament_data(tournament)
tournament_table = db.table("TOURNAMENT")
tournament = Query()
# changer une info :
tournament_table.update({"name": 1025}, tournament.location == "Paris")

# trouver une info :
print(tournament_table.search(Query()["name"] == "sophie"))
# tournament_table.truncate()


"""