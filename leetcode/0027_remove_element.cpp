// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int removeElement(vector<int>& nums, int val) {
        int last = -1;

        for (auto num : nums) {
            if (num != val) {
                nums[++last] = num;
            }
        }

        return last + 1;
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {3, 2, 2, 3};

    assert(2 == solution.removeElement(nums, 3));

    vector<int> expected = {2, 2};
    vector<int> result(nums.begin(), nums.begin() + 2);

    assert(expected == result);
}
