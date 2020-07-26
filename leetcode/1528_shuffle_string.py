# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [None] * len(s)
        for i, c in zip(indices, s):
            result[i] = c
        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()

    assert 'leetcode' == solution.restoreString('codeleet', [4, 5, 6, 7, 0, 2, 1, 3])
    assert 'abc' == solution.restoreString('abc', [0, 1, 2])
    assert 'nihao' == solution.restoreString('aiohn', [3, 1, 4, 2, 0])
    assert 'arigatou' == solution.restoreString('aaiougrt', [4, 0, 2, 6, 7, 3, 1, 5])
    assert 'rat' == solution.restoreString('art', [1, 0, 2])
