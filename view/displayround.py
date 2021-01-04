class DisplayRound:
    @staticmethod
    def display_first_round(players):
        print("*******************ROUND 1 ******************\n")
        print(f"{players[0].first_name} vs {players[4].first_name}")
        print(f"{players[1].first_name} vs {players[5].first_name}")
        print(f"{players[2].first_name} vs {players[6].first_name}")
        print(f"{players[3].first_name} vs {players[7].first_name}")

    @staticmethod
    def display_next_round(players):
        print(f"{players[i].first_name} vs {players[j].first_name}")