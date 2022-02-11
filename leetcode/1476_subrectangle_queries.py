# -*- coding: utf-8 -*-

from typing import List


class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.updates = []

    def updateSubrectangle(
        self, row1: int, col1: int, row2: int, col2: int, newValue: int
    ) -> None:
        self.updates.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        result = self.rectangle[row][col]
        for row1, col1, row2, col2, newValue in self.updates:
            if row1 <= row <= row2 and col1 <= col <= col2:
                result = newValue
        return result


if __name__ == "__main__":
    obj = SubrectangleQueries(
        [
            [1, 2, 1],
            [4, 3, 4],
            [3, 2, 1],
            [1, 1, 1],
        ]
    )
    assert 1 == obj.getValue(0, 2)
    obj.updateSubrectangle(0, 0, 3, 2, 5)
    assert 5 == obj.getValue(0, 2)
    assert 5 == obj.getValue(3, 1)
    obj.updateSubrectangle(3, 0, 3, 2, 10)
    assert 10 == obj.getValue(3, 1)
    assert 5 == obj.getValue(0, 2)

    obj = SubrectangleQueries(
        [
            [1, 1, 1],
            [2, 2, 2],
            [3, 3, 3],
        ]
    )
    assert 1 == obj.getValue(0, 0)
    obj.updateSubrectangle(0, 0, 2, 2, 100)
    assert 100 == obj.getValue(0, 0)
    assert 100 == obj.getValue(2, 2)
    obj.updateSubrectangle(1, 1, 2, 2, 20)
    assert 20 == obj.getValue(2, 2)
