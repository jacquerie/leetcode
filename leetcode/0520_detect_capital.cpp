// Copyright (c) 2019 Jacopo Notarstefano

#include <cassert>
#include <cctype>
#include <string>

using namespace std;

class Solution {
 public:
    bool detectCapitalUse(string word) {
        bool allLower = true, allUpper = true;
        bool firstUpper = true, restLower = true;

        for (int i = 0; i < word.length(); i++) {
            char c = word[i];
            if (islower(c)) {
                if (i == 0) {
                    firstUpper = false;
                }
                allUpper = false;
            } else if (isupper(c)) {
                if (i > 0) {
                    restLower = false;
                }
                allLower = false;
            }
        }

        return allLower || allUpper || (firstUpper && restLower);
    }
};

int main() {
    auto solution = Solution();

    assert(solution.detectCapitalUse("USA"));
    assert(solution.detectCapitalUse("leetcode"));
    assert(solution.detectCapitalUse("Google"));
    assert(!solution.detectCapitalUse("FlaG"));
}
