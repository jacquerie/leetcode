// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <vector>

using namespace std;

class Solution {
 public:
    bool isUgly(int num) {
        if (num == 0) {
            return false;
        }

        vector<int> factors = {2, 3, 5};
        for (auto factor : factors) {
            while (num % factor == 0) {
                num /= factor;
            }
        }

        return num == 1;
    }
};

int main() {
    auto solution = Solution();

    assert(solution.isUgly(1));
    assert(solution.isUgly(6));
    assert(solution.isUgly(8));
    assert(!solution.isUgly(14));
    assert(!solution.isUgly(0));
}
