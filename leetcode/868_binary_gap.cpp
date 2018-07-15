// Copyright (c) 2018 Jacopo Notarstefano

#include <algorithm>
#include <cassert>

using namespace std;

class Solution {
 public:
    int binaryGap(int N) {
        bool one_seen = false;
        int current_count = 0, current_max = 0;

        for (int i = 0; i < 32; i++) {
            if (N & (1 << i)) {
                if (!one_seen) {
                    one_seen = true;
                } else {
                    current_max = max(current_max, current_count + 1);
                }
                current_count = 0;
            } else {
                current_count++;
            }
        }

        return current_max;
    }
};

int main() {
    auto solution = Solution();

    assert(2 == solution.binaryGap(22));
    assert(2 == solution.binaryGap(5));
    assert(1 == solution.binaryGap(6));
    assert(0 == solution.binaryGap(8));
}
