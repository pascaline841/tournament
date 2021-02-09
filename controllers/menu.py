from controllers.player import PlayerController
from view.menu import MenuView
from view.report import DisplayReport
import sys


class MenuController:
    """Class controls all the different menus in the program."""

    def choose_inter_menu(
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
            3: "program end",
        }

        choice = MenuView.check_available_three_choices(
            "Enter your choice (1, 2, 3) :\n"
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
        elif choices[choice] == "program end":
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

    def choose_reports(tournaments_table, actors_table, user):
        """Display the reports' menu."""
        reports = {
            1: "sorted_actors report",
            2: "tournaments report",
            3: "rounds report",
            4: "players report",
            5: "general menu",
        }
        DisplayReport.display_reports()
        choice = MenuView.check_available_five_choices(
            "Enter your choice (1, 2, 3, 4, 5) :  \n"
        )
        if reports[choice] == "sorted_actors report":
            display_report = MenuController.sorted_actors(actors_table)
            DisplayReport.report_actors(display_report)
        elif reports[choice] == "tournaments report":
            display_report = tournaments_table.all()
            DisplayReport.report_tournaments(display_report)
        elif reports[choice] == "rounds report":
            display_report = MenuController.request_rounds(tournaments_table, user)
            DisplayReport.report_rounds(display_report)
        elif reports[choice] == "players report":
            display_report = MenuController.request_players(tournaments_table, user)
            DisplayReport.report_players(display_report)
        elif reports[choice] == "general menu":
            MenuView.welcome()
