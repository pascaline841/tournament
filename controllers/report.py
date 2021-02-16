from tinydb import TinyDB, Query

from view.check_input import CheckView
from view.report import ReportView as View


class Reports:
    """Display report menu."""

    def __init__(self):
        self.running = True
        self.view = View()

    def display(self):
        self.view.display()

    def get_command(self):
        """Display the reports' menu."""
        command = View.check_available_choices(
            "Enter your command (1, 2, 3, 4, 5) : \n"
        )
        if command == "1":
            return "sorted_actors report"
        elif command == "2":
            return "tournaments report"
        elif command == "3":
            return "rounds report"
        elif command == "4":
            return "players report"
        elif command == "5":
            return "general menu"

    @classmethod
    def sorted_actors(cls):
        """Sort all actors by alphabetic order or by rank."""
        db = TinyDB("ACTORS.json")
        actors = db.all()
        sorted_choice = CheckView.check_int("Sorted by Last Name (1) or by Rank (2) ? ")
        if sorted_choice == 1:
            return sorted(actors, key=lambda actor: actor["last name"])
        else:
            return sorted(actors, key=lambda actor: actor["rank"])

    @classmethod
    def request_players(cls):
        """Request for a tournament to display its players by alpha order or rank."""
        db = TinyDB("TOURNAMENT.json")
        query = Query()
        name = CheckView.check_str("What is it name ? ")
        command = db.search(query["name"] == name)
        players = command[0].get("players")
        sorted_choice = CheckView.check_int("Sorted by Last Name (1) or by Rank (2) ? ")
        if sorted_choice == 1:
            return sorted(players, key=lambda players: players["last name"])
        else:
            return sorted(players, key=lambda players: players["rank"])

    @classmethod
    def request_rounds(cls):
        """Request for a tournament to display its rounds or matchs."""
        db = TinyDB("TOURNAMENT.json")
        query = Query()
        name = CheckView.check_str("What is it name ? ")
        command = db.search(query["name"] == name)
        return command[0].get("rounds")
