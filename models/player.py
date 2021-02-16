from tinydb import Query, TinyDB


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
        """Display Rank:[] [First Name], [Last Name], Points: []."""
        return (
            f"Rank : {self.rank} {self.first_name} {self.last_name}, "
            f"Points : {self.points}\n"
        )

    def serialized_player(self):
        """Serialize player's data."""
        return vars(self)

    @classmethod
    def list(cls):
        """List of players for a demo."""
        db = TinyDB("ACTORS.json")
        players = []
        for player_data in db.all():
            player = Player(**player_data)
            players.append(player)
        return players

    @classmethod
    def get(cls, first_name):
        """Get a player from the database if exists."""
        db = TinyDB("ACTORS.json")
        query = Query()
        player_data = db.get(query["first name"] == first_name)
        if player_data:
            return Player(**player_data)
        return None

    def save(self):
        """Store new actor's informations in the database."""
        db = TinyDB("ACTORS.json")
        query = Query()
        db.update(
            {"rank": self.rank, "score": self.score},
            query["first name"] == self.first_name
            and query["last name"] == self.last_name,
        )
        serialized_player = vars(self)
        if serialized_player not in db:
            db.insert(serialized_player)

    def update_score(self, score):
        """Update actor's score in the database."""
        db = TinyDB("ACTORS.json")
        query = Query()
        db.update(
            {"score": score},
            query["first name"] == self.first_name
            and query["last name"] == self.last_name,
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
