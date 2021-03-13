from .main_menu import MainMenu
from .player import PlayerController
from .pull_tournament import PullTournament
from .report import Reports
from .tournament import TournamentController


class MainController:
    """Main class to control the program."""

    def __init__(self):
        """Init."""
        self.running = True
        self.controller = MainMenu()

    def run(self):
        """Run the program."""
        while self.running:
            self.controller.display()
            command = self.controller.get_command()
            self.update(command)

    def update(self, command: str):
        """Update the application."""
        if command == "quit":
            print("Program ended ! See you soon ! ")
            self.running = False
        elif command == "create player":
            self.controller = PlayerController()
        elif command == "create tournament":
            self.controller = TournamentController()
        elif command == "pull tournament":
            self.controller = PullTournament()
        elif command == "update rank":
            self.controller.update_rank()
        elif command == "display reports":
            self.controller = Reports()
        elif command == "main menu":
            self.controller = MainMenu()
