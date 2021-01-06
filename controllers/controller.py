from models.database import Data
from models.rounds import Round
from models.players import Player
from view.menu import MainView
from controllers.menu import MenuController
from controllers.progress import TournamentController
from tinydb import TinyDB, Query


class MainController:
    """Main class to control the program. """

    def start_program():
        """Run the program."""
        tournament_table = TinyDB("TOURNAMENTS.json")
        actors_table = TinyDB("ACTORS.json")
        user = Query()
        ser_rounds = []
        ser_players = []
        choice = MainView.welcome()

        if choice == 1:
            players = []
            player = MenuController.create_player()
            Data.data_actors(player, user, actors_table)
            print("\n A player has been created. \n")

        elif choice == 2:
            players = TournamentController.create_auto_players()
            tournament = MenuController.create_tournament(players)
            Data.data_tournament(
                tournament, players, user, actors_table, tournament_table
            )
            print(tournament)
            rounds = tournament.rounds
            round_one = TournamentController.create_first_round(
                tournament, rounds, players
            )
            ser_round = Round.serialized_round(round_one)
            ser_rounds.append(ser_round)
            for player in players:
                ser_player = Player.serialized_player(player)
                ser_players.append(ser_player)
            tournament_table.update(
                {
                    "rounds": ser_rounds,
                    "players": ser_players,
                }
            )
            del ser_players[:]
            MenuController.inter_menu(actors_table, tournament_table, user)

            nb_rounds = tournament.nb_rounds

            while nb_rounds > 1:
                nb_rounds -= 1
                next_round = TournamentController.create_next_round(
                    tournament, rounds, players
                )
                ser_round = Round.serialized_round(next_round)
                ser_rounds.append(ser_round)
                for player in players:
                    ser_player = Player.serialized_player(player)
                    ser_players.append(ser_player)
                tournament_table.update(
                    {
                        "rounds": ser_rounds,
                        "players": ser_players,
                    }
                )
                del ser_players[:]
                MenuController.inter_menu(actors_table, tournament_table, user)

            MainView.display_final(tournament, players)
            for player in players:
                score = player.add_final_score(player.score_game, player.score)
                Data.update_score(player, actors_table, score, user)
                ser_player = Player.serialized_player(player)
                ser_players.append(ser_player)
                tournament_table.update(
                    {
                        "players": ser_players,
                    }
                )
        elif choice == 3:
            # Choice = Continue an existing tournament
            print("BUILDING")
        elif choice == 4:
            Data.update_rank(actors_table, tournament_table, user)
        elif choice == 5:
            MenuController.display_reports(tournament_table, actors_table, user)
        elif choice == 6:
            print("Program ended ! See you soon !")
        else:
            print("An error occurred.")
        MenuController.back_menu(actors_table, tournament_table, user)
