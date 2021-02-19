class TournamentView:
    def display(self):
        """Display the creation of a new tournament."""
        print("\n==================================================")
        print("************CREATE A NEW TOURNAMENT**************\n")

    def display_menu(self):
        """Display the menu between 2 rounds during a tournament."""
        print("\n==================================================")
        print("\n What would you like to do ?")
        print("1 - CONTINUE THE TOURNAMENT")
        print("2 - Change the ranking from a player ?")
        print("3 - End the program")

    @staticmethod
    def check_available_three_choices(message):
        """Check the input value when the choices are from 1 to 3."""
        boolean = True
        while boolean:
            try:
                command = input(message)
                if command not in ["1", "2", "3"]:
                    raise ValueError
                print(f"Your command ({command}) has been successfully entered...\n")
                boolean = False
                return command
            except ValueError:
                print("The value entered doesn't match the possible choices !\n")
            except TypeError:
                print("Incorrect value, it has to be a positive number !")

    @staticmethod
    def check_score(message):
        """
        Check the value of the score is correct
        Enter the scores for each round:
        1 point for the winner,
        0.5 point if draw,
        0 point for the loser.
        """
        boolean = True
        while boolean:
            try:
                add_point = int(input(message))
                if add_point not in [0, 0.5, 1]:
                    raise ValueError
                boolean = False
                return add_point
            except ValueError:
                print(
                    "Incorrect score, it has to be 1 point for the winner, "
                    "0.5 point if draw, 0 point for the loser!"
                )
            except TypeError:
                print(
                    "Incorrect score, it has to be 1 point for the winner, "
                    "0.5 point if draw, 0 point for the loser!"
                )

    def display_final_score(self, players):
        """Display the final menu with the final score of the tournament."""
        print("\n==================================================")
        print(f"FINAL RESULTS OF {self.name} :\n")
        for player in players:
            print(f"SCORE : {player.points}, {player.first_name} {player.last_name}")
        print("\n==================================================")

    def display_next_round(players, i, j):
        """Display a match of a round different to the 1st round."""
        print(f"{players[i].first_name} vs {players[j].first_name}")
