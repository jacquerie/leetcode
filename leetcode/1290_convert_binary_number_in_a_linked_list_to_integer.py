# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        current, result = head, 0
        while current is not None:
            result = 2 * result + current.val
            current = current.next
        return result


if __name__ == "__main__":
    solution = Solution()

    l0_0 = ListNode(1)
    l0_1 = ListNode(0)
    l0_2 = ListNode(1)
    l0_1.next = l0_2
    l0_0.next = l0_1

    assert 5 == solution.getDecimalValue(l0_0)

    l1_0 = ListNode(0)

    assert 0 == solution.getDecimalValue(l1_0)

    l2_0 = ListNode(1)

    assert 1 == solution.getDecimalValue(l2_0)

    l3_0 = ListNode(1)
    l3_1 = ListNode(0)
    l3_2 = ListNode(0)
    l3_3 = ListNode(1)
    l3_4 = ListNode(0)
    l3_5 = ListNode(0)
    l3_6 = ListNode(1)
    l3_7 = ListNode(1)
    l3_8 = ListNode(1)
    l3_9 = ListNode(0)
    l3_10 = ListNode(0)
    l3_11 = ListNode(0)
    l3_12 = ListNode(0)
    l3_13 = ListNode(0)
    l3_14 = ListNode(0)
    l3_13.next = l3_14
    l3_12.next = l3_13
    l3_11.next = l3_12
    l3_10.next = l3_11
    l3_9.next = l3_10
    l3_8.next = l3_9
    l3_7.next = l3_8
    l3_6.next = l3_7
    l3_5.next = l3_6
    l3_4.next = l3_5
    l3_3.next = l3_4
    l3_2.next = l3_3
    l3_1.next = l3_2
    l3_0.next = l3_1

    assert 18880 == solution.getDecimalValue(l3_0)

    l4_0 = ListNode(0)
    l4_1 = ListNode(0)
    l4_0.next = l4_1

    assert 0 == solution.getDecimalValue(l4_0)
