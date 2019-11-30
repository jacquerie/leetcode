# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return (
            other is not None and
            self.val == other.val and
            self.next == other.next
        )


class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        lenA, lenB = 1, 1
        currA, currB = headA, headB

        while currA.next is not None:
            currA = currA.next
            lenA += 1

        while currB.next is not None:
            currB = currB.next
            lenB += 1

        currA, currB = headA, headB

        if lenA >= lenB:
            for _ in range(lenA - lenB):
                currA = currA.next
        else:
            for _ in range(lenB - lenA):
                currB = currB.next

        while (currA.next is not None and currB.next is not None and currA != currB):
            currA = currA.next
            currB = currB.next

        if currA == currB:
            return currA
        return None


if __name__ == '__main__':
    solution = Solution()

    c1 = ListNode('c1')
    c2 = ListNode('c2')
    c3 = ListNode('c3')
    c1.next = c2
    c2.next = c3

    a1 = ListNode('a1')
    a2 = ListNode('a2')
    a1.next = a2
    a2.next = c1

    b1 = ListNode('b1')
    b2 = ListNode('b2')
    b3 = ListNode('b3')
    b1.next = b2
    b2.next = b3
    b3.next = c1

    assert c1 == solution.getIntersectionNode(a1, b1)
