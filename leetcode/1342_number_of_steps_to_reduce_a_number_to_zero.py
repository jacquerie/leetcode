# -*- coding: utf-8 -*-


class Solution:
    def numberOfSteps(self, num: int) -> int:
        result = 0

        while num != 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            result += 1

        return result


if __name__ == "__main__":
    solution = Solution()

    assert 6 == solution.numberOfSteps(14)
    assert 4 == solution.numberOfSteps(8)
    assert 12 == solution.numberOfSteps(123)
