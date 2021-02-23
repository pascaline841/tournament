class ReportView:
    """Display the different reports."""

    def display(self):
        """Display the menu of the reports."""
        print("\n==================================================")
        print("\n************REPORTS**************\n")
        print("1 - List of all actors")
        print("2 - List of all tournaments")
        print("3 - List of all rounds for a tournament")
        print("4 - List of all players for a tournament")
        print("5 - return to the general menu")

    def report_actors(display_report):
        """Display a list of all the actors."""
        for actor in display_report:
            print(
                f"{actor['last_name']} {actor['first_name']} RANK: {actor['rank']} "
                f"SCORE: {actor['score']}"
            )

    def report_tournaments(display_report):
        """Display a list of all the tournaments."""
        for tournament in display_report:
            print(
                f"{tournament['name']} DATE : {tournament['date']} LOCATION : "
                f"{tournament['location']} MODE : {tournament['mode']}"
            )

    def report_rounds(display_report):
        """Display a list of all the rounds of a tournament."""
        for round in display_report:
            print(f"{round['name']} {round['start']} {round['end']}")

    def report_players(display_report):
        """Display a list of all the players of a tournament."""
        for player in display_report:
            print(
                f"{player['first_name']} {player['last_name']} RANK : {player['rank']}"
                f" POINTS: {player['score game']}"
            )
