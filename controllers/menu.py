from models.players import Player
from models.tournaments import Tournament
from models.database import Data
from view.menu import MainView
from view.newplayer import NewPlayer
from view.newtournament import NewTournament
from view.report import DisplayReport


class MenuController:
    """Class controls all the different menus in the program."""

    def create_player():
        """Create a new player."""
        first_name = NewPlayer.player_first_name()
        last_name = NewPlayer.player_last_name()
        birth_date = NewPlayer.player_birth_date()
        gender = NewPlayer.player_gender()
        rank = NewPlayer.player_rank()
        score = NewPlayer.player_score()
        return Player(first_name, last_name, birth_date, gender, rank, score)

    def create_tournament(players):
        """Create a new tournament. """
        name = NewTournament.tournament_name()
        location = NewTournament.tournament_location()
        mode = NewTournament.tournament_mode()
        description = NewTournament.tournament_description()
        return Tournament(name, location, mode, description, players)

    def display_reports(tournament_table, actors_table, user):
        """Display the reports' menu. """
        report = DisplayReport.menu_report()
        if report == 1:
            display_report = Data.sorted_actors(actors_table)
            DisplayReport.report_1(display_report)
        elif report == 2:
            display_report = tournament_table.all()
            DisplayReport.report_2(display_report)
        elif report == 3:
            display_report = Data.request_tournament(tournament_table, user)
            DisplayReport.report_3(display_report)
        elif report == 4:
            display_report = Data.request_players(tournament_table, user)
            DisplayReport.report_4(display_report)
        else:
            MainView.welcome()
        DisplayReport.menu_report()

    def back_menu(actors_table, tournament_table, user):
        """Display menu to go back to the Main Menu."""
        choice = MainView.back_menu()
        if choice == 1:
            MainView.welcome()
        elif choice == 2:
            Data.update_rank(actors_table, tournament_table, user)
            return MenuController.back_menu()
        elif choice == 3:
            print("Program ended ! See you soon !")
        else:
            print("An error occurred.")
            return MenuController.back_menu()

    def inter_menu(actors_table, tournament_table, user):
        """Display menu between rounds."""
        choice = MainView.interround_menu()
        if choice == 1:
            pass
        elif choice == 2:
            Data.update_rank(actors_table, tournament_table, user)
            return MenuController.inter_menu(actors_table, tournament_table, user)
        elif choice == 3:
            MainView.welcome()
        elif choice == 4:
            print("Program ended ! See you soon !")
        else:
            print("An error occurred.")
            return MenuController.inter_menu(actors_table, user)