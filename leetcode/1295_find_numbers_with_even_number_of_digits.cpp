// Copyright (c) 2020 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int findNumbers(vector<int>& nums) {
        return count_if(nums.begin(), nums.end(), evenDigits);
    }

 private:
    static bool evenDigits(int num) {
        return (10 <= num && num < 100) || (1000 <= num && num < 10000);
    }
};

int main() {
    auto solution = Solution();

    vector<int> nums = {12, 345, 2, 6, 7896};

    assert(2 == solution.findNumbers(nums));
}
