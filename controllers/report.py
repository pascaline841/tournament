from tinydb import TinyDB, Query

from .check_input import CheckInputController as CheckInput

from view.report import ReportView as View


class Reports:
    """Display report menu."""

    def __init__(self):
        self.view = View()

    def display(self):
        self.view.display()

    def get_command(self):
        """Display the reports' menu."""
        command = CheckInput.check_available_five_choices(
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
            return "main menu"

    def update(self, command: str):
        db = TinyDB("TOURNAMENTS.json")
        if command == "sorted_actors report":
            display_report = self.sorted_actors()
            View.report_actors(display_report)
        elif command == "tournaments report":
            display_report = db.all()
            View.report_tournaments(display_report)
        elif command == "rounds report":
            display_report = self.request_rounds()
            View.report_rounds(display_report)
        elif command == "players report":
            display_report = self.request_players()
            View.report_players(display_report)
        elif command == "main menu":
            return "main menu"

    @classmethod
    def sorted_actors(cls):
        """Sort all actors by alphabetic order or by rank."""
        db = TinyDB("ACTORS.json")
        actors = db.all()
        sorted_choice = CheckInput.check_int(
            "Sorted by Last Name (1) or by Rank (2) ? "
        )
        if sorted_choice == 1:
            return sorted(actors, key=lambda actor: actor["last_name"])
        else:
            return sorted(actors, key=lambda actor: actor["rank"])

    @classmethod
    def request_players(cls):
        """Request for a tournament to display its players by alpha order or rank."""
        db = TinyDB("TOURNAMENTS.json")
        query = Query()
        name = CheckInput.check_str("What is it name ? ")
        command = db.search(query["name"] == name)
        players = command[0].get("players")
        sorted_choice = CheckInput.check_int(
            "Sorted by Last Name (1) or by Rank (2) ? "
        )
        if sorted_choice == 1:
            return sorted(players, key=lambda players: players["last_name"])
        else:
            return sorted(players, key=lambda players: players["rank"])

    @classmethod
    def request_rounds(cls):
        """Request for a tournament to display its rounds or matchs."""
        db = TinyDB("TOURNAMENTS.json")
        query = Query()
        name = CheckInput.check_str("What is it name ? ")
        command = db.search(query["name"] == name)
        return command[0].get("rounds")
