# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import random


class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        result = self.nums[:]
        random.shuffle(result)
        return result


if __name__ == '__main__':
    obj = Solution([1, 2, 3])

    assert [1, 2, 3] == obj.reset()
    assert [1, 2, 3] == sorted(obj.shuffle())
    assert [1, 2, 3] == obj.reset()
