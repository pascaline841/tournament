class MenuView:
    """Display the different menus."""

    @classmethod
    def welcome(cls):
        """Display the main menu."""
        print("\n************ WELCOME TO CHESS TOURNEMENT MANAGER **************\n")
        print("What would you like to do ?")
        print("1 - Create a new player")
        print("2 - Create a new tournament")
        print("3 - Continue an existing tournament")
        print("4 - Change the ranking from a player ?")
        print("5 -  Edit reports")
        print("6 - End the program")

    @classmethod
    def interround_menu(cls):
        """Display the menu between 2 rounds during a tournament."""
        print("\n==================================================")
        print("\n What would you like to do ?")
        print("1 - CONTINUE THE TOURNAMENT")
        print("2 - Change the ranking from a player ?")
        print("3 - Back to the Main Menu")
        print("4 - End the program")

    def display_final_score(self, players):
        """Display the final menu with the final score of the tournament."""
        print("\n==================================================")
        print(f"FINAL RESULTS OF {self.name} :\n")
        for player in players:
            print(f"SCORE : {player.points}, {player.first_name} {player.last_name}")
