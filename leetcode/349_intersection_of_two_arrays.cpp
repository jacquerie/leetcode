// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <set>
#include <vector>

using namespace std;

class Solution {
 public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> result;

        set<int> nums1_set(nums1.begin(), nums1.end());
        set<int> nums2_set(nums2.begin(), nums2.end());
        set_intersection(
            nums1_set.begin(), nums1_set.end(),
            nums2_set.begin(), nums2_set.end(),
            back_inserter(result));

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums1 = {1, 2, 2, 1};
    vector<int> nums2 = {2, 2};

    vector<int> expected = {2};
    vector<int> result = solution.intersection(nums1, nums2);

    assert(expected == result);
}
