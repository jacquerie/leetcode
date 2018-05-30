#include <algorithm>
#include <cassert>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> result;
        if (s.length() < p.length()) {
            return result;
        }

        vector<int> counts(26);
        for (auto c : p) {
            ++counts[c - 'a'];
        }
        for (int i = 0; i < p.length(); ++i) {
            --counts[s[i] - 'a'];
        }

        for (int i = p.length(); i < s.length(); ++i) {
            if (all_of(counts.begin(), counts.end(), [](int count) { return count == 0; })) {
                result.emplace_back(i - p.length());
            }

            --counts[s[i] - 'a'];
            ++counts[s[i - p.length()] - 'a'];
        }
        if (all_of(counts.begin(), counts.end(), [](int count) { return count == 0; })) {
            result.emplace_back(s.length() - p.length());
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<int> expected = {0, 6};
    vector<int> result = solution.findAnagrams("cbaebabacd", "abc");

    assert(expected == result);
}
