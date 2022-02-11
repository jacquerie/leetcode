# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def combinationSum(self, candidates, target):
        result = [[[] for j in range(target + 1)] for i in range(len(candidates))]

        for j in range(1, target + 1):
            if j % candidates[0] == 0:
                result[0][j].append(Counter({candidates[0]: j // candidates[0]}))

        for i in range(1, len(candidates)):
            for j in range(1, target + 1):
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


if __name__ == "__main__":
    solution = Solution()

    assert [[2, 2, 3], [7]] == solution.combinationSum([2, 3, 6, 7], 7)
    assert [
        [2, 2, 2, 2],
        [2, 3, 3],
        [3, 5],
    ] == solution.combinationSum([2, 3, 5], 8)
