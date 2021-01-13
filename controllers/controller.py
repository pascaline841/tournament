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
        serialized_rounds = []

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
                TournamentController.progress_first_round(
                    tournament,
                    players,
                    tournament_table,
                    user,
                    actors_table,
                    serialized_rounds,
                )
                nb_rounds = tournament.nb_rounds
                while nb_rounds > 1:
                    TournamentController.progress_next_rounds(
                        tournament,
                        players,
                        serialized_rounds,
                        tournament_table,
                        user,
                        actors_table,
                        nb_rounds,
                    )

            elif choices[choice] == "pull_tournament":
                name = input("Name of an UNcompleted tournament ? ")
                serialized_tournament = tournament_table.get(user["name"] == name)
                tournament = Tournament.deserialized_tournament(serialized_tournament)
                rounds = tournament.rounds
                for round in rounds:
                    ser_round = Round.serialized_round(round)
                    serialized_rounds.append(ser_round)
                players = tournament.players
                rounds_done = len(rounds)
                total_rounds = tournament.nb_rounds
                nb_rounds = total_rounds - rounds_done
                while nb_rounds > 1:
                    TournamentController.progress_next_rounds(
                        tournament,
                        players,
                        serialized_rounds,
                        tournament_table,
                        user,
                        actors_table,
                        nb_rounds,
                    )

            elif choices[choice] == "update_rank":
                Data.update_rank(actors_table, tournament_table, user)

            elif choices[choice] == "display_reports":
                MenuController.display_reports(tournament_table, actors_table, user)

            elif choices[choice] == "program_end":
                print("Program ended ! See you soon !")
                run_program = False
            else:
                print("An error occurred.")
