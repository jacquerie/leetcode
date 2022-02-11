# -*- coding: utf-8 -*-


class Solution:
    def relativeSortArray(self, arr1, arr2):
        ranks = {el: i for i, el in enumerate(arr2)}
        return sorted(arr1, key=lambda el: (ranks.get(el, float("inf")), el))


if __name__ == "__main__":
    solution = Solution()

    assert [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19] == solution.relativeSortArray(
        [2, 3, 1, 3, 2, 4, 6, 19, 9, 2, 7], [2, 1, 4, 3, 9, 6]
    )
