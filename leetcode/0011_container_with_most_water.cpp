// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int maxArea(vector<int>& height) {
        int i = 0, j = height.size() - 1, result = 0;

        while (i < j) {
            result = max(result, min(height[i], height[j]) * (j - i));

            if (height[i] > height[j]) {
                j--;
            } else if (height[i] < height[j]) {
                i++;
            } else {
                i++;
                j--;
            }
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<int> height = {5, 3, 4, 1, 2};

    assert(8 == solution.maxArea(height));
}
