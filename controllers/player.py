from tinydb import TinyDB, Query

from .abstract import ABSController

from helpers import Input

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
        first_name = Input.for_string("Please enter player's first name: ").capitalize()
        last_name = Input.for_string("Please enter player's last name: ").capitalize()
        birth_date = input("Please enter player's birth date (format = DD/MM/YYYY): ")
        gender = Input.for_gender("Please enter player's gender ('m' / 'f'): ")
        rank = Input.for_integer("Please enter player's rank : ")
        score = Input.for_integer("Please enter player's total score : ")
        print("\n A player has been created.\n")

        player = Player(first_name, last_name, birth_date, gender, rank, score)
        player.save()
        return "main menu"

    @classmethod
    def update_rank_tournament(cls, players, tournament):
        """Update player's rank in the database and in the current tournament."""
        db = TinyDB("USERS.json")
        query = Query()
        first_name = Input.for_string("First name ? ").capitalize()
        last_name = Input.for_string("Last name ? ").capitalize()
        new_rank = Input.for_integer("Please enter player's  new rank : ")
        db.update(
            {"rank": new_rank},
            query["first_name"] == first_name and query["last_name"] == last_name,
        )
        for player in players:
            if first_name == player.first_name and last_name == player.last_name:
                player.rank = new_rank
                tournament.update_players(players)
        print("Rank updated !\n")
