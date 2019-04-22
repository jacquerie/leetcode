// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <string>

using namespace std;

class Solution {
 public:
    int strStr(string haystack, string needle) {
        auto result = haystack.find(needle);
        if (result == string::npos) {
            return -1;
        } else {
            return result;
        }
    }
};

int main() {
    auto solution = Solution();

    assert(2 == solution.strStr("hello", "ll"));
    assert(-1 == solution.strStr("aaaaa", "bba"));
}
