class DisplayRound:
    """Display the matchs of the round during a tournament."""

    @staticmethod
    def display_first_round(players):
        """Display the matchs of the 1st round."""
        print("*******************ROUND 1 ******************\n")
        print(f"{players[0].first_name} vs {players[4].first_name}")
        print(f"{players[1].first_name} vs {players[5].first_name}")
        print(f"{players[2].first_name} vs {players[6].first_name}")
        print(f"{players[3].first_name} vs {players[7].first_name}")

    @staticmethod
    def display_next_round(players):
        """Display a match of a round different to the 1st round."""
        print(f"{players[i].first_name} vs {players[j].first_name}")