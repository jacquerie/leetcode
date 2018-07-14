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

bool operator==(TreeNode& p, TreeNode& q) {
    bool left, right;

    if (!p.left && !q.left) {
        left = true;
    } else if (!p.left || !q.left) {
        left = false;
    } else {
        left = *(p.left) == *(q.left);
    }

    if (!p.right && !q.right) {
        right = true;
    } else if (!p.right || !q.right) {
        right = false;
    } else {
        right = *(p.right) == *(q.right);
    }

    return p.val == q.val && left && right;
}

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

    auto t1_0 = TreeNode(2);
    auto t1_1 = TreeNode(1);
    auto t1_2 = TreeNode(3);
    t1_0.right = &t1_2;
    t1_0.left = &t1_1;

    assert(t1_0 == *(solution.searchBST(&t0_0, 2)));
}
