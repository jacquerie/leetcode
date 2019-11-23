# -*- coding: utf-8 -*-

from collections import Counter


class Leaderboard(object):
    def __init__(self):
        self.scores = Counter()

    def addScore(self, playerId, score):
        self.scores[playerId] += score

    def top(self, K):
        return sum(score for _, score in self.scores.most_common(K))

    def reset(self, playerId):
        self.scores[playerId] = 0


if __name__ == '__main__':
    obj = Leaderboard()

    obj.addScore(1, 73)
    obj.addScore(2, 56)
    obj.addScore(3, 39)
    obj.addScore(4, 51)
    obj.addScore(5, 4)
    assert 73 == obj.top(1)
    obj.reset(1)
    obj.reset(2)
    obj.addScore(2, 51)
    assert 141 == obj.top(3)
