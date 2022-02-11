# -*- coding: utf-8 -*-

from bisect import bisect
from collections import Counter


class TopVotedCandidate:
    def __init__(self, persons, times):
        self.leaders = []
        self.times = times

        leader, votes = None, Counter()
        for person in persons:
            votes[person] += 1
            if votes[person] >= votes[leader]:
                leader = person
            self.leaders.append(leader)

    def q(self, t):
        return self.leaders[bisect(self.times, t) - 1]


if __name__ == "__main__":
    obj = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])

    assert 0 == obj.q(3)
    assert 1 == obj.q(12)
    assert 1 == obj.q(25)
    assert 0 == obj.q(15)
    assert 0 == obj.q(24)
    assert 1 == obj.q(8)
