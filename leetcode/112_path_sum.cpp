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
    bool hasPathSum(TreeNode* root, int sum) {
        if (!root) {
            return false;
        } else if (!root->left && !root->right) {
            return root->val == sum;
        } else {
            return hasPathSum(root->left, sum - root->val) || hasPathSum(root->right, sum - root->val);
        }
    }
};

int main() {
    auto solution = Solution();

    auto t0_0 = TreeNode(5);
    auto t0_1 = TreeNode(4);
    auto t0_2 = TreeNode(8);
    auto t0_3 = TreeNode(11);
    auto t0_4 = TreeNode(13);
    auto t0_5 = TreeNode(4);
    auto t0_6 = TreeNode(7);
    auto t0_7 = TreeNode(2);
    auto t0_8 = TreeNode(1);
    t0_5.right = &t0_8;
    t0_3.right = &t0_7;
    t0_3.left = &t0_6;
    t0_2.right = &t0_5;
    t0_2.left = &t0_4;
    t0_1.left = &t0_3;
    t0_0.right = &t0_2;
    t0_0.left = &t0_1;

    assert(solution.hasPathSum(&t0_0, 22));
}
