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
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next) {
            return head;
        }

        auto current = head;

        int n = 1;
        while (current->next) {
            n++;
            current = current->next;
        }

        current->next = head;

        current = head;
        for (int i = 0; i < n - k % n - 1; i++) {
            current = current->next;
        }

        head = current->next;
        current->next = NULL;

        return head;
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

    auto l1_0 = ListNode(4);
    auto l1_1 = ListNode(5);
    auto l1_2 = ListNode(1);
    auto l1_3 = ListNode(2);
    auto l1_4 = ListNode(3);
    l1_3.next = &l1_4;
    l1_2.next = &l1_3;
    l1_1.next = &l1_2;
    l1_0.next = &l1_1;

    assert(l1_0 == *(solution.rotateRight(&l0_0, 2)));
}
