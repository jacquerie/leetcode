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
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> leaves1, leaves2;
        leafSimilarHelper(root1, leaves1);
        leafSimilarHelper(root2, leaves2);

        return leaves1 == leaves2;
    }

 private:
     void leafSimilarHelper(TreeNode* root, vector<int>& leaves) {
         if (!root) {
             return;
         } else if (!root->left && !root->right) {
             leaves.push_back(root->val);
         } else {
             leafSimilarHelper(root->left, leaves);
             leafSimilarHelper(root->right, leaves);
         }
     }
};

int main() {
    auto solution = Solution();

    auto t0_0 = TreeNode(3);
    auto t0_1 = TreeNode(5);
    auto t0_2 = TreeNode(1);
    auto t0_3 = TreeNode(6);
    auto t0_4 = TreeNode(2);
    auto t0_5 = TreeNode(9);
    auto t0_6 = TreeNode(8);
    auto t0_7 = TreeNode(7);
    auto t0_8 = TreeNode(4);
    t0_4.right = &t0_8;
    t0_4.left = &t0_7;
    t0_2.right = &t0_6;
    t0_2.left = &t0_5;
    t0_1.right = &t0_4;
    t0_1.left = &t0_3;
    t0_0.right = &t0_2;
    t0_0.left = &t0_1;

    auto t1_0 = TreeNode(3);
    auto t1_1 = TreeNode(5);
    auto t1_2 = TreeNode(1);
    auto t1_3 = TreeNode(6);
    auto t1_4 = TreeNode(7);
    auto t1_5 = TreeNode(2);
    auto t1_6 = TreeNode(8);
    auto t1_7 = TreeNode(4);
    auto t1_8 = TreeNode(9);
    t1_5.right = &t1_8;
    t1_5.left = &t1_7;
    t1_2.right = &t1_6;
    t1_2.left = &t1_5;
    t1_1.right = &t1_4;
    t1_1.left = &t1_3;
    t1_0.right = &t1_2;
    t1_0.left = &t1_1;

    assert(solution.leafSimilar(&t0_0, &t1_0));
}
