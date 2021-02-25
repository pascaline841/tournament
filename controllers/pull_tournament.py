from .tournament import TournamentController
from .check_input import CheckInputController as CheckInput

from models.round import Round
from models.tournament import Tournament

from view.tournament import TournamentView as View


class PullTournament(TournamentController):
    """To continue an unfinished tournament."""

    def __init__(self):
        self.view = View()

    def display(self):
        pass

    def get_command(self):
        "Choose a uncompleted tournament in the database."
        serialized_tournament = None
        while not serialized_tournament:
            name = CheckInput.check_str("Name of an UNcompleted tournament ? ")
            serialized_tournament = Tournament.get(name)
            if serialized_tournament is None:
                print("The value entered doesn't match any tournament !\n")
        tournament = Tournament.deserialized(serialized_tournament)
        rounds = tournament.rounds
        serialized_rounds = []
        for round in rounds:
            serialized_round = Round.serialized(round)
            serialized_rounds.append(serialized_round)
        players = tournament.players
        nb_rounds = 5 - len(rounds)
        super().progress_next_rounds(
            tournament,
            players,
            serialized_rounds,
            nb_rounds,
        )
        return "main menu"  # NE MARCHE PAS/meme erreur que dans controllers.tournament
