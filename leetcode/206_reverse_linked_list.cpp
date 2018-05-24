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
    } else {
        return !(lhs.next || rhs.next);
    }
};

class Solution {
public:
    ListNode* reverseList (ListNode* head) {
        if (!head || !head->next) {
            return head;
        } else {
            auto newHead = reverseList(head->next);
            head->next->next = head;
            head->next = NULL;
            return newHead;
        }
    }
};

int main () {
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

    auto l1_0 = ListNode(5);
    auto l1_1 = ListNode(4);
    auto l1_2 = ListNode(3);
    auto l1_3 = ListNode(2);
    auto l1_4 = ListNode(1);
    l1_3.next = &l1_4;
    l1_2.next = &l1_3;
    l1_1.next = &l1_2;
    l1_0.next = &l1_1;

    assert(l1_0 == *(solution.reverseList(&l0_0)));
}
