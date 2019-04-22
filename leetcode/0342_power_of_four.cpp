// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>

using namespace std;

class Solution {
 public:
    bool isPowerOfFour(int num) {
        return
            num == 1 ||
            num == 4 ||
            num == 16 ||
            num == 64 ||
            num == 256 ||
            num == 1024 ||
            num == 4096 ||
            num == 16384 ||
            num == 65536 ||
            num == 262144 ||
            num == 1048576 ||
            num == 4194304 ||
            num == 16777216 ||
            num == 67108864 ||
            num == 268435456 ||
            num == 1073741824;
    }
};

int main() {
    auto solution = Solution();

    assert(solution.isPowerOfFour(16));
    assert(!solution.isPowerOfFour(5));
}
