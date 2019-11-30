# -*- coding: utf-8 -*-


class Solution:
    def hIndex(self, citations):
        length = len(citations)

        histogram = [0] * (length + 1)
        for count in citations:
            histogram[min(count, length)] += 1

        sum_ = 0
        for i, count in reversed(list(enumerate(histogram))):
            sum_ += count
            if sum_ >= i:
                return i

        return 0


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.hIndex([3, 0, 6, 1, 5])
