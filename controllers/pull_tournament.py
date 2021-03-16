from .tournament import TournamentController

from helpers import Input

from models.round import Round
from models.tournament import Tournament

from view.tournament import TournamentView as View


class PullTournament(TournamentController):
    """To continue an unfinished tournament."""

    def __init__(self):
        """Init."""
        self.view = View()
        self.tournament = None

    def display(self):
        tournament = self.tournament
        if not tournament:
            print("The value entered doesn't match any tournament !\n")

    def get_command(self):
        "Choose a uncompleted tournament in the database."
        tournament = self.tournament
        if not tournament:
            name = Input.for_string("Name of an UNcompleted tournament ? ")
            tournament = Tournament.get(name)
        if not tournament:
            return ""
        rounds = tournament.rounds
        serialized_rounds = []
        for round in rounds:
            serialized_round = Round.serialized(round)
            serialized_rounds.append(serialized_round)

        players = tournament.players
        nb_rounds = 4 - len(rounds)
        super().progress_next_rounds(
            tournament,
            players,
            serialized_rounds,
            nb_rounds,
        )
        return "main menu"
