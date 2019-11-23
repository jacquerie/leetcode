# -*- coding: utf-8 -*-

from heapq import heappop, heappush


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

    def __lt__(self, other):
        return (
            other is not None and
            self.val < other.val
        )


class ListHeap(object):
    def __init__(self, lists):
        self.els = []
        for el in lists:
            if el is not None:
                heappush(self.els, (el.val, el))

    def __bool__(self):
        return len(self.els) > 0

    def pop(self):
        _, el = heappop(self.els)
        return el

    def push(self, el):
        heappush(self.els, (el.val, el))


class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        current = dummy

        heap = ListHeap(lists)
        while heap:
            node = heap.pop()
            current.next = node
            current = current.next
            if node.next is not None:
                heap.push(node.next)

        return dummy.next


if __name__ == '__main__':
    solution = Solution()

    l0_0 = ListNode(1)
    l0_1 = ListNode(4)
    l0_2 = ListNode(5)
    l0_1.next = l0_2
    l0_0.next = l0_1

    l1_0 = ListNode(1)
    l1_1 = ListNode(3)
    l1_2 = ListNode(4)
    l1_1.next = l1_2
    l1_0.next = l1_1

    l2_0 = ListNode(2)
    l2_1 = ListNode(6)
    l2_0.next = l2_1

    l3_0 = ListNode(1)
    l3_1 = ListNode(1)
    l3_2 = ListNode(2)
    l3_3 = ListNode(3)
    l3_4 = ListNode(4)
    l3_5 = ListNode(4)
    l3_6 = ListNode(5)
    l3_7 = ListNode(6)
    l3_6.next = l3_7
    l3_5.next = l3_6
    l3_4.next = l3_5
    l3_3.next = l3_4
    l3_2.next = l3_3
    l3_1.next = l3_2
    l3_0.next = l3_1

    assert l3_0 == solution.mergeKLists([l0_0, l1_0, l2_0])
