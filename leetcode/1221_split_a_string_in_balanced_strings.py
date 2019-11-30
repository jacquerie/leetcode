# -*- coding: utf-8 -*-


class Solution:
    def balancedStringSplit(self, s):
        r_count, result = 0, 0

        for char in s:
            r_count += 1 if char == 'R' else -1
            if r_count == 0:
                result += 1

        return result


if __name__ == '__main__':
    solution = Solution()

    assert 4 == solution.balancedStringSplit("RLRRLLRLRL")
    assert 3 == solution.balancedStringSplit("RLLLLRRRLR")
    assert 1 == solution.balancedStringSplit("LLLLRRRR")
