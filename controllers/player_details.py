from models.tournament import Tournament
from view.check_input import CheckView


class PlayerDetails:
    """Class controls all the different menus about the player in the program."""

    def choose_actors(i, actors_table, user):
        "Choose a player from the database to play in a tournament."
        boolean = True
        while boolean:
            choice = CheckView.check_str(
                f"PLAYER {i}: What is the FIRST NAME ? "
            ).capitalize()
            try:
                serialized_player = actors_table.get((user["first name"] == choice))
                if serialized_player is None:
                    raise TypeError
                boolean = False
                return serialized_player
            except TypeError:
                print("The value entered doesn't match the possible choices !\n")

    def update_rank(actors_table, user):
        """Update actor's rank in the database."""
        first_name = CheckView.check_str("First name ? ").capitalize()
        last_name = CheckView.check_str("Last name ? ").capitalize()
        new_rank = CheckView.check_int("Please enter player's  new rank : ")
        actors_table.update(
            {"rank": new_rank},
            user["first name"] == first_name and user["last name"] == last_name,
        )

    def update_rank_tournament(
        actors_table, tournaments_table, user, players, tournament
    ):
        """Update actor's rank in the database and in the current tournament."""
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
