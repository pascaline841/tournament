from view.main_menu import MainMenuView as View

from controllers.player_creation import PlayerCreation
from controllers.tournament_creation import TournamentCreation
from controllers.report import Reports
from controllers.pull_tournament import PullTournament

from tinydb import TinyDB, Query


class MainMenu:
    """Main page controller."""

    tournaments_table = TinyDB("TOURNAMENTS.json")
    actors_table = TinyDB("ACTORS.json")
    user = Query()
    serialized_rounds = []

    def __init__(self):
        self.running = True
        self.messages = []
        self.view = View()

    def display(self):
        self.view.display()

    def run(self):
        while self.running:
            self.display()
            command = self.get_command()
            self.update(command)

    def get_command(self):
        command = View.check_available_choices("Enter your command (1, 2, 3, 4, 5) :\n")
        if command == "1":
            return "create player"
        elif command == "2":
            return "create tournament"
        elif command == "3":
            return "pull tournament"
        elif command == "4":
            return "update rank"
        elif command == "5":
            return "display reports"
        elif command == "6":
            return "quit"

    def update(self, command: str):
        """Update the application."""
        if command == "quit":
            print("Program ended ! See you soon !")
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
