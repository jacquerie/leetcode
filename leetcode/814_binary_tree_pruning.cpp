// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cstddef>
#include <iostream>

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
    TreeNode* pruneTree(TreeNode* root) {
        if (!root) {
            return NULL;
        }

        root->left = pruneTree(root->left);
        root->right = pruneTree(root->right);

        if (!root->left && !root->right && root->val == 0) {
            return NULL;
        }

        return root;
    }
};

int main() {
    auto solution = Solution();

    auto t0_0 = TreeNode(1);
    auto t0_1 = TreeNode(0);
    auto t0_2 = TreeNode(0);
    auto t0_3 = TreeNode(1);
    t0_1.right = &t0_3;
    t0_1.left = &t0_2;
    t0_0.right = &t0_1;

    auto t1_0 = TreeNode(1);
    auto t1_1 = TreeNode(0);
    auto t1_2 = TreeNode(1);
    t1_1.right = &t1_2;
    t1_0.right = &t1_1;

    assert(t1_0 == *(solution.pruneTree(&t0_0)));
}
