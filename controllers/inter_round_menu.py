from view.inter_round_menu import InterRoundMenuView as View


class InterRoundMenu:
    """Class controls all the menus between 2 rounds during a tournament."""

    def __init__(self):
        self.view = View()

    def display(self):
        self.view.display()

    def get_command(self):
        choice = View.check_available_choices("Enter your choice (1, 2, 3) : \n")
        if choice == "1":
            return "continue tournament"
        elif choice == "2":
            return "update rank"
        elif choice == "3":
            return "quit"
