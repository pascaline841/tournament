from .player import PlayerController

from view.inter_round_menu import InterRoundMenuView as View


class InterRoundController:
    """Class displays and controls the menu between 2 rounds during a tournament."""

    def __init__(self):
        self.view = View()

    def display(self):
        self.view.display()

    def get_command(self):
        command = View.check_available_choices("Enter your command (1, 2, 3) : \n")
        if command == "1":
            return "continue tournament"
        elif command == "2":
            return "update rank"
        elif command == "3":
            return "quit"

    def update(self, command: str, tournament, players):
        """Display menu between rounds."""
        if command == "quit":
            self.running = False
        elif command == "continue tournament":
            pass
        elif command == "update rank":
            PlayerController.update_rank_tournament(players, tournament)
