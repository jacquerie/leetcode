// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <climits>
#include <cstddef>
#include <cstdint>
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
    int maxLevelSum(TreeNode* root) {
        int64_t current_max = INT_MIN;
        int current_index = 0, result;

        vector<TreeNode*> current, next;
        current.push_back(root);

        while (!current.empty()) {
            int64_t current_sum = 0;
            next.clear();

            for (auto node : current) {
                current_sum += node->val;

                if (node->right) {
                    next.push_back(node->right);
                }

                if (node->left) {
                    next.push_back(node->left);
                }
            }

            current_index++;
            if (current_sum > current_max) {
                current_max = current_sum;
                result = current_index;
            }
            swap(current, next);
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    auto t0_0 = TreeNode(1);
    auto t0_1 = TreeNode(7);
    auto t0_2 = TreeNode(0);
    auto t0_3 = TreeNode(7);
    auto t0_4 = TreeNode(-8);
    t0_2.right = &t0_4;
    t0_2.left = &t0_3;
    t0_0.right = &t0_1;
    t0_0.left = &t0_2;

    assert(2 == solution.maxLevelSum(&t0_0));
}
