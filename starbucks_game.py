# https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b
import random
from typing import List
from typing import Dict


class badgeBoard(object):
    def __init__(self, name: str, columns: int, winPool: int, seed: float):
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
        return ret

    def finished(self)-> bool:
        badges: int = min(self.columns.values())
        fullSheet: bool = (badges != 0)
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


seed: float = random.random()
game: badgeBoard = badgeBoard('game', 50, 1000, seed)
i: int = 0
freePlay: int = 0
freePlayCounter: int = 0
keepPlaying: bool = True
print(game, i, freePlayCounter)
while (keepPlaying):
    i += 1
    if(game.play() == 0):
        print(game, i, freePlayCounter)
        pass
    else:
        freePlay += 1
        if (freePlay == 3):
            i -= 1
            freePlay = 0
            freePlayCounter += 1
    keepPlaying = (not game.finished())
