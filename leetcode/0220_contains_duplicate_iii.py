# -*- coding: utf-8 -*-

from collections import OrderedDict


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        buckets = OrderedDict()
        for num in nums:
            if len(buckets) > k:
                buckets.popitem(last=False)
            i = num if t == 0 else num // t
            for j in (i - 1, i, i + 1):
                if buckets.get(j) is not None and abs(num - buckets[j]) <= t:
                    return True
            buckets[i] = num
        return False


if __name__ == '__main__':
    solution = Solution()

    assert solution.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)
    assert solution.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2)
    assert not solution.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3)
