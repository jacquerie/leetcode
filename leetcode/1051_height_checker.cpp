// Copyright (c) 2019 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int heightChecker(vector<int>& heights) {
        vector<int> sortedHeights(heights.begin(), heights.end());
        sort(sortedHeights.begin(), sortedHeights.end());

        int result = 0;

        for (int i = 0; i < heights.size(); i++) {
            if (heights[i] != sortedHeights[i]) {
                result++;
            }
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<int> heights = {1, 1, 4, 2, 1, 3};

    assert(3 == solution.heightChecker(heights));
}
