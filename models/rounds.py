from datetime import date


class Round:
    """Define a round."""

    def __init__(self, name, start, end=0):
        """
        Name : Round 1, Round 2, Round 3, Round 4
        Start date and time :  AUTO
        End date and time : AUTO
        List of matchs : 4 by Round.
        """
        self.name = name
        self.start = start
        self.list_match = []
        self.end = end

    def __repr__(self):
        """Display : ROUND[], START : [date/time] END :[date/time]"""
        return " {} START : {} END : {} \n".format(self.name, self.start, self.end)

    def get_first_opponent(players):
        """
        First Round : The players are ranked by best ranking.
        Add oppponent's name to the player's opponent list.
        """
        players[0].opponent.append(players[4].first_name)
        players[4].opponent.append(players[0].first_name)
        players[1].opponent.append(players[5].first_name)
        players[5].opponent.append(players[1].first_name)
        players[2].opponent.append(players[6].first_name)
        players[6].opponent.append(players[2].first_name)
        players[3].opponent.append(players[7].first_name)
        players[7].opponent.append(players[3].first_name)
        return players

    def display_first_round(self, players):
        """
        First Round : The players are ranked by best ranking.
        The matches are :
        player[0] vs players[4]
        player[1] vs players[5]
        player[2] vs players[6]
        player[3] vs players[5].
        """
        self.list_match = []
        match1 = (
            (players[0].first_name, players[0].score_game),
            (players[4].first_name, players[4].score_game),
        )
        match2 = (
            (players[1].first_name, players[1].score_game),
            (players[5].first_name, players[5].score_game),
        )
        match3 = (
            (players[2].first_name, players[2].score_game),
            (players[6].first_name, players[6].score_game),
        )
        match4 = (
            (players[3].first_name, players[3].score_game),
            (players[7].first_name, players[7].score_game),
        )
        self.list_match.extend([match1, match2, match3, match4])
        return self.list_match

    def get_opponent_match1(players):
        """
        The player meets the player below him in the score_game ranking.
        If they have already met, it goes on to the next one.
        """
        if players[1].first_name not in players[0].opponent:
            players[0].opponent.append(players[1].first_name)
            players[1].opponent.append(players[0].first_name)
            print(f"{players[0].first_name} vs {players[1].first_name}")
            del players[1]

        elif players[1].first_name in players[0].opponent:
            players[0].opponent.append(players[2].first_name)
            players[2].opponent.append(players[0].first_name)
            print(f"{players[0].first_name} vs {players[2].first_name}")
            del players[2]

        elif players[2].first_name in players[0].opponent:
            players[0].opponent.append(players[3].first_name)
            players[3].opponent.append(players[0].first_name)
            print(f"{players[0].first_name} vs {players[3].first_name}")
            del players[3]

        elif players[3].first_name in players[0].opponent:
            players[0].opponent.append(players[4].first_name)
            players[4].opponent.append(players[0].first_name)
            print(f"{players[0].first_name} vs {players[4].first_name}")
            del players[4]

        elif players[4].first_name in players[0].opponent:
            players[0].opponent.append(players[5].first_name)
            players[5].opponent.append(players[0].first_name)
            print(f"{players[0].first_name} vs {players[5].first_name}")
            del players[5]

        elif players[5].first_name in players[0].opponent:
            players[0].opponent.append(players[6].first_name)
            players[6].opponent.append(players[0].first_name)
            print(f"{players[0].first_name} vs {players[6].first_name}")
            del players[6]

        else:
            players[0].opponent.append(players[7].first_name)
            players[7].opponent.append(players[0].first_name)
            print(f"{players[0].first_name} vs {players[7].first_name}")
            del players[7]

        del players[0]
        return players

    def get_opponent_match2(players):
        """
        The player meets the player below him in the score_game ranking.
        If they have already met, it goes on to the next one.
        """
        if players[1].first_name not in players[0].opponent:
            players[0].opponent.append(players[1].first_name)
            players[1].opponent.append(players[0].first_name)
            print(f"{players[0].first_name} vs {players[1].first_name}")
            del players[1]

        elif players[1].first_name in players[0].opponent:
            players[0].opponent.append(players[2].first_name)
            players[2].opponent.append(players[0].first_name)
            print(f"{players[0].first_name} vs {players[2].first_name}")
            del players[2]

        elif players[2].first_name in players[0].opponent:
            players[0].opponent.append(players[3].first_name)
            players[3].opponent.append(players[0].first_name)
            print(f"{players[0].first_name} vs {players[3].first_name}")
            del players[3]

        elif players[3].first_name in players[0].opponent:
            players[0].opponent.append(players[4].first_name)
            players[4].opponent.append(players[0].first_name)
            print(f"{players[0].first_name} vs {players[4].first_name}")
            del players[4]

        else:
            players[0].opponent.append(players[5].first_name)
            players[5].opponent.append(players[0].first_name)
            print(f"{players[0].first_name} vs {players[5].first_name}")
            del players[5]

        del players[0]
        return players

    def get_opponent_match3(players):
        """
        The player meets the player below him in the score_game ranking.
        If they have already met, it goes on to the next one.
        """
        if players[2].first_name in players[3].opponent:
            if players[0].first_name not in players[2].opponent:
                players[0].opponent.append(players[2].first_name)
                players[2].opponent.append(players[0].first_name)
                print(f"{players[0].first_name} vs {players[2].first_name}")
                del players[2]
            else:
                players[0].opponent.append(players[3].first_name)
                players[3].opponent.append(players[0].first_name)
                print(f"{players[0].first_name} vs {players[3].first_name}")
                del players[3]

        else:
            if players[1].first_name not in players[0].opponent:
                players[0].opponent.append(players[1].first_name)
                players[1].opponent.append(players[0].first_name)
                print(f"{players[0].first_name} vs {players[1].first_name}")
                del players[1]

            elif players[1].first_name in players[0].opponent:
                players[0].opponent.append(players[2].first_name)
                players[2].opponent.append(players[0].first_name)
                print(f"{players[0].first_name} vs {players[2].first_name}")
                del players[2]

            else:
                players[0].opponent.append(players[3].first_name)
                players[3].opponent.append(players[0].first_name)
                print(f"{players[0].first_name} vs {players[3].first_name}")
                del players[3]
        del players[0]
        return players

    def get_opponent_match4(players):
        """
        The player meets the player below him in the score_game ranking.
        If they have already met, it goes on to the next one.
        """
        players[0].opponent.append(players[1].first_name)
        players[1].opponent.append(players[0].first_name)
        print(f"{players[0].first_name} vs {players[1].first_name}")
        return players

    def display_list_match(self, players):
        """
        Next Round : The players are ranked by score_game.
        The matches are :
        player[0] vs players[1]
        player[2] vs players[3]
        player[4] vs players[5]
        player[6] vs players[7].
        """
        # trouver comment afficher le score du 2e joueur
        self.list_match = []
        match1 = (
            (players[0].first_name, players[0].score_game),
            (players[0].opponent[-1]),
        )
        match2 = (
            (players[2].first_name, players[2].score_game),
            (players[2].opponent[-1]),
        )
        match3 = (
            (players[4].first_name, players[4].score_game),
            (players[4].opponent[-1]),
        )
        match4 = (
            (players[6].first_name, players[6].score_game),
            (players[6].opponent[-1]),
        )
        self.list_match.extend([match1, match2, match3, match4])
        return self.list_match