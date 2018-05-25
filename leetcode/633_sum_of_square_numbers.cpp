#include <cassert>

using namespace std;

class Solution {
public:
    bool judgeSquareSum (int c) {
        if (c < 2) {
            return true;
        }

        while (c % 2 == 0) {
            c = c / 2;
        }

        for (int i = 3; i <= c; i = i + 2) {
            int j = 0;
            while (c % i == 0) {
                c = c / i;
                j = j + 1;
            }

            if (i % 4 == 3 && j % 2 == 1) {
                return false;
            }
        }

        return true;
    }
};

int main () {
    auto solution = Solution();

    assert(solution.judgeSquareSum(5));
    assert(!solution.judgeSquareSum(3));
    assert(solution.judgeSquareSum(0));
    assert(solution.judgeSquareSum(1));
    assert(solution.judgeSquareSum(93854834));
}
