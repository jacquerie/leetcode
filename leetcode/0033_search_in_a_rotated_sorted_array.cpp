// Copyright (c) 2019 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int search(vector<int>& nums, int target) {
        int mid, first = 0, last = nums.size() - 1;

        while (first <= last) {
            mid = first + (last - first) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if ((nums[first] <= nums[mid] && nums[first] <= target && target < nums[mid]) ||
                       (nums[first] > nums[mid] && !(nums[mid] < target && target <= nums[last]))) {
                last = mid - 1;
            } else {
                first = mid + 1;
            }
        }

        return -1;
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {4, 5, 6, 7, 0, 1, 2};

    assert(4 == solution.search(nums, 0));
    assert(-1 == solution.search(nums, 3));
}
