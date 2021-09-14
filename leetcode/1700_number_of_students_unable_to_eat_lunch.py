# -*- coding: utf-8 -*-

from collections import Counter
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = Counter(students)
        for sandwich in sandwiches:
            if counts[sandwich] > 0:
                counts[sandwich] -= 1
            else:
                break
        return sum(counts.values())


if __name__ == '__main__':
    solution = Solution()

    assert 0 == solution.countStudents([1, 1, 0, 0], [0, 1, 0, 1])
    assert 3 == solution.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])
