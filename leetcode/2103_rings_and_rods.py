# -*- coding: utf-8 -*-

class Solution:
    def countPoints(self, rings: str) -> int:
        red, green, blue = set(), set(), set()
        for i in range(0, len(rings), 2):
            color, rod = rings[i], int(rings[i + 1])
            if color == 'R':
                red.add(rod)
            elif color == 'G':
                green.add(rod)
            elif color == 'B':
                blue.add(rod)
        return len(red & green & blue)


if __name__ == '__main__':
    solution = Solution()

    assert 1 == solution.countPoints('B0B6G0R6R0R6G9')
    assert 1 == solution.countPoints('B0R0G0R9R0B0G0')
    assert 0 == solution.countPoints('G4')
