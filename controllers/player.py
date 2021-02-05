from models.players import Player
from models.tournaments import Tournament
from view.menu import MenuView


class PlayerController:
    """Class controls all the different menus about the player in the program."""

    @staticmethod
    def create_player():
        """Create a new player."""
        print("\n************CREATE A NEW PLAYER **************\n")
        first_name = MenuView.check_str(
            "Please enter player's first name: "
        ).capitalize()
        last_name = MenuView.check_str("Please enter player's last name: ").capitalize()
        birth_date = input("Please enter player's birth date (format = DD/MM/YYYY): ")
        gender = MenuView.check_gender("Please enter player's gender ('m' / 'f'): ")
        rank = MenuView.check_int("Please enter player's rank : ")
        score = MenuView.check_int("Please enter player's total score : ")
        print("\n A player has been created. \n")
        return Player(first_name, last_name, birth_date, gender, rank, score)

    def choose_actors(i, actors_table, user):
        "Choose a player from the database to play in a tournament."
        try:
            choice = input(f"PLAYER {i}: What is the FIRST NAME ? ").capitalize()
            serialized_player = actors_table.get((user["first name"] == choice))
            if serialized_player is None:
                raise TypeError
        except TypeError:
            print("The value entered doesn't match the possible choices !\n")
            return PlayerController.choose_actors(i, actors_table, user)
        return serialized_player

    def update_rank(actors_table, tournaments_table, user):
        """Update actor's rank in the database."""
        first_name = MenuView.check_str("First name ? ").capitalize()
        last_name = MenuView.check_str("Last name ? ").capitalize()
        new_rank = MenuView.check_int("Please enter player's  new rank : ")
        actors_table.update(
            {"rank": new_rank},
            user["first name"] == first_name and user["last name"] == last_name,
        )

    def update_rank_tournament(
        actors_table, tournaments_table, user, players, tournament
    ):
        """Update actor's rank in the database and in the current tournament."""
        first_name = MenuView.check_str("First name ? ").capitalize()
        last_name = MenuView.check_str("Last name ? ").capitalize()
        new_rank = MenuView.check_int("Please enter player's  new rank : ")
        actors_table.update(
            {"rank": new_rank},
            user["first name"] == first_name and user["last name"] == last_name,
        )
        for player in players:
            if first_name == player.first_name and last_name == player.last_name:
                player.rank = new_rank
                Tournament.update_players(tournament, players, tournaments_table, user)
