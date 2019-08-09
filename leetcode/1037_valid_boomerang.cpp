// Copyright (c) 2019 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    bool isBoomerang(vector<vector<int>>& points) {
        int x1 = points[0][0], y1 = points[0][1];
        int x2 = points[1][0], y2 = points[1][1];
        int x3 = points[2][0], y3 = points[2][1];

        return (x3 - x1) * (y2 - y1) != (y3 - y1) * (x2 - x1);
    }
};

int main() {
    auto solution = Solution();

    vector<vector<int>> points = {
        {1, 1},
        {2, 3},
        {3, 2},
    };

    assert(solution.isBoomerang(points));
}
