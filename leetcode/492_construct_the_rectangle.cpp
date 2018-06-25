// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cmath>
#include <vector>

using namespace std;

class Solution {
 public:
    vector<int> constructRectangle(int area) {
        int width = sqrt(area);

        while (area % width) {
            width--;
        }

        return {area / width, width};
    }
};

int main() {
    auto solution = Solution();

    vector<int> expected = {2, 2};
    vector<int> result = solution.constructRectangle(4);

    assert(expected == result);
}
