// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <string>
#include <vector>

using namespace std;

class Solution {
 public:
    vector<vector<string>> solveNQueens(int n) {
        vector<int> positions(n);
        vector<vector<int>> solutions;
        solveNQueensHelper(n, positions, solutions, 0);

        vector<vector<string>> result;
        for (auto solution : solutions) {
            result.push_back(solutionToBoard(n, solution));
        }
        return result;
    }

 private:
    void solveNQueensHelper(int n, vector<int>& positions, vector<vector<int>>& solutions, int i) {
        if (i == n) {
            if (isValid(n, positions)) {
                solutions.push_back(positions);
            }
        } else {
            for (int j = 0; j < n; j++) {
                positions[i] = j;
                if (isValid(i, positions)) {
                    solveNQueensHelper(n, positions, solutions, i + 1);
                }
            }
        }
    }

    vector<string> solutionToBoard(int n, vector<int>& solution) {
        vector<string> result;

        for (auto el : solution) {
            string row(n, '.');
            row[el] = 'Q';
            result.push_back(row);
        }

        return result;
    }

    bool isValid(int n, vector<int>& positions) {
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (positions[i] == positions[j]) {
                    return false;
                } else if (positions[i] - positions[j] == i - j) {
                    return false;
                } else if (positions[i] - positions[j] == j - i) {
                    return false;
                }
            }
        }

        return true;
    }
};

int main() {
    auto solution = Solution();

    vector<vector<string>> expected = {
        {
            ".Q..",
            "...Q",
            "Q...",
            "..Q.",
        },
        {
            "..Q.",
            "Q...",
            "...Q",
            ".Q..",
        },
    };
    vector<vector<string>> result = solution.solveNQueens(4);

    assert(expected == result);
}
