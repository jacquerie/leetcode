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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && !q) {
            return true;
        } else if (!p || !q) {
            return false;
        } else {
            return p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        }
    }
};

int main() {
    auto solution = Solution();

    auto t0_0 = TreeNode(1);
    auto t0_1 = TreeNode(2);
    auto t0_2 = TreeNode(3);
    t0_0.right = &t0_2;
    t0_0.left = &t0_1;

    auto t1_0 = TreeNode(1);
    auto t1_1 = TreeNode(2);
    auto t1_2 = TreeNode(3);
    t1_0.right = &t1_2;
    t1_0.left = &t1_1;

    assert(solution.isSameTree(&t0_0, &t1_0));
}
