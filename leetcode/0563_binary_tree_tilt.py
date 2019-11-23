# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTilt(self, root):
        def _findTilt(root):
            if root is None:
                return 0, 0

            leftSum, leftTiltSum = _findTilt(root.left)
            rightSum, rightTiltSum = _findTilt(root.right)

            return (
                leftSum + root.val + rightSum,
                leftTiltSum + abs(leftSum - rightSum) + rightTiltSum,
            )

        _, result = _findTilt(root)
        return result


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(1)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(3)
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert 1 == solution.findTilt(t0_0)
