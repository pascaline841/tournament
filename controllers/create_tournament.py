from view.display_create_tournament import CreateTournamentView as View
from view.check_view import CheckView
from models.tournaments import Tournament as Tournament

import datetime


class CreateTournament:
    """Create a new tournament controller."""

    def __init__(self):
        self.view = View()
        self.tournament = Tournament()

    def display(self):
        self.view.display()

    def get_command(self, players):
        """Create a new tournament."""
        name = CheckView.check_str("Please enter tournament's name : ")
        location = CheckView.check_str("Please enter tournament's location : ")
        date = datetime.date.today().strftime("%d/%m/%Y")
        mode = CheckView.check_str(
            "How would you like to play ? bullet / blitz / fast : "
        )
        rounds = []
        description = input("Please enter tournament's description : ")
        players = players
        return Tournament(name, location, date, mode, rounds, description, players)
