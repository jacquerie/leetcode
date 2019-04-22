// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <string>

using namespace std;

class Solution {
 public:
    int titleToNumber(string s) {
        int result = 0;

        for (auto c : s) {
            result *= 26;
            result += c - 'A' + 1;
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    assert(1 == solution.titleToNumber("A"));
    assert(28 == solution.titleToNumber("AB"));
    assert(701 == solution.titleToNumber("ZY"));
}
