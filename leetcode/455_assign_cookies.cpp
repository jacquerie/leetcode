#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        int result = 0;
        if (g.empty() || s.empty()) {
            return result;
        }

        sort(g.begin(), g.end());
        sort(s.begin(), s.end());

        int i = 0, j = 0;
        while (i <= g.size() - 1 && j <= s.size() - 1) {
            if (g[i] > s[j]) {
                j++;
            } else {
                i++;
                j++;
                result++;
            }
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<int> g = {1, 2, 3};
    vector<int> s = {1, 1};

    assert(1 == solution.findContentChildren(g, s));
}
