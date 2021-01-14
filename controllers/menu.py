import datetime
from models.players import Player
from models.tournaments import Tournament
from view.menu import MenuView
from view.report import DisplayReport


class MenuController:
    """Class controls all the different menus in the program."""

    @classmethod
    def choose_welcome_menu(cls):
        """Input to the Welcome Menu."""
        MenuView.welcome()
        try:
            choice = int(input("Enter your choice (1, 2, 3, 4, 5) : \n"))
            if choice > 7:
                raise ValueError
            print("Your choice ({}) has been successfully entered...\n".format(choice))
            return choice
        except ValueError:
            print("The value entered doesn't match the possible choices !\n")
            return MenuController.choose_welcome_menu()

    @classmethod
    def create_player(cls):
        """Create a new player."""
        print("\n************CREATE A NEW PLAYER **************\n")
        first_name = input("Please enter player's first name : ").capitalize()
        last_name = input("Please enter player's last name : ").capitalize()
        birth_date = input("Please enter player's birth date (format = DD/MM/YYYY) : ")
        gender = input("Please enter player's gender (format = 'm' / 'f') : ")
        rank = MenuController.choose_player_rank()
        score = MenuController.choose_player_score()
        print("\n A player has been created. \n")
        return Player(first_name, last_name, birth_date, gender, rank, score)

    @classmethod
    def choose_actors(cls, i, actors_table, user):
        "Choose a player from the database to play in a tournament."
        try:
            choice = input(f"PLAYER {i}: What is the FIRST NAME ? ").capitalize()
            serialized_player = actors_table.get((user["first name"] == choice))
            if serialized_player is None:
                raise TypeError
        except TypeError:
            print("The value entered doesn't match the possible choices !\n")
            return MenuController.choose_actors(i, actors_table, user)
        return serialized_player
         
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
            return MenuController.choose_actors(tournaments_table, user)
        return serialized_tournament
    
    @classmethod
    def choose_player_rank(cls):
        """Choose the player's rank."""
        try:
            return int(input("Please enter player's rank : "))
        except ValueError:
            print("Incorrect value, it has to be a positive number !")
            return MenuController.choose_player_rank()

    @classmethod
    def choose_player_score(cls):
        """Choose the player's score."""
        try:
            return int(input("Please enter player's total score : "))
        except ValueError:
            print("Incorrect value, it has to be a positive number !")
            return MenuController.choose_player_score()

    @classmethod
    def change_rank(cls):
        """Request to change the player's rank."""
        choice_last_name = input("Please enter player's last name : ").capitalize()
        return choice_last_name
        try:
            rank = int(input("Please enter player's rank : "))
            return rank
        except ValueError:
            print("Incorrect value, it has to be a positive number !")
            return MenuController.change_rank()

    @classmethod
    def choose_reports(cls, tournaments_table, actors_table, user):
        """Display the reports' menu."""
        reports = {
            1: "sorted_actors report",
            2: "tournaments report",
            3: "rounds report",
            4: "players report",
        }
        DisplayReport.display_reports()
        try:
            report = int(input("Enter your choice (1, 2, 3, 4, 5) : \n"))
            if report > 6:
                raise ValueError
            print("Your choice ({}) has been successfully entered\n".format(report))
        except ValueError:
            print("The value entered doesn't match the possible choices !\n")
            return MenuController.choose_reports
        if reports[report] == "sorted_actors report":
            display_report = MenuController.sorted_actors(actors_table)
            DisplayReport.report_actors(display_report)
        elif reports[report] == "tournaments report":
            display_report = tournaments_table.all()
            DisplayReport.report_tournaments(display_report)
        elif reports[report] == "rounds report":
            display_report = MenuController.request_rounds(tournaments_table, user)
            DisplayReport.report_rounds(display_report)
        elif reports[report] == "players report":
            display_report = MenuController.request_players(tournaments_table, user)
            DisplayReport.report_players(display_report)
        else:
            MenuView.welcome()

    @classmethod
    def choose_inter_menu(cls, actors_table, tournaments_table, user):
        """Display menu between rounds."""
        MenuView.interround_menu()
        choices = {
            1: "continue tournament",
            2: "update rank",
            3: "welcome menu",
            4: "end program",
        }
        try:
            choice = int(input("Enter your choice (1, 2, 3, 4): \n"))
            if choice > 5:
                raise ValueError
            print("Your choice ({}) has been successfully entered...".format(choice))
        except ValueError:
            print("The value entered doesn't match the possible choices !\n")
            return MenuController.choose_inter_menu()
        if choices[choice] == "continue tournament":
            pass
        elif choices[choice] == "update rank":
            MenuController.update_rank(actors_table, tournaments_table, user)
            return MenuController.choose_inter_menu(
                actors_table, tournaments_table, user
            )
        elif choices[choice] == "welcome menu":
            return MenuView.welcome()
        elif choices[choice] == "end program":
            return print("Program ended ! See you soon!")
            # A CORRIGER POUR SORTIR DU PROGRAMME
        else:
            print("An error occurred.")
            return MenuController.choose_inter_menu(
                actors_table, tournaments_table, user
            )

    @classmethod
    def request_players(cls, tournaments_table, user):
        """Request for a tournament to display its players by alpha order or rank."""
        name = input("What is it name ? ")
        choice = tournaments_table.search(user["name"] == name)
        players = choice[0].get("players")
        sorted_choice = int(input("Sorted by Last Name (1) or by Rank (2) ? "))
        if sorted_choice == 1:
            return sorted(players, key=lambda players: players["last name"])
        else:
            return sorted(players, key=lambda players: players["rank"])

    @classmethod
    def request_rounds(cls, tournaments_table, user):
        """Request for a tournament to display its rounds or matchs."""
        name = input("What is it name ? ")
        choice = tournaments_table.search(user["name"] == name)
        return choice[0].get("rounds")

    @classmethod
    def add_score_match(cls, player):
        """
        Enter the scores for each round:
        1 point for the winner,
        0.5 point if draw,
        0 point for the loser.
        """
        try:
            add_point = float(input(f"Please enter {player.first_name}'s score : "))
            if add_point not in [0, 0.5, 1]:
                raise ValueError
            print("Score entered successfully...")
            return add_point
        except ValueError:
            print(
                "Incorrect score, it has to be 1 point for the winner, 0.5 point if draw, 0 point for the loser!"
            )
            return MenuController.add_score_match(player)
        except TypeError:
            print(
                "Incorrect score, it has to be 1 point for the winner, 0.5 point if draw, 0 point for the loser!"
            )
            return MenuController.add_score_match(player)

    @classmethod
    def update_rank(cls, actors_table, tournaments_table, user):
        """Update actor's rank in the database and in the current tournament."""
        first_name = input("First name ? ").capitalize()
        last_name = input("Last name ? ").capitalize()
        new_rank = int(input("New rank ? "))
        actors_table.update(
            {"rank": new_rank},
            user["first name"] == first_name and user["last name"] == last_name,
        )
        # NE FONCTIONNE PAS SUR LE TOURNOIS . A CORRIGER
        tournaments_table.update(
            {"rank": new_rank},
            user["first name"] == first_name and user["last name"] == last_name,
        )

    @classmethod
    def sorted_actors(cls, actors_table):
        """Sort all actors by alphabetic order or by rank."""
        actors = actors_table.all()
        sorted_choice = int(input("Sorted by Last Name (1) or by Rank (2) ? "))
        if sorted_choice == 1:
            return sorted(actors, key=lambda actor: actor["last name"])
        else:
            return sorted(actors, key=lambda actor: actor["rank"])
