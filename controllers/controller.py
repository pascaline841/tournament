import sys
from models.players import Player
from models.tournaments import Tournament
from models.rounds import Round

from models.database import Data

from view.menu import MainView
from view.newplayer import NewPlayer
from view.newtournament import NewTournament
from view.score import Score
from view.displayround import DisplayRound
from view.report import DisplayReport


import datetime
from tinydb import TinyDB, Query

# a enlever pour DataBase __init__
db = TinyDB("db.json")
tournament_table = db.table("TOURNAMENTS")
players_by_tournament = db.table("PLAYERS")
actors_table = db.table("ACTORS")
rounds_table = db.table("ROUNDS")
matches_table = db.table("MATCHES")
user = Query()


def create_player():
    """ Create a new player. """
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
        MainView.welcome()
    elif choice == 2:
        Data.update_rank(actors_table, players_by_tournament, user)
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
        pass
    elif choice == 2:
        Data.update_rank(actors_table, players_by_tournament, user)
        return inter_menu()
    elif choice == 3:
        MainView.welcome()
    elif choice == 4:
        print("Program ended ! See you soon !")
    else:
        print("An error occurred.")
        return inter_menu()


def display_reports():
    # a enlever pour DataBase __init__
    db = TinyDB("db.json")
    tournament_table = db.table("TOURNAMENTS")
    actors_table = db.table("ACTORS")
    rounds_table = db.table("ROUNDS")
    matches_table = db.table("MATCHES")
    user = Query()
    report = DisplayReport.menu_report()
    if report == 1:
        display_report = Data.sorted_actors(actors_table)
        DisplayReport.report_1(display_report)
    elif report == 2:
        display_report = tournament_table.all()
        DisplayReport.report_2(display_report)
    elif report == 3:
        display_report = Data.request_tournament(tournament_table, user)
        DisplayReport.report_3(display_report)
    elif report == 4:
        display_report = Data.request_players(tournament_table, user)
        DisplayReport.report_4(display_report)
    else:
        MainView.welcome()
    DisplayReport.menu_report()


def create_tournament(players):
    """Create a new tournament. """
    name = NewTournament.tournament_name()
    location = NewTournament.tournament_location()
    mode = NewTournament.tournament_mode()
    description = NewTournament.tournament_description()
    return Tournament(name, location, mode, description, players)


def create_first_round(players):
    """Create the first round of a tournament. """
    players = sorted(players, key=lambda player: player.rank)
    round1 = Round("Round 1")
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
    round1.list_match = round1.display_first_score(players)
    tournament.matches.append(round1.list_match)
    players = sorted(
        players, key=lambda player: (player.score_game, player.score), reverse=True
    )
    round1.end = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    rounds.append(round1)
    print(f"\n{round1}")
    return round1


def create_next_round(players):
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
    Data.data_actors(player, actors_table)
    print("\n A player has been created \n")

elif choice == 2:
    players = create_auto_players()
    tournament = create_tournament(players)
    Data.data_tournaments(
        tournament, players, actors_table, players_by_tournament, tournament_table
    )
    print(tournament)
    rounds = tournament.rounds
    round1 = create_first_round(players)
    Data.update_tournament(
        rounds,
        tournament_table,
        players_by_tournament,
        rounds_table,
        matches_table,
    )
    inter_menu()
    nb_rounds = tournament.nb_rounds

    while nb_rounds > 1:
        nb_rounds -= 1
        round = create_next_round(players)
        Data.update_tournament(
            rounds,
            tournament_table,
            players_by_tournament,
            rounds_table,
            matches_table,
        )
        inter_menu()

    MainView.display_final(tournament, players)
    for player in players:
        score = player.add_final_score(player.score_game, player.score)
        Data.update_score(actors_table, players_by_tournament, score)
        player.score_game = 0
        del player.opponent[:]
    Data.truncate_data(players_by_tournament, matches_table, rounds_table)

elif choice == 3:
    # Choice = Continue an existing tournament
    print("BUILDING")
elif choice == 4:
    Data.update_rank()
elif choice == 5:
    display_reports()
elif choice == 6:
    print("Program ended ! See you soon !")
else:
    print("An error occurred.")
back_menu()
