class DisplayReport:
    @staticmethod
    def menu_report():
        print("************REPORTS**************")
        print("1 - List of all actors")
        print("2 - List of all tournaments")
        print("3 - List of all rounds and matches for a tournament")
        print("4 - List of all players for a tournament")
        print("5 - return to the general menu")
        try:
            report = int(input("Enter your choice (1, 2, 3, 4, 5) : \n"))
            if report > 6:
                raise ValueError
            print("Your choice ({}) has been successfully entered\n".format(report))
            return report

        except ValueError:
            print("The value entered doesn't match the possible choices !\n")
            return DisplayReport.menu_report
