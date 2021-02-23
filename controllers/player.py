from tinydb import TinyDB, Query

from .abstract import ABSController
from .check_input import CheckInputController as CheckInput

from models.player import Player

from view.player import PlayerView as View


class PlayerController(ABSController):
    """Create a new player controller."""

    def __init__(self):
        self.view = View()

    def display(self):
        self.view.display()

    def get_command(self):
        """Create a new player."""
        first_name = CheckInput.check_str(
            "Please enter player's first name: "
        ).capitalize()
        last_name = CheckInput.check_str(
            "Please enter player's last name: "
        ).capitalize()
        birth_date = input("Please enter player's birth date (format = DD/MM/YYYY): ")
        gender = CheckInput.check_gender("Please enter player's gender ('m' / 'f'): ")
        rank = CheckInput.check_int("Please enter player's rank : ")
        score = CheckInput.check_int("Please enter player's total score : ")
        print("\n A player has been created.\n")

        player = Player(first_name, last_name, birth_date, gender, rank, score)
        player.save()
        return "main menu"

    @classmethod
    def update_rank_tournament(cls, players, tournament):
        """Update player's rank in the database and in the current tournament."""
        db = TinyDB("ACTORS.json")
        query = Query()
        first_name = CheckInput.check_str("First name ? ").capitalize()
        last_name = CheckInput.check_str("Last name ? ").capitalize()
        new_rank = CheckInput.check_int("Please enter player's  new rank : ")
        db.update(
            {"rank": new_rank},
            query["first_name"] == first_name and query["last_name"] == last_name,
        )
        for player in players:
            if first_name == player.first_name and last_name == player.last_name:
                player.rank = new_rank
                tournament.update_players(players)
        print("Rank updated !\n")
