// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cctype>
#include <string>

using namespace std;

class Solution {
 public:
    bool isPalindrome(string s) {
        int i = 0, j = s.length() - 1;

        while (i < j) {
            if (!isalnum(s[i])) {
                i++;
            } else if (!isalnum(s[j])) {
                j--;
            } else if (tolower(s[i]) == tolower(s[j])) {
                i++;
                j--;
            } else {
                return false;
            }
        }

        return true;
    }
};

int main() {
    auto solution = Solution();

    assert(solution.isPalindrome("A man, a plan, a canal: Panama"));
    assert(!solution.isPalindrome("race a car"));
    assert(!solution.isPalindrome("0P"));
}
