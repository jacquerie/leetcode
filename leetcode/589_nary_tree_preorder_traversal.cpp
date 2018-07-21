// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>

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
    int maxDepth(Node* root) {
        if (!root) {
            return 0;
        } else {
            int result = 0;
            for (auto child : root->children) {
                result = max(result, maxDepth(child));
            }
            return 1 + result;
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

    assert(3 == solution.maxDepth(&t0_0));
}
