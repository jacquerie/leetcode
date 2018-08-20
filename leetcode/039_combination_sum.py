# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from collections import Counter


class Solution(object):
    def combinationSum(self, candidates, target):
        result = [[[] for j in xrange(target + 1)] for i in xrange(len(candidates))]

        for j in xrange(1, target + 1):
            if j % candidates[0] == 0:
                result[0][j].append(Counter({candidates[0]: j // candidates[0]}))

        for i in xrange(1, len(candidates)):
            for j in xrange(1, target + 1):
                result[i][j] = result[i - 1][j]
                if j - candidates[i] > 0:
                    for old in result[i][j - candidates[i]]:
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

    assert [[2, 2, 3], [7]] == solution.combinationSum([2, 3, 6, 7], 7)
    assert [
        [2, 2, 2, 2],
        [2, 3, 3],
        [3, 5],
    ] == solution.combinationSum([2, 3, 5], 8)
