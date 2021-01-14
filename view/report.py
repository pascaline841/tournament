class DisplayReport:
    """Display the different reports."""

    @staticmethod
    def display_reports():
        """Display the menu of the reports."""
        print("************REPORTS**************")
        print("1 - List of all actors")
        print("2 - List of all tournaments")
        print("3 - List of all rounds for a tournament")
        print("4 - List of all players for a tournament")
        print("5 - return to the general menu")

    @staticmethod
    def report_actors(display_report):
        """Display a list of all the actors."""
        for actor in display_report:
            print(f"{actor['last name']} {actor['first name']} RANK : {actor['rank']}")

    @staticmethod
    def report_tournaments(display_report):
        """Display a list of all the tournaments."""
        for tournament in display_report:
            print(
                f"{tournament['name']} DATE : {tournament['date']} LOCATION : {tournament['location']} MODE : {tournament['mode']}"
            )

    @staticmethod
    def report_rounds(display_report):
        """Display a list of all the rounds of a tournament."""
        for round in display_report:
            print(f"{round['name']} {round['start']} {round['end']}")

    @staticmethod
    def report_players(display_report):
        """Display a list of all the players of a tournament."""
        for player in display_report:
            print(
                f"{player['first name']} {player['last name']} RANK : {player['rank']}"
            )
