# -*- coding: utf-8 -*-


class Solution:
    def countEven(self, num: int) -> int:
        digit_sum, original_num = 0, num
        while num:
            num, remainder = divmod(num, 10)
            digit_sum += remainder

        return original_num // 2 if digit_sum % 2 == 0 else (original_num - 1) // 2


if __name__ == "__main__":
    solution = Solution()

    assert 2 == solution.countEven(4)
    assert 14 == solution.countEven(30)
