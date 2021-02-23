from tinydb import TinyDB, Query

from .abstract import ABSController
from .check_input import CheckInputController as CheckInput

from view.main_menu import MainMenuView as View


class MainMenu(ABSController):
    """Display Main menu."""

    def __init__(self):
        self.view = View()

    def display(self):
        self.view.display()

    def get_command(self):
        command = CheckInput.check_available_six_choices(
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

    def update_rank(self):
        db = TinyDB("ACTORS.json")
        query = Query()
        """Update actor's rank in the database."""
        first_name = CheckInput.check_str("First name ? ").capitalize()
        last_name = CheckInput.check_str("Last name ? ").capitalize()
        new_rank = CheckInput.check_int("Please enter player's  new rank : ")
        db.update(
            {"rank": new_rank},
            query["first_name"] == first_name and query["last_name"] == last_name,
        )
        print("Rank updated !")
