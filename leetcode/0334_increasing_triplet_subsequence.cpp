// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <climits>
#include <vector>

using namespace std;

class Solution {
 public:
    bool increasingTriplet(vector<int>& nums) {
        int min = INT_MAX, x = INT_MAX, y = INT_MAX;

        for (auto num : nums) {
            if (num <= min) {
                min = num;
            } else if (num <= y) {
                x = min;
                y = num;
            } else {
                return true;
            }
        }

        return false;
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {1, 2, 3, 4, 5};

    assert(solution.increasingTriplet(nums));
}
