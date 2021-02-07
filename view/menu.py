class MenuView:
    """Display the different menus and check the different Value or Type Error."""

    @staticmethod
    def welcome():
        """Display the main menu."""
        print("\n************ WELCOME TO CHESS TOURNEMENT MANAGER **************\n")
        print("What would you like to do ?")
        print("1 - Create a new player")
        print("2 - Create a new tournament")
        print("3 - Continue an existing tournament")
        print("4 - Change the ranking from a player ?")
        print("5 -  Edit reports")
        print("6 - End the program")

    @staticmethod
    def display_create_tournament()
        """Display the creation of a new tournament."""
        print("\n==================================================")
        print("************CREATE A NEW TOURNAMENT**************\n")

    @staticmethod
    def display_create_player():
        """Display the creation of a new player."""
        print("\n==================================================")
        print("\n************CREATE A NEW PLAYER **************\n")

    @staticmethod
    def interround_menu():
        """Display the menu between 2 rounds during a tournament."""
        print("\n==================================================")
        print("\n What would you like to do ?")
        print("1 - CONTINUE THE TOURNAMENT")
        print("2 - Change the ranking from a player ?")
        print("3 - End the program")

    def display_final_score(self, players):
        """Display the final menu with the final score of the tournament."""
        print("\n==================================================")
        print(f"FINAL RESULTS OF {self.name} :\n")
        for player in players:
            print(f"SCORE : {player.points}, {player.first_name} {player.last_name}\n")
        print("\n==================================================")

    def display_next_round(players, i, j):
        """Display a match of a round different to the 1st round."""
        print(f"{players[i].first_name} vs {players[j].first_name}")

    @staticmethod
    def check_str(message):
        """Check if the value of an input is a string."""
        boolean = True
        while boolean:
            try:
                value = input(message)
                if value.isalpha() is False:
                    raise ValueError
                boolean = False
                return value
            except ValueError:
                print("Incorrect value, it has to be a word !")

    @staticmethod
    def check_int(message):
        """Check if the value of an input is an integer."""
        try:
            return int(input(message))
        except ValueError:
            print("Incorrect value, it has to be a positive number !")
            return MenuView.check_int(message)

    @staticmethod
    def check_gender(message):
        """Check if the gender value is 'm' or 'f'."""
        boolean = True
        while boolean:
            try:
                gender = input(message).lower()
                if gender not in ["m", "f"]:
                    raise ValueError
                print("Gender entered successfully...")
                boolean = False
                return gender
            except TypeError:
                print("Incorrect gender, it has to be 'm' / 'f' !")
            except ValueError:
                print("Incorrect gender, it has to be 'm' / 'f' !")

    @staticmethod
    def check_available_three_choices(message):
        """Check the input value when the choice are from 1 to 3."""
        boolean = True
        while boolean:
            try:
                choice = int(input(message))
                if choice > 3:
                    raise ValueError
                print(f"Your choice ({choice}) has been successfully entered...\n")
                boolean = False
                return choice
            except ValueError:
                print("The value entered doesn't match the possible choices !\n")
            except TypeError:
                print("Incorrect value, it has to be a positive number !")

    @staticmethod
    def check_available_five_choices(message):
        """Check the input value when the choice are from 1 to 5."""
        boolean = True
        while boolean:
            try:
                choice = int(input(message))
                if choice > 5:
                    raise ValueError
                print(f"Your choice ({choice}) has been successfully entered...\n")
                boolean = False
                return choice
            except ValueError:
                print("The value entered doesn't match the possible choices !\n")
            except TypeError:
                print("Incorrect value, it has to be a positive number !")

    @staticmethod
    def check_score(message):
        """
        Enter the scores for each round:
        1 point for the winner,
        0.5 point if draw,
        0 point for the loser.
        """
        boolean = True
        while boolean:
            try:
                add_point = float(input(message))
                if add_point not in [0, 0.5, 1]:
                    raise ValueError
                boolean = False
                return add_point
            except ValueError:
                print(
                    "Incorrect score, it has to be 1 point for the winner, "
                    "0.5 point if draw, 0 point for the loser!"
                )
            except TypeError:
                print(
                    "Incorrect score, it has to be 1 point for the winner, "
                    "0.5 point if draw, 0 point for the loser!"
                )
