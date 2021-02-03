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
        points=0,
        opponents=[],
    ):
        """
        First name :
        Last Name :
        Date of birth :
        Gender :
        Ranking :
        Score :
        Points : 0
        Opponents : list of opponents already met during a tournament.
        """
        
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        self.score = score
        self.points = points
        self.opponents = []

    def __repr__(self):
        """Display Rank:[] [First Name], [Last Name], Points: [], Opponnents :[]."""
        return (
            f"Rank : {self.rank} {self.first_name} {self.last_name}, "
            f"Points : {self.points}, Opponents : {self.opponents}\n"
        )

    def serialized_player(self):
        """Serialize player's data."""
        return {
            "first name": self.first_name,
            "last name": self.last_name,
            "birth date": self.birth_date,
            "gender": self.gender,
            "rank": self.rank,
            "score": self.score,
            "points": self.points,
            "opponents": self.opponents,
        }

    @classmethod
    def deserialized_player(cls, ser_player):
        """Pull player's informations from the database to continue a tournament."""
        first_name = ser_player["first name"]
        last_name = ser_player["last name"]
        birth_date = ser_player["birth date"]
        gender = ser_player["gender"]
        rank = ser_player["rank"]
        score = ser_player["score"]
        points = ser_player["points"]
        opponents = ser_player["opponents"]
        return Player(
            first_name,
            last_name,
            birth_date,
            gender,
            rank,
            score,
            points,
            opponents,
        )

    def store_data_actors(self, user, actors_table):
        """Store actor's informations in the database."""
        ser_player = Player.serialized_player(self)
        actors_table.update(
            {"rank": self.rank, "score": self.score},
            user["first name"] == self.first_name
            and user["last name"] == self.last_name,
        )
        if ser_player not in actors_table:
            actors_table.insert(ser_player)
        return ser_player

    def update_score(self, actors_table, score, user):
        """Update actor's score in the database."""
        actors_table.update(
            {"score": score},
            user["first name"] == self.first_name
            and user["last name"] == self.last_name,
        )

    def add_points(self, add_point):
        """At the end of all the rounds.
        Add match score to player's points."""
        
        self.points += add_point
        return self.points

    def add_final_score(self, points, score):
        """Last round only.
        Add tournament score to player's total score."""

        self.score = points + score
        return self.score
