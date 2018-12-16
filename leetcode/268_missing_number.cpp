// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <numeric>
#include <vector>

using namespace std;

class Solution {
 public:
    int missingNumber(vector<int>& nums) {
        int expected_sum = (nums.size() * (nums.size() + 1)) / 2;
        int actual_sum = accumulate(nums.begin(), nums.end(), 0);

        return expected_sum - actual_sum;
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {3, 0, 1};

    assert(2 == solution.missingNumber(nums));
}
