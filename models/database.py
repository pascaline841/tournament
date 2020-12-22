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
        Tournament.serialized_tournament(self)
        list_players = []
        for player in players:
            ser_player = Player.serialized_player(player)
            if ser_player not in actors_table:
                actors_table.insert(ser_player)
            list_players.append(ser_player)
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
                "players": list_players,
            }
        )
        return tournament_table

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

    def update_tournament(rounds):
        """ Update tournament's rounds and matches in the database."""
        db = TinyDB("db.json")
        tournament_table = db.table("TOURNAMENTS")
        list_ser_rounds = []
        list_ser_matches = []
        for round in rounds:
            ser_round = Round.serialized_round(round)
            list_ser_rounds.append(ser_round)
            """for match in round.list_match:
                ser_player1 = match[0][0].serialized_player()
                ser_player2 = match[1][0].serialized_player()
                ser_match = {
                    "player1": ser_player1.first_name,
                    "score_player1": ser_player1.score_game,
                    "player2": ser_player2.first_name,
                    "score_player2": ser_player2.score_game,
                }
                list_ser_matches.append(ser_match)
                """
        tournament = tournament_table.all()
        id_tournament = len(tournament)
        tournament_table.update(
            {
                "rounds": list_ser_rounds,
                "matches": list_ser_matches,
            },
            doc_ids=[id_tournament],
        )

    def update_rank():
        """Update actor/player rank in the datatbase."""
        db = TinyDB("db.json")
        actors_table = db.table("ACTORS")
        players_by_tournament = db.table("PLAYERS")
        user = Query()
        first_name = input("First name ? ").capitalize()
        last_name = input("Last name ? ").capitalize()
        new_rank = int(input("New rank ? "))
        actors_table.update(
            {"rank": new_rank},
            user["first name"] == first_name and user["last name"] == last_name,
        )
        players_by_tournament.update(
            {"rank": new_rank},
            user["first name"] == first_name and user["last name"] == last_name,
        )

    def update_score():
        """Update actor/player score in the database."""
        db = TinyDB("db.json")
        actors_table = db.table("ACTORS")
        players_by_tournament = db.table("PLAYERS")
        user = Query()
        first_name = input("First name ?").capitalize()
        last_name = input("Last name ?").capitalize()
        new_score = int(input("New score ? "))
        actors_table.update(
            {"score": new_score},
            user["first name"] == first_name and user["last name"] == last_name,
        )
        players_by_tournament.update(
            {"score": new_score},
            user["first name"] == first_name and user["last name"] == last_name,
        )

    def sorted_actors():
        """Sort all actors by alphabetic order or by rank."""
        db = TinyDB("db.json")
        actors_table = db.table("ACTORS")
        all_data_actors = actors_table.all()
        list_actors = []
        for actor in range(len(all_data_actors)):
            data_actors = (
                all_data_actors[actor].get("first name"),
                all_data_actors[actor].get("last name"),
                all_data_actors[actor].get("birth date"),
                all_data_actors[actor].get("gender"),
                all_data_actors[actor].get("rank"),
                all_data_actors[actor].get("score"),
            )
            list_actors.append(data_actors)
        sorted_actors = int(input("Sorted by Last Name (1) or by Rank (2) ? "))
        if sorted_actors == "1":
            sorted_list = sorted(list_actors, key=lambda colonnes: colonnes[2])
        else:
            sorted_list = sorted(
                list_actors, key=lambda colonnes: colonnes[5], reverse=True
            )
        print(sorted_list)

    def sorted_players():
        """Sort all players by alphabetic order or by rank for the current tournamen."""
        db = TinyDB("db.json")
        players_by_tournament = db.table("PLAYERS")
        sorted_players = int(input("Sorted by Last Name (1) or by Rank (2) ? "))
        all_data_players = players_by_tournament.all()
        list_players = []
        for player in range(len(all_data_players)):
            data_players = (
                all_data_players[player].get("last name"),
                all_data_players[player].get("first name"),
                all_data_players[player].get("birth date"),
                all_data_players[player].get("gender"),
                all_data_players[player].get("rank"),
                all_data_players[player].get("score"),
            )
            list_players.append(data_players)
        if sorted_players == "1":
            sorted_list = sorted(list_players, key=lambda colonnes: colonnes[1])
        else:
            sorted_list = sorted(list_players, key=lambda colonnes: colonnes[5])
        print(sorted_list)

    def display_all_tournaments():
        """Display all tournaments" report."""
        print("Display all tournaments' report. ")
        db = TinyDB("db.json")
        tournament_table = db.table("TOURNAMENTS")
        all_data_tournaments = tournament_table.all()
        list_tournaments = []
        for tournament in range(len(all_data_tournaments)):
            data_tournaments = (
                all_data_tournaments[tournament].get("name"),
                all_data_tournaments[tournament].get("location"),
                all_data_tournaments[tournament].get("date"),
                all_data_tournaments[tournament].get("mode"),
                all_data_tournaments[tournament].get("rounds"),
                all_data_tournaments[tournament].get("description"),
                all_data_tournaments[tournament].get("players"),
            )
            list_tournaments.append(data_tournaments)
        print(list_tournaments)

    def request_tournament():
        """Request for a tournament to display its rounds or matches."""
        db = TinyDB("db.json")
        tournament_table = db.table("TOURNAMENTS")
        user = Query()
        date = input("Tournament's date ? (format : DD/MM/YYYY)")
        choice = tournament_table.search(user["date"] == date)
        request_tournament = int(input("Display ROUNDS (1) or MATCHES (2) ? "))
        if request_tournament == 1:
            print(choice[0].get("rounds"))
        else:
            print(choice[0].get("matches"))

    def request_players():
        """Request for a tournament to display its players by alphabetic order or rank."""
        db = TinyDB("db.json")
        tournament_table = db.table("TOURNAMENTS")
        user = Query()
        date = input("Tournament's date ? (format : DD/MM/YYYY) ")
        choice = tournament_table.search(user["date"] == date)
        all_data_players = choice[0].get("players")
        list_players = []
        for player in range(len(all_data_players)):
            data_players = (
                all_data_players[player].get("first name"),
                all_data_players[player].get("last name"),
                all_data_players[player].get("birth date"),
                all_data_players[player].get("gender"),
                all_data_players[player].get("rank"),
                all_data_players[player].get("score"),
            )
            list_players.append(data_players)
        sorted_players = int(input("Sorted by Last Name (1) or by Rank (2) ? "))
        if sorted_players == 1:
            sorted_list = sorted(list_players, key=lambda colonnes: colonnes[2])
        else:
            sorted_list = sorted(
                list_players, key=lambda colonnes: colonnes[5], reverse=True
            )
        print(sorted_list)
