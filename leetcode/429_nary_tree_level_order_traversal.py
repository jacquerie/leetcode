# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import itertools


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        result = []

        current = [root]
        while current:
            result.append([node.val for node in current])
            current = list(itertools.chain.from_iterable([
                node.children for node in current]))

        return result


if __name__ == '__main__':
    solution = Solution()

    t0_5 = Node(6, [])
    t0_4 = Node(5, [])
    t0_3 = Node(4, [])
    t0_2 = Node(2, [])
    t0_1 = Node(3, [t0_4, t0_5])
    t0_0 = Node(1, [t0_1, t0_2, t0_3])

    assert [[1], [3, 2, 4], [5, 6]] == solution.levelOrder(t0_0)
