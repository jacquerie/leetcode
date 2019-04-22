// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <climits>
#include <string>
#include <vector>

using namespace std;

class Solution {
 public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) {
            return "";
        }

        string result;

        int minLength = INT_MAX;
        for (auto str : strs) {
            int length = str.length();
            if (length < minLength) {
                minLength = length;
            }
        }

        for (int j = 0; j < minLength; j++) {
            for (int i = 1; i < strs.size(); i++) {
                if (strs[i][j] != strs[0][j]) {
                    return result;
                }
            }

            result.push_back(strs[0][j]);
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<string> strs = {"flower", "flow", "flight"};

    assert("fl" == solution.longestCommonPrefix(strs));
}
