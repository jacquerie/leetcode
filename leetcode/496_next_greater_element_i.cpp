// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
        vector<int> result(findNums.size());

        for (int i = 0; i < findNums.size(); i++) {
            result[i] = nextGreaterElementHelper(findNums[i], nums);
        }

        return result;
    }

 private:
    int nextGreaterElementHelper(int findNum, const vector<int>& nums) {
        bool found = false;
        for (auto num : nums) {
            if (found && num > findNum) {
                return num;
            } else if (num == findNum) {
                found = true;
            }
        }

        return -1;
    }
};

int main() {
    auto solution = Solution();

    vector<int> findNums = {4, 1, 2};
    vector<int> nums = {1, 3, 4, 2};

    vector<int> expected = {-1, 3, -1};
    vector<int> result = solution.nextGreaterElement(findNums, nums);

    assert(expected == result);
}
