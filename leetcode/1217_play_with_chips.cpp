// Copyright (c) 2019 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int minCostToMoveChips(vector<int>& chips) {
        int count_even = 0, count_odd = 0;
        for (const auto& chip : chips) {
            if (chip % 2 == 0) {
                count_even++;
            } else {
                count_odd++;
            }
        }

        return min(count_even, count_odd);
    }
};

int main() {
    auto solution = Solution();

    vector<int> chips = {1, 2, 3};

    assert(1 == solution.minCostToMoveChips(chips));
}
