// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        return rec1[0] < rec2[2] && rec1[2] > rec2[0] && rec1[1] < rec2[3] && rec1[3] > rec2[1];
    }
};

int main() {
    auto solution = Solution();

    vector<int> rec1 = {0, 0, 2, 2};
    vector<int> rec2 = {1, 1, 3, 3};

    assert(solution.isRectangleOverlap(rec1, rec2));

    vector<int> rec3 = {0, 0, 1, 1};
    vector<int> rec4 = {1, 0, 2, 1};

    assert(!solution.isRectangleOverlap(rec3, rec4));

    vector<int> rec5 = {-6, -10, 9, 2};
    vector<int> rec6 = {0, 5, 4, 8};

    assert(!solution.isRectangleOverlap(rec5, rec6));
}
