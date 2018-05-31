#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int totalHammingDistance(vector<int>& nums) {
        int result = 0, n = nums.size();

        for (int i = 0; i < 32; i++) {
            int k = 0;
            for (int j = 0; j < n; j++) {
                k += (nums[j] >> i) & 1;
            }
            result += (n - k) * k;
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {4, 14, 2};

    int expected = 6;
    int result = solution.totalHammingDistance(nums);

    assert(expected == result);
}
