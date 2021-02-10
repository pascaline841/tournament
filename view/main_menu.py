class MainMenuView:
    def display(self):
        """Display the main menu."""
        print("\n==================================================")
        print("\n************ WELCOME TO CHESS TOURNEMENT MANAGER **************\n")
        print("What would you like to do ?")
        print("1 - Create a new player")
        print("2 - Create a new tournament")
        print("3 - Continue an existing tournament")
        print("4 - Change the ranking from a player ?")
        print("5 -  Edit reports")
        print("6 - End the program")

    @staticmethod
    def check_available_choices(message):
        """Check the input value when the choices are from 1 to 6."""
        boolean = True
        while boolean:
            try:
                command = input(message)
                if command not in ["1", "2", "3", "4", "5", "6"]:
                    raise ValueError
                print(f"Your command ({command}) has been successfully entered...\n")
                boolean = False
                return command
            except ValueError:
                print("The value entered doesn't match the possible choices !\n")
            except TypeError:
                print("Incorrect value, it has to be a positive number !")
