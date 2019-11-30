# -*- coding: utf-8 -*-


class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return 0

        current = triangle[0]
        for row in triangle[1:]:
            next = []
            for i, el in enumerate(row):
                if i == 0:
                    next.append(el + current[i])
                elif i == len(row) - 1:
                    next.append(el + current[i - 1])
                else:
                    next.append(el + min(current[i - 1], current[i]))
            current = next

        return min(current)


if __name__ == '__main__':
    solution = Solution()

    assert 11 == solution.minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3],
    ])
