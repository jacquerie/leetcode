// Copyright (c) 2018 Jacopo Notarstefano

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
            } else if (nums[mid] > target) {
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

    vector<int> nums = {-1, 0, 3, 5, 9, 12};

    assert(4 == solution.search(nums, 9));
    assert(-1 == solution.search(nums, 2));
}
