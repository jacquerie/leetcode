// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <string>

using namespace std;

class Solution {
 public:
    int minAddToMakeValid(string S) {
        int open_count = 0, result = 0;

        for (auto c : S) {
            if (c == ')' && open_count == 0) {
                result += 1;
            } else if (c == ')') {
                open_count -= 1;
            } else {
                open_count += 1;
            }
        }

        return open_count + result;
    }
};

int main() {
    auto solution = Solution();

    assert(1 == solution.minAddToMakeValid("())"));
    assert(3 == solution.minAddToMakeValid("((("));
    assert(0 == solution.minAddToMakeValid("()"));
    assert(4 == solution.minAddToMakeValid("()))(("));
}
