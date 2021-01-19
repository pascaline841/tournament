class DisplayReport:
    """Display the different reports."""

    @classmethod
    def display_reports(cls):
        """Display the menu of the reports."""
        print("************REPORTS**************")
        print("1 - List of all actors")
        print("2 - List of all tournaments")
        print("3 - List of all rounds for a tournament")
        print("4 - List of all players for a tournament")
        print("5 - return to the general menu")

    @classmethod
    def report_actors(cls, display_report):
        """Display a list of all the actors."""
        for actor in display_report:
            print(
                f"{actor['last name']} {actor['first name']} RANK: {actor['rank']}"
                f"SCORE: {actor['score']}"
            )

    @classmethod
    def report_tournaments(cls, display_report):
        """Display a list of all the tournaments."""
        for tournament in display_report:
            print(
                f"{tournament['name']} DATE : {tournament['date']} LOCATION : "
                f"{tournament['location']} MODE : {tournament['mode']}"
            )

    @classmethod
    def report_rounds(cls, display_report):
        """Display a list of all the rounds of a tournament."""
        for round in display_report:
            print(f"{round['name']} {round['start']} {round['end']}")

    @classmethod
    def report_players(display_report):
        """Display a list of all the players of a tournament."""
        for player in display_report:
            print(
                f"{player['first name']} {player['last name']} RANK : {player['rank']}"
                f" POINT: {player['score game']}"
            )
