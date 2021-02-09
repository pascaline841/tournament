from view.create_player import CreatePlayerView as View
from view.check_view import CheckView
from models.players import Player as Player


class CreatePlayer:
    """Create a new player controller."""

    def __init__(self):
        self.view = View()
        self.player = Player()

    def display(self):
        self.view.display()

    def get_command(self):
        """Create a new player."""
        first_name = CheckView.check_str(
            "Please enter player's first name: "
        ).capitalize()
        last_name = CheckView.check_str(
            "Please enter player's last name: "
        ).capitalize()
        birth_date = input("Please enter player's birth date (format = DD/MM/YYYY): ")
        gender = View.check_gender("Please enter player's gender ('m' / 'f'): ")
        rank = CheckView.check_int("Please enter player's rank : ")
        score = CheckView.check_int("Please enter player's total score : ")
        print("\n A player has been created. \n")
        return Player(first_name, last_name, birth_date, gender, rank, score)
