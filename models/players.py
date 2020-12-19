class Player:
    """Define the characteristics of a player."""

    def __init__(
        self,
        first_name,
        last_name,
        birth_date,
        gender,
        rank,
        score,
        score_game=0,
        point=0,
        opponent_point=0,
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
        self.point = point
        self.opponent = []
        self.opponent_point = opponent_point

    def add_score_game(self, score_game, add_point):  # round 1 2 3 4
        """Add match score to player's score_game."""
        self.score_game = score_game + add_point
        return self.score_game

    def add_final_score(self, score_game, score):  # round 4
        """Add tournament score to player's total score."""
        self.score = score_game + score
        return self.score

    def __repr__(self):
        """Rank:[] [First Name], [Last Name], Score : [], Opponnents :[]."""
        return "Rank : {} {} {}, Score : {}, Opponnents :{}\n".format(
            self.rank, self.first_name, self.last_name, self.score_game, self.opponent
        )

    def serial_p(self, p_tab):
        """serialized player's data"""
        serial_p = {
            "firt name": self.first_name,
            "last name": self.last_name,
            "birth date": self.birth_date,
            "gender": self.gender,
            "rank": self.rank,
            "score": self.score,
        }
        search_f = self.first_name
        search_l = self.last_name
        search_r = self.rank
        return serial_p, search_f, search_l, search_r