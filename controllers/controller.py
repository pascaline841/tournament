from models.players import Player
from models.tournaments import Tournament
from models.rounds import Round
from models.reports import Reports

from view.menu import MainView
from view.newplayer import NewPlayer
from view.newtournament import NewTournament
from view.report import Report
from view.score import Score
from view.displayround import DisplayRound

import datetime


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


def back_menu():
    """Display menu to go back to the Main Menu."""
    choice = MainView.back_menu()
    if choice == 1:
        choice = MainView.welcome()
    elif choice == 2:
        print("Program ended ! See you soon !")
    else:
        print("An error occurred.")


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
    print(players)
    round1 = Round("Round 1")
    DisplayRound.display_first_round(players)
    Round.get_first_opponent(players)
    for player in players:
        add_point = Score.player_add_score_match(player)
        player.add_score_game(0, add_point)
    round1.list_match = round1.display_first_round(players)
    tournament.matches.append(round1.list_match)
    players = sorted(
        players, key=lambda player: (player.score_game, player.score), reverse=True
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
    round.end = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    rounds.append(round)
    print(f"\n{round}")
    return round


# def start_program():
"""Run the program"""
choice = MainView.welcome()
if choice == 1:
    player = create_player()
    print("\n A player has been created \n")  # A CHANGER
    end_player = back_menu()
elif choice == 2:
    print("\n==================================================")
    players = []
    players.append(Player("Romain", "Turgeon", "Male", "01/12/1989", 1, 1000))
    players.append(Player("William", "Smith", "Male", "03/11/1980", 2, 998))
    players.append(Player("Damien", "Billard", "Male", "10/08/1978", 3, 996))
    players.append(Player("Mickael", "Fitz", "Male", "25/06/2000", 4, 994))
    players.append(Player("Ricardo", "Gagnon", "Male", "29/02/1988", 5, 992))
    players.append(Player("Manon", "Tremblay", "Female", "13/06/1999", 6, 990))
    players.append(Player("Claire", "Beaulieu", "Female", "17/11/1992", 7, 988))
    players.append(Player("Julie", "Stefen", "Female", "14/05/1993", 8, 986))

    tournament = create_tournament(players)
    print(tournament)
    rounds = []
    round1 = create_first_round(players)
    players_copy = new_list(players)

    while len(rounds) < 4:
        round = create_next_round(players)
        players = players_copy[:]
        players = sorted(
            players, key=lambda player: (player.score_game, player.score), reverse=True
        )

    print(f" Finale results of {tournament.name} :")
    print(rounds)
    for player in players:
        print(f"SCORE : {player.score_game}, {player.first_name} {player.last_name}")
        player.add_final_score(player.score_game, player.score)
        player.score_game = 0
        del player.opponent[:]

    end_tournament = back_menu()

elif choice == 3:
    # Choice = Continue an existing tournament
    print("BUILDING")

elif choice == 4:
    # Choice = Change a player's rank
    print("BUILDING")

elif choice == 5:
    display_reports = display_reports()

elif choice == 6:
    print("Program ended ! See you soon !")

else:
    print("An error occurred.")
