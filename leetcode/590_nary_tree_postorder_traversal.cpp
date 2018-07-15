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
    vector<int> postorder(Node* root) {
        vector<int> result;
        if (!root) {
            return result;
        }

        postorderHelper(root, result);

        return result;
    }

 private:
    void postorderHelper(Node* root, vector<int>& result) {
        for (auto child : root->children) {
            postorderHelper(child, result);
        }

        result.push_back(root->val);
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

    vector<int> expected = {5, 6, 3, 2, 4, 1};
    vector<int> result = solution.postorder(&t0_0);

    assert(expected == result);
}
