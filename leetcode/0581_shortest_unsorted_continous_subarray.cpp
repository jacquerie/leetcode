// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <climits>
#include <vector>

using namespace std;

class Solution {
 public:
    int findUnsortedSubarray(vector<int>& nums) {
        int current_max = INT_MIN, violation_max = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > current_max) {
                current_max = nums[i];
            } else if (nums[i] < current_max) {
                violation_max = i;
            }
        }

        int current_min = INT_MAX, violation_min = nums.size() - 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            if (nums[i] < current_min) {
                current_min = nums[i];
            } else if (nums[i] > current_min) {
                violation_min = i;
            }
        }

        if (violation_max == 0 && violation_min == nums.size() - 1) {
            return 0;
        } else {
            return violation_max - violation_min + 1;
        }
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {2, 6, 4, 8, 10, 9, 15};

    assert(5 == solution.findUnsortedSubarray(nums));
}
