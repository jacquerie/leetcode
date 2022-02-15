# -*- coding: utf-8 -*-


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        result = 0

        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                ops, num1 = divmod(num1, num2)
            else:
                ops, num2 = divmod(num2, num1)
            result += ops

        return result


if __name__ == "__main__":
    solution = Solution()

    assert 3 == solution.countOperations(2, 3)
    assert 1 == solution.countOperations(10, 10)
