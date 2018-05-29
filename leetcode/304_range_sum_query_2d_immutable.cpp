#include <cassert>
#include <vector>

using namespace std;

class NumMatrix {
public:
    NumMatrix (vector<vector<int>> matrix) {
        if (matrix.empty()) {
            return;
        }

        int num_rows = matrix.size(), num_cols = matrix[0].size();

        for (int i = 0; i <= num_rows; i++) {
            sums_.emplace_back(num_cols + 1, 0);
        }

        for (int i = 1; i <= num_rows; i++) {
            for (int j = 1; j <= num_cols; j++) {
                sums_[i][j] = matrix[i - 1][j - 1] + sums_[i - 1][j] + sums_[i][j - 1] - sums_[i - 1][j - 1];
            }
        }
    }

    int sumRegion (int row1, int col1, int row2, int col2) {
        return sums_[row2 + 1][col2 + 1] - sums_[row2 + 1][col1] - sums_[row1][col2 + 1] + sums_[row1][col1];
    }

private:
    vector<vector<int>> sums_;
};

int main () {
    vector<vector<int>> matrix = {
        {3, 0, 1, 4, 2},
        {5, 6, 3, 2, 1},
        {1, 2, 0, 1, 5},
        {4, 1, 0, 1, 7},
        {1, 0, 3, 0, 5},
    };

    auto obj = NumMatrix(matrix);

    assert(8 == obj.sumRegion(2, 1, 4, 3));
    assert(11 == obj.sumRegion(1, 1, 2, 2));
    assert(12 == obj.sumRegion(1, 2, 2, 4));
}
