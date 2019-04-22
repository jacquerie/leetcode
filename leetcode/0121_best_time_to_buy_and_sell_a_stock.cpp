// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <climits>
#include <vector>

using namespace std;

class Solution {
 public:
    int maxProfit(vector<int>& prices) {
        int minimum_price = INT_MAX, maximum_profit = 0;

        for (auto price : prices) {
            if (price < minimum_price) {
                minimum_price = price;
            }
            if (price - minimum_price > maximum_profit) {
                maximum_profit = price - minimum_price;
            }
        }

        return maximum_profit;
    }
};

int main() {
    auto solution = Solution();

    vector<int> prices = {7, 1, 5, 3, 6, 4};

    assert(5 == solution.maxProfit(prices));
}
