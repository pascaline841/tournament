class ReportView:
    """Display the different reports."""

    def display(self):
        """Display the menu of the reports."""
        print("\n==================================================")
        print("\n************REPORTS**************\n")
        print("1 - List of all users")
        print("2 - List of all tournaments")
        print("3 - List of all rounds for a tournament")
        print("4 - List of all players for a tournament")
        print("5 - Back to the general menu")

    def report_users(self):
        """Display a list of all the users."""
        for user in self:
            print(
                f"{user['last_name']} {user['first_name']} RANK: {user['rank']} "
                f"TOTAL SCORE: {user['score']}"
            )

    def report_tournaments(self):
        """Display a list of all the tournaments."""
        for tournament in self:
            print(
                f"{tournament['name']} DATE : {tournament['date']} LOCATION : "
                f"{tournament['location']} MODE : {tournament['mode']}"
            )

    def report_rounds(self):
        """Display a list of all the rounds of a tournament."""
        for round in self:
            print(f"{round['name']} {round['start']} {round['end']}")

    def report_players(self):
        """Display a list of all the players of a tournament."""
        for player in self:
            print(
                f"{player['first_name']} {player['last_name']} RANK : {player['rank']}"
                f" POINTS: {player['points']}"
            )
