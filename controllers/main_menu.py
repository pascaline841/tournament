from tinydb import TinyDB, Query

from .abstract import ABSController

from view.main_menu import MainMenuView as View
from view.check_input import CheckView


class MainMenu(ABSController):
    """Display Main menu."""

    def __init__(self):
        self.view = View()

    def display(self):
        self.view.display()

    def get_command(self):
        command = View.check_available_choices(
            "Enter your command(1, 2, 3, 4, 5, 6):\n"
        )
        if command == "1":
            return "create player"
        elif command == "2":
            return "create tournament"
        elif command == "3":
            return "pull tournament"
        elif command == "4":
            return "update rank"
        elif command == "5":
            return "display reports"
        elif command == "6":
            return "quit"

    @staticmethod
    def update_rank(cls):
        db = TinyDB("ACTORS.json")
        query = Query()
        """Update actor's rank in the database."""
        first_name = CheckView.check_str("First name ? ").capitalize()
        last_name = CheckView.check_str("Last name ? ").capitalize()
        new_rank = CheckView.check_int("Please enter player's  new rank : ")
        db.update(
            {"rank": new_rank},
            query["first_name"] == first_name and query["last_name"] == last_name,
        )
        print("Rank updated !")
