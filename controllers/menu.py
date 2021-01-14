import datetime
from models.players import Player
from models.tournaments import Tournament
from view.menu import MenuView
from view.newplayer import NewPlayer
from view.report import DisplayReport


class MenuController:
    """Class controls all the different menus in the program."""

    @classmethod
    def choose_welcome_menu(cls):
        """Input to the Welcome Menu."""
        MenuView.welcome()
        try:
            choice = int(input("Enter your choice (1, 2, 3, 4, 5) : \n"))
            if choice > 7:
                raise ValueError
            print("Your choice ({}) has been successfully entered...\n".format(choice))
            return choice
        except ValueError:
            print("The value entered doesn't match the possible choices !\n")
            return MenuController.choose_welcome_menu()

    @classmethod
    def create_player(cls):
        """Create a new player."""
        print("\n************CREATE A NEW PLAYER **************\n")
        first_name = input("Please enter player's first name : ").capitalize()
        last_name = input("Please enter player's last name : ").capitalize()
        birth_date = input("Please enter player's birth date (format = DD/MM/YYYY) : ")
        gender = NewPlayer.player_gender()
        rank = NewPlayer.player_rank()
        score = NewPlayer.player_score()
        print("\n A player has been created. \n")
        return Player(first_name, last_name, birth_date, gender, rank, score)

    @classmethod
    def create_tournament(cls, players):
        """Create a new tournament."""
        print("\n==================================================")
        print("************CREATE A NEW TOURNAMENT**************\n")
        name = input("Please enter tournament's name : ")
        location = input("Please enter tournament's location : ")
        date = datetime.date.today().strftime("%d/%m/%Y")
        mode = input("How would you like to play ? bullet / blitz / fast : ")
        rounds = []
        description = input("Please enter tournament's description : ")
        players = players
        return Tournament(name, location, date, mode, rounds, description, players)

    @classmethod
    def choose_reports(cls, tournament_table, actors_table, user):
        """Display the reports' menu."""
        reports = {
            1: "sorted_actors report",
            2: "tournaments report",
            3: "rounds report",
            4: "players report",
        }
        DisplayReport.display_reports()
        try:
            report = int(input("Enter your choice (1, 2, 3, 4, 5) : \n"))
            if report > 6:
                raise ValueError
            print("Your choice ({}) has been successfully entered\n".format(report))
        except ValueError:
            print("The value entered doesn't match the possible choices !\n")
            return MenuController.choose_reports
        if reports[report] == "sorted_actors report":
            display_report = Player.sorted_actors(actors_table)
            DisplayReport.report_actors(display_report)
        elif reports[report] == "tournaments report":
            display_report = tournament_table.all()
            DisplayReport.report_tournaments(display_report)
        elif reports[report] == "rounds report":
            display_report = MenuController.request_rounds(tournament_table, user)
            DisplayReport.report_rounds(display_report)
        elif reports[report] == "players report":
            display_report = MenuController.request_players(tournament_table, user)
            DisplayReport.report_players(display_report)
        else:
            MenuView.welcome()

    @classmethod
    def choose_inter_menu(cls, actors_table, tournament_table, user):
        """Display menu between rounds."""
        MenuView.interround_menu()
        choices = {
            1: "continue tournament",
            2: "update rank",
            3: "welcome menu",
            4: "end program",
        }
        try:
            choice = int(input("Enter your choice (1, 2, 3, 4): \n"))
            if choice > 5:
                raise ValueError
            print("Your choice ({}) has been successfully entered...".format(choice))
        except ValueError:
            print("The value entered doesn't match the possible choices !\n")
            return MenuController.choose_inter_menu()
        if choices[choice] == "continue tournament":
            pass
        elif choices[choice] == "update rank":
            Player.update_rank(actors_table, tournament_table, user)
            return MenuController.choose_inter_menu(
                actors_table, tournament_table, user
            )
        elif choices[choice] == "welcome menu":
            MenuView.welcome()
        elif choices[choice] == "end program":
            print("Program ended ! See you soon!")
            # A CORRIGER POUR SORTIR DU PROGRAMME
        else:
            print("An error occurred.")
            return MenuController.choose_inter_menu(
                actors_table, tournament_table, user
            )

    @classmethod
    def request_players(cls, tournament_table, user):
        """Request for a tournament to display its players by alpha order or rank."""
        name = input("What is it name ? ")
        choice = tournament_table.search(user["name"] == name)
        players = choice[0].get("players")
        sorted_choice = int(input("Sorted by Last Name (1) or by Rank (2) ? "))
        if sorted_choice == 1:
            return sorted(players, key=lambda players: players["last name"])
        else:
            return sorted(players, key=lambda players: players["rank"])

    @classmethod
    def request_rounds(cls, tournament_table, user):
        """Request for a tournament to display its rounds or matchs."""
        name = input("What is it name ? ")
        choice = tournament_table.search(user["name"] == name)
        return choice[0].get("rounds")
