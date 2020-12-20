class NewPlayer:
    @staticmethod
    def player_first_name():
        first_name = input("Please enter player's first name : ")
        print("First name entered successfully...")
        return first_name

    @staticmethod
    def player_last_name():
        last_name = input("Please enter player's last name : ")
        print("Last name entered successfully...")
        return last_name

    @staticmethod
    def player_birth_date():
        birth_date = input("Please enter player's birth date (format = DD/MM/YYYY) : ")
        print("Birth date entered successfully...")
        return birth_date

    @staticmethod
    def player_gender():
        try:
            gender = input(
                "Please enter player's gender (format = 'Male' / 'Female') : "
            )
            if gender not in ["Male", "Female"]:
                raise ValueError
            print("Gender entered successfully...")
            return gender
        except ValueError:
            print("Incorrect gender, it has to be 'Male' / 'Female' !")
            return NewPlayer.player_gender()

    @staticmethod
    def player_rank():
        try:
            rank = int(input("Please enter player's rank : "))
            print("Rank entered successfully...")
            return rank
        except ValueError:
            print("Incorrect value, it has to be a positive number !")
            return NewPlayer.player_rank()

    @staticmethod
    def player_score():
        try:
            score = int(input("Please enter player's total score : "))
            print("Score entered successfully...")
            return score
        except ValueError:
            print("Incorrect value, it has to be a positive number !")
            return NewPlayer.player_score()

    @staticmethod
    def change_rank():
        """Menu to change the player's rank.  """

        choice_last_name = input("Please enter player's last name : ")
        print("Last name entered successfully...")
        try:
            rank = int(input("Please enter player's rank : "))
            print("Rank entered successfully...")
            return rank
        except ValueError:
            print("Incorrect value, it has to be a positive number !")
            return NewPlayer.change_rank()