class Team:
    def __init__(self, teamName):
        self.teamName = teamName
        self.teamOrigin = "NaN"

    def defineTeamName(self, name):
        self.teamName = name

    def defineTeamOrigin(self, origin):
        self.teamOrigin = origin


class Player(Team):
    def __init__(self, teamName="Perspolis"):
        Team.__init__(self, teamName)
        self.playerName = "NaN"
        self.playerNumber = "NaN"

    def definePlayerName(self, name):
        self.playerName = name

    def definePlayerNumber(self, number):
        self.playerNumber = number


player1 = Player()
player1.definePlayerName("Mahini")
player1.definePlayerNumber(3)
player1.defineTeamOrigin("Tehran")
print(player1.teamName, player1.teamOrigin)
print(player1.playerNumber, player1.playerName)
print(player1)
