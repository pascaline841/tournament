import datetime

from view.tournament import TournamentView as View


class Round:
    """Define a round."""

    def __init__(self, name, start, matchs, end=0):
        """
        Name : Round 1, Round 2, Round 3, Round 4
        Start date and time :  AUTO
        End date and time : AUTO
        List of matchs : 4 by Round.
        """
        self.name = name
        self.start = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        self.matchs = matchs
        self.players_paired = []
        self.end = end

    def __repr__(self):
        """Display : ROUND[], START : [date/time] END : [date/time]."""
        return (
            f"{self.name} START : {self.start} END : {self.end} \n "
            f"MATCHS : {self.matchs} "
        )

    def serialized(self):
        """Serialize round's data."""
        return vars(self)

    def first_matchs(self, players):
        """
        First Round : The players are ranked by best ranking.
        index = number of matchs by round = 4
        The matchs are :
        player[0] vs players[4]
        player[1] vs players[5]
        player[2] vs players[6]
        player[3] vs players[5].
        """
        players = sorted(players, key=lambda player: player.rank)
        for index in range(4):
            match = (
                (
                    players[index].first_name,
                    players[index].points,
                ),
                (
                    players[index + 4].first_name,
                    players[index + 4].points,
                ),
            )
            self.matchs.append(match)
        return self.matchs

    def get_opponents(self, players):
        """
        Rounds 2 3 4 : The players are ranked by best score then best rank.
        The players can't meet each others twice.
        The matchs are :
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
                    or players[j].first_name in players[i].opponents
                    or players[i].first_name in players[j].opponents
                ):
                    j += 1
                players[i].opponents.append(players[j].first_name)
                players[j].opponents.append(players[i].first_name)
                match = (
                    (players[i].first_name, players[i].points),
                    (players[j].first_name, players[j].points),
                )
                self.matchs.append(match)
                self.players_paired.append(players[i].first_name)
                self.players_paired.append(players[j].first_name)
                View.display_next_round(players, i, j)
            i += 1
        return self.matchs
