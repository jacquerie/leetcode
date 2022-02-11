# -*- coding: utf-8 -*-


class FenwickTree:
    def __init__(self, nums):
        self.els = [0] * (len(nums) + 2)
        for i, num in enumerate(nums, 1):
            self.add(i, num)

    def add(self, i, k):
        while i < len(self.els):
            self.els[i] += k
            i += i & -i

    def sumPrefix(self, i):
        result = 0
        while i > 0:
            result += self.els[i]
            i -= i & -i
        return result


class NumArray:
    def __init__(self, nums):
        self.tree = FenwickTree(nums)

    def update(self, i, val):
        self.tree.add(i + 1, val - self.sumRange(i, i))

    def sumRange(self, i, j):
        return self.tree.sumPrefix(j + 1) - self.tree.sumPrefix(i)


if __name__ == "__main__":
    obj = NumArray([1, 3, 5])

    assert 9 == obj.sumRange(0, 2)
    obj.update(1, 2)
    assert 8 == obj.sumRange(0, 2)

    obj = NumArray([-1])

    assert -1 == obj.sumRange(0, 0)
    obj.update(0, 1)
    assert 1 == obj.sumRange(0, 0)
