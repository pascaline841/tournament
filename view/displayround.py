class DisplayRound:
    """Display the matchs of the round during a tournament."""

    @classmethod
    def display_first_round(cls, players):
        """Display the matchs of the 1st round."""
        print("*******************ROUND 1 ******************\n")
        i = 0
        for i in range(4):
            print(f"{players[i].first_name} vs {players[i+4].first_name}")
            i += 1

    @classmethod
    def display_next_round(cls, players):
        """Display a match of a round different to the 1st round."""
        print(f"{players[i].first_name} vs {players[j].first_name}")
