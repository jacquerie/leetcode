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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* current = root;
        int minVal = min(p->val, q->val), maxVal = max(p->val, q->val);

        while (current->val < minVal || current->val > maxVal) {
            while (current->val < minVal) {
                current = current->right;
            }

            while (current->val > maxVal) {
                current = current->left;
            }
        }

        return current;
    }
};

int main() {
    auto solution = Solution();

    auto t0_0 = TreeNode(6);
    auto t0_1 = TreeNode(2);
    auto t0_2 = TreeNode(8);
    auto t0_3 = TreeNode(0);
    auto t0_4 = TreeNode(4);
    auto t0_5 = TreeNode(7);
    auto t0_6 = TreeNode(9);
    auto t0_7 = TreeNode(3);
    auto t0_8 = TreeNode(5);
    t0_4.right = &t0_8;
    t0_4.left = &t0_7;
    t0_2.right = &t0_6;
    t0_2.left = &t0_5;
    t0_1.right = &t0_4;
    t0_1.left = &t0_3;
    t0_0.right = &t0_2;
    t0_0.left = &t0_1;

    assert(&t0_0 == solution.lowestCommonAncestor(&t0_0, &t0_1, &t0_2));
    assert(&t0_1 == solution.lowestCommonAncestor(&t0_0, &t0_1, &t0_4));
}
