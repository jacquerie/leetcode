# -*- coding: utf-8 -*-


class Solution:
    def arrayNesting(self, nums):
        result = 0

        for num in nums:
            if num is None:
                continue
            current, length = num, 0
            while nums[current] is not None:
                previous = current
                current = nums[current]
                nums[previous] = None
                length += 1
            result = max(result, length)

        return result


if __name__ == "__main__":
    solution = Solution()

    assert 4 == solution.arrayNesting([5, 4, 0, 3, 1, 6, 2])
