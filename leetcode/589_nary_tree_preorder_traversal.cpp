// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Node {
 public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};

class Solution {
 public:
    vector<int> preorder(Node* root) {
        vector<int> result;
        if (!root) {
            return result;
        }

        preorderHelper(root, result);

        return result;
    }

 private:
    void preorderHelper(Node* root, vector<int>& result) {
        result.push_back(root->val);

        for (auto child : root->children) {
            preorderHelper(child, result);
        }
    }
};

int main() {
    auto solution = Solution();

    auto t0_4 = Node(5, {});
    auto t0_5 = Node(6, {});
    auto t0_1 = Node(3, {&t0_4, &t0_5});
    auto t0_2 = Node(2, {});
    auto t0_3 = Node(4, {});
    auto t0_0 = Node(1, {&t0_1, &t0_2, &t0_3});

    vector<int> expected = {1, 3, 5, 6, 2, 4};
    vector<int> result = solution.preorder(&t0_0);

    assert(expected == result);
}
