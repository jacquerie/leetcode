# -*- coding: utf-8 -*-


class Solution(object):
    def diStringMatch(self, S):
        i, j, result = 0, 0, [0]

        for c in S:
            if c == 'I':
                i += 1
                result.append(i)
            else:
                j -= 1
                result.append(j)

        return [el - j for el in result]


if __name__ == '__main__':
    solution = Solution()

    assert [2, 3, 1, 4, 0] == solution.diStringMatch('IDID')
    assert [0, 1, 2, 3] == solution.diStringMatch('III')
    assert [2, 1, 0, 3] == solution.diStringMatch('DDI')
