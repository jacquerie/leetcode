#include <cassert>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int longestPalindrome (string s) {
        unordered_map<char, int> counter;
        for (auto c: s) {
            counter[c]++;
        }

        int odd = 0, result = 0;

        for (auto it: counter) {
            if (it.second % 2) {
                result += it.second - 1;
                odd = 1;
            } else {
                result += it.second;
            }
        }

        return result + odd;
    }
};

int main () {
    auto solution = Solution();

    assert(7 == solution.longestPalindrome("abccccdd"));
}
