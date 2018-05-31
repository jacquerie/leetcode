#include <cassert>
#include <cmath>

using namespace std;

class Solution {
 public:
    bool judgeSquareSum(int c) {
        if (c < 2) {
            return true;
        } else if (c % 4 == 3) {
            return false;
        }

        while (c % 2 == 0) {
            c = c / 2;
        }

        int n = c;
        for (int i = 3; i <= sqrt(c); i = i + 2) {
            int j = 0;
            while (n % i == 0) {
                n = n / i;
                j = j + 1;
            }

            if (i % 4 == 3 && j % 2 == 1) {
                return false;
            }
        }

        return !(n % 4 == 3);
    }
};

int main() {
    auto solution = Solution();

    assert(solution.judgeSquareSum(5));
    assert(!solution.judgeSquareSum(3));
    assert(solution.judgeSquareSum(0));
    assert(solution.judgeSquareSum(1));
    assert(solution.judgeSquareSum(93854834));
    assert(!solution.judgeSquareSum(11));
    assert(!solution.judgeSquareSum(22));
}
