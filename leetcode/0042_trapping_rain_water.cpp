// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int trap(vector<int>& height) {
        vector<int> tallestLeft(height.size(), 0);
        for (int i = 0; i < height.size(); i++) {
            tallestLeft[i] = max(height[i], ((i != 0) ? tallestLeft[i - 1] : 0));
        }

        vector<int> tallestRight(height.size(), 0);
        for (int i = height.size() - 1; i >=0; i--) {
            tallestRight[i] = max(height[i], ((i != height.size() - 1) ? tallestRight[i + 1] : 0));
        }

        int result = 0;

        for (int i = 0; i < height.size(); i++) {
            result += min(tallestLeft[i], tallestRight[i]) - height[i];
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<int> height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};

    assert(6 == solution.trap(height));
}
