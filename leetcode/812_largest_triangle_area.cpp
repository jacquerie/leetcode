// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cmath>
#include <vector>

using namespace std;

class Solution {
 public:
    double largestTriangleArea(vector<vector<int>>& points) {
        double result = 0;

        for (int i = 0; i < points.size() - 2; i++) {
            for (int j = i + 1; j < points.size() - 1; j++) {
                for (int k = j + 1; k < points.size(); k++) {
                    double x_a = points[i][0], y_a = points[i][1];
                    double x_b = points[j][0], y_b = points[j][1];
                    double x_c = points[k][0], y_c = points[k][1];
                    double area = abs((x_a - x_c) * (y_b - y_a) - (x_a - x_b) * (y_c - y_a)) / 2;
                    if (area > result) {
                        result = area;
                    }
                }
            }
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    vector<vector<int>> points = {{0, 0}, {0, 1}, {1, 0}, {0, 2}, {2, 0}};

    assert(2 == solution.largestTriangleArea(points));
}
