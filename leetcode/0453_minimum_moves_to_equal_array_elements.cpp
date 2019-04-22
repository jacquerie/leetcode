// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <climits>
#include <vector>

using namespace std;

class Solution {
 public:
    int minMoves(vector<int>& nums) {
        int count = 0, min = INT_MAX, sum = 0;

        for (auto num : nums) {
            if (num < min) {
                min = num;
            }

            count++;
            sum = sum + num;
        }

        return sum - count * min;
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {1, 2, 3};

    assert(3 == solution.minMoves(nums));
}
