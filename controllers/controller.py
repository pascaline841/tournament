from tinydb import TinyDB, Query

from controllers.main_menu import MainMenu
from controllers.player_creation import PlayerCreation
from controllers.tournament_creation import TournamentCreation
from controllers.tournament_details import TournamentDetails
from controllers.player_details import PlayerDetails
from controllers.report import Reports
from controllers.pull_tournament import PullTournament

from models.player import Player
from models.tournament import Tournament


class MainController:
    """Main class to control the program."""

    def __init__(self):
        self.running = True
        self.controller = MainMenu()
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
            self.controller = PlayerCreation()
        elif command == "create tournament":
            self.controller = TournamentCreation()
        elif command == "pull tournament":
            self.controller = PullTournament()
        elif command == "update rank":
            self.controller = UpdateRank()
        elif command == "display reports":
            self.controller = Reports()
        else:
            print("An error occurred.")

    def start_program(self):
        """Run the program."""

        while self.running:
            choice = MainMenu.get_command()

            if choice == "create player":
                player = PlayerDetails.create_player()
                Player.store_data_actors(player, user, actors_table)

            elif choice == "create tournament":
                # CHOOSE BETWEEN AUTO or MANUAL list of players :
                players = TournamentDetails.create_auto_players()
                # players = TournamentDetails.create_list_players(actors_table, user)
                tournament = TournamentDetails.create_tournament(players)
                Tournament.store_data_tournament(
                    tournament, players, user, actors_table, tournaments_table
                )
                print(tournament)
                TournamentDetails.progress_first_round(
                    tournament,
                    players,
                    tournaments_table,
                    user,
                    actors_table,
                    serialized_rounds,
                )
                nb_rounds = tournament.nb_rounds
                TournamentDetails.progress_next_rounds(
                    tournament,
                    players,
                    serialized_rounds,
                    tournaments_table,
                    user,
                    actors_table,
                    nb_rounds,
                )

            elif choice == "pull tournament":
                TournamentDetails.pull_tournament(
                    tournaments_table,
                    serialized_rounds,
                    actors_table,
                    user,
                )

            elif choice == "update rank":
                PlayerDetails.update_rank(actors_table, user)

            elif choice == "display reports":
                Reports.get_command()

            elif choice == "program end":
                print("Program ended ! See you soon !")
                self.running = False
