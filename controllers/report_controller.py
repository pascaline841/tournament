from tinydb import TinyDB

from .report import Report

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

    def update(self, command: str):
        db = TinyDB("TOURNAMENT.json")
        if command == "sorted_actors report":
            display_report = self.controller.sorted_actors()
            View.report_actors(display_report)
        elif command == "tournaments report":
            display_report = db.all()
            View.report_tournaments(display_report)
        elif command == "rounds report":
            display_report = self.controller.request_rounds()
            View.report_rounds(display_report)
        elif command == "players report":
            display_report = self.controller.request_players()
            View.report_players(display_report)
        elif command == "general menu":
            self.running = False
        self.running = False
