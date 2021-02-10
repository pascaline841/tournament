from controllers.player_details import PlayerDetails
from view.inter_round_menu import InterRoundMenuView as View


class InterRoundMenu:
    """Class controls the menu between 2 rounds during a tournament."""

    def __init__(self):
        self.running = True
        self.view = View()

    def display(self):
        self.view.display()

    def run(self):
        while self.running:
            self.display()
            command = self.get_command()
            self.update(command)

    def get_command(self):
        command = View.check_available_choices("Enter your command (1, 2, 3) : \n")
        if command == "1":
            return "continue tournament"
        elif command == "2":
            return "update rank"
        elif command == "3":
            return "quit"

    def update(
        self,
        command: str,
        actors_table,
        tournaments_table,
        user,
        tournament,
        players,
    ):
        """Display menu between rounds."""
        if command == "quit":
            self.running = False
        elif command == "continue tournament":
            pass
        elif command == "update rank":
            self.controller = PlayerDetails.update_rank_tournament(
                actors_table, tournaments_table, user, players, tournament
            )
