#include <algorithm>
#include <cassert>
#include <climits>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string customSortString (string S, string T) {
        vector<int> order(256, INT_MAX);
        for (size_t i = 0; i < S.length(); i++) {
            order[S[i]] = i;
        }

        sort(T.begin(), T.end(), [&order] (char x, char y) {
            return order[x] < order[y];
        });
        return T;
    }
};

int main () {
    auto solution = Solution();

    assert("cbad" == solution.customSortString("cba", "abcd"));
    assert("eexvw" == solution.customSortString("exv", "xwvee"));
}
