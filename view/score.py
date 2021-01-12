class Score:
    """Request the score after a round."""

    @classmethod
    def player_add_score_match(cls, player):
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
            return Score.player_add_score_match(player)
        except TypeError:
            print(
                "Incorrect score, it has to be 1 point for the winner, 0.5 point if draw, 0 point for the loser!"
            )
            return Score.player_add_score_match(player)
