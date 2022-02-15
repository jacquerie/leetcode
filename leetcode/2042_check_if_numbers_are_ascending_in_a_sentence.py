# -*- coding: utf-8 -*-


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        numbers = [int(word) for word in s.split() if word.isnumeric()]
        return all(numbers[i - 1] < numbers[i] for i in range(1, len(numbers)))


if __name__ == "__main__":
    solution = Solution()

    assert solution.areNumbersAscending(
        "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
    )
    assert not solution.areNumbersAscending("hello world 5 x 5")
    assert not solution.areNumbersAscending(
        "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
    )
