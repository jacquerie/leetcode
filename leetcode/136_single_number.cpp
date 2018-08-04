// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int singleNumber(vector<int>& nums) {
        int result = 0;

        for (auto num : nums) {
            result ^= num;
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {2, 2, 1};

    assert(1 == solution.singleNumber(nums));
}
