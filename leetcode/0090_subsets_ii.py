# -*- coding: utf-8 -*-


class Solution(object):
    def subsetsWithDup(self, nums):
        result = []
        self._subsetsWithDup(sorted(nums), [], result)
        return result

    def _subsetsWithDup(self, nums, current, result):
        if not nums:
            if current not in result:
                result.append(current)
        else:
            self._subsetsWithDup(nums[1:], current, result)
            self._subsetsWithDup(nums[1:], current + [nums[0]], result)


if __name__ == '__main__':
    solution = Solution()

    assert [
        [],
        [2],
        [2, 2],
        [1],
        [1, 2],
        [1, 2, 2],
    ] == solution.subsetsWithDup([1, 2, 2])
    assert [
        [],
        [4],
        [4, 4],
        [4, 4, 4],
        [4, 4, 4, 4],
        [1],
        [1, 4],
        [1, 4, 4],
        [1, 4, 4, 4],
        [1, 4, 4, 4, 4],
    ] == solution.subsetsWithDup([4, 4, 4, 1, 4])
