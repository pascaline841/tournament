from view.report import ReportView as View
from view.check_input import CheckView


class Reports:
    """Report controller."""

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

    def update(self, command: str, tournaments_table, actors_table, user):
        if command == "sorted_actors report":
            display_report = self.controller.sorted_actors(actors_table)
            View.report_actors(display_report)
        elif command == "tournaments report":
            display_report = tournaments_table.all()
            View.report_tournaments(display_report)
        elif command == "rounds report":
            display_report = self.controller.request_rounds(tournaments_table, user)
            View.report_rounds(display_report)
        elif command == "players report":
            display_report = self.controller.request_players(tournaments_table, user)
            View.report_players(display_report)
        elif command == "general menu":
            self.running = False

    def sorted_actors(actors_table):
        """Sort all actors by alphabetic order or by rank."""
        actors = actors_table.all()
        sorted_choice = CheckView.check_int("Sorted by Last Name (1) or by Rank (2) ? ")
        if sorted_choice == 1:
            return sorted(actors, key=lambda actor: actor["last name"])
        else:
            return sorted(actors, key=lambda actor: actor["rank"])

    def request_players(tournaments_table, user):
        """Request for a tournament to display its players by alpha order or rank."""
        name = CheckView.check_str("What is it name ? ")
        command = tournaments_table.search(user["name"] == name)
        players = command[0].get("players")
        sorted_choice = CheckView.check_int("Sorted by Last Name (1) or by Rank (2) ? ")
        if sorted_choice == 1:
            return sorted(players, key=lambda players: players["last name"])
        else:
            return sorted(players, key=lambda players: players["rank"])

    def request_rounds(tournaments_table, user):
        """Request for a tournament to display its rounds or matchs."""
        name = CheckView.check_str("What is it name ? ")
        command = tournaments_table.search(user["name"] == name)
        return command[0].get("rounds")
