#include <cassert>
#include <vector>

using namespace std;

class Solution {
public:
    int pivotIndex (vector<int>& nums) {
        int totalSum = 0;
        for (auto num : nums) {
            totalSum += num;
        }

        int leftSum = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (leftSum == totalSum - leftSum - nums[i]) {
                return i;
            }

            leftSum += nums[i];
        }

        return -1;
    }
};

int main () {
    auto solution = Solution();

    vector<int> nums = {1, 7, 3, 6, 5, 6};

    assert(3 == solution.pivotIndex(nums));
}
