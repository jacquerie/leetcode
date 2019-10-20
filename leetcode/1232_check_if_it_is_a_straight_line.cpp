// Copyright (c) 2019 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int x0 = coordinates[0][0];
        int y0 = coordinates[0][1];
        int x1 = coordinates[1][0];
        int y1 = coordinates[1][1];

        double m = (x1 != x0) ? (y1 - y0) / (x1 - x0) : 0;
        double q = y0 - m * x0;

        return all_of(
            coordinates.cbegin(),
            coordinates.cend(),
            [m, q](const vector<int>& c) {
                return c[1] == m * c[0] + q;
            });
    }
};

int main() {
    auto solution = Solution();

    vector<vector<int>> coordinates = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}};

    assert(solution.checkStraightLine(coordinates));
}
