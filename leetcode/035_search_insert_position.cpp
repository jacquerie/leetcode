// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int searchInsert(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] >= target) {
                return i;
            }
        }

        return nums.size();
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {1, 3, 5, 6};

    assert(2 == solution.searchInsert(nums, 5));
    assert(1 == solution.searchInsert(nums, 2));
    assert(4 == solution.searchInsert(nums, 7));
    assert(0 == solution.searchInsert(nums, 0));
}
