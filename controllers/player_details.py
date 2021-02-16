from tinydb import TinyDB, Query

from models.tournament import Tournament

from view.check_input import CheckView


class PlayerDetails:
    """Class controls all the different menus about the player in the program."""

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
