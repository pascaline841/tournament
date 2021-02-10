from controllers.report import Report
from view.report import ReportView as View


class ReportController:
    """Reports controller."""

    def __init__(self):
        self.running = True
        self.controller = Report()
        self.display = View()

    def run(self):
        while self.running:
            self.display()
            command = self.get_command()
            self.update(command)

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
        self.running = False
