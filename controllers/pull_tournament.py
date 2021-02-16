from tinydb import TinyDB, Query

from .tournament_details import TournamentDetails

from models.round import Round
from models.tournament import Tournament

from view.check_input import CheckView as View


class PullTournament:
    """To continue an unfinished tournament."""

    def __init__(self):
        self.view = View()

    def run(self):
        serialized_tournament = self.get_command()
        self.update(serialized_tournament)

    def get_command(self):
        "Choose a uncompleted tournament in the database."
        db = TinyDB("TOURNAMENTS.json")
        query = Query()
        boolean = True
        while boolean:
            name = View.check_str("Name of an UNcompleted tournament ? ")
            try:
                serialized_tournament = db.get(query["name"] == name)
                if serialized_tournament is None:
                    raise TypeError
                boolean = False
                return serialized_tournament
            except TypeError:
                print("The value entered doesn't match any tournament !\n")

    def update(self, serialized_tournament: str):
        """To continue an unfinished tournament."""
        serialized_rounds = []
        tournament = Tournament.deserialized_tournament(serialized_tournament)
        rounds = tournament.rounds

        for round in rounds:
            serialized_round = Round.serialized_round(round)
            serialized_rounds.append(serialized_round)
        players = tournament.players
        rounds_done = len(rounds)
        total_rounds = tournament.nb_rounds
        nb_rounds = total_rounds - rounds_done
        TournamentDetails.progress_next_rounds(
            tournament,
            players,
            serialized_rounds,
            nb_rounds,
        )
