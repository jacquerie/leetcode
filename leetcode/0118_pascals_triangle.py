# -*- coding: utf-8 -*-


class Solution:
    def generate(self, numRows):
        result = []
        if not numRows:
            return result

        current = [1]
        for row in range(numRows):
            next = []
            for col in range(row + 1):
                if col == 0:
                    next.append(current[col])
                elif col == row:
                    next.append(current[col - 1])
                else:
                    next.append(current[col - 1] + current[col])
            result.append(next)
            current = next

        return result


if __name__ == "__main__":
    solution = Solution()

    assert [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
    ] == solution.generate(5)
