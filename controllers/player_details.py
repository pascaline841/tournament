from models.tournament import Tournament
from view.check_input import CheckView


class PlayerDetails:
    """Class controls all the different menus about the player in the program."""

    @staticmethod
    def update_rank(actors_table, user):
        """Update actor's rank in the database."""
        first_name = CheckView.check_str("First name ? ").capitalize()
        last_name = CheckView.check_str("Last name ? ").capitalize()
        new_rank = CheckView.check_int("Please enter player's  new rank : ")
        actors_table.update(
            {"rank": new_rank},
            user["first name"] == first_name and user["last name"] == last_name,
        )

    @staticmethod
    def update_rank_tournament(
        actors_table, tournaments_table, user, players, tournament
    ):
        """Update player's rank in the database and in the current tournament."""
        first_name = CheckView.check_str("First name ? ").capitalize()
        last_name = CheckView.check_str("Last name ? ").capitalize()
        new_rank = CheckView.check_int("Please enter player's  new rank : ")
        actors_table.update(
            {"rank": new_rank},
            user["first name"] == first_name and user["last name"] == last_name,
        )
        for player in players:
            if first_name == player.first_name and last_name == player.last_name:
                player.rank = new_rank
                Tournament.update_players(tournament, players, tournaments_table, user)
