// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <string>

using namespace std;

class Solution {
 public:
    string reverseString(string s) {
        string result = s;
        reverse(result.begin(), result.end());
        return result;
    }
};

int main() {
    auto solution = Solution();

    assert("olleh" == solution.reverseString("hello"));
}
