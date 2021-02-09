class DisplayInterRoundMenu:
    def display(self):
        """Display the menu between 2 rounds during a tournament."""
        print("\n==================================================")
        print("\n What would you like to do ?")
        print("1 - CONTINUE THE TOURNAMENT")
        print("2 - Change the ranking from a player ?")
        print("3 - End the program")

    @staticmethod
    def check_available_three_choices(message):
        """Check the input value when the choices are from 1 to 3."""
        boolean = True
        while boolean:
            try:
                choice = input(message)
                if choice not in [1, 2, 3]:
                    raise ValueError
                print(f"Your choice ({choice}) has been successfully entered...\n")
                boolean = False
                return choice
            except ValueError:
                print("The value entered doesn't match the possible choices !\n")
            except TypeError:
                print("Incorrect value, it has to be a positive number !")