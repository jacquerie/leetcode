// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int arrayNesting(vector<int>& nums) {
        int result = 0;

        for (auto num : nums) {
            if (num == -1) {
                continue;
            }
            int current = num, length = 0;
            while (nums[current] != -1) {
                int previous = current;
                current = nums[current];
                nums[previous] = -1;
                length++;
            }
            result = max(result, length);
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {5, 4, 0, 3, 1, 6, 2};

    assert(4 == solution.arrayNesting(nums));
}
