#include <cassert>
#include <vector>

using namespace std;

class Solution {
public:
    bool isToeplitzMatrix (vector<vector<int>>& matrix) {
        for (int i = 1; i < matrix.size(); ++i) {
            for (int j = 1; j < matrix[0].size(); ++j) {
                if (matrix[i - 1][j - 1] != matrix[i][j]) {
                    return false;
                }
            }
        }

        return true;
    }
};

int main () {
    auto solution = Solution();

    vector<vector<int>> matrix(3, vector<int>(4, 1));
    matrix[0][0] = 1; matrix[0][1] = 2; matrix[0][2] = 3; matrix[0][3] = 4;
    matrix[1][0] = 5; matrix[1][1] = 1; matrix[1][2] = 2; matrix[1][3] = 3;
    matrix[2][0] = 9; matrix[2][1] = 5; matrix[2][2] = 1; matrix[2][3] = 2;

    assert(solution.isToeplitzMatrix(matrix));
}
