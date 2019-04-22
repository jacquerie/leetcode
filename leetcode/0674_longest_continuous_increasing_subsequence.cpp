// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <climits>
#include <vector>

using namespace std;

class Solution {
 public:
    int findLengthOfLCIS(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        int lastSeen = nums[0];
        int currentLength = 1, maxLength = INT_MIN;

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > lastSeen) {
                currentLength++;
            } else {
                if (currentLength > maxLength) {
                    maxLength = currentLength;
                }
                currentLength = 1;
            }
            lastSeen = nums[i];
        }

        if (currentLength > maxLength) {
            maxLength = currentLength;
        }

        return maxLength;
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {1, 3, 5, 4, 7};

    assert(3 == solution.findLengthOfLCIS(nums));
}
