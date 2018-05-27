#include <cassert>
#include <string>

using namespace std;

class Solution {
public:
    string reverseVowels (string s) {
        int i = 0, j = s.size() - 1;

        while (i <= j) {
            if (isNotVowel(s[i])) {
                i++;
            } else if (isNotVowel(s[j])) {
                j--;
            } else {
                swap(s[i++], s[j--]);
            }
        }

        return s;
    }

private:
    const string vowels_ = "AEIOUaeiou";

    bool isNotVowel (char c) {
        return vowels_.find(c) == string::npos;
    }
};

int main () {
    auto solution = Solution();

    assert("holle" == solution.reverseVowels("hello"));
    assert("Aa" == solution.reverseVowels("aA"));
}
