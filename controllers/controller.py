from tinydb import TinyDB, Query
from controllers.menu import MenuController
from controllers.tournament import TournamentController
from controllers.player import PlayerController
from models.players import Player
from models.tournaments import Tournament


class MainController:
    """Main class to control the program."""

    def start_program():
        """Run the program."""
        tournaments_table = TinyDB("TOURNAMENTS.json")
        actors_table = TinyDB("ACTORS.json")
        user = Query()
        serialized_rounds = []

        run_program = True
        choices = {
            1: "create player",
            2: "create tournament",
            3: "pull tournament",
            4: "update rank",
            5: "display reports",
            6: "program end",
        }
        while run_program:
            choice = MenuController.choose_welcome_menu()
            if choices[choice] == "create player":
                player = PlayerController.create_player()
                Player.store_data_actors(player, user, actors_table)

            elif choices[choice] == "create tournament":
                # CHOOSE BETWEEN AUTO or MANUAL list of players :
                players = TournamentController.create_auto_players()
                # players = TournamentController.create_list_players(actors_table, user)
                tournament = TournamentController.create_tournament(players)
                Tournament.store_data_tournament(
                    tournament, players, user, actors_table, tournaments_table
                )
                print(tournament)
                TournamentController.progress_first_round(
                    tournament,
                    players,
                    tournaments_table,
                    user,
                    actors_table,
                    serialized_rounds,
                )
                nb_rounds = tournament.nb_rounds
                TournamentController.progress_next_rounds(
                    tournament,
                    players,
                    serialized_rounds,
                    tournaments_table,
                    user,
                    actors_table,
                    nb_rounds,
                )

            elif choices[choice] == "pull tournament":
                TournamentController.pull_tournament(
                    tournaments_table,
                    serialized_rounds,
                    actors_table,
                    user,
                )

            elif choices[choice] == "update rank":
                PlayerController.update_rank(actors_table, user)

            elif choices[choice] == "display reports":
                MenuController.choose_reports(tournaments_table, actors_table, user)

            elif choices[choice] == "program end":
                print("Program ended ! See you soon !")
                run_program = False
            else:
                print("An error occurred.")
