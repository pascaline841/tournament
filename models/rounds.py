import datetime
from view.displayround import DisplayRound


class Round:
    """Define a round."""

    def __init__(self, name, end=0):
        """
        Name : Round 1, Round 2, Round 3, Round 4
        Start date and time :  AUTO
        End date and time : AUTO
        List of matchs : 4 by Round.
        """
        self.name = name
        self.start = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        self.matches = []
        self.players_paired = []
        self.end = end

    def __repr__(self):
        """Display : ROUND[], START : [date/time] END :[date/time]."""
        return " {} START : {} END : {} \n MATCHES : {} ".format(
            self.name, self.start, self.end, self.matches
        )

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

    def first_matches(self, players):
        """
        First Round : The players are ranked by best ranking.
        The matches are :
        player[0] vs players[4]
        player[1] vs players[5]
        player[2] vs players[6]
        player[3] vs players[5].
        """
        players_sorted = sorted(players, key=lambda player: player.rank)
        match1 = (
            (
                players_sorted[0].first_name,
                players_sorted[0].score_game,
            ),
            (
                players_sorted[4].first_name,
                players_sorted[4].score_game,
            ),
        )
        match2 = (
            (
                players_sorted[1].first_name,
                players_sorted[1].score_game,
            ),
            (
                players_sorted[5].first_name,
                players_sorted[5].score_game,
            ),
        )
        match3 = (
            (
                players_sorted[2].first_name,
                players_sorted[2].score_game,
            ),
            (
                players_sorted[6].first_name,
                players_sorted[6].score_game,
            ),
        )
        match4 = (
            (
                players_sorted[3].first_name,
                players_sorted[3].score_game,
            ),
            (
                players_sorted[7].first_name,
                players_sorted[7].score_game,
            ),
        )
        self.matches.extend([match1, match2, match3, match4])
        return self.matches

    def get_opponent(self, players):
        """
        Rounds 2 3 4 : The players are ranked by best score
        The matches are :
        player[0] vs players[1]
        player[2] vs players[3]
        player[4] vs players[5]
        player[6] vs players[7].
        """

        for i in range(len(players)):
            while players[i].first_name not in self.players_paired:
                j = i + 1
                while (
                    j < len(players)
                    and players[j].first_name in self.players_paired
                    and players[j].first_name in players[i].opponent
                    and players[i].first_name in players[j].opponent
                ):
                    j += 1
                players[i].opponent.append(players[j].first_name)
                players[j].opponent.append(players[i].first_name)
                match = (players[i].first_name, players[j].first_name)
                self.matches.append(match)
                self.players_paired.append(players[i].first_name)
                self.players_paired.append(players[j].first_name)
                print(f"{players[i].first_name} vs {players[j].first_name}")

            i += 1
        return self.matches

    def serialized_round(self):
        """serialized round's data."""
        return {
            "name": self.name,
            "start": self.start,
            "matches": self.matches,
            "end": self.end,
        }
