# -*- coding: utf-8 -*-


class Solution(object):
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s

        p = self.manachersAlgorithm(s)

        m = self.argMax(p)
        start = (m - 1 - p[m]) // 2
        end = start + p[m]

        return s[start:end]

    def manachersAlgorithm(self, s):
        c, r = 0, 0
        s = '^#' + '#'.join(s) + '#$'
        p = [0] * len(s)

        for i in range(1, len(s) - 1):
            if i < r:
                p[i] = min(r - i, p[2 * c - i])
            while s[i + 1 + p[i]] == s[i - 1 - p[i]]:
                p[i] += 1
            if i + p[i] < r:
                c, r = i + p[i]

        return p

    def argMax(self, p):
        result = 0
        for i, el in enumerate(p):
            if el > p[result]:
                result = i
        return result


if __name__ == '__main__':
    solution = Solution()

    assert 'bab' == solution.longestPalindrome('babad')
    assert 'bb' == solution.longestPalindrome('cbbd')
    assert 'a' == solution.longestPalindrome('a')
    assert 'ccc' == solution.longestPalindrome('ccc')
