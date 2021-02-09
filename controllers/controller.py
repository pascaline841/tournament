from tinydb import TinyDB, Query
from controllers.menu import MenuController
from controllers.tournament import TournamentController
from controllers.player import PlayerController
from models.players import Player
from models.tournaments import Tournament

from controllers.main_page import MainPageController


class MainController:
    """Main class to control the program."""

    def __init__(self):
        self.running = True
        self.controller = MainPageController()
        self.messages = []

    def run(self):
        # tournaments_table = TinyDB("TOURNAMENTS.json")
        # actors_table = TinyDB("ACTORS.json")
        # user = Query()
        # serialized_rounds = []
        while self.running:
            self.controller.display()
            command = self.controller.get_command()
            self.update(command)

    def update(self, command: str):
        """Update the application."""
        if command == "quit":
            self.running = False
        elif command == "create player":
            self.controller = CreatePlayer()
        elif command == "create tournament":
            self.controller = CreateTournament()
        elif command == "pull tournament":
            self.controller = PullTournament()
        elif command == "update rank":
            self.controller = UpdateRank()
        elif command == "display reports":
            self.controller = ReportsController()
        else:
            print("An error occurred.")

    def start_program(self):
        """Run the program."""

        while self.running:
            choice = MenuController.choose_welcome_menu()

            if choice == "create player":
                player = PlayerController.create_player()
                Player.store_data_actors(player, user, actors_table)

            elif choice == "create tournament":
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

            elif choice == "pull tournament":
                TournamentController.pull_tournament(
                    tournaments_table,
                    serialized_rounds,
                    actors_table,
                    user,
                )

            elif choice == "update rank":
                PlayerController.update_rank(actors_table, user)

            elif choice == "display reports":
                MenuController.choose_reports(tournaments_table, actors_table, user)

            elif choice == "program end":
                print("Program ended ! See you soon !")
                run_program = False
