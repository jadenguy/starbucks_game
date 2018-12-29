from random import gauss
import random
from typing import List


class group(object):
    def __init__(self, name: str):
        values: List[int] = list(range(3))
        self.winner: int = random.choice(values)
        values.remove(self.winner)
        self.losers: List[int] = values
        self.score: List[str] = []
        for x in range(3):
            self.score.append("_")

    def __repr__(self):
        return "%s is the winner and the losers are %s and %s" % (self.winner, self.losers[0], self.losers[1])

    def scoreboard(self):
        return "[%s][%s][%s]" % (self.score[0], self.score[1], self.score[2])


x = group('game')
print(x)
print(x.scoreboard())
