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
    TreeNode* trimBST(TreeNode* root, int L, int R) {
        if (!root) {
            return NULL;
        } else if (root->val < L) {
            return trimBST(root->right, L, R);
        } else if (root->val > R) {
            return trimBST(root->left, L, R);
        }

        root->left = trimBST(root->left, L, R);
        root->right = trimBST(root->right, L, R);

        return root;
    }
};

int main() {
    auto solution = Solution();

    auto t0_0 = TreeNode(1);
    auto t0_1 = TreeNode(0);
    auto t0_2 = TreeNode(2);
    t0_0.right = &t0_1;
    t0_0.left = &t0_2;

    auto t1_0 = TreeNode(1);
    auto t1_1 = TreeNode(2);
    t0_0.left = &t0_1;

    assert(t1_0 == *(solution.trimBST(&t0_0, 1, 2)));
}
