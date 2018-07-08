// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    vector<vector<int>> transpose(vector<vector<int>>& A) {
        int m = A.size(), n = A[0].size();

        vector<vector<int>> result;
        for (int i = 0; i < n; i++) {
            result.emplace_back(m, 0);
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                result[j][i] = A[i][j];
            }
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<vector<int>> A = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9},
    };

    vector<vector<int>> expected = {
        {1, 4, 7},
        {2, 5, 8},
        {3, 6, 9},
    };
    vector<vector<int>> result = solution.transpose(A);

    assert(expected == result);
}
