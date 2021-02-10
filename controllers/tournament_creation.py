from view.tournament_creation import TournamentCreationView as View
from view.check_input import CheckView
from models.tournament import Tournament as Tournament
from models.player import Player as Player
import datetime


class TournamentCreation:
    """Create a new tournament controller."""

    def __init__(self):
        self.view = View()

    def display(self):
        self.view.display()

    def run(self):
        self.display()
        self.get_command()

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
        players = self.controller.create_auto_players()
        # players = PlayerDetails.create_list_players(actors_table, user)
        return Tournament(name, location, date, mode, rounds, description, players)

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
