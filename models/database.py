from models.players import Player
from models.tournaments import Tournament
from models.rounds import Round
from tinydb import TinyDB, Query


class Data:
    def data_tournaments(self, players):
        """ Enter players and tournament informations in the database."""
        db = TinyDB("db.json")
        actors_table = db.table("ACTORS")
        players_by_tournament = db.table("PLAYERS")
        tournament_table = db.table("TOURNAMENTS")
        for player in players:
            ser_player = player.serialized_player()
            if ser_player not in actors_table:
                actors_table.insert(ser_player)
            players_by_tournament.insert(ser_player)
        tournament_table.insert(
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

    def data_actors(self):
        """ Enter actor's informations in the database."""
        db = TinyDB("db.json")
        actors_table = db.table("ACTORS")
        ser_player = Player.serialized_player(self)
        if ser_player not in actors_table:
            actors_table.insert(ser_player)
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

    def update_rank(self, actors_table):
        """Update actor/player rank in the datatbase."""
        db = TinyDB("db.json")
        players_by_tournament = db.table("PLAYERS")
        self = Query()
        first_name = input("First name ? ")
        last_name = input("Last name ? ")
        new_rank = int(input("New rank ? "))
        actors_table.update(
            {"rank": new_rank},
            self["first name"] == first_name and self["last name"] == last_name,
        )
        players_by_tournament.update(
            {"rank": new_rank},
            self["first name"] == first_name and self["last name"] == last_name,
        )

    def update_score(self, actors_table):
        """Update actor/player score in the database."""
        db = TinyDB("db.json")
        players_by_tournament = db.table("PLAYERS")
        self = Query()
        first_name = input("First name ?")
        last_name = input("Last name ?")
        new_score = int(input("New score ? "))

        players_by_tournament.update(
            {"score": new_score},
            self["first name"] == first_name and self["last name"] == last_name,
        )

    def sorted_actors(self, actors_table):
        """Sort all actors by alphabetic order or by rank."""
        db = TinyDB("db.json")
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

    def sorted_players(self):
        """Sort all players by alphabetic order or by rank."""
        db = TinyDB("db.json")
        players_by_tournament = db.table("PLAYERS")
        sorted_players = int(input("Sorted by Last Name (1) or by Rank (2) ? "))
        all_data_players = players_by_tournament.all()
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
        print(sorted_list)

    def display_all_tournaments(self):
        """Display all tournaments" report."""
        print("Display all tournaments' report. ")
        db = TinyDB("db.json")
        tournament_table = db.table("TOURNAMENTS")
        all_data_tournaments = tournament_table.all()
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

    def request_tournament(self):
        """Request for a tournament to display its rounds or matches."""
        db = TinyDB("db.json")
        tournament_table = db.table("TOURNAMENTS")
        self = Query()
        date = input("Tournament's date ? (format : DD/MM/YYYY)")
        choice = tournament_table.search(self["date"] == date)
        print(choice)
        request_tournament = int(input("Display ROUNDS (1) or MATCHES (2) ? "))
        if request_tournament == 1:
            print(choice[0].get("rounds"))
        else:
            print(choice[0].get("matches"))

    def request_players(self):
        """Request for a tournament to display its players by alphabetic order or rank."""
        db = TinyDB("db.json")
        tournament_table = db.table("TOURNAMENTS")
        self = Query()
        date = input("Tournament's date ? (format : DD/MM/YYYY) ")
        choice = tournament_table.search(self["date"] == date)
        print(choice)
        sorted_players = int(input("Sorted by Last Name (1) or by Rank (2) ? "))
        if sorted_players == 1:
            list_players = choice[0].get("players")
            sorted_list = sorted(list_players, key=lambda colonnes: colonnes[0])
        else:
            choice[0].get("players")
            list_players = choice[0].get("players")
            sorted_list = sorted(list_players, key=lambda colonnes: colonnes[1])
        print(sorted_list)
