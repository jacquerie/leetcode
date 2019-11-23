# -*- coding: utf-8 -*-


class Solution(object):
    def reconstructQueue(self, people):
        people.sort(key=lambda person: (-person[0], person[1]))

        result = []
        for person in people:
            result.insert(person[1], person)
        return result


if __name__ == '__main__':
    solution = Solution()

    assert [
        [5, 0],
        [7, 0],
        [5, 2],
        [6, 1],
        [4, 4],
        [7, 1],
    ] == solution.reconstructQueue([
        [7, 0],
        [4, 4],
        [7, 1],
        [5, 0],
        [6, 1],
        [5, 2],
    ])
