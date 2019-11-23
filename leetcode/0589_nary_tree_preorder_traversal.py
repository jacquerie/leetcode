# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        def _preorder(root, result):
            result.append(root.val)
            for child in root.children:
                _preorder(child, result)

        if root is None:
            return []

        result = []
        _preorder(root, result)
        return result


if __name__ == '__main__':
    solution = Solution()

    t0_5 = Node(6, [])
    t0_4 = Node(5, [])
    t0_3 = Node(4, [])
    t0_2 = Node(2, [])
    t0_1 = Node(3, [t0_4, t0_5])
    t0_0 = Node(1, [t0_1, t0_2, t0_3])

    assert [1, 3, 5, 6, 2, 4] == solution.preorder(t0_0)
