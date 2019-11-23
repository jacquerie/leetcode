# -*- coding: utf-8 -*-


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        result = set()
        if len(s) < 11:
            return []

        seen = set([s[:10]])
        for i in range(10, len(s)):
            sequence = s[i - 9:i + 1]
            if sequence in seen:
                result.add(sequence)
            seen.add(sequence)

        return list(result)


if __name__ == '__main__':
    solution = Solution()

    expected = ['AAAAACCCCC', 'CCCCCAAAAA']
    result = solution.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')

    assert sorted(expected) == sorted(result)
