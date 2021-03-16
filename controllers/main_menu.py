from tinydb import TinyDB, Query

from .abstract import ABSController

from helpers import Input

from view.main_menu import MainMenuView as View


class MainMenu(ABSController):
    """Display Main menu."""

    def __init__(self):
        self.view = View()

    def display(self):
        self.view.display()

    def get_command(self):
        command = Input.for_range(
            "Enter your command(1, 2, 3, 4, 5, 6):\n", [1, 2, 3, 4, 5, 6]
        )
        if command == 1:
            return "create player"
        elif command == 2:
            return "create tournament"
        elif command == 3:
            return "pull tournament"
        elif command == 4:
            return "update rank"
        elif command == 5:
            return "display reports"
        elif command == 6:
            return "quit"

    def update_rank(self):
        """Update user's rank in the database."""
        db = TinyDB("USERS.json")
        query = Query()
        first_name = Input.for_string("First name ? ").capitalize()
        last_name = Input.for_string("Last name ? ").capitalize()
        new_rank = Input.for_integer("Please enter player's  new rank : ")
        db.update(
            {"rank": new_rank},
            query["first_name"] == first_name and query["last_name"] == last_name,
        )
        print("Rank updated ! ")
