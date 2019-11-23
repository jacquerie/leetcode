# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other):
        return (
            other is not None and
            self.val == other.val and
            self.left == other.left and
            self.right == other.right
        )


class Solution(object):
    def allPossibleFBT(self, N):
        if N == 1:
            return [TreeNode(0)]

        result = []

        for i in range(1, N, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(N - i - 1):
                    node = TreeNode(0)
                    node.left = left
                    node.right = right
                    result.append(node)

        return result


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(0)
    t0_1 = TreeNode(0)
    t0_2 = TreeNode(0)
    t0_3 = TreeNode(0)
    t0_4 = TreeNode(0)
    t0_5 = TreeNode(0)
    t0_6 = TreeNode(0)
    t0_4.right = t0_6
    t0_4.left = t0_5
    t0_2.right = t0_4
    t0_2.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    t1_0 = TreeNode(0)
    t1_1 = TreeNode(0)
    t1_2 = TreeNode(0)
    t1_3 = TreeNode(0)
    t1_4 = TreeNode(0)
    t1_5 = TreeNode(0)
    t1_6 = TreeNode(0)
    t1_3.right = t1_6
    t1_3.left = t1_5
    t1_2.right = t1_4
    t1_2.left = t1_3
    t1_0.right = t1_2
    t1_0.left = t1_1

    t2_0 = TreeNode(0)
    t2_1 = TreeNode(0)
    t2_2 = TreeNode(0)
    t2_3 = TreeNode(0)
    t2_4 = TreeNode(0)
    t2_5 = TreeNode(0)
    t2_6 = TreeNode(0)
    t2_2.right = t2_6
    t2_2.left = t2_5
    t2_1.right = t2_4
    t2_1.left = t2_3
    t2_0.right = t2_2
    t2_0.left = t2_1

    t3_0 = TreeNode(0)
    t3_1 = TreeNode(0)
    t3_2 = TreeNode(0)
    t3_3 = TreeNode(0)
    t3_4 = TreeNode(0)
    t3_5 = TreeNode(0)
    t3_6 = TreeNode(0)
    t3_4.right = t3_6
    t3_4.left = t3_5
    t3_1.right = t3_4
    t3_1.left = t3_3
    t3_0.right = t3_2
    t3_0.left = t3_1

    t4_0 = TreeNode(0)
    t4_1 = TreeNode(0)
    t4_2 = TreeNode(0)
    t4_3 = TreeNode(0)
    t4_4 = TreeNode(0)
    t4_5 = TreeNode(0)
    t4_6 = TreeNode(0)
    t4_3.right = t4_6
    t4_3.left = t4_5
    t4_1.right = t4_4
    t4_1.left = t4_3
    t4_0.right = t4_2
    t4_0.left = t4_1

    assert [t0_0, t1_0, t2_0, t3_0, t4_0] == solution.allPossibleFBT(7)
