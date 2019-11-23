# -*- coding: utf-8 -*-


class Solution(object):
    def findContentChildren(self, g, s):
        i, j = 0, 0
        ng, ns = len(g), len(s)

        g.sort()
        s.sort()

        result = 0

        while i <= ng - 1 and j <= ns - 1:
            if g[i] > s[j]:
                j += 1
            elif g[i] <= s[j]:
                result += 1
                i += 1
                j += 1

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.findContentChildren([1, 2, 3], [1, 1])
    assert 2 == solution.findContentChildren([1, 2], [1, 2, 3])
    assert 2 == solution.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8])
