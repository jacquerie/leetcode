// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cmath>

using namespace std;

class Solution {
 public:
    int bulbSwitch(int n) {
        return sqrt(n);
    }
};

int main() {
    auto solution = Solution();

    assert(1 == solution.bulbSwitch(3));
}
