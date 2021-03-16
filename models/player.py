from tinydb import Query, TinyDB


class Player:
    """Define the characteristics of a player.
    Attrs:
        first_name (str)
        last_name (str)
        date_of_birth (str)
        gender (str): 'm' or 'f'
        rank (int)
        score (int)
        points (int)
        opponents (list): opponents already met during a tournament
    """

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
        """Init."""
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        self.score = score
        self.points = points
        self.opponents = []

    def __repr__(self):
        """Display Rank:[] [First Name], [Last Name], Points: []."""
        return (
            f"Rank : {self.rank} {self.first_name} {self.last_name}, "
            f"Points : {self.points}\n"
        )

    def serialized(self):
        """Serialize player's data."""
        return vars(self)

    @classmethod
    def deserialized(cls, data):
        """Pull player's datas from the database to continue a tournament."""
        return Player(**data)

    @classmethod
    def get(cls, first_name):
        """Get a player from the database if exists."""
        db = TinyDB("USERS.json")
        query = Query()
        data = db.get(query["first_name"] == first_name)
        if data:
            return Player(**data)
        return None

    def save(self):
        """Store new user's informations in the database."""
        db = TinyDB("USERS.json")
        query = Query()
        db.update(
            {"rank": self.rank, "score": self.score},
            query["first_name"] == self.first_name
            and query["last_name"] == self.last_name,
        )
        serialized_player = Player.serialized(self)
        if serialized_player not in db:
            db.insert(serialized_player)

    def update_score(self, score):
        """Update user's score in the database."""
        db = TinyDB("USERS.json")
        query = Query()
        db.update(
            {"score": score},
            query["first_name"] == self.first_name
            and query["last_name"] == self.last_name,
        )

    def add_points(self, add_point):
        """
        At the end of all the rounds.
        Add match score to player's points.
        """
        self.points += add_point
        return self.points

    def add_final_score(self, points, score):
        """
        Last round only.
        Add tournament score to player's total score.
        """
        self.score = points + score
        return self.score
