// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    vector<int> searchRange(vector<int>& nums, int target) {
        auto first = lower_bound(nums.begin(), nums.end(), target);
        auto last = upper_bound(nums.begin(), nums.end(), target);

        if (first != nums.end() && *first == target) {
            return {
              static_cast<int>(first - nums.begin()),
              static_cast<int>(last - nums.begin() - 1),
            };
        } else {
            return {-1, -1};
        }
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {5, 7, 7, 8, 8, 10};

    vector<int> expected = {3, 4};
    vector<int> result = solution.searchRange(nums, 8);

    assert(expected == result);
}
