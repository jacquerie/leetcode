// Copyright (c) 2019 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
 public:
    int maxNumberOfBalloons(string text) {
        unordered_map<char, int> counts;
        for (const auto& c : text) {
            counts[c]++;
        }

        return min({
            counts['b'],
            counts['a'],
            counts['l'] / 2,
            counts['o'] / 2,
            counts['n']
        });
    }
};

int main() {
    auto solution = Solution();

    assert(1 == solution.maxNumberOfBalloons("nlaebolko"));
    assert(2 == solution.maxNumberOfBalloons("loonbalxballpoon"));
    assert(0 == solution.maxNumberOfBalloons("leetcode"));
}
