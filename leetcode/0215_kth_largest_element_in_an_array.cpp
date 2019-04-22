// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <functional>
#include <vector>

using namespace std;

class Solution {
 public:
    int findKthLargest(vector<int>& nums, int k) {
        nth_element(nums.begin(), nums.begin() + k - 1, nums.end(), greater<int>());
        return nums[k - 1];
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {3, 2, 1, 5, 6, 4};

    assert(5 == solution.findKthLargest(nums, 2));
}
