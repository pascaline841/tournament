from models.players import Player
from models.tournaments import Tournament
from models.rounds import Round
from tinydb import TinyDB, Query


class Data:
    def data_tournaments(self):
        db = TinyDB("tournaments.json")
        tournaments_table = db.table("TOURNAMENTS")
        tournaments_table.insert(
            {
                "name": self.name,
                "location": self.location,
                "date": self.date,
                "mode": self.mode,
                "rounds": self.rounds,
                "matches": self.matches,
                "description": self.description,
                "players": self.players,
            }
        )
        tournaments_table.update(
            {
                "rounds": self.rounds,
                "matches": self.matches,
                "players": self.players,
            }
        )
        return tournaments_table

    def data_players(self):
        db = TinyDB("actor.json")
        actors_table = db.table("PLAYER")
        actors_table.insert(
            {
                "first name": self.first_name,
                "last name": self.last_name,
                "birth date": self.birth_date,
                "gender": self.gender,
                "rank": self.rank,
                "score": self.score,
            }
        )
        return actors_table

    def update_rank():
        """update rank."""
        db = TinyDB("actor.json")
        actors_table = db.table("PLAYER")
        user = Query()
        print(
            "\n================================================== \n Update ranking : \n"
        )
        first_name = input("First name ? ")
        last_name = input("Last name ? ")
        new_rank = int(input("New rank ? "))
        actors_table.update(
            {"rank": new_rank},
            user["first name"] == first_name and user["last name"] == last_name,
        )
        print("The new rank has been successfully updated...")

    def update_score(self, actors_table):
        """update score."""
        self = Query()
        first_name = input("First name ?")
        last_name = input("Last name ?")
        new_score = int(input("New score ? "))
        actors_table.update(
            {"score": new_score},
            self["first name"] == first_name and self["last name"] == last_name,
        )

    def sorted_players(self, actors_table):
        """Sort actors by alphabetic order or by rank."""
        sorted_actors = int(input("Sorted by Last Name (1) or by Rank (2) ? "))
        all_data_actors = actors_table.all()
        list_actors = []
        for nb in range(len(all_data_actors)):
            data_actors = (
                all_data_actors[nb].get("last name"),
                all_data_actors[nb].get("first name"),
                all_data_actors[nb].get("birth date"),
                all_data_actors[nb].get("gender"),
                all_data_actors[nb].get("rank"),
                all_data_actors[nb].get("score"),
            )
            list_actors.append(data_actors)
        if sorted_actors == "1":
            sorted_list = sorted(list_actors, key=lambda colonnes: colonnes[1])
        else:
            sorted_list = sorted(list_actors, key=lambda colonnes: colonnes[5])
        print(sorted_list)

    def display_all_tournaments(self, tournaments_table):
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
        print(list_tournaments)

    def request_tournament(self, tournaments_table):
        """ request a date and display a tournament' rounds and matches."""
        self = Query()
        date = input("Tournament's date ? (format : DD/MM/YYYY)")
        choice = tournaments_table.search(self["date"] == date)
        print(choice)
        request_tournament = int(input("Display ROUNDS (1) or MATCHES (2) ? "))
        if request_tournament == 1:
            print(choice[0].get("rounds"))
        else:
            print(choice[0].get("matches"))

    def request_players(self, tournament_table):
        self = Query()
        date = input("Tournament's date ? (format : DD/MM/YYYY) ")
        choice = tournaments_table.search(self["date"] == date)
        print(choice)
        sorted_players = int(input("Sorted by Last Name (1) or by Rank (2) ? "))
        if sorted_players == 1:
            list_players = choice[0].get("players")
            sorted_list = sorted(list_players, key=lambda colonnes: colonnes[0])
        else:
            choice[0].get("players")
            list_players = choice[0].get("players")
            sorted_list = sorted(list_players, key=lambda colonnes: colonnes[1])
        # changer le colonne[] par celui correspondant au rank ou last_name
        print(sorted_list)


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