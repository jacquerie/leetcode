// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>

using namespace std;

class Solution {
 public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int left = max(A, E), right = min(C, G), bottom = max(B, F), top = min(D, H);
        if (left < right && bottom < top) {
            return (C - A) * (D - B) + (G - E) * (H - F) - (right - left) * (top - bottom);
        } else {
            return (C - A) * (D - B) + (G - E) * (H - F);
        }
    }
};

int main() {
    auto solution = Solution();

    assert(45 == solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2));
    assert(17 == solution.computeArea(-2, -2, 2, 2, 3, 3, 4, 4));
}
