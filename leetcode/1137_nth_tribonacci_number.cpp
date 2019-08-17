// Copyright (c) 2019 Jacopo Notarstefano

#include <cassert>

using namespace std;

class Solution {
 public:
    int tribonacci(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else if (n == 2) {
            return 1;
        } else {
            int x = 0, y = 1, z = 1;

            for (int i = 3; i <= n; i++) {
                int tmp = x + y + z;
                x = y;
                y = z;
                z = tmp;
            }

            return z;
        }
    }
};

int main() {
    auto solution = Solution();

    assert(4 == solution.tribonacci(4));
    assert(1389537 == solution.tribonacci(25));
}

