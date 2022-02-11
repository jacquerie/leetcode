# -*- coding: utf-8 -*-


class Solution:
    def repeatedNTimes(self, A):
        seen = set()
        for el in A:
            if el in seen:
                return el
            seen.add(el)


if __name__ == "__main__":
    solution = Solution()

    assert 3 == solution.repeatedNTimes([1, 2, 3, 3])
    assert 2 == solution.repeatedNTimes([2, 1, 2, 5, 3, 2])
    assert 5 == solution.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4])
