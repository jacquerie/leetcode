# -*- coding: utf-8 -*-


class Solution(object):
    def minFlipsMonoIncr(self, S):
        ones_count, result = 0, 0

        for char in S:
            if char == '0' and ones_count == 0:
                continue
            elif char == '0':
                result += 1
            else:
                ones_count += 1

            result = min(result, ones_count)

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.minFlipsMonoIncr('00110')
    assert 2 == solution.minFlipsMonoIncr('010110')
    assert 2 == solution.minFlipsMonoIncr('00011000')
    assert 3 == solution.minFlipsMonoIncr('0101100011')
