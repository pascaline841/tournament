import datetime

from .abstract import ABSController
from .inter_round import InterRoundController

from models.player import Player
from models.round import Round
from models.tournament import Tournament

from view.check_input import CheckView
from view.score import ScoreView
from view.tournament import TournamentView as View


class TournamentController(ABSController):
    """Create a new tournament controller."""

    def __init__(self):
        self.view = View()

    def display(self):
        self.view.display()

    def get_command(self):
        """Create a new tournament."""
        name = CheckView.check_str("Please enter tournament's name : ")
        location = CheckView.check_str("Please enter tournament's location : ")
        date = datetime.date.today().strftime("%d/%m/%Y")
        mode = CheckView.check_str(
            "How would you like to play ? bullet / blitz / fast : "
        )
        rounds = []
        serialized_rounds = []
        description = input("Please enter tournament's description : ")
        # CHOOSE BETWEEN AUTO or MANUAL list of players :
        players = self.create_auto_players()
        # players = self.create_list_players()

        tournament = Tournament(
            name, location, date, mode, rounds, description, players
        )
        # tournament.save() NE MARCHE PAS
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

    def create_list_players(self):
        """Create a list of 8 players from the database."""
        players = []
        print("CHOOSE 8 PLAYERS FROM THE DATABASE\n")

        for index in range(1, 9):
            player = self.choose_actors(index)
            players.append(player)
        return players

    def choose_actors(self, index):
        "Choose a player from the database to play in a tournament."
        player = None
        while not player:
            message = f"PLAYER {index}: What is the FIRST NAME ? "
            first_name = CheckView.check_str(message).capitalize()
            try:
                player = Player.get(first_name=first_name)
            except TypeError:
                print("The value entered doesn't match the possible choices !\n")
        return player

    def create_auto_players(self):
        """Create 8 players for a demo."""
        players = [Player("Romain", "Turgeon", "m", "01/12/1989", 1, 1000)]
        players.append(Player("William", "Smith", "m", "03/11/1980", 2, 998))
        players.append(Player("Damien", "Billard", "m", "10/08/1978", 3, 996))
        players.append(Player("Mickael", "Fitz", "m", "25/06/2000", 4, 994))
        players.append(Player("Ricardo", "Gagnon", "m", "29/02/1988", 5, 992))
        players.append(Player("Manon", "Tremblay", "f", "13/06/1999", 6, 990))
        players.append(Player("Claire", "Beaulieu", "f", "17/11/1992", 7, 988))
        players.append(Player("Julie", "Stefen", "f", "14/05/1993", 8, 986))
        for player in players:
            player.save()
        return players

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
        self.controller = InterRoundController

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
            self.controller = InterRoundController
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
        for index in range(4):
            players[index].opponents.append(players[index + 4].first_name)

        for index in range(4, 8):
            players[index].opponents.append(players[index - 4].first_name)
        return players
