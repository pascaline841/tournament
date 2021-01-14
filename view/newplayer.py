class NewPlayer:
    """Request player's informations."""

    @staticmethod
    def player_gender():
        """Request player's gender."""
        try:
            gender = input(
                "Please enter player's gender (format = 'm' / 'f') : "
            ).lower()
            if gender not in ["m", "f"]:
                raise ValueError
            print("Gender entered successfully...")
            return gender
        except ValueError:
            print("Incorrect gender, it has to be 'm' / 'f' !")
            return NewPlayer.player_gender()

    @staticmethod
    def player_rank():
        """Request player's rank."""
        try:
            rank = int(input("Please enter player's rank : "))
            print("Rank entered successfully...")
            return rank
        except ValueError:
            print("Incorrect value, it has to be a positive number !")
            return NewPlayer.player_rank()

    @staticmethod
    def player_score():
        """Request player's score."""
        try:
            score = int(input("Please enter player's total score : "))
            print("Score entered successfully...")
            return score
        except ValueError:
            print("Incorrect value, it has to be a positive number !")
            return NewPlayer.player_score()

    @staticmethod
    def change_rank():
        """Request to change the player's rank."""
        choice_last_name = input("Please enter player's last name : ").capitalize()
        print("Last name entered successfully...")
        return choice_last_name
        try:
            rank = int(input("Please enter player's rank : "))
            print("Rank entered successfully...")
            return rank
        except ValueError:
            print("Incorrect value, it has to be a positive number !")
            return NewPlayer.change_rank()
