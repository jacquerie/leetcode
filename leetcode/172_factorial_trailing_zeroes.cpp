// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>

using namespace std;

class Solution {
 public:
    int trailingZeroes(int n) {
        int result = 0;

        while (n > 0) {
            result += n / 5;
            n /= 5;
        }

        return result;
    }
};

int main() {
    auto solution = Solution();

    assert(0 == solution.trailingZeroes(3));
    assert(1 == solution.trailingZeroes(5));
    assert(24 == solution.trailingZeroes(100));
    assert(452137076 == solution.trailingZeroes(1808548329));
}
