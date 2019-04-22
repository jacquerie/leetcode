// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
 public:
    int lengthOfLongestSubstring(string s) {
        int current_first = 0, result = 0;
        unordered_map<char, int> lastSeen;

        for (int i = 0; i < s.length(); i++) {
            auto it = lastSeen.find(s[i]);
            if (it == lastSeen.end()) {
                lastSeen[s[i]] = i;
            } else {
                if (it->second >= current_first) {
                    result = max(result, i - current_first);
                    current_first = it->second + 1;
                }
                it->second = i;
            }
        }

        return max(result, static_cast<int>(s.size()) - current_first);
    }
};

int main() {
    auto solution = Solution();

    assert(3 == solution.lengthOfLongestSubstring("abcabcbb"));
    assert(1 == solution.lengthOfLongestSubstring("bbbbb"));
    assert(3 == solution.lengthOfLongestSubstring("pwwkew"));
    assert(2 == solution.lengthOfLongestSubstring("aab"));
    assert(3 == solution.lengthOfLongestSubstring("dvdf"));
}
