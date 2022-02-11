# -*- coding: utf-8 -*-


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y, visited = 0, 0, set([(0, 0)])
        for char in path:
            if char == "N":
                x += 1
            elif char == "E":
                y += 1
            elif char == "S":
                x -= 1
            elif char == "W":
                y -= 1
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False


if __name__ == "__main__":
    solution = Solution()

    assert not solution.isPathCrossing("NES")
    assert solution.isPathCrossing("NESWW")
