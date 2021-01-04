from models.database import Data
from view.menu import MainView
from controllers.menucontrol import MenuController
from controllers.tournamentcontrol import TournamentController
from tinydb import TinyDB, Query


class MainController:
    def start_program():
        """Run the program"""
        tournament_table = TinyDB("TOURNAMENTS.json")
        actors_table = TinyDB("ACTORS.json")
        players_table = TinyDB("PLAYERS.json")
        # rounds_table = TinyDB("ROUNDS.json")
        # matches_table = TinyDB("MATCHES.json")
        user = Query()

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
                players_table,
                tournament_table,
            )
            print(tournament)
            rounds = tournament.rounds
            round_one = TournamentController.create_first_round(
                tournament, rounds, players
            )
            Data.update_tournament(
                round_one,
                tournament_table,
                players_table,
                tournament,
            )

            MenuController.inter_menu(
                tournament_table, actors_table, players_table, user
            )

            nb_rounds = tournament.nb_rounds

            while nb_rounds > 1:
                nb_rounds -= 1
                next_round = TournamentController.create_next_round(
                    tournament, rounds, players
                )
                Data.update_tournament(
                    next_round,
                    tournament_table,
                    players_table,
                )
                MenuController.inter_menu(
                    tournament_table, actors_table, players_table, user
                )

            MainView.display_final(tournament, players)
            for player in players:
                score = player.add_final_score(player.score_game, player.score)
                Data.update_score(actors_table, players_table, score)
                player.score_game = 0
                del player.opponent[:]
            Data.truncate_data(players_table)

        elif choice == 3:
            # Choice = Continue an existing tournament
            print("BUILDING")
        elif choice == 4:
            Data.update_rank(actors_table, players_table, user)
        elif choice == 5:
            MenuController.display_reports(tournament_table, actors_table, user)
        elif choice == 6:
            print("Program ended ! See you soon !")
        else:
            print("An error occurred.")
        MenuController.back_menu(tournament_table, actors_table, players_table, user)
