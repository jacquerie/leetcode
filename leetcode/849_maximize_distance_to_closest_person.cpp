// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>
#include <climits>
#include <vector>

using namespace std;

class Solution {
 public:
    int maxDistToClosest(vector<int>& seats) {
        vector<int> distances(seats.size(), 0);

        int currentLeftDistance = INT_MAX;
        for (int i = 0; i < seats.size(); i++) {
            if (seats[i] == 1) {
                currentLeftDistance = 0;
            } else if (currentLeftDistance < INT_MAX) {
                currentLeftDistance++;
            }

            distances[i] = currentLeftDistance;
        }

        int currentRightDistance = INT_MAX;
        for (int i = seats.size() - 1; i >= 0; i--) {
            if (seats[i] == 1) {
                currentRightDistance = 0;
            } else if (currentRightDistance < INT_MAX) {
                currentRightDistance++;
            }

            distances[i] = min(distances[i], currentRightDistance);
        }

        return *max_element(distances.begin(), distances.end());
    }
};

int main() {
    auto solution = Solution();

    vector<int> seats = {1, 0, 0, 0, 1, 0, 1};

    assert(1 == solution.maxDistToClosest(seats));
}
