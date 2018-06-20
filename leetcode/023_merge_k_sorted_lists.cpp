// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cstddef>
#include <queue>

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

class Compare {
 public:
    bool operator()(ListNode* x, ListNode* y) {
        return x->val > y->val;
    }
};

class Solution {
 public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto head = ListNode(0);
        auto current = &head;

        priority_queue<ListNode*, vector<ListNode*>, Compare> heap;
        for (auto list : lists) {
            if (list) {
                heap.push(list);
            }
        }

        while (!heap.empty()) {
            auto node = heap.top();
            heap.pop();
            current->next = node;
            current = current->next;
            if (node->next) {
                heap.push(node->next);
            }
        }

        return head.next;
    }
};

int main() {
    auto solution = Solution();

    auto l0_0 = ListNode(1);
    auto l0_1 = ListNode(4);
    auto l0_2 = ListNode(5);
    l0_1.next = &l0_2;
    l0_0.next = &l0_1;

    auto l1_0 = ListNode(1);
    auto l1_1 = ListNode(3);
    auto l1_2 = ListNode(4);
    l1_1.next = &l1_2;
    l1_0.next = &l1_1;

    auto l2_0 = ListNode(2);
    auto l2_1 = ListNode(6);
    l2_0.next = &l2_1;

    vector<ListNode*> lists = {&l0_0, &l1_0, &l2_0};

    auto l3_0 = ListNode(1);
    auto l3_1 = ListNode(1);
    auto l3_2 = ListNode(2);
    auto l3_3 = ListNode(3);
    auto l3_4 = ListNode(4);
    auto l3_5 = ListNode(4);
    auto l3_6 = ListNode(5);
    auto l3_7 = ListNode(6);
    l3_6.next = &l3_7;
    l3_5.next = &l3_6;
    l3_4.next = &l3_5;
    l3_3.next = &l3_4;
    l3_2.next = &l3_3;
    l3_1.next = &l3_2;
    l3_0.next = &l3_1;

    assert(l3_0 == *(solution.mergeKLists(lists)));
}
