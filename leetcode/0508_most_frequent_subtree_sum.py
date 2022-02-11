# -*- coding: utf-8 -*-

from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findFrequentTreeSum(self, root):
        def _findFrequentTreeSum(root, counts):
            if root is None:
                return 0

            leftSum = _findFrequentTreeSum(root.left, counts)
            rightSum = _findFrequentTreeSum(root.right, counts)

            sum = leftSum + root.val + rightSum
            counts[sum] += 1

            return sum

        if root is None:
            return []

        counts = defaultdict(int)
        _findFrequentTreeSum(root, counts)
        max_count = max(counts.values())
        return [sum for sum, count in counts.items() if count == max_count]


if __name__ == "__main__":
    solution = Solution()

    t0_0 = TreeNode(5)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(-3)
    t0_0.left = t0_1
    t0_0.right = t0_2

    expected = [-3, 2, 4]
    result = sorted(solution.findFrequentTreeSum(t0_0))

    assert expected == result

    t1_0 = TreeNode(5)
    t1_1 = TreeNode(2)
    t1_2 = TreeNode(-5)
    t1_0.left = t1_1
    t1_0.right = t1_2

    expected = [2]
    result = sorted(solution.findFrequentTreeSum(t1_0))

    assert expected == result
