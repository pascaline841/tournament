class NewTournament:
    """Request tournament's information."""

    @staticmethod
    def tournament_name():
        """Request tournament's name."""
        print("\n==================================================")
        print("************CREATE A NEW TOURNAMENT**************\n")
        name = input("Please enter tournament's name : ")
        print("Name entered successfully...")
        return name

    @staticmethod
    def tournament_location():
        """Request tournament's location."""
        location = input("Please enter tournament's location : ")
        print("Location entered successfully...")
        return location

    @staticmethod
    def tournament_mode():
        """Request tournament's mode : bullet, blitz or fast."""
        try:
            mode = input(
                "How would you like to play ? bullet / blitz / fast : "
            ).lower()
            if mode not in ["bullet", "blitz", "fast"]:
                raise ValueError
            print("Mode entered successfully...")
            return mode
        except ValueError:
            print("Incorrect timer type, it has to be bullet / blitz / fast !")
            return NewTournament.tournament_mode()

    @staticmethod
    def tournament_description():
        """Request tournament's description."""
        description = input("Please enter tournament's description : ")
        print("Description entered successfully...")
        return description
