from .abstract import ABSController

from view.main_menu import MainMenuView as View


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