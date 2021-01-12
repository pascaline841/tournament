import datetime
from models.players import Player
from models.rounds import Round
from view.score import Score
from view.displayround import DisplayRound


class TournamentController:
    """Class controls the tournament progress."""

    @classmethod
    def create_auto_players(cls):
        """Create 8 players for a demo."""
        players = [Player("Romain", "Turgeon", "m", "01/12/1989", 1, 1000)]
        players.append(Player("William", "Smith", "m", "03/11/1980", 2, 998))
        players.append(Player("Damien", "Billard", "m", "10/08/1978", 3, 996))
        players.append(Player("Mickael", "Fitz", "m", "25/06/2000", 4, 994))
        players.append(Player("Ricardo", "Gagnon", "m", "29/02/1988", 5, 992))
        players.append(Player("Manon", "Tremblay", "f", "13/06/1999", 6, 990))
        players.append(Player("Claire", "Beaulieu", "f", "17/11/1992", 7, 988))
        players.append(Player("Julie", "Stefen", "f", "14/05/1993", 8, 986))
        return players

    @classmethod
    def create_first_round(cls, tournament, rounds, players):
        """Create the first round of a tournament."""
        players = sorted(players, key=lambda player: player.rank)
        round1 = Round(
            "Round 1",
        )
        DisplayRound.display_first_round(players)
        Round.get_first_opponents(players)
        for player in players:
            add_point = Score.player_add_score_match(player)
            player.add_score_game(add_point)
        Round.first_matchs(round1, players)
        tournament.matchs.append(round1.matchs)
        players = sorted(
            players, key=lambda player: (player.score_game, player.score), reverse=True
        )
        round1.end = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        rounds.append(round1)
        print(f"\n{round1}")
        return round1

    @classmethod
    def create_next_round(tournament, rounds, players):
        """Create Round 2, 3 , 4."""
        print(f"\n*******************ROUND {len(rounds)+1}******************\n")
        round = Round(f"Round {len(rounds) + 1}")
        players = sorted(
            players, key=lambda player: (player.score_game, player.score), reverse=True
        )
        print(players)
        round.get_opponents(players)
        for player in players:
            add_point = float(input(f"Please enter {player.first_name}'s score : "))
            Score.player_add_score_match(add_point)
            player.add_score_game(add_point)
            if add_point == 0:
                player.point = 1
            elif add_point == 1:
                player.point = 0
            else:
                player.point = 0.5

        tournament.matchs.append(round.matchs)
        round.end = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        rounds.append(round)
        print(f"\n{round}")
        return round
