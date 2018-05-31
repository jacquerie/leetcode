#include <cassert>
#include <string>

using namespace std;

class Solution {
 public:
    bool isSubsequence(string s, string t) {
        if (s.empty()) {
            return true;
        }

        int i = 0, l = s.length();
        for (auto c : t) {
            if (c == s[i]) {
                i++;
                if (i == l) {
                    return true;
                }
            }
        }

        return false;
    }
};

int main() {
    auto solution = Solution();

    assert(solution.isSubsequence("abc", "ahbgdc"));
    assert(!solution.isSubsequence("axc", "ahbgdc"));
    assert(solution.isSubsequence("", "ahbgdc"));
    assert(solution.isSubsequence("a", "ab"));
}
