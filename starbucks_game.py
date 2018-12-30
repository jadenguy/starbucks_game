# https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b
from random import gauss
import random
from typing import List
from typing import Dict


class group(object):
    def __init__(self, name: str, columns: int, winPool: int):
        self.columnCount: int = columns
        values: List[int] = list(range(columns))
        self.columns: Dict[int, int] = dict.fromkeys(values, 0)
        self.winner: int = random.choice(values)
        values.remove(self.winner)
        self.losers: List[int] = values
        self.winPool = winPool

    def __repr__(self) -> str:
        ret: str = ""
        columnBadge: str = ""
        for x in range(self.columnCount):
            if (self.columns[x] > 0):
                columnBadge = "X"
            else:
                columnBadge = "_"
            ret += "[%s]" % (columnBadge)
        return ret

    def finished(self)-> bool:
        badges: int = sum(self.columns.values())
        fullSheet: bool = (badges == self.columnCount)
        return fullSheet

    def play(self)-> int:
        selection: int = random.randint(1, self.winPool)
        amIAWinner: bool = (selection % self.winPool == 0)
        ret: int = 0
        if (amIAWinner):
            pickColumn = self.columns[self.winner]
        else:
            pickColumn = random.choice(self.losers)
        if (self.columns[pickColumn] == 0):
            self.columns[pickColumn] = 1
        else:
            ret = 1
        return ret


game = group('game', 10, 3)
i = 0
keepPlaying = (not game.finished())
while (keepPlaying):
    # while (game.finished == False or i == 1000):
    if(game.play()==0):
        print(game, i)
    i += 1
    keepPlaying = (not game.finished() and i < 100000)