// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cstddef>
#include <cstdlib>

using namespace std;

struct ListNode {
    int val;
    ListNode* next;

    explicit ListNode(int x): val(x), next(NULL) {}
};

class Solution {
 public:
    explicit Solution(ListNode* head): head_(head), seed_(0) {}

    int getRandom() {
        int count = 0, reservoir;

        auto current = head_;
        while (current) {
            if (rand_r(&seed_) % ++count == 0) {
                reservoir = current->val;
            }

            current = current->next;
        }

        return reservoir;
    }

 private:
    ListNode* head_;
    unsigned int seed_;
};

int main() {
    auto l0_0 = ListNode(1);
    auto l0_1 = ListNode(2);
    auto l0_2 = ListNode(3);
    l0_1.next = &l0_2;
    l0_0.next = &l0_1;

    auto obj = Solution(&l0_0);

    assert(1 == obj.getRandom());
}
