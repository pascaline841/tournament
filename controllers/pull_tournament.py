from view.menu import MenuView as View
from models.tournaments import Tournament as Tournament
from models.rounds import Round as Round

from controller.tournament import TournamentController


class PullTournament:
    """To continue an unfinished tournament."""

    def __init__(self):
        self.tournament = Tournament()
        self.round = Round()

    def choose_tournament(self, tournaments_table, user):
        "Choose a uncompleted tournament in the database."
        boolean = True
        while boolean:
            name = View.check_str("Name of an UNcompleted tournament ? ")
            try:
                serialized_tournament = tournaments_table.get(user["name"] == name)
                if serialized_tournament is None:
                    raise TypeError
                boolean = False
                return serialized_tournament
            except TypeError:
                print("The value entered doesn't match any tournament !\n")

    def get_command(self, tournaments_table, serialized_rounds, actors_table, user):
        """To continue an unfinished tournament."""
        serialized_tournament = PullTournament.choose_tournament(
            tournaments_table, user
        )
        tournament = Tournament.deserialized_tournament(serialized_tournament)
        rounds = tournament.rounds
        for round in rounds:
            serialized_round = Round.serialized_round(round)
            serialized_rounds.append(serialized_round)
        players = tournament.players
        rounds_done = len(rounds)
        total_rounds = tournament.nb_rounds
        nb_rounds = total_rounds - rounds_done
        TournamentController.progress_next_rounds(
            tournament,
            players,
            serialized_rounds,
            tournaments_table,
            user,
            actors_table,
            nb_rounds,
        )
