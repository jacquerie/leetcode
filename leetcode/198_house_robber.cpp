// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int rob(vector<int>& nums) {
        int current = 0, previous = 0;

        for (auto num : nums) {
            int tmp = current;
            current = max(current, previous + num);
            previous = tmp;
        }

        return current;
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {1, 2, 3, 1};

    assert(4 == solution.rob(nums));
}
