from tinydb import TinyDB, Query
from controllers.menu import MenuController
from controllers.progress import TournamentController
from models.players import Player
from models.tournaments import Tournament
from models.rounds import Round


class MainController:
    """Main class to control the program."""

    @classmethod
    def start_program(cls):
        """Run the program."""
        tournament_table = TinyDB("TOURNAMENTS.json")
        actors_table = TinyDB("ACTORS.json")
        user = Query()

        serialized_rounds = []

        run_program = True
        choices = {
            1: "create player",
            2: "create tournament",
            3: "pull tournament",
            4: "update rank",
            5: "display reports",
            6: "program end",
        }
        while run_program:
            choice = MenuController.choose_welcome_menu()
            if choices[choice] == "create player":
                player = MenuController.create_player()
                Player.store_data_actors(player, user, actors_table)

            elif choices[choice] == "create tournament":
                players = TournamentController.create_list_players(actors_table, user)
                tournament = MenuController.create_tournament(players)
                Tournament.store_data_tournament(
                    tournament, players, user, actors_table, tournament_table
                )
                # print(tournament)
                TournamentController.progress_first_round(
                    tournament,
                    players,
                    tournament_table,
                    user,
                    actors_table,
                    serialized_rounds,
                )
                nb_rounds = tournament.nb_rounds
                TournamentController.progress_next_rounds(
                    tournament,
                    players,
                    serialized_rounds,
                    tournament_table,
                    user,
                    actors_table,
                    nb_rounds,
                )

            elif choices[choice] == "pull tournament":
                name = input("Name of an UNcompleted tournament ? ")
                serialized_tournament = tournament_table.get(user["name"] == name)
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
                    tournament_table,
                    user,
                    actors_table,
                    nb_rounds,
                )

            elif choices[choice] == "update rank":
                Player.update_rank(actors_table, tournament_table, user)

            elif choices[choice] == "display reports":
                MenuController.choose_reports(tournament_table, actors_table, user)

            elif choices[choice] == "program end":
                print("Program ended ! See you soon !")
                run_program = False
            else:
                print("An error occurred.")
