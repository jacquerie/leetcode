// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cmath>
#include <vector>

using namespace std;

class Solution {
 public:
    bool escapeGhosts(vector<vector<int>>& ghosts, vector<int>& target) {
        vector<int> origin = {0, 0};

        int distance = computeDistance(origin, target);
        for (auto ghost : ghosts) {
            if (computeDistance(ghost, target) < distance) {
                return false;
            }
        }

        return true;
    }

 private:
    int computeDistance(vector<int>& p, vector<int>& q) {
        return abs(p[0] - q[0]) + abs(p[1] - q[1]);
    }
};

int main() {
    auto solution = Solution();

    vector<vector<int>> ghosts = {{1, 0}, {0, 3}};
    vector<int> target = {0, 1};

    assert(solution.escapeGhosts(ghosts, target));
}
