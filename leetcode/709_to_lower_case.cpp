// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cctype>
#include <string>

using namespace std;

class Solution {
 public:
    string toLowerCase(string str) {
        string result;
        if (!str.length()) {
            return result;
        }

        for (auto c : str) {
            result.push_back(tolower(c));
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    assert("foobar" == solution.toLowerCase("fooBAR"));
}
