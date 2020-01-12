// Copyright (c) 2020 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    vector<int> decompressRLElist(vector<int>& nums) {
        vector<int> result;

        for (int i = 0; i < nums.size(); i = i + 2) {
            vector<int> partial(nums[i], nums[i + 1]);
            result.insert(result.end(), begin(partial), end(partial));
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {1, 2, 3, 4};

    vector<int> expected = {2, 4, 4, 4};
    vector<int> result = solution.decompressRLElist(nums);

    assert(expected == result);
}
