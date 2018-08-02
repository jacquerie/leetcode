// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cstddef>

using namespace std;

struct ListNode {
    int val;
    ListNode* next;

    explicit ListNode(int x): val(x), next(NULL) {}
};

bool operator==(ListNode& lhs, ListNode& rhs) {
    if (lhs.next && rhs.next) {
        return lhs.val == rhs.val && *(lhs.next) == *(rhs.next);
    } else {
        return !(lhs.next || rhs.next);
    }
}

class Solution {
 public:
    ListNode* middleNode(ListNode* head) {
        int listLength = getListLength(head);
        auto current = head;

        for (int i = 0; i < listLength / 2; i++) {
            current = current->next;
        }

        return current;
    }

 private:
    int getListLength(ListNode* head) {
        int result = 1;
        auto current = head;

        while (current->next) {
            result++;
            current = current->next;
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    auto l0_0 = ListNode(1);
    auto l0_1 = ListNode(2);
    auto l0_2 = ListNode(3);
    auto l0_3 = ListNode(4);
    auto l0_4 = ListNode(5);
    l0_3.next = &l0_4;
    l0_2.next = &l0_3;
    l0_1.next = &l0_2;
    l0_0.next = &l0_1;

    auto l1_0 = ListNode(3);
    auto l1_1 = ListNode(4);
    auto l1_2 = ListNode(5);
    l1_1.next = &l1_2;
    l1_0.next = &l1_1;

    assert(l1_0 == *(solution.middleNode(&l0_0)));

    auto l2_0 = ListNode(1);
    auto l2_1 = ListNode(2);
    auto l2_2 = ListNode(3);
    auto l2_3 = ListNode(4);
    auto l2_4 = ListNode(5);
    auto l2_5 = ListNode(6);
    l2_4.next = &l2_5;
    l2_3.next = &l2_4;
    l2_2.next = &l2_3;
    l2_1.next = &l2_2;
    l2_0.next = &l2_1;

    auto l3_0 = ListNode(4);
    auto l3_1 = ListNode(5);
    auto l3_2 = ListNode(6);
    l3_1.next = &l3_2;
    l3_0.next = &l3_1;

    assert(l3_0 == *(solution.middleNode(&l2_0)));
}
