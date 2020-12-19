class NewTournament:
    @staticmethod
    def tournament_name():
        name = input("Please enter tournament's name : ")
        print("Name entered successfully...")
        return name

    @staticmethod
    def tournament_location():
        location = input("Please enter tournament's location : ")
        print("Location entered successfully...")
        return location

    @staticmethod
    def tournament_mode():
        try:
            mode = input("How would you like to play ? bullet / blitz / fast : ")
            if mode not in ["bullet", "blitz", "fast"]:
                raise ValueError
            print("Mode entered successfully...")
            return mode
        except ValueError:
            print("Incorrect timer type, it has to be Bullet / Blitz / Fast !")
            return NewTournament.tournament_mode()

    @staticmethod
    def tournament_description():
        description = input("Please enter tournament's description : ")
        print("Description entered successfully...")
        return description