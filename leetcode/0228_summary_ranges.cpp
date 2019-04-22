// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <string>
#include <vector>

using namespace std;

class Solution {
 public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> result;
        if (nums.empty()) {
            return result;
        }

        int first = nums[0], last = nums[0];
        for (int i = 1; i <= nums.size(); i++) {
            if (i < nums.size() && nums[i] - last == 1) {
                last = nums[i];
            } else {
                if (first == last) {
                    result.push_back(to_string(first));
                } else {
                    result.push_back(to_string(first) + "->" + to_string(last));
                }
                first = nums[i];
                last = nums[i];
            }
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {0, 1, 2, 4, 5, 7};

    vector<string> expected = {"0->2", "4->5", "7"};
    vector<string> result = solution.summaryRanges(nums);

    assert(expected == result);
}
