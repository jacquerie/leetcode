# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import Counter


class Solution(object):
    def combinationSum2(self, candidates, target):
        counts = Counter(candidates)
        candidates = sorted(counts.keys())

        result = [[[] for j in xrange(target + 1)] for i in xrange(len(candidates))]

        for j in xrange(1, target + 1):
            if j % candidates[0] == 0 and j // candidates[0] <= counts[candidates[0]]:
                result[0][j].append(Counter({candidates[0]: j // candidates[0]}))

        for i in xrange(1, len(candidates)):
            for j in xrange(1, target + 1):
                result[i][j] = result[i - 1][j]
                if j - candidates[i] > 0:
                    for old in result[i][j - candidates[i]]:
                        if old[candidates[i]] < counts[candidates[i]]:
                            new = Counter(old)
                            new[candidates[i]] += 1
                            result[i][j].append(new)
                elif j - candidates[i] == 0:
                    result[i][j].append(Counter({candidates[i]: 1}))

        return self.solutionToList(result[-1][-1])

    def solutionToList(self, solution):
        return [sorted(counter.elements()) for counter in solution]


if __name__ == '__main__':
    solution = Solution()

    assert [
        [1, 2, 5],
        [1, 1, 6],
        [2, 6],
        [1, 7],
    ] == solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    assert [[1, 2, 2], [5]] == solution.combinationSum2([2, 5, 2, 1, 2], 5)
