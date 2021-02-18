import datetime

from .inter_round_controller import InterRoundController
from .tournament_creation import TournamentCreation

from models.player import Player
from models.round import Round
from models.tournament import Tournament

from view.score import ScoreView


class TournamentDetails:
    """Class controls the tournament progress."""

    def __init__(self):
        self.controller = TournamentCreation()

    def run(self):
        tournament = self.controller
        self.get_command(tournament)

    def get_command(
        self,
        tournament,
        players,
        serialized_rounds,
    ):
        print(tournament)
        self.progress_first_round(
            tournament,
            players,
            serialized_rounds,
        )
        nb_rounds = tournament.nb_rounds
        self.progress_next_rounds(
            tournament,
            players,
            serialized_rounds,
            nb_rounds,
        )

    def get_first_round(self, rounds, players):
        """Create the first round of a tournament."""
        players = sorted(players, key=lambda player: player.rank)
        round = Round(
            "Round 1", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), matchs=[]
        )
        for index in range(4):
            print(f"{players[index].first_name} vs {players[index+4].first_name}")
        self.get_first_opponents(players)
        for player in players:
            add_point = ScoreView.check_score(
                f"Please enter {player.first_name}'s score : "
            )
            player.add_points(add_point)
        Round.first_matchs(round, players)
        round.end = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        rounds.append(round)
        print(f"\n{round}")
        return round

    def progress_first_round(
        self,
        tournament,
        players,
        serialized_rounds,
    ):
        """Run the first round."""
        rounds = tournament.rounds
        round = self.get_first_round(rounds, players)
        serialized_round = Round.serialized_round(round)
        serialized_rounds.append(serialized_round)
        Tournament.update_round(tournament, serialized_rounds)
        Tournament.update_players(tournament, players)
        InterRoundController.run()

    def get_next_round(self, tournament, rounds, players):
        """Create Round 2, 3 , 4."""
        print(f"\n*******************ROUND {len(rounds)+1}******************\n")
        round = Round(
            f"Round {len(rounds) + 1}",
            datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            matchs=[],
        )
        players = sorted(
            sorted(
                players,
                key=lambda player: player.rank,
            ),
            key=lambda player: player.points,
            reverse=True,
        )
        print(players)
        round.get_opponents(players)
        for player in players:
            add_point = ScoreView.check_score(
                f"Please enter {player.first_name}'s score : "
            )
            player.add_points(add_point)
        round.end = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        rounds.append(round)
        print(f"\n{round}")
        return round

    def progress_next_rounds(
        self,
        tournament,
        players,
        serialized_rounds,
        nb_rounds,
    ):
        """Run the following rounds."""
        while nb_rounds > 1:
            nb_rounds -= 1
            rounds = tournament.rounds
            round = self.get_next_round(tournament, rounds, players)
            serialized_round = Round.serialized_round(round)
            serialized_rounds.append(serialized_round)
            Tournament.update_round(tournament, serialized_rounds)
            Tournament.update_players(tournament, players)
            InterRoundController.run()
            players = sorted(
                sorted(
                    players,
                    key=lambda player: player.rank,
                ),
                key=lambda player: player.points,
                reverse=True,
            )
        for player in players:
            score = player.add_final_score(player.points, player.score)
            Player.update_score(player, score)
        ScoreView.display_final_score(tournament, players)

    @staticmethod
    def get_first_opponents(players):
        """
        First Round : The players are ranked by best ranking.
        Add oppponent's name to the player's opponents list.
        """
        players[0].opponents.append(players[4].first_name)
        players[4].opponents.append(players[0].first_name)
        players[1].opponents.append(players[5].first_name)
        players[5].opponents.append(players[1].first_name)
        players[2].opponents.append(players[6].first_name)
        players[6].opponents.append(players[2].first_name)
        players[3].opponents.append(players[7].first_name)
        players[7].opponents.append(players[3].first_name)
        return players
