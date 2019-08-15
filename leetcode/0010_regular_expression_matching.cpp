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
                result[0][j] = j > 1 && result[0][j - 2];
            }
        }

        for (int i = 1; i <= s.length(); i++) {
            for (int j = 1; j <= p.length(); j++) {
                if (p[j - 1] == '*') {
                    result[i][j] = (j > 1 && result[i][j - 2]) || (isCharMatch(s[i - 1], p[j - 2]) && result[i - 1][j]);
                } else {
                    result[i][j] = isCharMatch(s[i - 1], p[j - 1]) && result[i - 1][j - 1];
                }
            }
        }

        return result[s.length()][p.length()];
    }

 private:
    bool isCharMatch(char c, char d) {
        return c == d || d == '.';
    }
};

int main() {
    auto solution = Solution();

    assert(!solution.isMatch("aa", "a"));
    assert(solution.isMatch("aa", "a*"));
    assert(solution.isMatch("ab", ".*"));
    assert(solution.isMatch("aab", "c*a*b"));
    assert(!solution.isMatch("mississippi", "mis*is*p*."));
    assert(!solution.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"));
    assert(solution.isMatch("aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s"));
}
