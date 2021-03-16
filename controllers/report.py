from tinydb import TinyDB, Query

from helpers import Input

from view.report import ReportView as View


class Reports:
    """Display report menu."""

    def __init__(self):
        """Init."""
        self.view = View()

    def display(self):
        self.view.display()

    def get_command(self):
        """Display the reports' menu."""
        db = TinyDB("TOURNAMENTS.json")
        command = Input.for_range(
            "Enter your command (1, 2, 3, 4, 5) : \n", [1, 2, 3, 4, 5]
        )
        choices = {
            1: "sorted users report",
            2: "tournaments report",
            3: "rounds report",
            4: "players report",
            5: "main menu",
        }
        if choices[command] == "sorted users report":
            display_report = Reports.sorted_users()
            View.report_users(display_report)
        elif choices[command] == "tournaments report":
            display_report = db.all()
            View.report_tournaments(display_report)
        elif choices[command] == "rounds report":
            display_report = self.request_rounds()
            View.report_rounds(display_report)
        elif choices[command] == "players report":
            display_report = self.request_players()
            View.report_players(display_report)
        elif choices[command] == "main menu":
            return "main menu"

    @classmethod
    def sorted_users(cls):
        """Sort all users by alphabetic order or by rank."""
        db = TinyDB("USERS.json")
        users = db.all()
        sorted_choice = Input.for_integer("Sorted by Last Name (1) or by Rank (2) ? ")
        if sorted_choice == 1:
            return sorted(users, key=lambda user: user["last_name"])
        else:
            return sorted(users, key=lambda user: user["rank"])

    @classmethod
    def request_players(cls):
        """Request for a tournament to display its players by alpha order or rank."""
        db = TinyDB("TOURNAMENTS.json")
        query = Query()
        name = Input.for_string("What is the tournament's name ? ")
        data = db.search(query["name"] == name)
        players = data[0].get("players")
        sorted_choice = Input.for_integer("Sorted by Last Name (1) or by Rank (2) ? ")
        if sorted_choice == 1:
            return sorted(players, key=lambda players: players["last_name"])
        else:
            return sorted(players, key=lambda players: players["rank"])

    @classmethod
    def request_rounds(cls):
        """Request for a tournament to display its rounds or matchs."""
        db = TinyDB("TOURNAMENTS.json")
        query = Query()
        name = Input.for_string("What is tournament's name ? ")
        data = db.search(query["name"] == name)
        return data[0].get("rounds")
