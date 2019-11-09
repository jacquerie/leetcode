// Copyright (c) 2019 Jacopo Notarstefano

#include <cassert>

using namespace std;

class Solution {
 public:
    double nthPersonGetsNthSeat(int n) {
        return (n == 1) ? 1 : 0.5;
    }
};

int main() {
    auto solution = Solution();

    assert(1 == solution.nthPersonGetsNthSeat(1));
    assert(0.5 == solution.nthPersonGetsNthSeat(2));
    assert(0.5 == solution.nthPersonGetsNthSeat(3));
}
