import datetime
from models.player import Player
from models.round import Round
from models.tournament import Tournament
from controllers.menu import MenuController
from controllers.player_details import PlayerDetails
from view.score import ScoreView


class TournamentDetails:
    """Class controls the tournament progress."""

    def create_list_players(actors_table, user):
        """Create a list of 8 players from the database."""
        players = []
        print("CHOOSE 8 PLAYERS FROM THE DATABASE\n")
        for i in range(1, 9):
            ser_player = PlayerDetails.choose_actors(i, actors_table, user)
            player = Player.deserialized_player(ser_player)
            players.append(player)
        return players

    @staticmethod
    def create_auto_players():
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

    def get_first_round(tournament, rounds, players):
        """Create the first round of a tournament."""
        players = sorted(players, key=lambda player: player.rank)
        round = Round(
            "Round 1", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), matchs=[]
        )
        for i in range(4):
            print(f"{players[i].first_name} vs {players[i+4].first_name}")
        Round.get_first_opponents(players)
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

    def get_next_round(tournament, rounds, players):
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

    def progress_first_round(
        tournament,
        players,
        tournaments_table,
        user,
        actors_table,
        serialized_rounds,
    ):
        """Run the first round."""
        rounds = tournament.rounds
        round = TournamentDetails.get_first_round(tournament, rounds, players)
        serialized_round = Round.serialized_round(round)
        serialized_rounds.append(serialized_round)
        Tournament.update_round(tournament, serialized_rounds, tournaments_table, user)
        Tournament.update_players(tournament, players, tournaments_table, user)
        MenuController.choose_inter_menu(
            actors_table,
            tournaments_table,
            user,
            tournament,
            players,
        )

    def progress_next_rounds(
        tournament,
        players,
        serialized_rounds,
        tournaments_table,
        user,
        actors_table,
        nb_rounds,
    ):
        """Run the following rounds."""

        while nb_rounds > 1:
            nb_rounds -= 1
            rounds = tournament.rounds
            round = TournamentDetails.get_next_round(tournament, rounds, players)
            serialized_round = Round.serialized_round(round)
            serialized_rounds.append(serialized_round)
            Tournament.update_round(
                tournament, serialized_rounds, tournaments_table, user
            )
            Tournament.update_players(tournament, players, tournaments_table, user)
            MenuController.choose_inter_menu(
                actors_table,
                tournaments_table,
                user,
                tournament,
                players,
            )
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
            Player.update_score(player, actors_table, score, user)
        ScoreView.display_final_score(tournament, players)
