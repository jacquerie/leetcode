// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int removeDuplicates(vector<int>& nums) {
        int last = -1;

        for (auto num : nums) {
            if (last == -1 || nums[last] != num) {
                nums[++last] = num;
            }
        }

        return last + 1;
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {1, 1, 2};

    assert(2 == solution.removeDuplicates(nums));

    vector<int> expected = {1, 2};
    vector<int> result(nums.begin(), nums.begin() + 2);

    assert(expected == result);
}
