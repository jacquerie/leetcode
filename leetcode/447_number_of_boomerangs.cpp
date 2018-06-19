// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <unordered_map>
#include <utility>
#include <vector>

using namespace std;

class Solution {
 public:
    int numberOfBoomerangs(vector<pair<int, int>>& points) {
        int result = 0;

        for (int i = 0; i < points.size(); i++) {
            unordered_map<int, int> distanceCounts;
            for (int j = 0; j < points.size(); j++) {
                if (i == j) {
                   continue;
                }
                distanceCounts[getSquaredDistance(points[i], points[j])]++;
            }

            for (auto distanceCount : distanceCounts) {
                if (distanceCount.second > 1) {
                    result += distanceCount.second * (distanceCount.second - 1);
                }
            }
        }

        return result;
    }

 private:
    int getSquaredDistance(pair<int, int> p1, pair<int, int> p2) {
        int dx = p1.first - p2.first;
        int dy = p1.second - p2.second;

        return dx * dx + dy * dy;
    }
};

int main() {
    auto solution = Solution();

    vector<pair<int, int>> points = {{0, 0}, {1, 0}, {2, 0}};

    assert(2 == solution.numberOfBoomerangs(points));
}
