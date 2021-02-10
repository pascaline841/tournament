from models.tournament import Tournament
from models.player import Player
from view.check_input import CheckView


class PlayerDetails:
    """Class controls all the different menus about the player in the program."""

    @staticmethod
    def create_list_players(actors_table, user):
        """Create a list of 8 players from the database."""
        players = []
        print("CHOOSE 8 PLAYERS FROM THE DATABASE\n")
        for i in range(1, 9):
            ser_player = PlayerDetails.choose_actors(i, actors_table, user)
            player = Player.deserialized_player(ser_player)
            players.append(player)
        return players

    def choose_actors(i, actors_table, user):
        "Choose a player from the database to play in a tournament."
        boolean = True
        while boolean:
            command = CheckView.check_str(
                f"PLAYER {i}: What is the FIRST NAME ? "
            ).capitalize()
            try:
                serialized_player = actors_table.get((user["first name"] == command))
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
