class MenuView:
    """Display the different menus and check the different Value or Type Error."""

    def display_final_score(self, players):
        """Display the final menu with the final score of the tournament."""
        print("\n==================================================")
        print(f"FINAL RESULTS OF {self.name} :\n")
        for player in players:
            print(f"SCORE : {player.points}, {player.first_name} {player.last_name}\n")
        print("\n==================================================")

    def display_next_round(players, i, j):
        """Display a match of a round different to the 1st round."""
        print(f"{players[i].first_name} vs {players[j].first_name}")

    @staticmethod
    def check_score(message):
        """
        Enter the scores for each round:
        1 point for the winner,
        0.5 point if draw,
        0 point for the loser.
        """
        boolean = True
        while boolean:
            try:
                add_point = input(message)
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
