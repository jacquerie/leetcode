// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int smallestRangeI(vector<int>& A, int K) {
        auto minmax = minmax_element(A.begin(), A.end());
        return max((*minmax.second - K) - (*minmax.first + K), 0);
    }
};

int main() {
    auto solution = Solution();

    vector<int> A = {1};

    assert(0 == solution.smallestRangeI(A, 0));
}
