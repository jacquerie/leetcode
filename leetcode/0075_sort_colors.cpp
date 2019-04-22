// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    void sortColors(vector<int>& nums) {
        int i = 0, j = 0, n = nums.size() - 1;

        while (j <= n) {
            if (nums[j] == 0) {
                swap(nums[i++], nums[j++]);
            } else if (nums[j] == 1) {
                j++;
            } else if (nums[j] == 2) {
                swap(nums[j], nums[n--]);
            }
        }
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {2, 0, 2, 1, 1, 0};

    vector<int> expected = {0, 0, 1, 1, 2, 2};
    solution.sortColors(nums);
    assert(expected == nums);
}
