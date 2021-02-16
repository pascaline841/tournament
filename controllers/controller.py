from controllers.main_menu import MainMenu
from controllers.player_creation import PlayerCreation
from controllers.tournament_creation import TournamentCreation
from controllers.report import Reports
from controllers.pull_tournament import PullTournament


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