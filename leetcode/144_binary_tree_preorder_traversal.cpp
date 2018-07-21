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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> result;
        if (root) {
            preorderTraversalHelper(root, result);
        }
        return result;
    }

 private:
    void preorderTraversalHelper(TreeNode* root, vector<int>& result) {
        result.push_back(root->val);
        if (root->left) {
            preorderTraversalHelper(root->left, result);
        }
        if (root->right) {
            preorderTraversalHelper(root->right, result);
        }
    }
};

int main() {
    auto solution = Solution();

    auto t0_0 = TreeNode(1);
    auto t0_1 = TreeNode(2);
    auto t0_2 = TreeNode(3);
    t0_1.left = &t0_2;
    t0_0.right = &t0_1;

    vector<int> expected = {1, 2, 3};
    vector<int> result = solution.preorderTraversal(&t0_0);

    assert(expected == result);
}
