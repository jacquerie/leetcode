// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
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
    int maxDepth(TreeNode* root) {
        if (!root) {
            return 0;
        } else {
            return 1 + max(maxDepth(root->left), maxDepth(root->right));
        }
    }
};

int main() {
    auto solution = Solution();

    auto t0_0 = TreeNode(3);
    auto t0_1 = TreeNode(9);
    auto t0_2 = TreeNode(20);
    auto t0_3 = TreeNode(15);
    auto t0_4 = TreeNode(7);
    t0_2.right = &t0_4;
    t0_2.left = &t0_3;
    t0_0.right = &t0_1;
    t0_0.left = &t0_2;

    assert(3 == solution.maxDepth(&t0_0));
}
