// Copyright (c) 2019 Jacopo Notarstefano

#include <cassert>
#include <string>

using namespace std;

class Solution {
 public:
    int balancedStringSplit(string s) {
        int r_count = 0, result = 0;

        for (const auto& c : s) {
            c == 'R' ? r_count++ : r_count--;
            if (r_count == 0) {
                result++;
            }
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    assert(4 == solution.balancedStringSplit("RLRRLLRLRL"));
    assert(3 == solution.balancedStringSplit("RLLLLRRRLR"));
    assert(1 == solution.balancedStringSplit("LLLLRRRR"));
}
