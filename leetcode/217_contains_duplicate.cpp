// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
 public:
    bool containsDuplicate(vector<int> nums) {
        unordered_set<int> seen;
        for (auto num : nums) {
            if (seen.find(num) != seen.end()) {
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {1, 2, 3, 1};

    assert(solution.containsDuplicate(nums));
}
