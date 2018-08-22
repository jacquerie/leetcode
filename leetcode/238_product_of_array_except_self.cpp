// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    vector<int> productExceptSelf(vector<int> nums) {
        vector<int> result(nums.size(), 1);

        int previous = 1;
        for (int i = 0; i < nums.size() - 1; i++) {
            result[i + 1] = previous * nums[i];
            previous *= nums[i];
        }

        previous = 1;
        for (int i = nums.size() - 1; i > 0; i--) {
            result[i - 1] *= previous * nums[i];
            previous *= nums[i];
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {1, 2, 3, 4};

    vector<int> expected = {24, 12, 8, 6};
    vector<int> result = solution.productExceptSelf(nums);

    assert(expected == result);
}
