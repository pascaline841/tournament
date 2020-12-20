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

    def sorted_players(self, players_table):
        """Sort players by alphabetic order or by rank."""
        sorted_players = input("Sorted by Last Name (1) or by Rank (2) ? ")
        all_data_players = players_table.all()
        list_players = []
        for nb in range(len(all_data_players)):
            data_players = (
                all_data_players[nb].get("last name"),
                all_data_players[nb].get("first name"),
                all_data_players[nb].get("birth date"),
                all_data_players[nb].get("gender"),
                all_data_players[nb].get("rank"),
                all_data_players[nb].get("score"),
            )
            list_players.append(data_players)
        if sorted_players == "1":
            sorted_list = sorted(list_players, key=lambda colonnes: colonnes[1])
        else:
            sorted_list = sorted(list_players, key=lambda colonnes: colonnes[5])
        # print(sorted_list)

    def display_all_tournaments(
        self, tournaments_table
    ):  # afficher/add rounds + matches
        """Display all tournaments' report."""
        print("Display all tournaments' report. ")
        all_data_tournaments = tournaments_table.all()
        list_tournaments = []
        for nb in range(len(all_data_tournaments)):
            data_tournaments = (
                all_data_tournaments[nb].get("name"),
                all_data_tournaments[nb].get("location"),
                all_data_tournaments[nb].get("date"),
                all_data_tournaments[nb].get("mode"),
                all_data_tournaments[nb].get("rounds"),
                all_data_tournaments[nb].get("description"),
                all_data_tournaments[nb].get("players"),
            )
            list_tournaments.append(data_tournaments)
        # print(list_tournaments)


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