// Copyright (c) 2018 Jacopo Notarstefano

#include <cassert>
#include <cmath>

using namespace std;

class Solution {
 public:
    int numSquares(int n) {
        if (isSquare(n)) {
            return 1;
        } else if (isSumOfTwoSquares(n)) {
            return 2;
        } else if (isSumOfThreeSquares(n)) {
            return 3;
        } else {
            return 4;
        }
    }

 private:
    bool isSquare(int n) {
        int nSqrt = sqrt(n);
        return n == nSqrt * nSqrt;
    }

    bool isSumOfTwoSquares(int n) {
        if (n < 2) {
            return true;
        } else if (n % 4 == 3) {
            return false;
        }

        while (n % 2 == 0) {
            n = n / 2;
        }

        int c = n;
        for (int i = 3; i <= sqrt(n); i = i + 2) {
            int j = 0;
            while (c % i == 0) {
                c = c / i;
                j = j + 1;
            }

            if (i % 4 == 3 && j % 2 == 1) {
                return false;
            }
        }

        return !(c % 4 == 3);
    }

    bool isSumOfThreeSquares(int n) {
        while (n % 4 == 0) {
            n = n / 4;
        }

        return !(n % 8 == 7);
    }
};

int main() {
    auto solution = Solution();

    assert(3 == solution.numSquares(12));
    assert(2 == solution.numSquares(13));
    assert(4 == solution.numSquares(28));
}
