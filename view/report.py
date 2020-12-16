class Report:
    @staticmethod
    def menu_report():
        print("\n\n\n\n************REPORTS**************\n\n\n\n")
        print("1 - List of all players in alphabetical order")
        print("2 - List of all players by ranking")
        print("3 - List of all tournaments")
        print("4 - List of all rounds by tournament")
        print("5 - List of all matches by tournament")
        print("6 - return to the general menu")
        try:
            choice = int(input("Enter your choice (1,2,3,4,5,6) : \n"))
            if choice > 7:
                raise ValueError
            print("\nYour choice ({}) has been successfully entered\n".format(choice))
            return choice

        except ValueError:
            print("\nThe value entered doesn't match the possible choices !\n")
            return Report.menu_report
