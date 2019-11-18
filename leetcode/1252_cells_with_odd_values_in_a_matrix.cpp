// Copyright (c) 2019 Jacopo Notarstefano

#include <cassert>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
 public:
    int oddCells(int n, int m, vector<vector<int>>& indices) {
        unordered_map<int, int> row_counts;
        unordered_map<int, int> col_counts;
        for (const auto& index : indices) {
            row_counts[index[0]]++;
            col_counts[index[1]]++;
        }

        int result = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                result += (row_counts[i] + col_counts[j]) % 2;
            }
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<vector<int>> indices = {{0, 1}, {1, 1}};

    assert(6 == solution.oddCells(2, 3, indices));
}
