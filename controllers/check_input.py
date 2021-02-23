class CheckInputController:
    def check_str(self):
        """Check if the value of an input is a string."""
        boolean = True
        while boolean:
            try:
                value = input(self)
                if value.isalpha() is False:
                    raise ValueError
                boolean = False
                return value
            except ValueError:
                print("Incorrect value, it has to be a word !")

    def check_int(self):
        """Check if the value of an input is an integer."""
        boolean = True
        while boolean:
            try:
                boolean = False
                return int(input(self))
            except ValueError:
                print("Incorrect value, it has to be a positive number !")

    def check_score(self):
        """
        Check the value of the score is correct
        Enter the scores for each round:
        1 point for the winner,
        0.5 point if draw,
        0 point for the loser.
        """
        boolean = True
        while boolean:
            try:
                add_point = int(input(self))
                if add_point not in [0, 0.5, 1]:
                    raise ValueError
                boolean = False
                return add_point
            except ValueError:
                print(
                    "Incorrect score, it has to be 1 point for the winner, "
                    "0.5 point if draw, 0 point for the loser!"
                )
            except TypeError:
                print(
                    "Incorrect score, it has to be 1 point for the winner, "
                    "0.5 point if draw, 0 point for the loser!"
                )

    def check_available_three_choices(self):
        """Check the input value when the choices are from 1 to 3."""
        boolean = True
        while boolean:
            try:
                command = input(self)
                if command not in ["1", "2", "3"]:
                    raise ValueError
                print(f"Your command ({command}) has been successfully entered...\n")
                boolean = False
                return command
            except ValueError:
                print("The value entered doesn't match the possible choices !\n")
            except TypeError:
                print("Incorrect value, it has to be a positive number !")

    def check_available_five_choices(self):
        """Check the input value when the choices are from 1 to 5."""
        boolean = True
        while boolean:
            try:
                command = input(self)
                if command not in ["1", "2", "3", "4", "5"]:
                    raise ValueError
                print(f"Your command ({command}) has been successfully entered...\n")
                boolean = False
                return command
            except ValueError:
                print("The value entered doesn't match the possible choices !\n")
            except TypeError:
                print("Incorrect value, it has to be a positive number !")

    def check_available_six_choices(self):
        """Check the input value when the choices are from 1 to 6."""
        boolean = True
        while boolean:
            try:
                command = input(self)
                if command not in ["1", "2", "3", "4", "5", "6"]:
                    raise ValueError
                print(f"Your command ({command}) has been successfully entered...\n")
                boolean = False
                return command
            except ValueError:
                print("The value entered doesn't match the possible choices !\n")
            except TypeError:
                print("Incorrect value, it has to be a positive number !")

    def check_gender(self):
        """Check if the gender value is 'm' or 'f'."""
        boolean = True
        while boolean:
            try:
                gender = input(self).lower()
                if gender not in ["m", "f"]:
                    raise ValueError
                boolean = False
                return gender
            except TypeError:
                print("Incorrect gender, it has to be 'm' / 'f' !")
            except ValueError:
                print("Incorrect gender, it has to be 'm' / 'f' !")
