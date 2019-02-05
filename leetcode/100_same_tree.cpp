// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cstddef>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    explicit TreeNode(int x): val(x), left(NULL), right(NULL) {}
};

class Solution {
 public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && !q) {
            return true;
        } else if (!p || !q) {
            return false;
        } else {
            return (
                p->val == q->val &&
                isSameTree(p->left, q->left) &&
                isSameTree(p->right, q->right));
        }
    }
};

int main() {
    auto solution = Solution();

    auto t0_0 = TreeNode(1);
    auto t0_1 = TreeNode(2);
    auto t0_2 = TreeNode(3);
    t0_0.right = &t0_2;
    t0_0.left = &t0_1;

    auto t1_0 = TreeNode(1);
    auto t1_1 = TreeNode(2);
    auto t1_2 = TreeNode(3);
    t1_0.right = &t1_2;
    t1_0.left = &t1_1;

    assert(solution.isSameTree(&t0_0, &t1_0));

    auto t2_0 = TreeNode(1);
    auto t2_1 = TreeNode(2);
    t2_0.left = &t2_1;

    auto t3_0 = TreeNode(1);
    auto t3_1 = TreeNode(2);
    t3_0.right = &t3_1;

    assert(!solution.isSameTree(&t2_0, &t3_0));

    auto t4_0 = TreeNode(1);
    auto t4_1 = TreeNode(2);
    auto t4_2 = TreeNode(1);
    t4_0.right = &t4_2;
    t4_0.left = &t4_1;

    auto t5_0 = TreeNode(1);
    auto t5_1 = TreeNode(1);
    auto t5_2 = TreeNode(2);
    t5_0.right = &t5_2;
    t5_0.left = &t5_1;

    assert(!solution.isSameTree(&t4_0, &t5_0));
}
