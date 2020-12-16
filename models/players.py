class Player:
    """Define the characteristics of a player."""

    def __init__(
        self, first_name, last_name, birth_date, gender, rank, score, score_game=0
    ):
        """
        First name :
        Last Name :
        Date of birth :
        Gender :
        Ranking :
        Score :
        Tournament Score : 0
        Opponents : list of opponents already met during a tournament.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        self.score = score
        self.score_game = score_game
        self.opponent = []

    def add_score_game(self, score_game, add_point):  # round 1 2 3 4
        """Add match score to player's score_game."""
        self.score_game = score_game + add_point
        return self.score_game

    def add_final_score(self, score_game, score):  # round 4
        """Add tournament score to player's total score."""
        self.score = score_game + score
        return self.score

    def delete_score_game(self, score_game):  # round 4
        """Clear tournament score."""
        self.score_game = 0
        return self.score_game

    def delete_opponent(self):  # round 4
        """Clear list of opponents."""
        self.opponent = []
        return self.opponent

    def __repr__(self):
        """Rank:[] [First Name], [Last Name], Score : [], Opponnents :[]."""
        return "Rank : {} {} {}, Score : {}, Opponnents :{}\n".format(
            self.rank, self.first_name, self.last_name, self.score_game, self.opponent
        )
