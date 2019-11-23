# -*- coding: utf-8 -*-


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


class Solution(object):
    def intervalIntersection(self, A, B):
        result = []

        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i].end < B[j].start:
                i += 1
            elif B[j].end < A[i].start:
                j += 1
            else:
                result.append(
                    Interval(
                        max(A[i].start, B[j].start),
                        min(A[i].end, B[j].end)
                    )
                )

                if A[i].end < B[j].end:
                    i += 1
                else:
                    j += 1

        return result


if __name__ == '__main__':
    solution = Solution()

    A = [
        Interval(0, 2),
        Interval(5, 10),
        Interval(13, 23),
        Interval(24, 25),
    ]
    B = [
        Interval(1, 5),
        Interval(8, 12),
        Interval(15, 24),
        Interval(25, 26),
    ]

    expected = [
        Interval(1, 2),
        Interval(5, 5),
        Interval(8, 10),
        Interval(15, 23),
        Interval(24, 24),
        Interval(25, 25),
    ]
    result = solution.intervalIntersection(A, B)

    assert expected == result
