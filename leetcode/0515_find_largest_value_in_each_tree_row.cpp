// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <climits>
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
    vector<int> largestValues(TreeNode* root) {
        vector<int> result;
        if (!root) {
            return result;
        }

        vector<TreeNode*> current, next;
        current.push_back(root);

        while (!current.empty()) {
            int current_maximum = INT_MIN;
            next.clear();

            for (auto node : current) {
                current_maximum = max(current_maximum, node->val);

                if (node->right) {
                    next.push_back(node->right);
                }

                if (node->left) {
                    next.push_back(node->left);
                }
            }

            result.push_back(current_maximum);
            swap(current, next);
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    auto t0_0 = TreeNode(1);
    auto t0_1 = TreeNode(3);
    auto t0_2 = TreeNode(2);
    auto t0_3 = TreeNode(5);
    auto t0_4 = TreeNode(3);
    auto t0_5 = TreeNode(9);
    t0_2.right = &t0_5;
    t0_1.right = &t0_4;
    t0_1.left = &t0_3;
    t0_0.right = &t0_1;
    t0_0.left = &t0_2;

    vector<int> expected = {1, 3, 9};
    vector<int> result = solution.largestValues(&t0_0);

    assert(expected == result);
}
