from models.players import Player
from models.tournaments import Tournament
from models.rounds import Round
from models.database import Data
from view.menu import MainView
from view.newplayer import NewPlayer
from view.newtournament import NewTournament
from view.score import Score
from view.displayround import DisplayRound
from view.report import DisplayReport
from controllers.menucontrol import MenuController
from controllers.tournamentcontrol import TournamentController
import datetime
from tinydb import TinyDB, Query


class MainController:
    
        db = TinyDB("db.json")
        tournament_table = db.table("TOURNAMENTS")
        actors_table = db.table("ACTORS")
        players_by_tournament = db.table("PLAYERS")
        rounds_table = db.table("ROUNDS")
        matches_table = db.table("MATCHES")
        user = Query()

    def start_program():
        """Run the program"""
        choice = MainView.welcome()
        if choice == 1:
            players = []
            player = MenuController.create_player()
            Data.data_actors(player, actors_table)
            print("\n A player has been created \n")

        elif choice == 2:
            players = TournamentController.create_auto_players()
            tournament = MenuController.create_tournament(players)
            Data.data_tournament(
                tournament,
                players,
                actors_table,
                players_by_tournament,
                tournament_table,
            )
            print(tournament)
            rounds = tournament.rounds
            TournamentController.create_first_round(players)
            Data.update_tournament(
                rounds,
                tournament_table,
                players_by_tournament,
                rounds_table,
                matches_table,
            )
            MenuController.inter_menu()
            nb_rounds = tournament.nb_rounds

            while nb_rounds > 1:
                nb_rounds -= 1
                TournamentController.create_next_round(players)
                Data.update_tournament(
                    rounds,
                    tournament_table,
                    players_by_tournament,
                    rounds_table,
                    matches_table,
                )
                MenuController.inter_menu()

            MainView.display_final(tournament, players)
            for player in players:
                score = player.add_final_score(player.score_game, player.score)
                Data.update_score(actors_table, players_by_tournament, score)
                player.score_game = 0
                del player.opponent[:]
            Data.truncate_data(players_by_tournament, matches_table, rounds_table)

        elif choice == 3:
            # Choice = Continue an existing tournament
            print("BUILDING")
        elif choice == 4:
            Data.update_rank()
        elif choice == 5:
            MenuController.display_reports()
        elif choice == 6:
            print("Program ended ! See you soon !")
        else:
            print("An error occurred.")
        MenuController.back_menu()
