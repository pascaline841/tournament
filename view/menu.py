class MainView:
    @staticmethod
    def welcome():
        print("************WELCOME TO CHESS TOURNEMENT**************\n\n\n\n")
        print("What would you like to do ?\n")
        print("1 - Create a new player\n")
        print("2 - Create a new tournament\n")
        print("3 - Continue an existing tournament\n")
        print("4 - Change the ranking from a player ? \n")
        print("5 -  Edit reports\n")
        print("6 - End the program\n")
        try:
            choice = int(input("Enter your choice (1, 2, 3, 4, 5) : \n"))
            if choice > 7:
                raise ValueError
            print(
                "\n Your choice ({}) has been successfully entered...\n".format(choice)
            )
            return choice
        except ValueError:
            print("\nThe value entered doesn't match the possible choices !\n")
            return MainView.welcome()

    @staticmethod
    def back_menu():
        print("\n==================================================")
        print("What would you like to do ?\n")
        print("1 - Back to the Main Menu\n")
        print("2 - Change the ranking from a player ? \n")
        print("3 - End the program\n")
        try:
            choice = int(input("Enter your choice (1, 2, 3) : \n"))
            if choice > 4:
                raise ValueError
            print("Your choice ({}) has been successfully entered...".format(choice))
            return choice
        except ValueError:
            print("\nThe value entered doesn't match the possible choices !\n")
            return MainView.back_menu()

    @staticmethod
    def interround_menu():
        print("\n==================================================")
        print("What would you like to do ?\n")
        print("1 - Back to the Main Menu\n")
        print("2 - Change the ranking from a player ? \n")
        print("3 - CONTINUE THE TOURNAMENT\n")
        print("4 - End the program\n")
        try:
            choice = int(input("Enter your choice (1, 2, 3, 4) : \n"))
            if choice > 5:
                raise ValueError
            print("Your choice ({}) has been successfully entered...".format(choice))
            return choice
        except ValueError:
            print("\nThe value entered doesn't match the possible choices !\n")
            return MainView.interround_menu()