// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <string>

using namespace std;

class Solution {
 public:
    int scoreOfParentheses(string S) {
        int current_depth = 0, result = 0;

        for (int i = 0; i < S.length(); i++) {
            if (S[i] == '(') {
                current_depth++;
            } else {
                current_depth--;
                if (S[i - 1] == '(') {
                    result += 1 << current_depth;
                }
            }
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    assert(1 == solution.scoreOfParentheses("()"));
    assert(2 == solution.scoreOfParentheses("(())"));
    assert(2 == solution.scoreOfParentheses("()()"));
    assert(6 == solution.scoreOfParentheses("(()(()))"));
}
