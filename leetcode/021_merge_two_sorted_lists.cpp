#include <cassert>
#include <cstddef>

using namespace std;

struct ListNode {
    int val;
    ListNode* next;

    ListNode (int x): val(x), next(NULL) {}
};

bool operator== (ListNode& lhs, ListNode& rhs) {
    if (lhs.next && rhs.next) {
        return lhs.val == rhs.val && *(lhs.next) == *(rhs.next);
    } else if (lhs.next || rhs.next) {
        return false;
    } else {
        return true;
    }
};

class Solution {
public:
    ListNode* mergeTwoLists (ListNode* l1, ListNode* l2) {
        auto head = ListNode(0);
        auto current = &head;

        while (l1 && l2) {
            if (l1->val <= l2->val) {
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }

            current = current->next;
        }

        if (l1) {
            current->next = l1;
        } else {
            current->next = l2;
        }

        return head.next;
    };
};

int main () {
    auto solution = Solution();

    auto l0_0 = ListNode(1);
    auto l0_1 = ListNode(2);
    auto l0_2 = ListNode(4);
    l0_1.next = &l0_2;
    l0_0.next = &l0_1;

    auto l1_0 = ListNode(1);
    auto l1_1 = ListNode(3);
    auto l1_2 = ListNode(4);
    l1_1.next = &l1_2;
    l1_0.next = &l1_1;

    auto l2_0 = ListNode(1);
    auto l2_1 = ListNode(1);
    auto l2_2 = ListNode(2);
    auto l2_3 = ListNode(3);
    auto l2_4 = ListNode(4);
    auto l2_5 = ListNode(4);
    l2_4.next = &l2_5;
    l2_3.next = &l2_4;
    l2_2.next = &l2_3;
    l2_1.next = &l2_2;
    l2_0.next = &l2_1;

    assert(l2_0 == *(solution.mergeTwoLists(&l0_0, &l1_0)));
}
