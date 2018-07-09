// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int matrixScore(vector<vector<int>>& A) {
        int m = A.size(), n = A[0].size();

        for (int i = 0; i < m; i++) {
            if (!A[i][0]) {
                for (int j = 0; j < n; j++) {
                    A[i][j] ^= 1;
                }
            }
        }

        for (int j = 0; j < n; j++) {
            int count = 0;
            for (int i = 0; i < m; i++) {
                count += A[i][j];
            }

            if (count <= m / 2) {
                for (int i = 0; i < m; i++) {
                    A[i][j] ^= 1;
                }
            }
        }

        int result = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                result += A[i][j] << (n - j - 1);
            }
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<vector<int>> A = {
        {0, 0, 1, 1},
        {1, 0, 1, 0},
        {1, 1, 0, 0},
    };

    assert(39 == solution.matrixScore(A));
}
