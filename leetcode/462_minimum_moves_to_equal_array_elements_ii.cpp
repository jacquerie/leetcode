#include <algorithm>
#include <cassert>
#include <cmath>
#include <vector>

using namespace std;

class Solution {
public:
    int minMoves2 (vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int median = nums[nums.size() / 2], result = 0;

        for (auto num: nums) {
            result += abs(num - median);
        }

        return result;
    }
};

int main () {
    auto solution = Solution();

    vector<int> nums = {1, 2, 3};

    assert(2 == solution.minMoves2(nums));
}
