from models.players import Player
from models.tournaments import Tournament
from models.database import Data
from view.menu import MainView
from view.newplayer import NewPlayer
from view.newtournament import NewTournament
from view.report import DisplayReport


class MenuController:
    """Class controls all the different menus in the program."""

    @classmethod
    def create_player(cls):
        """Create a new player."""
        first_name = NewPlayer.player_first_name()
        last_name = NewPlayer.player_last_name()
        birth_date = NewPlayer.player_birth_date()
        gender = NewPlayer.player_gender()
        rank = NewPlayer.player_rank()
        score = NewPlayer.player_score()
        return Player(first_name, last_name, birth_date, gender, rank, score)

    @classmethod
    def create_tournament(cls, players):
        """Create a new tournament."""
        name = NewTournament.tournament_name()
        location = NewTournament.tournament_location()
        mode = NewTournament.tournament_mode()
        description = NewTournament.tournament_description()
        return Tournament(name, location, mode, description, players)

    @classmethod
    def display_reports(cls, tournament_table, actors_table, user):
        """Display the reports' menu."""
        report = DisplayReport.menu_report()
        reports = {
            1: "sorted_actors_report",
            2: "tournaments_report",
            3: "rounds_report",
            4: "players_report",
        }
        if reports[report] == "sorted_actors_report":
            display_report = Data.sorted_actors(actors_table)
            DisplayReport.report_actors(display_report)
        elif reports[report] == "tournaments_report":
            display_report = tournament_table.all()
            DisplayReport.report_tournaments(display_report)
        elif reports[report] == "rounds_report":
            display_report = Data.request_tournament(tournament_table, user)
            DisplayReport.report_rounds(display_report)
        elif reports[report] == "players_report":
            display_report = Data.request_players(tournament_table, user)
            DisplayReport.report_players(display_report)
        else:
            MainView.welcome()
        DisplayReport.menu_report()

    @classmethod
    def back_menu(cls, actors_table, tournament_table, user):
        """Display menu to go back to the Main Menu."""
        choice = MainView.back_menu()
        choices = {
            1: "welcome_menu",
            2: "update_rank",
            3: "end_program",
        }
        if choices[choice] == "welcome_menu":
            MainView.welcome()
        elif choices[choice] == "update_rank":
            Data.update_rank(actors_table, tournament_table, user)
            return MenuController.back_menu()
        elif choices[choice] == "end_program":
            print("Program ended ! See you soon !")

        else:
            print("An error occurred.")
            return MenuController.back_menu()

    classmethod

    def inter_menu(cls, actors_table, tournament_table, user):
        """Display menu between rounds."""
        choice = MainView.interround_menu()
        choices = {
            1: "continue_tournamemnt",
            2: "update_rank",
            3: "welcome_menu",
            4: "end_program",
        }
        if choices[choice] == "continue_tournament":
            pass
        elif choices[choice] == "update_rank":
            Data.update_rank(actors_table, tournament_table, user)
            return MenuController.inter_menu(actors_table, tournament_table, user)
        elif choices[choice] == "welcome_menu":
            MainView.welcome()
        elif choices[choice] == "end_program":
            print("Program ended ! See you soon !")
        else:
            print("An error occurred.")
            return MenuController.inter_menu(actors_table, tournament_table, user)
