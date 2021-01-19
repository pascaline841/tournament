import datetime
from models.players import Player
from models.rounds import Round
from models.tournaments import Tournament
from controllers.menu import MenuController
from controllers.player import PlayerController
from view.menu import MenuView
from view.displayround import DisplayRound


class TournamentController:
    """Class controls the tournament progress."""

    @classmethod
    def create_tournament(cls, players):
        """Create a new tournament."""
        print("\n==================================================")
        print("************CREATE A NEW TOURNAMENT**************\n")
        name = input("Please enter tournament's name : ")
        location = input("Please enter tournament's location : ")
        date = datetime.date.today().strftime("%d/%m/%Y")
        mode = input("How would you like to play ? bullet / blitz / fast : ")
        rounds = []
        description = input("Please enter tournament's description : ")
        players = players
        return Tournament(name, location, date, mode, rounds, description, players)

    @classmethod
    def choose_tournament(cls, tournaments_table, user):
        "Choose a player from the database to play in a tournament."
        try:
            name = input("Name of an UNcompleted tournament ? ")
            serialized_tournament = tournaments_table.get(user["name"] == name)
            if serialized_tournament is None:
                raise TypeError
        except TypeError:
            print("The value entered doesn't match the possible choices !\n")
            return Tournament.choose_actors(tournaments_table, user)
        return serialized_tournament

    @classmethod
    def create_list_players(cls, actors_table, user):
        """Create a list of 8 players from the database."""
        players = []
        print("CHOOSE 8 PLAYERS FROM THE DATABASE\n")
        for i in range(1, 9):
            serialized_player = PlayerController.choose_actors(i, actors_table, user)
            player = Player.deserialized_player(serialized_player)
            players.append(player)
        return players

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
        print(players)
        round = Round(
            "Round 1", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), matchs=[]
        )
        DisplayRound.display_first_round(players)
        Round.get_first_opponents(players)
        for player in players:
            add_point = PlayerController.add_score_match(player)
            player.add_points(add_point)
        Round.first_matchs(round, players)
        round.end = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        rounds.append(round)
        print(f"\n{round}")
        return round

    @classmethod
    def create_next_round(cls, tournament, rounds, players):
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
            add_point = PlayerController.add_score_match(player)
            player.add_points(add_point)
            if add_point == 0:
                player.point = 1
            elif add_point == 1:
                player.point = 0
            else:
                player.point = 0.5
        round.end = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        rounds.append(round)
        print(f"\n{round}")
        return round

    @classmethod
    def progress_first_round(
        cls,
        tournament,
        players,
        tournaments_table,
        user,
        actors_table,
        serialized_rounds,
    ):
        """Run the first round."""
        rounds = tournament.rounds
        round = TournamentController.create_first_round(tournament, rounds, players)
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

    @classmethod
    def progress_next_rounds(
        cls,
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
            round = TournamentController.create_next_round(tournament, rounds, players)
            serialized_round = Round.serialized_round(round)
            serialized_rounds.append(serialized_round)
            Tournament.update_round(
                tournament, serialized_rounds, tournaments_table, user
            )
            Tournament.update_players(tournament, players, tournaments_table, user)
            MenuController.choose_inter_menu(
                actors_table, tournaments_table, user, tournament, players
            )
            players = sorted(
                sorted(
                    players,
                    key=lambda player: player.rank,
                ),
                key=lambda player: player.points,
                reverse=True,
            )
        MenuView.display_final_score(tournament, players)
        for player in players:
            score = player.add_final_score(player.points, player.score)
            Player.update_score(player, actors_table, score, user)

    @classmethod
    def pull_tournament(cls, tournaments_table, serialized_rounds, actors_table, user):
        """To continue an unfinished tournament."""
        serialized_tournament = TournamentController.choose_tournament(
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
