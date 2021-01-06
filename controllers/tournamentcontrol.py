from models.players import Player
from models.rounds import Round
from view.score import Score
from view.displayround import DisplayRound
import datetime


class TournamentController:
    def create_auto_players():
        players = [Player("Romain", "Turgeon", "m", "01/12/1989", 1, 1000)]
        players.append(Player("William", "Smith", "m", "03/11/1980", 2, 998))
        players.append(Player("Damien", "Billard", "m", "10/08/1978", 3, 996))
        players.append(Player("Mickael", "Fitz", "m", "25/06/2000", 4, 994))
        players.append(Player("Ricardo", "Gagnon", "m", "29/02/1988", 5, 992))
        players.append(Player("Manon", "Tremblay", "f", "13/06/1999", 6, 990))
        players.append(Player("Claire", "Beaulieu", "f", "17/11/1992", 7, 988))
        players.append(Player("Julie", "Stefen", "f", "14/05/1993", 8, 986))
        return players

    def create_first_round(tournament, rounds, players):
        """Create the first round of a tournament. """
        players = sorted(players, key=lambda player: player.rank)
        round1 = Round(
            "Round 1",
        )
        DisplayRound.display_first_round(players)
        Round.get_first_opponent(players)
        for player in players:
            add_point = Score.player_add_score_match(player)
            player.add_score_game(0, add_point)

            if add_point == 0:
                player.opponent_point = 1
            elif add_point == 1:
                player.opponent_point = 0
            else:
                player.opponent_point = 0.5
        round1.matches = DisplayRound.display_first_round(players)
        tournament.matches.append(round1.matches)
        players = sorted(
            players, key=lambda player: (player.score_game, player.score), reverse=True
        )
        round1.end = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        rounds.append(round1)
        print(f"\n{round1}")
        return round1

    def create_next_round(tournament, rounds, players):
        """Create Round 2, 3 , 4."""
        print(f"\n*******************ROUND {len(rounds)+1}******************\n")
        round = Round("Round " + str(len(rounds) + 1))
        players = sorted(players, key=lambda player: player.score_game, reverse=True)
        print(players)
        round.get_opponent(players)
        for player in players:
            add_point = Score.player_add_score_match(player)
            player.add_score_game(player.score_game, add_point)
            if add_point == 0:
                player.opponent_point = 1
            elif add_point == 1:
                player.opponent_point = 0
            else:
                player.opponent_point = 0.5
        tournament.matches.append(round.matches)
        round.end = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        rounds.append(round)
        print(f"\n{round}")
        return round
