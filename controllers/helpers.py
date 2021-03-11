"""Helpers."""


class Input:
    """Help class for input function."""

    @classmethod
    def for_string(cls, message):
        """Check if the value of an input is a string."""
        value = input(message)
        while not value.isalpha():
            print("Incorrect value, it has to be a word !")
            value = input(message)
        return value

    @classmethod
    def for_integer(cls, message):
        """Check if the value of an input is an integer."""
        value = input(message)
        while not value.isdigit() or "." in value:
            print("Incorrect value, it has to be a positive number !")
            value = input(message)
        return int(value)

    @classmethod
    def for_score(cls, message):
        """
        Check the value of the score is correct.
        Enter the scores for each round:
        1 point for the winner,
        0.5 point if draw,
        0 point for the loser.
        """
        score = -1
        scores = [0, 0.5, 1]
        error = (
            "Incorrect score, it has to be 1 point for the winner, "
            "0.5 point if draw, 0 point for the loser!"
        )
        while score not in scores:
            try:
                score = input(message)
                score = float(score) if "." not in score else float(score)
            except (ValueError, TypeError):
                print(error)
        return score

    @classmethod
    def for_range(cls, message, range=[1, 2, 3]):
        """Check the input value when the choices are multiple."""
        while True:
            try:
                choice = int(input(message))
                if choice not in range:
                    raise ValueError
                print(f"Your command ({choice}) has been successfully entered...\n")
                return choice
            except (ValueError, TypeError):
                print("The value entered doesn't match the possible choices !\n")

    @classmethod
    def for_gender(cls, message):
        """Check if the gender value is 'm' or 'f'."""
        genders = ["m", "f"]
        while True:
            try:
                gender = input(message).lower()
                if gender not in genders:
                    raise ValueError
                return gender
            except (ValueError, TypeError):
                print("Incorrect gender, it has to be 'm' / 'f' !")
