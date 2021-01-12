from tinydb import TinyDB, Query
from controllers.menu import MenuController
from controllers.progress import TournamentController
from models.players import Player
from models.tournaments import Tournament
from models.database import Data
from models.rounds import Round
from view.menu import MainView


class MainController:
    """Main class to control the program."""

    def start_program():  # mettre un self
        """Run the program."""
        tournament_table = TinyDB("TOURNAMENTS.json")
        actors_table = TinyDB("ACTORS.json")
        user = Query()
        choices = {
            1: "create_player",
            2: "create_tournament",
            3: "pull_tournament",
            4: "update_rank",
            5: "display_reports",
            6: "program_end",
        }

        run_program = True
        while run_program is True:
            choice = MainView.welcome()
            if choices[choice] == "create_player":
                player = MenuController.create_player()
                Player.store_data_actors(player, user, actors_table)

            elif choices[choice] == "create_tournament":
                players = TournamentController.create_auto_players()
                tournament = MenuController.create_tournament(players)
                Tournament.store_data_tournament(
                    tournament, players, user, actors_table, tournament_table
                )
                # print(tournament)
                rounds = tournament.rounds
                round = TournamentController.create_first_round(
                    tournament, rounds, players
                )
                serialized_rounds = []
                ser_round = Round.serialized_round(round)
                serialized_rounds.append(ser_round)
                Tournament.update_round(
                    tournament, serialized_rounds, tournament_table, user
                )
                Data.update_players(players, tournament_table, tournament, user)

                MenuController.inter_menu(actors_table, tournament_table, user)

                nb_rounds = tournament.nb_rounds

                while nb_rounds > 1:
                    nb_rounds -= 1
                    round = TournamentController.create_next_round(
                        tournament, rounds, players
                    )
                    ser_round = Round.serialized_round(round)
                    serialized_rounds.append(ser_round)
                    Tournament.update_round(
                        tournament, serialized_rounds, tournament_table, user
                    )
                    Data.update_players(players, tournament_table, tournament, user)

                    MenuController.inter_menu(actors_table, tournament_table, user)
                players = sorted(
                    players,
                    key=lambda player: (player.score_game, player.score),
                    reverse=True,
                )
                MainView.display_final_score(tournament, players)
                for player in players:
                    score = player.add_final_score(player.score_game, player.score)
                    Player.update_score(player, actors_table, score, user)
                Data.update_players(players, tournament_table, tournament, user)

            elif choices[choice] == "pull_tournament":
                # Choice = Continue an existing tournament
                print("BUILDING")

            elif choices[choice] == "update_rank":
                Data.update_rank(actors_table, tournament_table, user)

            elif choices[choice] == "display_reports":
                MenuController.display_reports(tournament_table, actors_table, user)

            elif choices[choice] == "program_end":
                print("Program ended ! See you soon !")
                run_program = False
            else:
                print("An error occurred.")
