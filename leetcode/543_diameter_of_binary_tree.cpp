// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <cstddef>
#include <utility>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    explicit TreeNode(int x): val(x), left(NULL), right(NULL) {}
};

class Solution {
 public:
    int diameterOfBinaryTree(TreeNode* root) {
        if (!root) {
            return 0;
        }

        return diameterAndHeightOfBinaryTree(root).first - 1;
    }

 private:
    pair<int, int> diameterAndHeightOfBinaryTree(TreeNode* root) {
        if (!root) {
            return pair<int, int>(0, 0);
        }

        auto left = diameterAndHeightOfBinaryTree(root->left);
        auto right = diameterAndHeightOfBinaryTree(root->right);

        int diameter = max(max(left.first, right.first), left.second + right.second + 1);
        int height = 1 + max(left.second, right.second);

        return pair<int, int>(diameter, height);
    }
};

int main() {
    auto solution = Solution();

    auto t0_0 = TreeNode(1);
    auto t0_1 = TreeNode(2);
    auto t0_2 = TreeNode(3);
    auto t0_3 = TreeNode(4);
    auto t0_4 = TreeNode(5);
    t0_2.right = &t0_4;
    t0_2.left = &t0_3;
    t0_0.right = &t0_1;
    t0_0.left = &t0_2;

    assert(3 == solution.diameterOfBinaryTree(&t0_0));
}
