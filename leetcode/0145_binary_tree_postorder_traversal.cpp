// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cstddef>
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    explicit TreeNode(int x): val(x), left(NULL), right(NULL) {}
};

class Solution {
 public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> result;
        if (root) {
            postorderTraversalHelper(root, result);
        }
        return result;
    }

 private:
    void postorderTraversalHelper(TreeNode* root, vector<int>& result) {
        if (root->left) {
            postorderTraversalHelper(root->left, result);
        }
        if (root->right) {
            postorderTraversalHelper(root->right, result);
        }
        result.push_back(root->val);
    }
};

int main() {
    auto solution = Solution();

    auto t0_0 = TreeNode(1);
    auto t0_1 = TreeNode(2);
    auto t0_2 = TreeNode(3);
    t0_1.left = &t0_2;
    t0_0.right = &t0_1;

    vector<int> expected = {3, 2, 1};
    vector<int> result = solution.postorderTraversal(&t0_0);

    assert(expected == result);
}
