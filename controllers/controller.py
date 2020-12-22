from models.players import Player
from models.tournaments import Tournament
from models.rounds import Round
from models.reports import Reports
from models.database import Data

from view.menu import MainView
from view.newplayer import NewPlayer
from view.newtournament import NewTournament
from view.report import Report
from view.score import Score
from view.displayround import DisplayRound

import datetime

from tinydb import TinyDB


def display_reports():
    choice = int(Report.menu_report())
    if choice == 1:
        choice = Reports.display_actors()
    elif choice == 2:
        choice = Reports.display_players()
    elif choice == 3:
        choice = Reports.display_tournaments()
    elif choice == 4:
        choice = Reports.display_rounds()
    elif choice == 5:
        choice = Reports.display_matchs()
    elif choice == 6:
        choice = MainView.welcome()
    back_menu()


def create_player():
    """ Create a new player. """
    print("\n\n\n\n************CREATE A NEW PLAYER **************\n\n\n\n")
    first_name = NewPlayer.player_first_name()
    last_name = NewPlayer.player_last_name()
    birth_date = NewPlayer.player_birth_date()
    gender = NewPlayer.player_gender()
    rank = NewPlayer.player_rank()
    score = NewPlayer.player_score()
    return Player(first_name, last_name, birth_date, gender, rank, score)


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


def back_menu():
    """Display menu to go back to the Main Menu."""
    choice = MainView.back_menu()
    if choice == 1:
        choice = MainView.welcome()
    elif choice == 2:
        choice == Data.update_rank()
        return back_menu()
    elif choice == 3:
        print("Program ended ! See you soon !")
    else:
        print("An error occurred.")
        return back_menu()


def inter_menu():
    """Display menu between rounds."""
    choice = MainView.interround_menu()
    if choice == 1:
        choice = MainView.welcome()
    elif choice == 2:
        choice == Data.update_rank()
        return inter_menu()
    elif choice == 3:
        pass
    elif choice == 4:
        print("Program ended ! See you soon !")
    else:
        print("An error occurred.")
        return back_menu()


def create_tournament(players):
    """Create a new tournament. """
    print("************CREATE A NEW TOURNAMENT**************\n\n\n\n")
    name = NewTournament.tournament_name()
    location = NewTournament.tournament_location()
    mode = NewTournament.tournament_mode()
    description = NewTournament.tournament_description()
    return Tournament(name, location, mode, description, players)


def create_first_round(players):
    """Create the first round of a tournament. """
    print("*******************ROUND 1 ******************\n")
    players = sorted(players, key=lambda player: player.rank)
    round1 = Round("Round 1")
    DisplayRound.display_first_round(players)
    Round.get_first_opponent(players)
    for player in players:
        add_point = Score.player_add_score_match(player)
        player.add_score_game(0, add_point)
    round1.list_match = round1.display_first_score(players)
    tournament.matches.append(round1.list_match)
    players = sorted(
        players,
        key=lambda player: (player.score_game, player.score),
        reverse=True,
    )
    round1.end = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    rounds.append(round1)
    print(f"\n{round1}")
    return round1


def new_list(players):
    players_copy = players[:]
    return players_copy


def create_next_round(players):
    """Create Round 2, 3 , 4."""
    print(f"\n*******************ROUND {len(rounds)+1}******************\n")
    round = Round("Round " + str(len(rounds) + 1))
    print(players)
    round.get_opponent_match1(players)
    round.get_opponent_match2(players)
    round.get_opponent_match3(players)
    round.get_opponent_match4(players)
    for player in players_copy:
        add_point = Score.player_add_score_match(player)
        player.add_score_game(player.score_game, add_point)
        if add_point == 0:
            player.opponent_point = 1
        elif add_point == 1:
            player.opponent_point = 0
        else:
            player.opponent_point = 0.5
    tournament.matches.append(round.list_match)
    round.end = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    rounds.append(round)
    print(f"\n{round}")
    return round


# def start_program():
"""Run the program"""
choice = MainView.welcome()
if choice == 1:
    players = []
    player = create_player()
    Data.data_actors(player)
    print("\n A player has been created \n")
    end_player = back_menu()
elif choice == 2:
    print("==================================================")
    players = create_auto_players()
    tournament = create_tournament(players)
    tournament_table = Data.data_tournaments(tournament, players)
    print(tournament)
    rounds = tournament.rounds
    round1 = create_first_round(players)
    Data.update_tournament(rounds)
    inter_menu()
    players_copy = new_list(players)
    nb_rounds = tournament.nb_rounds
    while nb_rounds > 1:
        nb_rounds -= 1
        round = create_next_round(players)
        players = players_copy[:]
        players = sorted(
            players,
            key=lambda player: (player.score_game, player.score),
            reverse=True,
        )
        Data.update_tournament(rounds)
        inter_menu()

    print("==================================================")
    print(f"FINAL RESULTS OF {tournament.name} :")
    for player in players:
        print(f"SCORE : {player.score_game}, {player.first_name} {player.last_name}")
        player.add_final_score(player.score_game, player.score)
        player.score_game = 0
        del player.opponent[:]
    print(rounds)
    db = TinyDB("db.json")
    players_by_tournament = db.table("PLAYERS")
    players_by_tournament.truncate()
    back_menu()

elif choice == 3:
    # Choice = Continue an existing tournament
    print("BUILDING")

elif choice == 4:
    choice == Data.update_rank()
    back_menu()
elif choice == 5:
    display_reports = display_reports()

elif choice == 6:
    print("Program ended ! See you soon !")

else:
    print("An error occurred.")
