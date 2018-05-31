#include <cassert>
#include <cstddef>
#include <queue>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    explicit TreeNode(int x): val(x), left(NULL), right(NULL) {}
};

class Solution {
 public:
    int findBottomLeftValue(TreeNode* root) {
        TreeNode* current = NULL;

        queue<TreeNode*> queue;
        queue.push(root);

        while (!queue.empty()) {
            current = queue.front();
            queue.pop();

            if (current->right) {
                queue.push(current->right);
            }

            if (current->left) {
                queue.push(current->left);
            }
        }

        return current->val;
    }
};

int main() {
    auto solution = Solution();

    auto t0_0 = TreeNode(1);
    auto t0_1 = TreeNode(2);
    auto t0_2 = TreeNode(3);
    auto t0_3 = TreeNode(4);
    auto t0_4 = TreeNode(5);
    auto t0_5 = TreeNode(6);
    auto t0_6 = TreeNode(7);
    t0_4.left = &t0_6;
    t0_2.right = &t0_4;
    t0_2.left = &t0_5;
    t0_1.left = &t0_3;
    t0_0.right = &t0_2;
    t0_0.left = &t0_1;

    assert(7 == solution.findBottomLeftValue(&t0_0));
}
