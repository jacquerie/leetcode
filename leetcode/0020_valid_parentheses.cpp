// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <stack>
#include <string>

using namespace std;

class Solution {
 public:
    int isValid(string s) {
        stack<char> stack;

        for (auto c : s) {
            if (c == '(') {
                stack.push(')');
            } else if (c == '[') {
                stack.push(']');
            } else if (c == '{') {
                stack.push('}');
            } else if (stack.empty()) {
                return false;
            } else {
                char top = stack.top();
                stack.pop();

                if (top != c) {
                    return false;
                }
            }
        }

        return stack.size() == 0;
    }
};

int main() {
    auto solution = Solution();

    assert(solution.isValid("()"));
    assert(solution.isValid("()[]{}"));
    assert(!solution.isValid("(]"));
    assert(!solution.isValid("([)]"));
    assert(solution.isValid("{[]}"));
    assert(!solution.isValid("]"));
    assert(!solution.isValid("["));
}
