class MainView:
    @staticmethod
    def welcome():
        print("************WELCOME TO CHESS TOURNEMENT**************\n\n\n\n")
        print("What would you like to do ?\n")
        print("1 - Create a new player\n")
        print("2 - Create a new tournament\n")
        print("3 - Continue an existing tournament\n")
        print("4 -  Edit reports\n")
        print("5 - End the program\n")
        try:
            choice = int(input("Enter your choice (1, 2, 3, 4) : \n"))
            if choice > 5:
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
        print("2 - End the program\n")
        try:
            choice = int(input("Enter your choice (1, 2) : \n"))
            if choice > 3:
                raise ValueError
            print(
                "\nYour choice ({}) has been successfully entered...\n".format(choice)
            )
            return choice
        except ValueError:
            print("\nThe value entered doesn't match the possible choices !\n")
            return MainView.back_menu()