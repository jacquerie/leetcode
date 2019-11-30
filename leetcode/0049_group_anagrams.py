# -*- coding: utf-8 -*-

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)

        for str in strs:
            anagrams[''.join(sorted(str))].append(str)

        return anagrams.values()


if __name__ == '__main__':
    solution = Solution()

    strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

    expected = [
        ['eat', 'tea', 'ate'],
        ['tan', 'nat'],
        ['bat'],
    ]
    result = solution.groupAnagrams(strs)

    assert sorted(expected) == sorted(result)
