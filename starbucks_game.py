# https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b
import random
from typing import List
from typing import Dict


class badgeBoard(object):
    def __init__(self, name: str, columns: int, winPool: int, seed: float) -> None:
        self.name = name
        self.r = random.Random(seed)
        self.columnCount: int = columns
        values: List[int] = list(range(columns))
        self.columns: Dict[int, int] = dict.fromkeys(values, 0)
        self.winner: int = self.r.choice(values)
        values.remove(self.winner)
        self.losers: List[int] = values
        self.winPool = winPool

    def __repr__(self) -> str:
        ret: str = ""
        for x in range(self.columnCount):
            columnBadge: str = "_"
            if x == self.winner:
                columnBadge = "*"
            if (self.columns[x] != 0):
                # columnBadge = str(self.columns[x])
                columnBadge = "X"
            ret += "[%s]" % (columnBadge)
        ret += " " + self.name
        if (self.finished()):
            ret += " Winner"
        return ret

    def finished(self)-> bool:
        fullSheet: bool = (min(self.columns.values()) != 0)
        return fullSheet

    def play(self)-> int:
        selection: int = self.r.randint(1, self.winPool)
        amIAWinner: bool = (selection % self.winPool == 0)
        ret: int = 0
        if (amIAWinner):
            pickColumn = self.winner
        else:
            pickColumn = self.r.choice(self.losers)
        if (self.columns[pickColumn] != 0):
            ret = 1
        self.columns[pickColumn] += 1
        return ret


class fullGame(object):
    def __init__(self, gameCount: int, badgeCount: int, winOutOf: int) -> None:
        self.gameCount = gameCount
        self.games: List[badgeBoard] = []
        self.repeats = 0
        self.freeGames = 0
        self.coffees = 0
        self.r = random.Random()
        for x in range(gameCount):
            self.games.append(badgeBoard(
                "Board "+str(x+1), badgeCount, winOutOf, self.r.random()))

    def __repr__(self) -> str:
        ret: str = ""
        for x in self.games:
            ret += str(x)
            ret += "\n"
        return ret

    def play(self) -> bool:
        selection: int = self.r.randint(1, self.gameCount) - 1
        ret: bool = False
        self.coffees += 1
        if(self.games[selection].play() == 0):
            title: str = str(self.coffees) + " coffees"
            if (self.freeGames > 0):
                title += " and " + str(self.freeGames) + " free games"
                title += " in"
            print(title)
            print(self)
            if (self.games[selection].finished()):
                ret = True
        else:
            self.repeats += 1
            if (self.repeats == 3):
                self.repeats = 0
                self.freeGames += 1
                self.coffees -= 1
        return ret


i: int = 0
freePlay: int = 0
freePlayCounter: int = 0
keepPlaying: bool = True
seed: float = random.random()
game: fullGame = fullGame(10, 3, 1000)
while (not game.play()):
    # print(game)
    pass
