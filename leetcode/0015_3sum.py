# -*- coding: utf-8 -*-


class Solution:
    def threeSum(self, nums):
        nums.sort()

        result = set()

        for k, _ in enumerate(nums):
            i, j = 0, len(nums) - 1
            while i < k and j > k:
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add((nums[i], nums[k], nums[j]))
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    i += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    j -= 1

        return [list(el) for el in result]


if __name__ == "__main__":
    solution = Solution()

    nums = [-1, 0, 1, 2, -1, -4]

    expected = [
        [-1, 0, 1],
        [-1, -1, 2],
    ]
    result = solution.threeSum(nums)

    assert sorted(expected) == sorted(result)

    nums = [3, 0, -2, -1, 1, 2]

    expected = [
        [-2, -1, 3],
        [-2, 0, 2],
        [-1, 0, 1],
    ]
    result = solution.threeSum(nums)

    assert sorted(expected) == sorted(result)
