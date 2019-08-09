// Copyright (c) 2019 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        vector<int> rowMax(grid.size(), 0);
        vector<int> colMax(grid[0].size(), 0);

        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                rowMax[i] = max(rowMax[i], grid[i][j]);
                colMax[j] = max(colMax[j], grid[i][j]);
            }
        }

        int result = 0;

        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                int localMax = min(rowMax[i], colMax[j]);
                result += localMax - grid[i][j];
            }
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<vector<int>> grid = {
        {3, 0, 8, 4},
        {2, 4, 5, 7},
        {9, 2, 6, 3},
        {0, 3, 1, 0},
    };

    assert(35 == solution.maxIncreaseKeepingSkyline(grid));
}
