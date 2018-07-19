// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    int totalNQueens(int n) {
        vector<int> positions(n);
        return totalNQueensHelper(n, positions, 0);
    }

 private:
    int totalNQueensHelper(int n, vector<int>& positions, int i) {
        if (i == n) {
            return isValid(n, positions) ? 1 : 0;
        } else {
            int result = 0;
            for (int j = 0; j < n; j++) {
                positions[i] = j;
                if (isValid(i, positions)) {
                    result += totalNQueensHelper(n, positions, i + 1);
                }
            }
            return result;
        }
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

    assert(2 == solution.totalNQueens(4));
    assert(352 == solution.totalNQueens(9));
}
