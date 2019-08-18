// Copyright (c) 2019 Jacopo Notarstefano

#include <cassert>
#include <string>
#include <vector>

using namespace std;

class Solution {
 public:
    bool isMatch(string s, string p) {
        vector<vector<bool>> result(s.length() + 1, vector<bool>(p.length() + 1));

        result[0][0] = true;

        for (int j = 1; j <= p.length(); j++) {
            if (p[j - 1] == '*') {
                result[0][j] = result[0][j - 1];
            }
        }

        for (int i = 1; i <= s.length(); i++) {
            for (int j = 1; j <= p.length(); j++) {
                if (p[j - 1] == '*') {
                    result[i][j] = result[i][j - 1] || result[i - 1][j];
                } else {
                    result[i][j] = isCharMatch(s[i - 1], p[j - 1]) && result[i - 1][j - 1];
                }
            }
        }

        return result[s.length()][p.length()];
    }

 private:
    bool isCharMatch(char c, char d) {
        return c == d || d == '?';
    }
};

int main() {
    auto solution = Solution();

    assert(!solution.isMatch("aa", "a"));
    assert(solution.isMatch("aa", "*"));
    assert(!solution.isMatch("cb", "?a"));
    assert(solution.isMatch("adceb", "*a*b"));
    assert(!solution.isMatch("acdcb", "a*c?b"));
}
