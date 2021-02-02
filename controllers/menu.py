from controllers.player import PlayerController
from view.menu import MenuView
from view.report import DisplayReport
import sys


class MenuController:
    """Class controls all the different menus in the program."""

    @classmethod
    def choose_welcome_menu(cls):
        """Inputs to the Welcome Menu."""
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
    def choose_inter_menu(
        cls,
        actors_table,
        tournaments_table,
        user,
        tournament,
        players,
    ):
        """Display menu between rounds."""
        MenuView.interround_menu()
        choices = {
            1: "continue tournament",
            2: "update rank",
            3: "end program",
        }
        try:
            choice = int(input("Enter your choice (1, 2, 3): \n"))
            if choice > 4:
                raise ValueError
            print("Your choice ({}) has been successfully entered...".format(choice))
        except ValueError:
            print("The value entered doesn't match the possible choices !\n")
            return MenuController.choose_inter_menu(
                actors_table,
                tournaments_table,
                user,
                tournament,
                players,
            )
        if choices[choice] == "continue tournament":
            pass
        elif choices[choice] == "update rank":
            PlayerController.update_rank_tournament(
                actors_table, tournaments_table, user, players, tournament
            )
            return MenuController.choose_inter_menu(
                actors_table,
                tournaments_table,
                user,
                tournament,
                players,
            )
        elif choices[choice] == "end program":
            sys.exit()
            return print("Program ended ! See you soon!")
        else:
            print("An error occurred.")
            return MenuController.choose_inter_menu(
                actors_table,
                tournaments_table,
                user,
                tournament,
                players,
            )

    @classmethod
    def choose_reports(cls, tournaments_table, actors_table, user):
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
            display_report = MenuController.sorted_actors(actors_table)
            DisplayReport.report_actors(display_report)
        elif reports[report] == "tournaments report":
            display_report = tournaments_table.all()
            DisplayReport.report_tournaments(display_report)
        elif reports[report] == "rounds report":
            display_report = MenuController.request_rounds(tournaments_table, user)
            DisplayReport.report_rounds(display_report)
        elif reports[report] == "players report":
            display_report = MenuController.request_players(tournaments_table, user)
            DisplayReport.report_players(display_report)
        else:
            MenuView.welcome()

    @classmethod
    def request_players(cls, tournaments_table, user):
        """Request for a tournament to display its players by alpha order or rank."""
        name = input("What is it name ? ")
        choice = tournaments_table.search(user["name"] == name)
        players = choice[0].get("players")
        sorted_choice = int(input("Sorted by Last Name (1) or by Rank (2) ? "))
        if sorted_choice == 1:
            return sorted(players, key=lambda players: players["last name"])
        else:
            return sorted(players, key=lambda players: players["rank"])

    @classmethod
    def request_rounds(cls, tournaments_table, user):
        """Request for a tournament to display its rounds or matchs."""
        name = input("What is it name ? ")
        choice = tournaments_table.search(user["name"] == name)
        return choice[0].get("rounds")

    @classmethod
    def sorted_actors(cls, actors_table):
        """Sort all actors by alphabetic order or by rank."""
        actors = actors_table.all()
        sorted_choice = int(input("Sorted by Last Name (1) or by Rank (2) ? "))
        if sorted_choice == 1:
            return sorted(actors, key=lambda actor: actor["last name"])
        else:
            return sorted(actors, key=lambda actor: actor["rank"])
