// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
 public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++) {
            auto it = seen.find(target - nums[i]);
            if (it != seen.end()) {
                return {it->second, i};
            }

            seen[nums[i]] = i;
        }
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {2, 7, 11, 15};

    vector<int> expected = {0, 1};
    vector<int> result = solution.twoSum(nums, 9);

    assert(expected == result);
}
