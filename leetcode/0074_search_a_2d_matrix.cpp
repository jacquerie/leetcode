// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) {
            return false;
        }

        int m = matrix.size(), n = matrix[0].size();
        int mid, first = 0, last = m * n - 1;

        while (first <= last) {
            mid = first + (last - first) / 2;
            if (matrix[mid / n][mid % n] == target) {
                return true;
            } else if (matrix[mid / n][mid % n] > target) {
                last = mid - 1;
            } else {
                first = mid + 1;
            }
        }

        return false;
    }
};

int main() {
    auto solution = Solution();

    vector<vector<int>> matrix = {
        {1, 3, 5, 7},
        {10, 11, 16, 20},
        {23, 30, 34, 50},
    };

    assert(solution.searchMatrix(matrix, 3));
    assert(!solution.searchMatrix(matrix, 13));
}
