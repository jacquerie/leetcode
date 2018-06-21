// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>

using namespace std;

class Solution {
 public:
    bool checkPerfectNumber(int num) {
        return
            num == 6 ||
            num == 28 ||
            num == 496 ||
            num == 8128 ||
            num == 33550336;
    }
};

int main() {
    auto solution = Solution();

    assert(solution.checkPerfectNumber(28));
}
