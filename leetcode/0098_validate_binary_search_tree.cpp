// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cstddef>
#include <cstdint>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    explicit TreeNode(int x): val(x), left(NULL), right(NULL) {}
};

class Solution {
 public:
    bool isValidBST(TreeNode* root) {
        return isValidBSTHelper(root, INT64_MIN, INT64_MAX);
    }

 private:
    bool isValidBSTHelper(TreeNode* root, int64_t minimum, int64_t maximum) {
        if (!root) {
            return true;
        } else {
            return minimum < root->val && root->val < maximum &&
              isValidBSTHelper(root->left, minimum, root->val) &&
              isValidBSTHelper(root->right, root->val, maximum);
        }
    }
};

int main() {
    auto solution = Solution();

    auto t0_0 = TreeNode(2);
    auto t0_1 = TreeNode(1);
    auto t0_2 = TreeNode(3);
    t0_0.right = &t0_2;
    t0_0.left = &t0_1;

    assert(solution.isValidBST(&t0_0));

    auto t1_0 = TreeNode(5);
    auto t1_1 = TreeNode(1);
    auto t1_2 = TreeNode(4);
    auto t1_3 = TreeNode(3);
    auto t1_4 = TreeNode(6);
    t1_2.right = &t1_4;
    t1_2.left = &t1_3;
    t1_0.right = &t1_2;
    t1_0.left = &t1_1;

    assert(!solution.isValidBST(&t1_0));

    auto t2_0 = TreeNode(2147483647);

    assert(solution.isValidBST(&t2_0));
}
