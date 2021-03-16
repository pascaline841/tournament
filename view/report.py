class ReportView:
    """Display the different reports."""

    @classmethod
    def display(cls):
        """Display the menu of the reports."""
        print("\n==================================================")
        print("\n************REPORTS**************\n")
        print("1 - List of all users")
        print("2 - List of all tournaments")
        print("3 - List of all rounds for a tournament")
        print("4 - List of all players for a tournament")
        print("5 - Back to the general menu")

    @classmethod
    def report_users(cls, display_report):
        """Display a list of all the users."""
        for user in display_report:
            print(
                f"{user['last_name']} {user['first_name']} RANK: {user['rank']} "
                f"TOTAL SCORE: {user['score']}"
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
    def report_players(cls, display_report):
        """Display a list of all the players of a tournament."""
        for player in display_report:
            print(
                f"{player['first_name']} {player['last_name']} RANK : {player['rank']}"
                f" POINTS: {player['points']}"
            )
