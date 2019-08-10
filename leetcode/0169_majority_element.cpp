// Copyright (c) 2019 Jacopo Notarstefano

#include <cassert>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
 public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> counts;
        int majority = nums.size() / 2 + 1;

        for (const auto& num : nums) {
            counts[num]++;
            if (counts[num] >= majority) {
                return num;
            }
        }
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {3, 2, 3};

    assert(3 == solution.majorityElement(nums));
}
