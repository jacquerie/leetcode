// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <string>
#include <vector>

using namespace std;

class Solution {
 public:
    bool checkInclusion(string s1, string s2) {
        if (s2.length() < s1.length()) {
            return false;
        }

        vector<int> counts(26);
        for (auto c : s1) {
            ++counts[c - 'a'];
        }
        for (int i = 0; i < s1.length(); ++i) {
            --counts[s2[i] - 'a'];
        }

        for (int i = s1.length(); i < s2.length(); ++i) {
            if (all_of(counts.begin(), counts.end(), [](int count) { return count == 0; })) {
                return true;
            }

            --counts[s2[i] - 'a'];
            ++counts[s2[i - s1.length()] - 'a'];
        }
        if (all_of(counts.begin(), counts.end(), [](int count) { return count == 0; })) {
            return true;
        }

        return false;
    }
};

int main() {
    auto solution = Solution();

    assert(solution.checkInclusion("ab", "eidbaooo"));
    assert(!solution.checkInclusion("ab", "eidboaoo"));
}
