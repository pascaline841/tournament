from models.players import Player
from models.tournaments import Tournament


class PlayerController:
    """Class controls all the different menus about the player in the program."""

    @classmethod
    def create_player(cls):
        """Create a new player."""
        print("\n************CREATE A NEW PLAYER **************\n")
        first_name = input("Please enter player's first name: ").capitalize()
        last_name = input("Please enter player's last name: ").capitalize()
        birth_date = input("Please enter player's birth date (format = DD/MM/YYYY): ")
        gender = PlayerController.choose_player_gender()
        rank = PlayerController.choose_player_rank()
        score = PlayerController.choose_player_score()
        print("\n A player has been created. \n")
        return Player(first_name, last_name, birth_date, gender, rank, score)

    @classmethod
    def choose_player_gender(cls):
        """Request player's gender."""
        try:
            gender = input(
                "Please enter player's gender (format = 'm' / 'f') : "
            ).lower()
            if gender not in ["m", "f"]:
                raise ValueError
            print("Gender entered successfully...")
            return gender
        except ValueError:
            print("Incorrect gender, it has to be 'm' / 'f' !")
            return PlayerController.chosse_player_gender()

    @classmethod
    def choose_player_rank(cls):
        """Choose the player's rank."""
        try:
            return int(input("Please enter player's rank : "))
        except ValueError:
            print("Incorrect value, it has to be a positive number !")
            return PlayerController.choose_player_rank()

    @classmethod
    def choose_player_score(cls):
        """Choose the player's score."""
        try:
            return int(input("Please enter player's total score : "))
        except ValueError:
            print("Incorrect value, it has to be a positive number !")
            return PlayerController.choose_player_score()

    @classmethod
    def choose_actors(cls, i, actors_table, user):
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

    @classmethod
    def add_score_match(cls, player):
        """
        Enter the scores for each round:
        1 point for the winner,
        0.5 point if draw,
        0 point for the loser.
        """
        try:
            add_point = float(input(f"Please enter {player.first_name}'s score : "))
            if add_point not in [0, 0.5, 1]:
                raise ValueError
            print("Score entered successfully...")
            return add_point
        except ValueError:
            print(
                "Incorrect score, it has to be 1 point for the winner, 0.5 point if draw, 0 point for the loser!"
            )
            return PlayerController.add_score_match(player)
        except TypeError:
            print(
                "Incorrect score, it has to be 1 point for the winner, 0.5 point if draw, 0 point for the loser!"
            )
            return PlayerController.add_score_match(player)

    @classmethod
    def update_rank(cls, actors_table, tournaments_table, user):
        """Update actor's rank in the database."""
        first_name = input("First name ? ").capitalize()
        last_name = input("Last name ? ").capitalize()
        try:
            new_rank = int(input("Please enter player's  new rank : "))
            actors_table.update(
                {"rank": new_rank},
                user["first name"] == first_name and user["last name"] == last_name,
            )
        except ValueError:
            print("Incorrect value, it has to be a positive number !")
            return PlayerController.update_rank()

    @classmethod
    def update_rank_tournament(
        cls, actors_table, tournaments_table, user, players, tournament
    ):
        """Update actor's rank in the database and in the current tournament."""
        first_name = input("First name ? ").capitalize()
        last_name = input("Last name ? ").capitalize()
        try:
            new_rank = int(input("Please enter player's  new rank : "))
            actors_table.update(
                {"rank": new_rank},
                user["first name"] == first_name and user["last name"] == last_name,
            )
            for player in players:
                if first_name == player.first_name and last_name == player.last_name:
                    player.rank = new_rank
                    Tournament.update_players(
                        tournament, players, tournaments_table, user
                    )
        except ValueError:
            print("Incorrect value, it has to be a positive number !")
            return PlayerController.update_rank_tournament(
                actors_table, tournaments_table, user, players, tournament
            )
