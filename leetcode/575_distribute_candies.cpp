// Copyright (c) 2019 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
 public:
    int distributeCandies(vector<int>& candies) {
        unordered_set<int> candiesSet(candies.begin(), candies.end());
        return min(candies.size() / 2, candiesSet.size());
    }
};

int main() {
    auto solution = Solution();

    vector<int> candies = {1, 1, 2, 2, 3, 3};

    assert(3 == solution.distributeCandies(candies));
}
