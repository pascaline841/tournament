from tinydb import TinyDB, Query

from .abstract import ABSController

from models.player import Player
from models.tournament import Tournament

from view.player import PlayerView as View
from view.check_input import CheckView


class PlayerController(ABSController):
    """Create a new player controller."""

    def __init__(self):
        self.view = View()

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

        player = Player(first_name, last_name, birth_date, gender, rank, score)
        player.save()

    @classmethod
    def update_rank(cls):
        db = TinyDB("ACTORS.json")
        query = Query()
        """Update actor's rank in the database."""
        first_name = CheckView.check_str("First name ? ").capitalize()
        last_name = CheckView.check_str("Last name ? ").capitalize()
        new_rank = CheckView.check_int("Please enter player's  new rank : ")
        db.update(
            {"rank": new_rank},
            query["first name"] == first_name and query["last name"] == last_name,
        )

    @classmethod
    def update_rank_tournament(cls, players, tournament):
        """Update player's rank in the database and in the current tournament."""
        db = TinyDB("ACTORS.json")
        query = Query()
        first_name = CheckView.check_str("First name ? ").capitalize()
        last_name = CheckView.check_str("Last name ? ").capitalize()
        new_rank = CheckView.check_int("Please enter player's  new rank : ")
        db.update(
            {"rank": new_rank},
            query["first name"] == first_name and query["last name"] == last_name,
        )
        for player in players:
            if first_name == player.first_name and last_name == player.last_name:
                player.rank = new_rank
                Tournament.update_players(players, tournament)
