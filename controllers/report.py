from view.report import ReportView as View
from view.check_view import CheckView  


class ReportsController:
    """Main page controller."""

    def __init__(self):
        self.view = View()

    def display(self):
        self.view.display()

    def get_command(self):
        choice = View.check_available_choices("Enter your choice (1, 2, 3, 4, 5) : \n")
        if choice == "1":
            return "sorted_actors report"
        elif choice == "2":
            return "tournaments report"
        elif choice == "3":
            return "rounds report"
        elif choice == "4":
            return "players report"
        elif choice == "5":
            return "general menu"

    def request_players(tournaments_table, user):
        """Request for a tournament to display its players by alpha order or rank."""
        name = MenuView.check_str("What is it name ? ")
        choice = tournaments_table.search(user["name"] == name)
        players = choice[0].get("players")
        sorted_choice = MenuView.check_int("Sorted by Last Name (1) or by Rank (2) ? "))
        if sorted_choice == 1:
            return sorted(players, key=lambda players: players["last name"])
        else:
            return sorted(players, key=lambda players: players["rank"])

    def request_rounds(tournaments_table, user):
        """Request for a tournament to display its rounds or matchs."""
        name = MenuView.check_str("What is it name ? ")
        choice = tournaments_table.search(user["name"] == name)
        return choice[0].get("rounds")

    def sorted_actors(actors_table):
        """Sort all actors by alphabetic order or by rank."""
        actors = actors_table.all()
        sorted_choice = MenuView.check_int("Sorted by Last Name (1) or by Rank (2) ? "))
        if sorted_choice == 1:
            return sorted(actors, key=lambda actor: actor["last name"])
        else:
            return sorted(actors, key=lambda actor: actor["rank"])
