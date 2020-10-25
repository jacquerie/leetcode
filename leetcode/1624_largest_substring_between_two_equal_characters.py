# -*- coding: utf-8 -*-


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        occurrences, result = {}, -1
        for i, c in enumerate(s):
            if c in occurrences:
                result = max(result, i - occurrences[c] - 1)
            else:
                occurrences[c] = i
        return result


if __name__ == '__main__':
    solution = Solution()

    assert 0 == solution.maxLengthBetweenEqualCharacters('aa')
    assert 2 == solution.maxLengthBetweenEqualCharacters('abca')
    assert -1 == solution.maxLengthBetweenEqualCharacters('cbzxy')
    assert 4 == solution.maxLengthBetweenEqualCharacters('cabbac')
