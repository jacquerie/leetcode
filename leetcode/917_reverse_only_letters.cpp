// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cctype>
#include <string>

using namespace std;

class Solution {
 public:
    string reverseOnlyLetters(string S) {
        int i = 0, j = S.length() - 1;
        while (i <= j) {
            if (!isalpha(S[i])) {
                i++;
            } else if (!isalpha(S[j])) {
                j--;
            } else {
                swap(S[i++], S[j--]);
            }
        }

        return S;
    }
};

int main() {
    auto solution = Solution();

    assert("dc-ba" == solution.reverseOnlyLetters("ab-cd"));
    assert("j-Ih-gfE-dCba" == solution.reverseOnlyLetters("a-bC-dEf-ghIj"));
    assert("Qedo1ct-eeLg=ntse-T!" == solution.reverseOnlyLetters("Test1ng-Leet=code-Q!"));
}
