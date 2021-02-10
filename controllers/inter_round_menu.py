from view.inter_round_menu import InterRoundMenuView as View


class InterRoundMenu:
    """Class displays the menu between 2 rounds during a tournament."""

    def __init__(self):
        self.view = View()

    def display(self):
        self.view.display()

    def get_command(self):
        command = View.check_available_choices("Enter your command (1, 2, 3) : \n")
        if command == "1":
            return "continue tournament"
        elif command == "2":
            return "update rank"
        elif command == "3":
            return "quit"
