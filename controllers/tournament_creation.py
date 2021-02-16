import datetime

# lib tierce part

from models.tournament import Tournament
from models.player import Player

from view.tournament_creation import TournamentCreationView as View
from view.check_input import CheckView


class TournamentCreation:
    """Create a new tournament controller."""

    def __init__(self):
        self.view = View()

    def display(self):
        self.view.display()

    def run(self):
        self.display()
        tournament = self.get_command()
        Tournament.store_data_tournament(
            tournament, players, user, actors_table, tournaments_table
        )

    def get_command(self):
        """Create a new tournament."""
        name = CheckView.check_str("Please enter tournament's name : ")
        location = CheckView.check_str("Please enter tournament's location : ")
        date = datetime.date.today().strftime("%d/%m/%Y")
        mode = CheckView.check_str(
            "How would you like to play ? bullet / blitz / fast : "
        )
        rounds = []

        description = input("Please enter tournament's description : ")
        # CHOOSE BETWEEN AUTO or MANUAL list of players :
        players = self.create_auto_players()
        # players = self.create_list_players()

        tournament = Tournament(
            name, location, date, mode, rounds, description, players
        )
        tournament.save()

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
        return players