#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
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

int main() {
    auto solution = Solution();

    vector<vector<int>> matrix = {
        {1, 2, 3, 4},
        {5, 1, 2, 3},
        {9, 5, 1, 2},
    };

    assert(solution.isToeplitzMatrix(matrix));
}
