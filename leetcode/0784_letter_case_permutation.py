# -*- coding: utf-8 -*-

from itertools import product


class Solution(object):
    def letterCasePermutation(self, S):
        return list(set(''.join(s) for s in product(*zip(S.lower(), S.upper()))))


if __name__ == '__main__':
    solution = Solution()

    assert sorted(['a1b2', 'a1B2', 'A1b2', 'A1B2']) == sorted(solution.letterCasePermutation('a1b2'))
    assert sorted(['3z4', '3Z4']) == sorted(solution.letterCasePermutation('3z4'))
    assert sorted(['12345']) == sorted(solution.letterCasePermutation('12345'))
