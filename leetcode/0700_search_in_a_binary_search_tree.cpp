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
    TreeNode* searchBST(TreeNode* root, int val) {
        if (!root || root->val == val) {
            return root;
        } else if (root->val > val) {
            return searchBST(root->left, val);
        } else {
            return searchBST(root->right, val);
        }
    }
};

int main() {
    auto solution = Solution();

    auto t0_0 = TreeNode(4);
    auto t0_1 = TreeNode(2);
    auto t0_2 = TreeNode(7);
    auto t0_3 = TreeNode(1);
    auto t0_4 = TreeNode(3);
    t0_1.right = &t0_4;
    t0_1.left = &t0_3;
    t0_0.right = &t0_2;
    t0_0.left = &t0_1;

    assert(&t0_1 == solution.searchBST(&t0_0, 2));
}
