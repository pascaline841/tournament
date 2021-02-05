import datetime
from view.menu import MenuView


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

    def serialized_round(self):
        """Serialize round's data."""
        return {
            "name": self.name,
            "start": self.start,
            "matchs": self.matchs,
            "end": self.end,
        }

    def deserialized_round(serialized_round):
        """Pull round's informations from the database to continue a tournament."""
        name = serialized_round["name"]
        start = serialized_round["start"]
        matchs = serialized_round["matchs"]
        end = serialized_round["end"]
        return Round(name, start, matchs, end)

    def get_first_opponents(players):
        """
        First Round : The players are ranked by best ranking.
        Add oppponent's name to the player's opponents list.
        """
        players[0].opponents.append(players[4].first_name)
        players[4].opponents.append(players[0].first_name)
        players[1].opponents.append(players[5].first_name)
        players[5].opponents.append(players[1].first_name)
        players[2].opponents.append(players[6].first_name)
        players[6].opponents.append(players[2].first_name)
        players[3].opponents.append(players[7].first_name)
        players[7].opponents.append(players[3].first_name)
        return players

    def first_matchs(self, players):
        """
        First Round : The players are ranked by best ranking.
        The matchs are :
        player[0] vs players[4]
        player[1] vs players[5]
        player[2] vs players[6]
        player[3] vs players[5].
        """
        players = sorted(players, key=lambda player: player.rank)
        match1 = (
            (
                players[0].first_name,
                players[0].points,
            ),
            (
                players[4].first_name,
                players[4].points,
            ),
        )
        match2 = (
            (
                players[1].first_name,
                players[1].points,
            ),
            (
                players[5].first_name,
                players[5].points,
            ),
        )
        match3 = (
            (
                players[2].first_name,
                players[2].points,
            ),
            (
                players[6].first_name,
                players[6].points,
            ),
        )
        match4 = (
            (
                players[3].first_name,
                players[3].points,
            ),
            (
                players[7].first_name,
                players[7].points,
            ),
        )
        self.matchs.extend([match1, match2, match3, match4])
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
                MenuView.display_next_round(players, i, j)
            i += 1
        return self.matchs
