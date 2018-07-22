// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int findTargetSumWays(vector<int>& nums, int S) {
        return findTargetSumWaysHelper(nums, S, 0, 0);
    }

 private:
    int findTargetSumWaysHelper(vector<int>& nums, int S, int s, int i) {
        if (i == nums.size()) {
            return s == S ? 1 : 0;
        } else {
            return findTargetSumWaysHelper(nums, S, s + nums[i], i + 1) +
                findTargetSumWaysHelper(nums, S, s - nums[i], i + 1);
        }
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {1, 1, 1, 1, 1};

    assert(5 == solution.findTargetSumWays(nums, 3));
}
