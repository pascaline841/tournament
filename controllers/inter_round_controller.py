from controllers.inter_round_menu import InterRoundMenu
from controllers.player_details import PlayerDetails


class InterRoundController:
    """Class controls the menu between 2 rounds during a tournament."""

    def __init__(self):
        self.running = True
        self.controller = InterRoundMenu()
        self.messages = []

    def run(self):
        """Run the program."""
        while self.running:
            self.controller.display()
            command = self.controller.get_command()
            self.update(command)

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
