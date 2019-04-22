// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <map>
#include <utility>
#include <vector>

using namespace std;

class Solution {
 public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        map<int, int> lengths;
        for (auto num : nums) {
            lengths[num] = 0;
        }

        for (auto num : nums) {
            auto it = lengths.find(num);
            if (it->second == 0) {
                it->second = 1;

                int left;
                auto leftIt = lengths.find(num - 1);
                if (leftIt == lengths.end()) {
                    left = 0;
                } else {
                    left = leftIt->second;
                }

                int right;
                auto rightIt = lengths.find(num + 1);
                if (rightIt == lengths.end()) {
                    right = 0;
                } else {
                    right = rightIt->second;
                }

                int length = 1 + left + right;
                lengths[num - left] = length;
                lengths[num + right] = length;
            }
        }

        auto it = max_element(
            lengths.begin(), lengths.end(),
            [] (pair<int, int> p, pair<int, int> q) {
                return p.second < q.second;
            });
        return it->second;
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {100, 4, 200, 1, 3, 2};

    assert(4 == solution.longestConsecutive(nums));
}
