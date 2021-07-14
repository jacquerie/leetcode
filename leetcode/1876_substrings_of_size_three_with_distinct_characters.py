# -*- coding: utf-8 -*-

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        return sum(ss[0] != ss[1] and ss[1] != ss[2] and ss[0] != ss[2] for ss in zip(*(s[i:] for i in range(3))))


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.countGoodSubstrings('xyzzaz')
    assert 4 == solution.countGoodSubstrings('aababcabc')
