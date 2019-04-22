// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cmath>

using namespace std;

class Solution {
 public:
    int mySqrt(int x) {
        return static_cast<int>(sqrt(x));
    }
};

int main() {
    auto solution = Solution();

    assert(2 == solution.mySqrt(4));
    assert(2 == solution.mySqrt(8));
}
