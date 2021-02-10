from controllers.player_details import PlayerDetails
from view.inter_round_menu import InterRoundMenuView
from view.report import ReportView
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
        InterRoundMenuView.display()
        choices = {
            1: "continue tournament",
            2: "update rank",
            3: "program end",
        }

        choice = InterRoundMenuView.check_available_three_choices(
            "Enter your choice (1, 2, 3) :\n"
        )

        if choices[choice] == "continue tournament":
            pass
        elif choices[choice] == "update rank":
            PlayerDetails.update_rank_tournament(
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
        ReportView.display()
        choice = ReportView.check_available_choices(
            "Enter your choice (1, 2, 3, 4, 5) :  \n"
        )
        if reports[choice] == "sorted_actors report":
            display_report = MenuController.sorted_actors(actors_table)
            ReportView.report_actors(display_report)
        elif reports[choice] == "tournaments report":
            display_report = tournaments_table.all()
            ReportView.report_tournaments(display_report)
        elif reports[choice] == "rounds report":
            display_report = MenuController.request_rounds(tournaments_table, user)
            ReportView.report_rounds(display_report)
        elif reports[choice] == "players report":
            display_report = MenuController.request_players(tournaments_table, user)
            ReportView.report_players(display_report)
        elif reports[choice] == "general menu":
            MainMenu.display()
