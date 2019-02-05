// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cstddef>

using namespace std;

struct ListNode {
    int val;
    ListNode* next;

    explicit ListNode(int x): val(x), next(NULL) {}
};

class Solution {
 public:
    ListNode* middleNode(ListNode* head) {
        auto slow = head, fast = head;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        return slow;
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

    assert(&l0_2 == solution.middleNode(&l0_0));

    auto l1_0 = ListNode(1);
    auto l1_1 = ListNode(2);
    auto l1_2 = ListNode(3);
    auto l1_3 = ListNode(4);
    auto l1_4 = ListNode(5);
    auto l1_5 = ListNode(6);
    l1_4.next = &l1_5;
    l1_3.next = &l1_4;
    l1_2.next = &l1_3;
    l1_1.next = &l1_2;
    l1_0.next = &l1_1;

    assert(&l1_3 == solution.middleNode(&l1_0));
}
