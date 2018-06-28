// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int maxProfit(vector<int>& prices) {
        int result = 0;
        if (prices.empty()) {
            return result;
        }

        for (int i = 0; i < prices.size() - 1; i++) {
            result += max(0, prices[i + 1] - prices[i]);
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<int> prices = {7, 1, 5, 3, 6, 4};

    assert(7 == solution.maxProfit(prices));
}
