// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int arrayPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int result = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (i % 2 == 0) {
                result += nums[i];
            }
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {1, 4, 3, 2};

    assert(4 == solution.arrayPairSum(nums));
}
