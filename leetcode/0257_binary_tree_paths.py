# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        def _binaryTreePaths(root):
            if root.left is None and root.right is None:
                return [[str(root.val)]]
            elif root.left is None:
                result = []
                for path in _binaryTreePaths(root.right):
                    path.append(str(root.val))
                    result.append(path)
                return result
            elif root.right is None:
                result = []
                for path in _binaryTreePaths(root.left):
                    path.append(str(root.val))
                    result.append(path)
                return result
            result = []
            for path in _binaryTreePaths(root.left):
                path.append(str(root.val))
                result.append(path)
            for path in _binaryTreePaths(root.right):
                path.append(str(root.val))
                result.append(path)
            return result

        if root is None:
            return []
        return ['->'.join(reversed(path)) for path in _binaryTreePaths(root)]


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(1)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(3)
    t0_3 = TreeNode(5)
    t0_1.right = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert ['1->2->5', '1->3'] == solution.binaryTreePaths(t0_0)
