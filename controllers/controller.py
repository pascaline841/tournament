from .main_menu import MainMenu
from .player import PlayerController
from .pull_tournament import PullTournament
from .tournament import TournamentController

from .report import Reports


class MainController:
    """Main class to control the program."""

    def __init__(self):
        self.running = True
        self.controller = MainMenu()
        self.messages = []

    def run(self):
        """Run the program."""
        while self.running:
            self.controller.display()
            command = self.controller.get_command()
            self.update(command)

    def update(self, command: str):
        """Update the application."""
        command = self.controller.update(command)

        if command == "quit":
            print("Program ended ! See you soon !")
            self.running = False
        elif command == "create player":
            self.controller = PlayerController()
        elif command == "create tournament":
            self.controller = TournamentController()
        elif command == "pull tournament":
            self.controller = PullTournament()
        elif command == "update rank":
            self.controller = UpdateRank()
        elif command == "display reports":
            self.controller = Reports()
        else:
            print("An error occurred.")
