// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        if (matrix.empty() || matrix[0].empty()) {
            return result;
        }

        int m = matrix.size(), n = matrix[0].size();

        for (int k = 0; k < m + n - 1; k++) {
            if (k % 2 == 0) {
                for (int i = k; i >= 0; i--) {
                    if (i < m && k - i < n) {
                        result.push_back(matrix[i][k - i]);
                    }
                }
            } else {
                for (int i = 0; i <= k; i++) {
                    if (i < m && k - i < n) {
                        result.push_back(matrix[i][k - i]);
                    }
                }
            }
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<vector<int>> matrix = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9},
    };

    vector<int> expected = {1, 2, 4, 7, 5, 3, 6, 8, 9};
    vector<int> result = solution.findDiagonalOrder(matrix);

    assert(expected == result);
}
