# -*- coding: utf-8 -*-


class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        lengths = {num: 0 for num in nums}
        for num in nums:
            if not lengths[num]:
                lengths[num] = 1
                left, right = lengths.get(num - 1, 0), lengths.get(num + 1, 0)
                length = 1 + left + right
                lengths[num - left], lengths[num + right] = length, length
        return max(lengths.values())


if __name__ == '__main__':
    solution = Solution()

    assert 4 == solution.longestConsecutive([100, 4, 200, 1, 3, 2])
    assert 0 == solution.longestConsecutive([])
    assert 3 == solution.longestConsecutive([1, 2, 0, 1])
