from view.main_menu import MainMenuView as View


class MainMenu:
    """Main page controller."""

    def __init__(self):
        self.view = View()

    def display(self):
        self.view.display()

    def get_command(self):
        choice = View.check_available_choices("Enter your choice (1, 2, 3, 4, 5) : \n")
        if choice == "1":
            return "create player"
        elif choice == "2":
            return "create tournament"
        elif choice == "3":
            return "pull tournament"
        elif choice == "4":
            return "update rank"
        elif choice == "5":
            return "display reports"
        elif choice == "6":
            return "quit"
