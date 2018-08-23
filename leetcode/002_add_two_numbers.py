# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return (
            other is not None and
            self.val == other.val and
            self.next == other.next
        )


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry, val = divmod(l1.val + l2.val, 10)
        l1 = l1.next
        l2 = l2.next

        result = ListNode(val)

        current = result
        while l1 is not None or l2 is not None:
            val = carry
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if l2 is not None:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            current.next = ListNode(val)
            current = current.next
        if carry:
            current.next = ListNode(1)

        return result


if __name__ == '__main__':
    solution = Solution()

    l0_0 = ListNode(2)
    l0_1 = ListNode(4)
    l0_2 = ListNode(3)
    l0_1.next = l0_2
    l0_0.next = l0_1

    l1_0 = ListNode(5)
    l1_1 = ListNode(6)
    l1_2 = ListNode(4)
    l1_1.next = l1_2
    l1_0.next = l1_1

    l2_0 = ListNode(7)
    l2_1 = ListNode(0)
    l2_2 = ListNode(8)
    l2_1.next = l2_2
    l2_0.next = l2_1

    assert l2_0 == solution.addTwoNumbers(l0_0, l1_0)
