// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> result;
        if (!root) {
            return result;
        }

        vector<TreeNode*> current, next;
        current.push_back(root);

        while (!current.empty()) {
            int current_count = 0;
            int64_t current_sum = 0;
            next.clear();

            for (auto node : current) {
                current_count++;
                current_sum += node->val;

                if (node->right) {
                    next.push_back(node->right);
                }

                if (node->left) {
                    next.push_back(node->left);
                }
            }

            result.push_back(static_cast<double>(current_sum) / current_count);
            swap(current, next);
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    auto t0_0 = TreeNode(3);
    auto t0_1 = TreeNode(9);
    auto t0_2 = TreeNode(20);
    auto t0_3 = TreeNode(15);
    auto t0_4 = TreeNode(7);
    t0_2.right = &t0_4;
    t0_2.left = &t0_3;
    t0_0.right = &t0_1;
    t0_0.left = &t0_2;

    vector<double> expected = {3, 14.5, 11};
    vector<double> result = solution.averageOfLevels(&t0_0);

    assert(expected == result);
}
