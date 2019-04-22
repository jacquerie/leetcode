// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <string>

using namespace std;

class Solution {
 public:
    int findLUSlength(string a, string b) {
        if (a == b) {
            return -1;
        } else {
            return max(a.length(), b.length());
        }
    }
};

int main() {
    auto solution = Solution();

    assert(3 == solution.findLUSlength("aba", "cdc"));
}
