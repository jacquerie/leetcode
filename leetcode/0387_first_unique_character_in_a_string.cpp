// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
 public:
    int firstUniqChar(string s) {
        unordered_map<char, int> counts;
        for (char c : s) {
            counts[c]++;
        }

        for (int i = 0; i < s.length(); i++) {
            if (counts[s[i]] == 1) {
                return i;
            }
        }

        return -1;
    }
};

int main() {
    auto solution = Solution();

    assert(0 == solution.firstUniqChar("leetcode"));
    assert(2 == solution.firstUniqChar("loveleetcode"));
    assert(-1 == solution.firstUniqChar(""));
}
