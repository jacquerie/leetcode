# -*- coding: utf-8 -*-


class Solution:
    def getRow(self, rowIndex):
        current = [1]
        for row in range(rowIndex + 1):
            next = []
            for col in range(row + 1):
                if col == 0:
                    next.append(current[col])
                elif col == row:
                    next.append(current[col - 1])
                else:
                    next.append(current[col - 1] + current[col])
            current = next
        return current


if __name__ == "__main__":
    solution = Solution()

    assert [1, 3, 3, 1] == solution.getRow(3)
