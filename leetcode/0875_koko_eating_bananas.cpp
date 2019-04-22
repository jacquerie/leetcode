// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cstdint>
#include <vector>

using namespace std;

class Solution {
 public:
    int minEatingSpeed(vector<int>& piles, int H) {
        int speed = 1;

        while (true) {
            int64_t timeSpent = timeSpentWithGivenSpeed(piles, speed);

            if (timeSpent <= H) {
                break;
            } else {
                speed *= 2;
            }
        }

        if (speed == 1) {
            return 1;
        }

        int mid, first = speed / 2, last = speed;

        while (first <= last) {
            mid = first + (last - first) / 2;
            int64_t timeSpent = timeSpentWithGivenSpeed(piles, mid);

            if (timeSpent <= H) {
                last = mid - 1;
            } else {
                first = mid + 1;
            }
        }

        return first;
    }

 private:
    int64_t timeSpentWithGivenSpeed(vector<int>& piles, int K) {
        int64_t timeSpent = 0;

        for (auto pile : piles) {
            timeSpent += pile / K;
            timeSpent += pile % K ? 1 : 0;
        }

        return timeSpent;
    }
};

int main() {
    auto solution = Solution();

    vector<int> piles = {3, 6, 7, 11};

    assert(4 == solution.minEatingSpeed(piles, 8));
}
