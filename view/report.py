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

    @staticmethod
    def check_available_choices(message):
        """Check the input value when the choices are from 1 to 5."""
        boolean = True
        while boolean:
            try:
                command = input(message)
                if command not in [1, 2, 3, 4, 5]:
                    raise ValueError
                print(f"Your command ({command}) has been successfully entered...\n")
                boolean = False
                return command
            except ValueError:
                print("The value entered doesn't match the possible choices !\n")
            except TypeError:
                print("Incorrect value, it has to be a positive number !")

    def report_actors(display_report):
        """Display a list of all the actors."""
        for actor in display_report:
            print(
                f"{actor['last name']} {actor['first name']} RANK: {actor['rank']} "
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
                f"{player['first name']} {player['last name']} RANK : {player['rank']}"
                f" POINT: {player['score game']}"
            )
